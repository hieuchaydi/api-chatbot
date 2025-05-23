# chatbot_engine.py
from gpt4all import GPT4All

class ChatBot:
    def __init__(self):
        self.model = GPT4All(
            model_name="tinyllama-1.1b-chat-v1.0.Q2_K.gguf",
            model_path=".",
            allow_download=False
        )

    def ask(self, prompt):
        full_prompt = (
            "You are an English tutor. Correct grammar/spelling mistakes, "
            "and explain difficult words.\n"
            f"Student said: '{prompt}'"
        )
        response = self.model.generate(full_prompt)
        if not response:
            response = "Sorry, I didn't understand that."
        else:
            response = response.replace("Student said:", "").strip()
        print(f"🤖 Bot: {response}")
        return response
