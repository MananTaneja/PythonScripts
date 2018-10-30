# isPhoneAndEmail.py - Finds all the phone numbers and the emails on the clipboard.

import pyperclip, re

# Mathces nummber in formats +91-0000000000 and 0000000000

phoneRegex = re.compile(r'([+91]-)?(\d{10})')

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
       phoneNum = '+91-'+(groups[1])
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


