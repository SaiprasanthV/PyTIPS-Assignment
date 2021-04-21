def is_palindrome(string):
    if(string==string[::-1]):
        return(True)
    return(False)

print(is_palindrome('radar'))