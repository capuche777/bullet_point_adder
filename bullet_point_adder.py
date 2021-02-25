#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip


text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):
    """ Loop through all indexes in the lies list and add star to each string """
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
