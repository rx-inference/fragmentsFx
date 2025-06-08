# PURPOSE: simple command line chatbot using ollama

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

# === PROMPT MODEL ===

class prompt_model:
    """handles loading and managing system prompts"""
    
    def __init__(self, prompt_path="system.prompt"):
        self.prompt_path = prompt_path
        self.system_prompt = self._load_system_prompt()
    
    def _load_system_prompt(self):
        """loads system prompt from file"""
        try:
            with open(self.prompt_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: System prompt file {self.prompt_path} not found")
            sys.exit(1)

# === OLLAMA MODEL ===

class ollama_model:
    """handles ollama client interactions"""
    
    def __init__(self, config):
        self.config = config
        self.client = ollama.Client()
    
    def generate_response(self, messages):
        """generates response using ollama model"""
        try:
            response = self.client.chat(
                model=self.config.settings['model'],
                messages=messages,
                options={
                    'temperature': float(self.config.settings['temperature']),
                    'num_ctx': int(self.config.settings['context_window']),
                    'num_predict': int(self.config.settings['max_predict'])
                }
            )
            return response['message']['content']
        except Exception as e:
            return f"Error generating response: {e}"

# === CHAT VIEW MODEL ===

class chat_view_model:
    """manages conversation state and interactions"""
    
    def __init__(self):
        self.config = config_model()
        self.prompt = prompt_model()
        self.ollama = ollama_model(self.config)
        self.conversation_history = []
        self._initialize_conversation()
    
    def _initialize_conversation(self):
        """initializes conversation with system prompt"""
        self.conversation_history.append({
            'role': 'system',
            'content': self.prompt.system_prompt
        })
    
    def process_user_input(self, user_input):
        """processes user input and generates response"""
        # --- ADD USER MESSAGE ---
        self.conversation_history.append({
            'role': 'user',
            'content': user_input
        })
        
        # --- GENERATE RESPONSE ---
        response = self.ollama.generate_response(self.conversation_history)
        
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
    
    def display_welcome(self):
        """displays welcome message"""
        print("=== OLLAMA CHATBOT ===")
        print("Type 'quit' or 'exit' to end the conversation")
        print("=" * 40)
    
    def get_user_input(self):
        """gets user input from command line"""
        return input("\nYou: ").strip()
    
    def display_response(self, response):
        """displays bot response"""
        print(f"\nBot: {response}")
    
    def run(self):
        """main chat loop"""
        self.display_welcome()
        
        while True:
            user_input = self.get_user_input()
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nGoodbye!")
                break
            
            if not user_input:
                continue
            
            response = self.view_model.process_user_input(user_input)
            self.display_response(response)

# === MAIN EXECUTION ===

def main():
    """main application entry point"""
    try:
        chatbot = chat_view()
        chatbot.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
