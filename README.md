# Advanced GPT Web Chatbot

This is a more advanced version of a GPT chatbot with:

- Web UI using Flask
- Chat history stored in sessions and saved to file
- Reset button to start over

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Replace `"YOUR_OPENAI_API_KEY"` in `app.py` with your actual key.

3. Run the app:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Features

- Persistent chat history (in session + file)
- Clean HTML interface
- Reset conversation button

Enjoy chatting!
