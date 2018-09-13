import imaplib
from email.parser import Parser
import email
import re
imap_host = 'mail.futunlocked.com'
imap_user = 'account2@futunlocked.com'
imap_pass = 'test'


## open a connection
imap = imaplib.IMAP4_SSL(imap_host)
mail = imap
## login
mail.login(imap_user, imap_pass)
mail.select()
print(mail.select())
# search all emails
result, data = mail.search(None, '(FROM "EA" SUBJECT  "Je EA-beveiligingscode is:")')
# i dont know what this those
ids = data[0] # data is a list.
# i dont know what this those
id_list = ids.split() # ids is a space separated string
# i think it says only get one email and only the latest email
latest_email_id = id_list[-1]
# get the latestes email
typ, data = mail.fetch(latest_email_id, "(RFC822)")
# i dont get this part here i saw raw_email is the same as data
raw_email = data[0][1]
# here i say emailtext is the same as raw_email
emailText =  raw_email
#calling the parser module
parser = Parser()
# email is the same as parser.parsesrt(emailtext)

#show me the emails
email_message = email.message_from_bytes(emailText)
emaiSubject = email_message["Subject"]
emaiSubject2 = emaiSubject[-7:]
print(emaiSubject2)

