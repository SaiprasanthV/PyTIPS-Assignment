def character_frequency(string):
    '''
    arg -> string
    print -> prints the frequency of character in the string
    '''
    dictionary = dict()
    print('Frequency of Characters:')
    for letter in string:
        dictionary[letter] = dictionary.get(letter, 0)+1
    print(dictionary)


string = "abbabcbdbabdbdbabababcbcbab"
character_frequency(string)
