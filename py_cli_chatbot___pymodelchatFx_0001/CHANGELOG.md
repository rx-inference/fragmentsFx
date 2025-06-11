# pymodelchatFx_0001 - CHANGELOG

notable changes will be documented.

this project adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## PROTOTYPING

### 2025-06-11

### v.0.4.xxx

- mod: Fx_0001 folder was renamed to its old name `py_cli_chatbot___quickbotFx_0001`; changed back to its new name `py_cli_chatbot___pymodelchatFx_0001`;;; /++ this was likely caused by a lack of attention or a previous rebase and wasn't recognized until now ++/
- doc: added fragment name to this changelog;;;
- doc: fixed version tagging to fit multi-project structure of the FragmentsFx repository for better clarification. (commit messages were not rebased to avoid chaos);;;
- doc: started to swap "." for internally standardized ";;;" as sentence ending delimiters, for better machine readability.
- doc: clarified change notation in `CHANGELOG.md`, documentation modification is now `doc`instead of `mod`;;;
- doc: clarified commentary in `config.yaml`;;;

### v0.4.4

- mod: displaying json output info now in info header;;;
- mod: code refactoring - welcome_display --> info_header;;;
- doc: removed version tags from `CHANGELOG.md` as previous commits were versioned incorrectly; version tags removed as a preparation for correction;;;
    - fix: fixed versioning issue; reworked `CHANGELOG.md`;;;
- doc: refactored `CHANGELOG.md` structure for better readability;;;
- doc: refactored `config.yaml` structure for better readability;;;

### v0.4.1

- mod: moved system prompt to `config.yaml`; deleted `system.prompt` file;;;

### v0.4.0

- add: functionality to let the model generate structured json output; enable/disable via `config.yaml`;;;

### v 0.3.0

- add: functionality to enable/disable user/ai interaction labels in chat display; enable/disable via `config.yaml`;;;

### 2025-06-10

### v0.2.1

- del: removed "goodbye" message when ctrl+c quitting the program;;;

### v0.2.0

- add: feature to enable/disable ollama message streaming via `config.yaml`;;;
- doc: removed issue badge from README.md;;;
- doc: removed links in CHANGELOG.md;;;
- doc: updated LICENSE, added copyright info;;;

### v0.1.2

- doc: renamed folder and filename of Fx_0001 (python cli chatbot fragment) for better clarification;;;

### 2025-06-09

### v0.1.0

- mod: welcome message to display model configuration details instead of basic chatbot header;;;
- mod: user/ai exchange markers from "you:"/"bot:" to "user:"/"ai:";;;
- del: quit/exit command functionality - program now only exits with ctrl+c;;;
- fix: temperature type conversion error for ollama integration (convert to float);;;
- fix: context_window and max_predict type conversion (convert to int);;;

## FOUNDATION

### 2025-06-09

### v0.0.3

- add: integration with local ollama service via the `ollama` python library;;;
- add: model config file as `config.yaml`;;;
- add: system prompt file as `system.prompt`;;;
- add: dependency management as `requirements.txt`;;;
- mod: switched from PyYAML to `strictyaml` for safer configuration parsing;;;

### 2025-06-08

### v0.0.2

- sec: added .env to `.gitignore` for all subfolders;;;
- add: `.env` file for api key setup;;;
- add: `.gitignore`;;;
- add: established basic project structure;;;
- Doc: `LICENSE` - apache 2.0;;;
- doc: fragmentsRx `README.md` to root, with basic content;;;

### v0.0.1

- add: initial commit;;;