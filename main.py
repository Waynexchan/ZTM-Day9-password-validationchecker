import re
# At least 8 char long
# contain any sort letters, numbers $%#@
# has to end with a number

def password_validation(password):
    password_pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[$%#@]).{7,}\d$')
    if re.match(password_pattern,password):
        return True
    else:
        return False


password_list = ['31d9888xxx#1','Yesgogo2#', 'Yes@@', 'Ohnon@onon3']
for item in password_list:
    print(f'Is {item} a valid password? {password_validation(item)}')

