def password_is_valid(password):
    exceptions_list = []

    if not password: exceptions_list.append('password should exist')
    if not len(password) > 8: exceptions_list.append('password should be longer than 8 characters')
    if not any(c.islower() for c in password): exceptions_list.append('password should contain a lowercase character')
    if not any(c.isupper() for c in password): exceptions_list.append('password should contain an uppercase character')
    if not any(d.isdigit() for d in password): exceptions_list.append('password should contain a digit')
    
    if exceptions_list: raise Exception(', '.join(exceptions_list))

    return True

def password_is_ok(password):
    print(password + 'is the password')
    try:
        password_is_valid(password)
    except Exception as exceptions_list:
        exceptions_list = str(exceptions_list)
        exceptions_list = exceptions_list.split(', ')
        if 'password should exist' in exceptions_list or 'password should be longer than 8 characters' in exceptions_list:
            return False
        if len(exceptions_list) <= 2: return True
    else:
        return True