def full_name(first_name, last_name, middle=''):
    if middle:
        full = first_name + ' ' + last_name + ' ' + middle
    else:
        full = first_name + ' ' + last_name
    return full.title()
