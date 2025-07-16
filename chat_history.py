import os
import json

HISTORY_FILE = "utils/chat_data.json"

def save_chat(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def load_chat():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []
