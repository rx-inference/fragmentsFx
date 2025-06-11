# PURPOSE: simple command line chatbot pymodelchatFx_Fx0001

import ollama
import strictyaml
import os
import sys

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
    
    def generate_response(self, messages, stream_callback=None):
        """generates response using ollama model"""
        try:
            stream_enabled = self.config.get_bool('enable_streaming', False)
            json_enabled = self.config.get_bool('json_output', False)
            
            params = {
                'model': self.config.settings['model'],
                'messages': messages,
                'stream': stream_enabled,
                'options': {
                    'temperature': float(self.config.settings['temperature']),
                    'num_ctx': int(self.config.settings['context_window']),
                    'num_predict': int(self.config.settings['max_predict'])
                }
            }

            if json_enabled:
                params['format'] = 'json'
            
            response = self.client.chat(**params)
            
            if stream_enabled and stream_callback:
                full_response = ""
                for chunk in response:
                    content = chunk['message']['content']
                    full_response += content
                    stream_callback(content)
                return full_response
            else:
                return response['message']['content']
        except Exception as e:
            return f"Error generating response: {e}"

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
    
    def process_user_input(self, user_input, stream_callback=None):
        """processes user input and generates response"""
        # --- ADD USER MESSAGE ---
        self.conversation_history.append({
            'role': 'user',
            'content': user_input
        })
        
        # --- GENERATE RESPONSE ---
        response = self.ollama.generate_response(self.conversation_history, stream_callback)
        
        # --- ADD ASSISTANT RESPONSE ---
        self.conversation_history.append({
            'role': 'assistant',
            'content': response
        })
        
        return response

# === CHAT VIEW ===

class chat_view:
    """handles user interface and display"""
    
    def __init__(self):
        self.view_model = chat_view_model()
    
    def info_header(self):
        """displays info header with configuration settings"""
        config = self.view_model.config.settings
        print("=== quickbotFx ===")
        print()
        print(f"model: {config['model']}")
        print(f"context: {config['context_window']}")
        print(f"max output tokens {config['max_predict']}")
        print(f"temperature: {config['temperature']}")
        print(f"streaming: {config.get('enable_streaming', False)}")
        print(f"json output: {config.get('json_output', False)}")
        print()
        print("=" * 30)
    
    def get_user_input(self):
        """gets user input from command line"""
        user_label = "USER: " if self.view_model.config.get_bool('show_labels', True) else ""
        return input(f"\n{user_label}").strip()
    
    def display_response(self, response):
        """displays bot response"""
        ai_label = "AI: " if self.view_model.config.get_bool('show_labels', True) else ""
        print(f"\n{ai_label}{response}")
    
    def _stream_callback(self, content):
        """callback for streaming response chunks"""
        print(content, end='', flush=True)
    
    def run(self):
        """main chat loop"""
        self.info_header()
        
        while True:
            user_input = self.get_user_input()
            
            if not user_input:
                continue
            
            # --- CHECK STREAMING MODE ---
            if self.view_model.config.get_bool('enable_streaming', False):
                ai_label = "AI: " if self.view_model.config.get_bool('show_labels', True) else ""
                print(f"\n{ai_label}", end='', flush=True)
                response = self.view_model.process_user_input(user_input, self._stream_callback)
                print()  # newline after streaming
            else:
                response = self.view_model.process_user_input(user_input)
                self.display_response(response)

# === MAIN EXECUTION ===

def main():
    """main application entry point"""
    try:
        chatbot = chat_view()
        chatbot.run()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
