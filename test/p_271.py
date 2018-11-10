#! python3
# mapIt.py - Launches a map in the browser suing an address from the
# command line or clipboard.


import webbrowser, sys, pyperclip

for i in range(len(sys.argv)):
    print('sys.argv[' + str(i) + '] = ' + sys.argv[i])

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
    
webbrowser.open('http://www.google.com/maps/place/' + address)