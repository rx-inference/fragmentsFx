# CHANGELOG

notable changes will be documented.

this project adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## WORK IN PROGRESS

### 2025-06-11

- mod: removed version tags from `CHANGELOG.md` as previous commits were versioned incorrectly; version tags removed as a preparation for correction.
- mod: refactored `CHANGELOG.md` structure for better readability.
- mod: refactored `config.yaml` structure for better readability.
- mod: displaying json output info now in info header.
- mod: code refactoring - welcome_display --> info_header.
- mod: moved system prompt to `config.yaml`; deleted `system.prompt` file.

### 2025-06-10

- add: functionality to let the model generate structured json output; enable/disable via `config.yaml`.

### 2025-06-10

- add: functionality to enable/disable user/ai interaction labels in chat display; enable/disable via `config.yaml`.

### 2025-06-10

- add: feature to enable/disable ollama message streaming via `config.yaml`.
- mod: removed issue badge from README.md.
- mod: removed links in CHANGELOG.md.
- mod: updated LICENSE, added copyright info.
- mod: renamed folder and filename of Fx_0001 (python cli chatbot fragment) for better clarification.
- del: removed "goodbye" message when ctrl+c quitting the program.

### 2025-06-09

- add: model configuration display in welcome message showing model, context, max tokens, and temperature.
- mod: welcome message to display model configuration details instead of basic chatbot header.
- mod: user/ai exchange markers from "you:"/"bot:" to "user:"/"ai:".
- del: quit/exit command functionality - program now only exits with ctrl+c.
- fix: temperature type conversion error for ollama integration (convert to float).
- fix: context_window and max_predict type conversion (convert to int).

### 2025-06-09

- add: integration with local ollama service via the `ollama` python library.
- add: model config file as `config.yaml`.
- add: system prompt file as `system.prompt`.
- add: dependency management as `requirements.txt`.
- mod: switched from PyYAML to `strictyaml` for safer configuration parsing.

### 2025-06-08

- sec: added .env to `.gitignore` for all subfolders.
- add: `.env` file for api key setup.
- add: fragmentsRx `README.md` to root, with basic conetnt.
- add: `LICENSE` - apache 2.0.
- add: `.gitignore`.
- add: established basic project structure.
- add: initial commit.