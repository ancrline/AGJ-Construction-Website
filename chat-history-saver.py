# Chat History Saver (Python Script)
#
# This script prompts you to paste your chat history and saves it to a timestamped file in your project folder.
# Usage: Run this script, paste your chat, then press Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) and Enter to save.

import os
from datetime import datetime

# Set the folder and filename pattern
folder = os.path.dirname(os.path.abspath(__file__))
filename = f"chat-history-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
filepath = os.path.join(folder, filename)

print("Paste your chat history below. Press Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) and Enter when done:")

try:
    chat = []
    while True:
        line = input()
        chat.append(line)
except EOFError:
    pass

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(chat))

print(f"Chat history saved to {filepath}")
