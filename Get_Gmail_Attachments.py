import email, getpass, imaplib, os, json, signal, sys
from collections import defaultdict

detach_dir = 'mail.json' # directory where to save all the info.
user = raw_input("Enter your GMail username:")
pwd = getpass.getpass("Enter your password: ")

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("[Gmail]/All Mail") # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes

resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check
items = items[0].split() # getting the mails id

dicto = defaultdict(list)

# Signal handeler
def signal_handler(signal, frame):
    print(dicto)
    # with open(detach_dir, 'w') as outfile:
    #     json.dump(dicto, outfile)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
# Add Signal handeler so all the data is saved before ctrl + c or anyinterrupt is executed.


for emailid in items:
    resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(email_body) # parsing the mail content to get a mail object
    print(mail["From"], mail["Subject"])
    dicto[mail["From"]].append(mail["Subject"])
