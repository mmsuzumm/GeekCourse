import re
mail_compile = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email_address):

    try:
        found = mail_compile.findall(email_address)[0]
    except IndexError:
        return f'Неверный мейл {email_address}'  # На случай отсутствия "@"
    else:
        if found:
            name, domain = found
        else:
            raise ValueError(f'Неверный мейл: {email_address}')
        return name, domain


print(email_parse('someone@gmail.com'))
print(email_parse('someone@gmailcom'))
print(email_parse('someonegmail.com'))
