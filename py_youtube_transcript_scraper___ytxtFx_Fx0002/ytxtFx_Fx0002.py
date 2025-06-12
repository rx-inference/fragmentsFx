# PURPOSE: cli tool to fetch a youtube transcript and print it to the console.

import sys
import re
import pathlib
import datetime
from typing import List

from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
)
from strictyaml import load, YAML, Map, Str, YAMLValidationError

# === CONFIG HANDLING ===
_CONFIG_FILE = pathlib.Path(__file__).with_name("config.yaml")
_TRANSCRIPTS_DIR = pathlib.Path(__file__).with_name("transcripts")
_SCHEMA = Map({
    "default_transcript_language": Str(),
    "output_folder": Str()
})


def _load_or_create_config() -> YAML:
    """load config.yaml or create it with defaults."""
    if not _CONFIG_FILE.exists():
        print("[error] config.yaml not found")
        sys.exit(1)
    try:
        return load(_CONFIG_FILE.read_text(encoding='utf-8'), _SCHEMA)
    except YAMLValidationError as exc:  # §_INFOSEC_03 sanitize config
        print(f"[error] invalid config file: {exc}")
        sys.exit(1)


# === MODEL ===
class YouTubeTranscriptModel:
    """retrieve the transcript from youtube."""

    # --- SUB HELPERS ---
    _youtube_regex = re.compile(
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"  # 11-char video id
    )

    def _extract_video_id(self, url: str) -> str:
        """sanitize and extract video id or raise."""
        match = self._youtube_regex.search(url.strip())
        if not match:
            raise ValueError("invalid youtube url")
        return match.group(1)

    # --- PUBLIC API ---
    def fetch_transcript(self, url: str, language: str) -> List[str]:
        """return plain text transcript lines."""
        video_id = self._extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=[language, language.lower()]
        )
        return [fragment["text"] for fragment in transcript]


# === VIEWMODEL ===
class TranscriptViewModel:
    """orchestrate model and present results."""

    def __init__(self, language: str) -> None:
        self.model = YouTubeTranscriptModel()
        self.language = language

    def process(self, url: str) -> List[str]:
        """fetch transcript or raise specific errors."""
        try:
            return self.model.fetch_transcript(url, self.language)
        except (
            TranscriptsDisabled,
            NoTranscriptFound,
        ):
            raise RuntimeError("no transcript available for this video")
        except Exception as exc:
            raise RuntimeError(str(exc)) from exc


# === VIEW / CONTROLLER ===
def _print_step(message: str) -> None:
    """unified step logging."""
    print(f"[info] {message}")


def _save_transcript(video_id: str, lines: List[str], output_dir: pathlib.Path) -> pathlib.Path:
    """write transcript to output_dir/[watchid_yyyy-mm-dd_hh-mm-ss].txt."""
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = output_dir / f"{video_id}_{timestamp}.txt"
    file_path.write_text("\n".join(lines), encoding='utf-8')
    return file_path


def main() -> None:
    """entry point for the cli app."""
    _print_step("starting youtube transcript downloader")

    # --- ARG VALIDATION ---
    if len(sys.argv) < 2:
        print("[error] please provide a youtube url")
        sys.exit(1)

    url = sys.argv[1]

    # --- LOAD CONFIG ---
    cfg = _load_or_create_config()
    language = cfg["default_transcript_language"].value
    output_folder = pathlib.Path(cfg["output_folder"].value)
    _print_step(f"config loaded (language: {language}, output: {output_folder})")

    # --- TRANSCRIPT RETRIEVAL ---
    view_model = TranscriptViewModel(language)
    _print_step("downloading transcript …")
    try:
        transcript_lines = view_model.process(url)
    except RuntimeError as exc:
        print(f"[error] {exc}")
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception:
        print("[error] connection problems")
        sys.exit(1)

    # --- OUTPUT ---
    _print_step("transcript downloaded")
    video_id = view_model.model._extract_video_id(url)
    file_path = _save_transcript(video_id, transcript_lines, output_folder)
    _print_step(f"saved to {file_path}\n")

    for line in transcript_lines:
        print(line)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # silent exit on ctrl+c
        pass