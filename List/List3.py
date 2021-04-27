def is_palindrome(string):
    '''
    arg -> string
    return -> returns True if it is a palindrome
            else False
    '''
    if(string == string[::-1]):
        return(True)
    return(False)


string = 'radar'
print('Check Palindrome for ', string, ':', is_palindrome(string))
