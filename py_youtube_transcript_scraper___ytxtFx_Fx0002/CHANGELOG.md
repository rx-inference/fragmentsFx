# ytytFx_Fx0002 - CHANGELOG

notable changes will be documented. this project adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html) with the addition, that this repo will also track minor documentation changes and other minor changes, and also minor notations as a v0.0.x to keep the commit history in regards to all subfolders and fragment additions structured and comprehensible. the changelog is not chronologically ordered, but follows a change classification hierarchy always starting with its referece:

1. sec ---> security implementation, update or fix.
2. chk ---> notable check, test or other investigation important for development progress.
3. add ---> added feature and functionality.
4. mod ---> change / modification.
5. fix ---> bugfix.
6. doc ---> addition, change / modification or correction in a document or code commentary.

## PROTOTYPING

### 2025-06-16

### v0.1.2

- Fx0002_doc: minor spelling corrections in this changelog. ;;;

### 2025-06-15

### v0.1.1

- Fx0002_doc: added info about change classification hierarchy to this changelog; added extended versioning convention, see header of this changelog. ;;;

### 2025-06-12

### v0.1.0

_program tested --> basic version is working; moving to v0.1.0._

- Fx0002_add: configurable output language setting in 'config.yaml' ;;;
- Fx0002_add: configurable output folder setting in 'config.yaml' ;;;
- Fx0002_add: transcript file saving functionality with timestamp format '[WATCHID_YYYY-MM-DD_HH-MM-SS].txt' ;;;
- Fx0002_add: header displays info on current actions when program is runs. ;;;
- Fx0002_mod: 'transcripts/' folder to '.gitignore' to prevent upload to github ;;;
- Fx0002_mod: updated 'requirements.txt' with correct dependencies 'strictyaml' and 'youtube-transcript-api>=0.6.1' ;;;
- Fx0002_doc: reformatted code group headers to follow uppercase convention standards ;;;
- Fx0002_fix: resolved import errors for 'youtube_transcript_api' and 'strictyaml' libraries ;;;
- Fx0002_fix: corrected unicode encoding issues in transcript output by specifying utf-8 encoding ;;;

## FOUNDATION

### 2025-06-11

### v0.0.1

- Fx0002_add: established boilerplate project structure, files added: `ytxtFx_0002.py`, `CHANGELOG.md`, `README.md`, `config.yaml`, `requirements.txt`;;;
- Fx0002_add: initial commit;;;