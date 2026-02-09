#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    adreess = ' '.join(sys.argv[1:])

# TODO: Get adress from clipboard
else:
    adreess = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adreess)