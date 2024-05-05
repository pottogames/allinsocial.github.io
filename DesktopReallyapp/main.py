# Import required libraries
from splash import *
from tkinter import Tk
import webview

# Define a function to go back to the previous page or action
def go_back(event=None):
    # Perform the action to go back here
    webview.evaluate_js("history.back()")  # JavaScript to go back in webview

# Define an instance of tkinter
root = Tk()


# Bind the keyboard shortcut to the root window
root.bind('<F2>', go_back)

# Hide the tkinter window
root.withdraw()

# Open the website in webview
webview.create_window('All in social', 'http://127.0.0.1:8000/')
webview.start()

# Run the tkinter main loop
root.mainloop()