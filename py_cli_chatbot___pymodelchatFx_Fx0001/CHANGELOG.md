# pymodelchatFx_Fx0001 - CHANGELOG

## INFO

This document tracks all significant changes made to the project. The project is oriented along [semantic versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which typically uses version numbers in the format "major.minor.patch" to indicate the type of changes made. However, unlike strict SemVer, this project also tracks documentation updates and small improvements as minor version increments to maintain a complete development history. Changes are organized by type and importance rather than chronological order.

<br>

## HIERARCHY

| Hierarchy | Type | Description |
|-----------|------|-------------|
| 1 | sec | security implementation, update or fix |
| 2 | chk | notable check, test or other investigation important for development progress |
| 3 | add | added feature and functionality |
| 4 | mod | change / modification |
| 5 | fix | bugfix |
| 6 | doc | addition, change / modification or correction in a document or code commentary |
| 7 | mrg | merge notice |

<br>

## CHANGES

| Date | Version | FxID | Type | Description | Remarks | Stage |
|------------|---------|------|------|----------------|---------|-------|
| 2025-06-19 | v0.5.2 | Fx0001 | mod | Implemented new changelog format. |  | PROTOTYPING |
| 2025-06-19 | v0.5.1 | Fx0001 | mod | Made 'Thinking...' tag persistent. | unstable | PROTOTYPING |
| 2025-06-17 | v0.5.0 | Fx0001 | mod | Changed header info from 'quickbotFx' ---> 'pymodelchatFx_Fx0001'. |  | PROTOTYPING |
| 2025-06-17 | v0.5.0 | Fx0001 | add | Added functionality and config entry to enable/disable thinking in reasoning models. |  | PROTOTYPING |
| 2025-06-16 | v0.4.8 | Fx0001 | doc | Minor spelling corrections in this changelog. |  | PROTOTYPING |
| 2025-06-15 | v0.4.7 | Fx0001 | doc | Added info about change classification hierarchy to this changelog;;; Added extended versioning convention, see header of this changelog. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Clarified commentary in 'config.yaml'. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Clarified change notation in 'CHANGELOG.md', documentation modification is now 'doc' instead of 'mod'. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Started to swap '.' for internally standardized ';;;' as sentence ending delimiters, for better machine readability. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Added fragment name to this changelog. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Fixed version tagging to fit multi-project structure of the FragmentsFx repository for better clarification. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Changed delimiters in 'CHANGELOG.md' to avoid conflicts ;;; Minor formatting correction. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Fixed tagging to follow new internal versioning and commit standards. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | doc | Fixed filename delimiters - removed backticks and replaced them with apostrophes. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | mod | Fx_0001 folder was renamed to its old name 'py_cli_chatbot___quickbotFx_0001';;; Changed back to its new name 'py_cli_chatbot___pymodelchatFx_0001'. |  | PROTOTYPING |
| 2025-06-11 | v0.4.6 | Fx0001 | mod | All Fx fragment will get a more distinct identification number: filenames and docs will be 'filenameFx_Fx0000' instead of 'filenameFx_0000' for better machine readability, changelogs will from now on be marked with the Fx id in fromt of every commit, to avoid missing to add this prefix in the commit message. |  | PROTOTYPING |
| 2025-06-11 | v0.4.4 | Fx0001 | doc | Refactored 'config.yaml' structure for better readability. |  | PROTOTYPING |
| 2025-06-11 | v0.4.4 | Fx0001 | doc | Refactored 'CHANGELOG.md' structure for better readability. |  | PROTOTYPING |
| 2025-06-11 | v0.4.4 | Fx0001 | doc | Removed version tags from 'CHANGELOG.md' as previous commits were versioned incorrectly;;; Version tags removed as a preparation for correction. |  | PROTOTYPING |
| 2025-06-11 | v0.4.4 | Fx0001 | fix | Fixed versioning issue;;; Reworked 'CHANGELOG.md'. |  | PROTOTYPING |
| 2025-06-11 | v0.4.4 | Fx0001 | mod | Code refactoring - welcome_display --> info_header. |  | PROTOTYPING |
| 2025-06-11 | v0.4.4 | Fx0001 | mod | Displaying json output info now in info header. |  | PROTOTYPING |
| 2025-06-11 | v0.4.1 | Fx0001 | mod | Moved system prompt to 'config.yaml';;; Deleted 'system.prompt' file. |  | PROTOTYPING |
| 2025-06-11 | v0.4.0 | Fx0001 | add | Functionality to let the model generate structured json output;;; Enable/disable via 'config.yaml'. |  | PROTOTYPING |
| 2025-06-11 | v0.3.0 | Fx0001 | add | Functionality to enable/disable user/ai interaction labels in chat display;;; Enable/disable via 'config.yaml'. |  | PROTOTYPING |
| 2025-06-10 | v0.2.1 | Fx0001 | mod | Removed 'goodbye' message when ctrl+c quitting the program. |  | PROTOTYPING |
| 2025-06-10 | v0.2.0 | Fx0001 | doc | Updated 'LICENSE', added copyright info. |  | PROTOTYPING |
| 2025-06-10 | v0.2.0 | Fx0001 | doc | Removed links in 'CHANGELOG.md'. |  | PROTOTYPING |
| 2025-06-10 | v0.2.0 | Fx0001 | doc | Removed issue badge from 'README.md'. |  | PROTOTYPING |
| 2025-06-10 | v0.2.0 | Fx0001 | add | Feature to enable/disable ollama message streaming via 'config.yaml'. |  | PROTOTYPING |
| 2025-06-09 | v0.1.2 | Fx0001 | doc | Renamed folder and filename of 'Fx_0001' (python cli chatbot fragment) for better clarification. |  | PROTOTYPING |
| 2025-06-09 | v0.1.0 | Fx0001 | fix | 'context_window' and 'max_predict' type conversion (convert to int). |  | PROTOTYPING |
| 2025-06-09 | v0.1.0 | Fx0001 | fix | Temperature type conversion error for ollama integration (convert to float). |  | PROTOTYPING |
| 2025-06-09 | v0.1.0 | Fx0001 | mod | Quit/exit command functionality - program now only exits with ctrl+c. |  | PROTOTYPING |
| 2025-06-09 | v0.1.0 | Fx0001 | mod | User/ai exchange markers from 'you:'/'bot:' to 'user:'/'ai:'. |  | PROTOTYPING |
| 2025-06-09 | v0.1.0 | Fx0001 | mod | Welcome message to display model configuration details instead of basic chatbot header. |  | PROTOTYPING |
| 2025-06-09 | v0.0.3 | Fx0001 | mod | Switched from 'PyYAML' to 'strictyaml' for safer configuration parsing. |  | FOUNDATION |
| 2025-06-09 | v0.0.3 | Fx0001 | add | Dependency management as 'requirements.txt'. |  | FOUNDATION |
| 2025-06-09 | v0.0.3 | Fx0001 | add | System prompt file as 'system.prompt'. |  | FOUNDATION |
| 2025-06-09 | v0.0.3 | Fx0001 | add | Model config file as 'config.yaml'. |  | FOUNDATION |
| 2025-06-09 | v0.0.3 | Fx0001 | add | Integration with local ollama service via the 'ollama' python library. |  | FOUNDATION |
| 2025-06-08 | v0.0.2 | Fx0001 | doc | FragmentsRx 'README.md' to root, with basic content. |  | FOUNDATION |
| 2025-06-08 | v0.0.2 | Fx0001 | doc | 'LICENSE' - apache 2.0. |  | FOUNDATION |
| 2025-06-08 | v0.0.2 | Fx0001 | add | Established basic project structure. |  | FOUNDATION |
| 2025-06-08 | v0.0.2 | Fx0001 | add | '.gitignore'. |  | FOUNDATION |
| 2025-06-08 | v0.0.2 | Fx0001 | add | '.env' file for api key setup. |  | FOUNDATION |
| 2025-06-08 | v0.0.2 | Fx0001 | sec | Added .env to '.gitignore' for all subfolders. |  | FOUNDATION |
| 2025-06-08 | v0.0.1 | Fx0001 | add | Initial commit. |  | FOUNDATION |