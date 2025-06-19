# pymodelchatFx_Fx0001 - CHANGELOG

## INFO

This document tracks all significant changes made to the project. The project is oriented along [semantic versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which typically uses version numbers in the format "major.minor.patch" to indicate the type of changes made. However, unlike strict SemVer, this project also tracks documentation updates and small improvements as minor version increments to maintain a complete development history.

<br>

## CHANGES

| Date | FxID | Version | Type | Description | Remarks | Stage |
|------------|------|---------|------|----------------|---------|-------|
| 2025-06-19 | Fx0001 | v0.6.0 | add | Added option to show/hide thinking tags + display in info header when program runs. | unstable | PROTOTYPING |
| 2025-06-19 | Fx0001 | v0.5.6 | mod | Changed the 'Thinking...' tag to read 'Reasoning...'. |  | PROTOTYPING |
| 2025-06-19 | Fx0001 | v0.5.5 | mod | Simplified 'config.yaml' and removed ollama setting section as long as we are not using other providers. |  | PROTOTYPING |
| 2025-06-19 | Fx0001 | v0.5.4 | doc | Simplified 'CHANGELOG.md' header & changed column order. |  | PROTOTYPING |
| 2025-06-19 | Fx0001 | v0.5.3 | mod | 'Thinking...' tag is now in its own line. | unstable | PROTOTYPING |
| 2025-06-19 | Fx0001 | v0.5.2 | mod | Implemented new changelog format. |  | PROTOTYPING |
| 2025-06-19 | Fx0001 | v0.5.1 | mod | Made 'Thinking...' tag persistent. | unstable | PROTOTYPING |
| 2025-06-17 | Fx0001 | v0.5.0 | mod | Changed header info from 'quickbotFx' ---> 'pymodelchatFx_Fx0001'. |  | PROTOTYPING |
| 2025-06-17 | Fx0001 | v0.5.0 | add | Added functionality and config entry to enable/disable thinking in reasoning models. |  | PROTOTYPING |
| 2025-06-16 | Fx0001 | v0.4.8 | doc | Minor spelling corrections in this changelog. |  | PROTOTYPING |
| 2025-06-15 | Fx0001 | v0.4.7 | doc | Added info about change classification hierarchy to this changelog;;; Added extended versioning convention, see header of this changelog. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Clarified commentary in 'config.yaml'. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Clarified change notation in 'CHANGELOG.md', documentation modification is now 'doc' instead of 'mod'. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Started to swap '.' for internally standardized ';;;' as sentence ending delimiters, for better machine readability. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Added fragment name to this changelog. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Fixed version tagging to fit multi-project structure of the FragmentsFx repository for better clarification. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Changed delimiters in 'CHANGELOG.md' to avoid conflicts ;;; Minor formatting correction. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Fixed tagging to follow new internal versioning and commit standards. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | doc | Fixed filename delimiters - removed backticks and replaced them with apostrophes. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | mod | Fx_0001 folder was renamed to its old name 'py_cli_chatbot___quickbotFx_0001';;; Changed back to its new name 'py_cli_chatbot___pymodelchatFx_0001'. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.6 | mod | All Fx fragment will get a more distinct identification number: filenames and docs will be 'filenameFx_Fx0000' instead of 'filenameFx_0000' for better machine readability, changelogs will from now on be marked with the Fx id in fromt of every commit, to avoid missing to add this prefix in the commit message. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.4 | doc | Refactored 'config.yaml' structure for better readability. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.4 | doc | Refactored 'CHANGELOG.md' structure for better readability. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.4 | doc | Removed version tags from 'CHANGELOG.md' as previous commits were versioned incorrectly;;; Version tags removed as a preparation for correction. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.4 | fix | Fixed versioning issue;;; Reworked 'CHANGELOG.md'. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.4 | mod | Code refactoring - welcome_display --> info_header. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.4 | mod | Displaying json output info now in info header. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.1 | mod | Moved system prompt to 'config.yaml';;; Deleted 'system.prompt' file. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.4.0 | add | Functionality to let the model generate structured json output;;; Enable/disable via 'config.yaml'. |  | PROTOTYPING |
| 2025-06-11 | Fx0001 | v0.3.0 | add | Functionality to enable/disable user/ai interaction labels in chat display;;; Enable/disable via 'config.yaml'. |  | PROTOTYPING |
| 2025-06-10 | Fx0001 | v0.2.1 | mod | Removed 'goodbye' message when ctrl+c quitting the program. |  | PROTOTYPING |
| 2025-06-10 | Fx0001 | v0.2.0 | doc | Updated 'LICENSE', added copyright info. |  | PROTOTYPING |
| 2025-06-10 | Fx0001 | v0.2.0 | doc | Removed links in 'CHANGELOG.md'. |  | PROTOTYPING |
| 2025-06-10 | Fx0001 | v0.2.0 | doc | Removed issue badge from 'README.md'. |  | PROTOTYPING |
| 2025-06-10 | Fx0001 | v0.2.0 | add | Feature to enable/disable ollama message streaming via 'config.yaml'. |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.1.2 | doc | Renamed folder and filename of 'Fx_0001' (python cli chatbot fragment) for better clarification. |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.1.0 | fix | 'context_window' and 'max_predict' type conversion (convert to int). |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.1.0 | fix | Temperature type conversion error for ollama integration (convert to float). |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.1.0 | mod | Quit/exit command functionality - program now only exits with ctrl+c. |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.1.0 | mod | User/ai exchange markers from 'you:'/'bot:' to 'user:'/'ai:'. |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.1.0 | mod | Welcome message to display model configuration details instead of basic chatbot header. |  | PROTOTYPING |
| 2025-06-09 | Fx0001 | v0.0.3 | mod | Switched from 'PyYAML' to 'strictyaml' for safer configuration parsing. |  | FOUNDATION |
| 2025-06-09 | Fx0001 | v0.0.3 | add | Dependency management as 'requirements.txt'. |  | FOUNDATION |
| 2025-06-09 | Fx0001 | v0.0.3 | add | System prompt file as 'system.prompt'. |  | FOUNDATION |
| 2025-06-09 | Fx0001 | v0.0.3 | add | Model config file as 'config.yaml'. |  | FOUNDATION |
| 2025-06-09 | Fx0001 | v0.0.3 | add | Integration with local ollama service via the 'ollama' python library. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.2 | doc | FragmentsRx 'README.md' to root, with basic content. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.2 | doc | 'LICENSE' - apache 2.0. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.2 | add | Established basic project structure. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.2 | add | '.gitignore'. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.2 | add | '.env' file for api key setup. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.2 | sec | Added .env to '.gitignore' for all subfolders. |  | FOUNDATION |
| 2025-06-08 | Fx0001 | v0.0.1 | add | Initial commit. |  | FOUNDATION |