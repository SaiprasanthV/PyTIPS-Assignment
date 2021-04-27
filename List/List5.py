def overlapping(list_of_numbers_1, list_of_numbers_2):
    '''
    arg -> list_of_numbers_1, list_of_numbers_2
    return -> returns True if there is a common number in both lists
            else False
    '''
    for num1 in list_of_numbers_1:
        for num2 in list_of_numbers_2:
            if(num1 == num2):
                return True
    return False


list_of_numbers_1 = [1, 2, 3, 4]
list_of_numbers_2 = [4, 5, 6, 7]

print("Checking whether there is common number in", list_of_numbers_1, 'and',
      list_of_numbers_2, ':', overlapping(list_of_numbers_1, list_of_numbers_2))
