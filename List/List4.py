def is_member(var,string):
    for char in string:
        if char==var:
            return True
    return False

print(is_member('a','Test'))