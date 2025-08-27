import pyperclip, re

#It should work for numbers with optional country code fot Poland (+48)
#and for most of emails formats

#Create phone regex.
phone_re = re.compile(r'''(
    (\+48)?  # Optional Country Code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)?  # Optional Separator
    (\d{3})  # Second three digits
    (\s|-|\.)?  # Optional Separator                  
    (\d{3})  # Last three digits
    )''', re.VERBOSE)

#Create email regex.
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # Username
    @  # @ symbol
    [a-zA-Z0-9.-]+  # Domain name
    (\.[a-zA-Z]{2,4})  # Dot-something
    )''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []

for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]], groups[7])
    matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))  
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found')