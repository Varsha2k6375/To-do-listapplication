import webbrowser
import os

# Path to your index.html file
file_path = os.path.abspath("index.html")

# Open in the default web browser
webbrowser.open_new_tab("file://" + file_path)

print("💖 Opening your Cute To-Do App...")
