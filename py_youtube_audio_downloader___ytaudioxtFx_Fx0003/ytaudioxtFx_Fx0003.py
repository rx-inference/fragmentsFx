# PURPOSE: ytaudioxtFx_Fx0003 - command line tool that extracts the audio track from a youtube video and downloads it.

# === IMPORTS ===
import sys
import os
import yt_dlp

# === DOWNLOAD_AUDIO FUNCTION ===
def download_audio(url):
    """Download audio from YouTube video and save as MP3"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')

# === MAIN EXECUTION ===
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ytdl.py [youtube_url]")
        sys.exit(1)
    
    url = sys.argv[1]
    output_file = download_audio(url)
    print(f"Downloaded: {os.path.basename(output_file)}")