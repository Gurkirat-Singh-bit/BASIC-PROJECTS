########################################################################################################################

# this is a mini project to test your typing speed
# it uses the curses library to create a terminal UI
# it loads a random line from a text file and displays it
# the user types the line and the program calculates the WPM
# the program uses color coding to indicate correct and incorrect characters     Starting : April 14,2025 10:30 PM
# the program also has a start screen and a completion message                   Completion : April 15,2025 12:30 AM
# the program is designed to be run in a terminal

# Note: This program requires the test_material.txt file to be present in the same directory
# The test_material.txt file should contain the text to be used for the typing test
# The text should be one line per test


########################################################################################################################

import curses
from curses import wrapper
import time
import random

def display_text(stdscr, target, current, wpm=0):
    # Display the target text
    stdscr.addstr(target)
    
    # Display the current WPM
    stdscr.addstr(1, 0, f"WPM : {wpm}")

    # Display the typed characters with color coding
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Default to green for correct characters

        if char != correct_char:
            color = curses.color_pair(2)  # Red for incorrect characters

        stdscr.addstr(0, i, char, color)

def start_screen(stdscr):
    # Clear the screen
    stdscr.clear()

    # Display welcome message
    stdscr.addstr("Welcome to the Speed Typing Test", curses.color_pair(3))

    # Display instructions
    stdscr.addstr("\nPress enter to continue or escape to exit..", curses.color_pair(3))

    # Refresh the screen to show changes
    stdscr.refresh()

    # Wait for user input
    key = stdscr.getkey()

def load_text():
    # Open the file with test material
    with open("test_material.txt", "r") as f:
        # Read all lines
        lines = f.readlines()

        # Return a random line with whitespace removed
        return random.choice(lines).strip()

def wpm_test(stdscr):     
    # Load random text from file
    target_text = load_text()

    # Initialize list to store user input
    current_text = []

    # Initialize WPM
    wpm = 0

    # Record start time
    start_time = time.time()

    # Enable non-blocking input
    stdscr.nodelay(True)

    while True:
        # Calculate time passed (minimum 1 second)
        time_escaped = max(time.time() - start_time, 1)

        # Calculate words per minute (assuming 5 chars = 1 word)
        wpm = round((len(current_text) / (time_escaped/60)) / 5)

        # Clear screen before refreshing display
        stdscr.clear()

        # Display the target and current text with WPM
        display_text(stdscr, target_text, current_text, wpm)

        # Refresh screen to show changes
        stdscr.refresh()

        # Check if the typing test is completed
        if "".join(current_text) == target_text:

            # Disable non-blocking input
            stdscr.nodelay(False)
            break

        try:
            # Get user input
            key = stdscr.getkey()
        except:
            # No key pressed, continue loop
            continue
        
        # Check for escape key
        if key == "\x1b" or key == "KEY_ESCAPE":
            break
            
        # Handle backspace
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        # Handle regular character input
        elif len(key) == 1 and len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    # Set up color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # For correct characters
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # For incorrect characters
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # For UI elements

    # Show the start screen
    start_screen(stdscr)

    while True:
        # Run the typing test
        wpm_test(stdscr)

        # Display completion message
        stdscr.addstr(3, 0, "you completed the test", curses.color_pair(3))

        # Display instructions for next action
        stdscr.addstr(3, 0, "Press escape key to exit or any key to continue again", curses.color_pair(3))

        # Get user input
        key = stdscr.getkey()

        # Exit if escape key is pressed
        if key == "\x1b" or key == "KEY_ESCAPE":
           break
        
# Start the curses application
wrapper(main)

##############################################################################################################################