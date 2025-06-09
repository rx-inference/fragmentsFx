# CHANGELOG

notable changes will be documented.

this project adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## WORK IN PROGRESS

### [v0.0.3](https://github.com/rx-inference/fragmentsRx/compare/v0.0.2...v0.0.3) - 2025-06-09

#### UPDATES / CHANGES

- changed welcome message to display model configuration details instead of basic chatbot header
- changed user/ai exchange markers from "you:"/"bot:" to "user:"/"ai:"

#### ADDED

- added model configuration display in welcome message showing model, context, max tokens, and temperature

#### FIXED

- fixed temperature type conversion error for ollama integration (convert to float)
- fixed context_window and max_predict type conversion (convert to int)

#### REMOVED

- removed quit/exit command functionality - program now only exits with ctrl+c

### [v0.0.2](https://github.com/rx-inference/fragmentsRx/compare/v0.0.1...v0.0.2) - 2025-06-09

#### UPDATES / CHANGES

- changed switched from PyYAML to `strictyaml` for safer configuration parsing.

#### ADDED

- added integration with local ollama service via the `ollama` python library.
- added model config file as `config.yaml`.
- added system prompt file as `system.prompt`.
- added dependency management as `requirements.txt`.

### [v0.0.1](https://github.com/rx-inference/fragmentsRx/compare/v0.0.0...v0.0.1) - 2025-06-08

#### SECURITY

- added .env to `.gitignore` for all subfolders.

#### ADDED

- added `.env` file for api key setup.
- added fragmentsRx `README.md` to root, with basic conetnt.
- added `LICENSE` - apache 2.0.
- added `.gitignore`.

#### INIT

- established basic project structure.
- initial commit.