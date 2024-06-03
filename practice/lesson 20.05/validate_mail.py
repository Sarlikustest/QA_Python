import re

def validate_email(mail):
    mail_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(mail_pattern, mail):
        return False
    return True
print(validate_email('sash_an@mail.ru'))