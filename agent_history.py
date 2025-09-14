# agent_history.py

class State:
    def __init__(self):
        self.messages = []
        self.summary = ""

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages
