# pymodelchatFx_Fx0001 - CHANGELOG

notable changes will be documented. this project adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html) with the addition, that this repo will also track minor documentation changes and other minor changes, and also minor notations as a v0.0.x to keep the commit history in regards to all subfolders and fragment additions structured and comprehensible. the changelog is not chronologically ordered, but follows a change classification hierarchy always starting with its referece:

1. sec ---> security implementation, update or fix.
2. chk ---> notable check, test or other investigation important for development progress.
3. add ---> added feature and functionality.
4. mod ---> change / modification.
5. fix ---> bugfix.
6. doc ---> addition, change / modification or correction in a document or code commentary.

## PROTOTYPING

### ### 2025-06-17

### v0.4.x

- Fx0001_add: added functionality and config entry to enable/disable thinking in reasoning models. ;;;
- Fx0001_mod: changed header info from 'quickbotFx' ---> 'pymodelchatFx_Fx0001'. ;;;

### 2025-06-16

### v.0.4.8

- Fx0001_doc: minor spelling corrections in this changelog. ;;;

### 2025-06-15

### v.0.4.7

- Fx0001_doc: added info about change classification hierarchy to this changelog; added extended versioning convention, see header of this changelog. ;;;

### 2025-06-11

### v.0.4.6

- Fx0001_mod: all Fx fragment will get a more distinct identification number: filenames and docs will be 'filenameFx_Fx0000' instead of 'filenameFx_0000' for better machine readability, changelogs will from now on be marked with the Fx id in fromt of every commit, to avoid missing to add this prefix in the commit message;;; /+++ though these changes are modifications to internal standards, they are logged here, as they have emerged while working on fragmentsFx; commit messages will not be rabased to avoid chaos. +++/ ;;;
- Fx0001_mod: Fx_0001 folder was renamed to its old name 'py_cli_chatbot___quickbotFx_0001'; changed back to its new name 'py_cli_chatbot___pymodelchatFx_0001';;; /+++ this was likely caused by a lack of attention or a previous rebase and wasn`t recognized until now +++/ ;;;
- Fx0001_doc: fixed filename delimiters - removed backticks and replaced them with apostrophes.;;;
- Fx0001_doc: fixed tagging to follow new internal versioning and commit standards;;; /+++ though these changes are modifications to internal standards, they are logged here, as they have emerged while working on fragmentsFx +++/ ;;;
- Fx0001_doc: changed delimiters in 'CHANGELOG.md' to avoid conflicts + minor formatting correction;;;
- Fx0001_doc: fixed version tagging to fit multi-project structure of the FragmentsFx repository for better clarification;;; /+++ all changes made were documented, but last commit messages may not match their changes; this is caused intentionally by a correction in documentation, commits and versioning as a tradeoff to a rebase which would have potentially caused chaos. +++/ ;;;
- Fx0001_doc: added fragment name to this changelog;;;
- Fx0001_doc: started to swap '.' for internally standardized ';;;' as sentence ending delimiters, for better machine readability;;;
- Fx0001_doc: clarified change notation in 'CHANGELOG.md', documentation modification is now 'doc' instead of 'mod';;;
- Fx0001_doc: clarified commentary in 'config.yaml';;;

### v0.4.4

- Fx0001_mod: displaying json output info now in info header;;;
- Fx0001_mod: code refactoring - welcome_display --> info_header;;;
- Fx0001_doc: removed version tags from 'CHANGELOG.md' as previous commits were versioned incorrectly; version tags removed as a preparation for correction;;;
    - Fx0001_fix: fixed versioning issue; reworked 'CHANGELOG.md';;;
- Fx0001_doc: refactored 'CHANGELOG.md' structure for better readability;;;
- Fx0001_doc: refactored 'config.yaml' structure for better readability;;;

### v0.4.1

- Fx0001_mod: moved system prompt to 'config.yaml'; deleted 'system.prompt' file;;;

### v0.4.0

- Fx0001_add: functionality to let the model generate structured json output; enable/disable via 'config.yaml';;;

### v 0.3.0

- Fx0001_add: functionality to enable/disable user/ai interaction labels in chat display; enable/disable via 'config.yaml';;;

### 2025-06-10

### v0.2.1

- Fx0001_del: removed 'goodbye' message when ctrl+c quitting the program;;;

### v0.2.0

- Fx0001_add: feature to enable/disable ollama message streaming via 'config.yaml';;;
- Fx0001_doc: removed issue badge from 'README.md';;;
- Fx0001_doc: removed links in 'CHANGELOG.md';;;
- Fx0001_doc: updated 'LICENSE', added copyright info;;;

### v0.1.2

- Fx0001_doc: renamed folder and filename of 'Fx_0001' (python cli chatbot fragment) for better clarification;;;

### 2025-06-09

### v0.1.0

- Fx0001_mod: welcome message to display model configuration details instead of basic chatbot header;;;
- Fx0001_mod: user/ai exchange markers from 'you:'/'bot:' to 'user:'/'ai:';;;
- Fx0001_del: quit/exit command functionality - program now only exits with ctrl+c;;;
- Fx0001_fix: temperature type conversion error for ollama integration (convert to float);;;
- Fx0001_fix: 'context_window' and 'max_predict' type conversion (convert to int);;;

## FOUNDATION

### 2025-06-09

### v0.0.3

- Fx0001_add: integration with local ollama service via the 'ollama' python library;;;
- Fx0001_add: model config file as 'config.yaml';;;
- Fx0001_add: system prompt file as 'system.prompt';;;
- Fx0001_add: dependency management as 'requirements.txt';;;
- Fx0001_mod: switched from 'PyYAML' to 'strictyaml' for safer configuration parsing;;;

### 2025-06-08

### v0.0.2

- Fx0001_sec: added .env to '.gitignore' for all subfolders;;;
- Fx0001_add: '.env' file for api key setup;;;
- Fx0001_add: '.gitignore';;;
- Fx0001_add: established basic project structure;;;
- Fx0001_doc: 'LICENSE' - apache 2.0;;;
- Fx0001_doc: fragmentsRx 'README.md' to root, with basic content;;;

### v0.0.1

- Fx0001_add: initial commit;;;