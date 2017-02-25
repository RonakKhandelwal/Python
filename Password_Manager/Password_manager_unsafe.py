#! python 3
# pw.py - An insecure password Manager

PASSWORDS = {'gmail': 'password1',
            'blog': 'password2'
            }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage python pw.py [account] - copy acount password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password copied to clipboard')
else:
    print('No Account Exists')
