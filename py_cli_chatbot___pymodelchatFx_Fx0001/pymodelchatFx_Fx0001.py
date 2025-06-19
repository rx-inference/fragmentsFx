# PURPOSE: simple command line chatbot pymodelchatFx_Fx0001

import ollama
import strictyaml
import os
import sys
import re

# === CONFIGURATION MODEL ===

class config_model:
    """handles loading and storing configuration settings"""
    
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.settings = self._load_config()
    
    def _load_config(self):
        """loads configuration from yaml file"""
        try:
            with open(self.config_path, 'r') as file:
                return strictyaml.load(file.read()).data
        except FileNotFoundError:
            print(f"Error: Configuration file {self.config_path} not found")
            sys.exit(1)
        except strictyaml.YAMLError as e:
            print(f"Error reading configuration file: {e}")
            sys.exit(1)

    def get_bool(self, key, default=False):
        """gets a configuration value as a boolean, handling string values"""
        value = self.settings.get(key, default)
        return str(value).lower() == 'true'

# === PROMPT MODEL ===

class prompt_model:
    """handles loading and managing system prompts"""
    
    def __init__(self, config):
        self.config = config
        self.system_prompt = self.config.settings['system_prompt']

# === OLLAMA MODEL ===

class ollama_model:
    """handles ollama client interactions"""
    
    def __init__(self, config):
        self.config = config
        self.client = ollama.Client()
    
    def generate_response_stream(self, messages):
        """generates response using ollama model, yielding chunks for streaming"""
        try:
            params = {
                'model': self.config.settings['model'],
                'messages': messages,
                'stream': True,
                'options': {
                    'temperature': float(self.config.settings['temperature']),
                    'num_ctx': int(self.config.settings['context_window']),
                    'num_predict': int(self.config.settings['max_predict'])
                }
            }
            if self.config.get_bool('json_output', False):
                params['format'] = 'json'
            
            for chunk in self.client.chat(**params):
                yield chunk

        except Exception as e:
            yield {'message': {'content': f"\nError generating response: {e}\n"}, 'done': True}

# === CHAT VIEW MODEL ===

class chat_view_model:
    """manages conversation state and interactions"""
    
    def __init__(self):
        self.config = config_model()
        self.prompt = prompt_model(self.config)
        self.ollama = ollama_model(self.config)
        self.conversation_history = []
        self._initialize_conversation()
    
    def _initialize_conversation(self):
        """initializes conversation with system prompt"""
        self.conversation_history.append({
            'role': 'system',
            'content': self.prompt.system_prompt
        })

# === CHAT VIEW ===

class chat_view:
    """handles user interface and display"""
    
    def __init__(self):
        self.view_model = chat_view_model()

    def info_header(self):
        """displays info header with configuration settings"""
        config = self.view_model.config.settings
        print()
        print("pymodelchatFx_Fx0001")
        print()
        for key, value in config.items():
            print(f"{key}: {value}")
        print()
        print("=" * 30)
    
    def get_user_input(self):
        """gets user input from command line"""
        user_label = "USER: " if self.view_model.config.get_bool('show_labels', True) else ""
        return input(f"{user_label}").strip()
    
    def run(self):
        """main chat loop"""
        self.info_header()
        
        reasoning_tags = [
            "think", "thinking", "thoughts", "dreaming", "reasoning", "reason",
            "reflecting", "reflection", "contemplating", "contemplation", "cot", "chainofthought"
        ]
        
        while True:
            try:
                user_input = self.get_user_input()
                if not user_input:
                    continue

                self.view_model.conversation_history.append({'role': 'user', 'content': user_input})
                print()  # blank line separator after user input
                
                stream = self.view_model.ollama.generate_response_stream(self.view_model.conversation_history)
                
                if not self.view_model.config.get_bool('reasoning_active', False):
                    # --- Non-reasoning simple streaming ---
                    ai_label = "AI: " if self.view_model.config.get_bool('show_labels', True) else ""
                    print(f"{ai_label}", end="")
                    full_response = ""
                    first_chunk = True
                    for chunk_data in stream:
                        content = chunk_data['message']['content']
                        if first_chunk:
                            content = content.lstrip()
                            first_chunk = False
                        print(content, end="", flush=True)
                        full_response += content
                    print() # final newline for next prompt
                    print() # extra blank line separator between sections
                    self.view_model.conversation_history.append({'role': 'assistant', 'content': full_response})
                    continue

                # --- Real-time Reasoning Stream Parsing ---
                current_state = "INITIAL"
                buffer = ""
                full_response_for_history = ""
                answer_for_history = ""
                active_reasoning_tag = None
                
                reasoning_printed = False
                ai_printed = False
                answer_started = False  # tracks first non-whitespace answer chunk
                reasoning_started = False  # tracks first non-whitespace reasoning chunk

                for chunk_data in stream:
                    content = chunk_data['message']['content']
                    full_response_for_history += content
                    buffer += content
                    
                    if current_state == "INITIAL":
                        for tag in reasoning_tags:
                            open_tag = f"<{tag}>"
                            if open_tag in buffer:
                                reasoning_content = buffer.split(open_tag, 1)[1]
                                buffer = reasoning_content
                                current_state = "REASONING"
                                active_reasoning_tag = tag
                                break
                    
                    if current_state == "REASONING":
                        if not reasoning_printed:
                            print("REASONING: ", end="")
                            buffer = buffer.lstrip()
                            if buffer:
                                reasoning_started = True
                            reasoning_printed = True
                        
                        close_tag = f"</{active_reasoning_tag}>"
                        if close_tag in buffer:
                            reasoning_part, rest = buffer.split(close_tag, 1)
                            if not reasoning_started:
                                reasoning_part = reasoning_part.lstrip()
                                if reasoning_part:
                                    reasoning_started = True
                            print(reasoning_part, end="", flush=True)
                            buffer = rest
                            current_state = "ANSWERING"
                        else:
                            if not reasoning_started:
                                buffer = buffer.lstrip()
                                if buffer:
                                    reasoning_started = True
                            print(buffer, end="", flush=True)
                            buffer = ""

                    if current_state == "ANSWERING":
                        if not ai_printed:
                            print("AI: ", end="")
                            ai_printed = True
                            answer_started = False  # reset for new answer section
                        
                        # remove leading whitespace/newlines before the first answer chunk
                        if not answer_started:
                            buffer = buffer.lstrip()
                            if buffer:
                                answer_started = True

                        if buffer:
                            print(buffer, end="", flush=True)
                            answer_for_history += buffer
                        buffer = ""
                
                # final print for any remaining buffer
                if buffer and current_state == "ANSWERING":
                    if not answer_started:
                        buffer = buffer.lstrip()
                    print(buffer, end="", flush=True)
                    answer_for_history += buffer

                print() # newline for next prompt
                print() # extra blank line separator
                self.view_model.conversation_history.append({'role': 'assistant', 'content': answer_for_history})

            except KeyboardInterrupt:
                print("\n\nExiting chatbot.")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
                break

# === MAIN EXECUTION ===

def main():
    """main application entry point"""
    chatbot = chat_view()
    chatbot.run()

if __name__ == "__main__":
    main()
