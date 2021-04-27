def is_member(letter, word):
    '''
    arg -> letter, word
    return -> returns True if the word has the letter
            else False
    '''
    for char in word:
        if char == letter:
            return True
    return False


letter = 'a'
word = 'Test'
print('Check whether the word', word, 'has',
      letter, ':', is_member(letter, word))
