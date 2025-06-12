<!-- PURPOSE: documentation for the llm provider config files fragment. -->
<div align="center">

  <h1>llmbaseconfigFx_Fx0004</h1>
  <p>
    <b>a comprehensive yaml configuration template for llm provider settings across multiple ai services.</b>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Prototype / Work in Progress-crimson" alt="prototype">
    <img src="https://img.shields.io/badge/fragmentsFx-FFE000" alt="fragmentsFx">
    <img src="https://img.shields.io/badge/Fx0004-FFE000" alt="Fx0003">
    <a href="https://github.com/rx-inference/fragmentsFx/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
    <a href="https://github.com/rx-inference/fragmentsFx/releases"><img src="https://img.shields.io/badge/Version-v0.0.1-brightgreen" alt="Version"></a>
  </p>


</div>

---

## PROTOTYPING / WORK IN PROGRESS (⚠️)

This software is a work in progress and currently in its prototyping phase. It is not intended for production use. Errors may occur, features may change, and documentation may be fragmented or incomplete. During the prototyping phase, all support inquiries about this software will be ignored.

## OVERVIEW

llmbaseconfigFx_Fx0004 provides a ready-to-use yaml configuration template containing recommended settings for popular llm providers including ollama, openai, and openrouter. the fragment includes pre-configured prompt modules for common ai tasks and standardized settings that can be directly integrated into applications.

## KEY FEATURES

- **🔧 multi-provider support:** configurations for ollama, openai, and openrouter services
- **📝 prompt modules:** pre-built prompts for summarization, translation, code generation, security review, and more
- **⚙️ standardized settings:** consistent parameter naming and value ranges across providers
- **🎯 task-specific:** specialized prompt modules for different use cases
- **📋 ready-to-use:** simply delete unused sections to create a custom config file

## USAGE

1. copy `llmprovider.yaml` to your project
2. remove provider sections you don't need
3. adjust settings like temperature, context window, and model names
4. integrate the config into your application's yaml parser

## CONFIGURATION SECTIONS

- **general settings:** system prompt, temperature, display options
- **prompt modules:** specialized prompts for various ai tasks
- **ollama settings:** local ollama service configuration
- **openai settings:** openai api configuration  
- **openrouter settings:** openrouter api configuration

## PROMPT MODULES INCLUDED

- summarizer, translator, code generator
- code optimizer, refactoring, security review
- documentation generator, topic explainer
- personal information handling (censoring/extraction)
- json extractor, email responder

## REQUIREMENTS

- yaml parser in your target application (strictyaml is recommended).
- local ollama installation (if using ollama settings)

## COPYRIGHT CONTEXT & LICENSE

Copyright 2025 - Robin Winkelmann | robinRx | rx-inference

This fragment is part of the FragmentsRx suite, an open-source, AI-navigable library of functional code fragments. The entire suite is licensed under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. See the [LICENSE](https://github.com/rx-inference/fragmentsFx/blob/main/LICENSE) in the root of the project for details. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.