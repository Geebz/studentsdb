def to_alternating_case(string):
    value = ''
    for elem in string:
        if elem.isupper():
            value += elem.lower()
        elif elem.islower():
            value += elem.upper()
        else:
            value+=elem
    return value


print to_alternating_case('12345adad')

