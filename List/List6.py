def generate_n_chars(number, character):
    '''
    arg -> number, character
    return -> returns the string of n times the character
    '''
    g_char = ''
    for iter in range(number):
        g_char += character
    return g_char


number = 5
character = 'x'
print('Prints the character', character, '->', number,
      'times: /n', generate_n_chars(number, character))
