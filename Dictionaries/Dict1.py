def translate(English_list):
    '''
    arg -> English_list
    return -> converts English words into Swedish words and returns them as a list
    '''
    Swedish_list = []
    dictionary = {"merry": "god", "christmas": "jul",
                  "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    for English_word in English_list:
        Swedish_list.append(dictionary[English_word])
    return Swedish_list


English_list = ['merry', 'christmas', 'and', 'happy', 'new', 'year']
Swedish_list = translate(English_list)
print('Convert these English words', English_list,
      'into Swedish words:', Swedish_list)
