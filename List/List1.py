def sum(list_of_numbers):
    '''
    arg -> list of numbers
    return -> sum of numbers
    '''
    sum_of_number = 0
    for number in list_of_numbers:
        sum_of_number += number
    return(sum_of_number)


def multiply(list_of_numbers):
    '''
    arg -> list of numbers
    return -> multiple of numbers
    '''
    mul_of_number = 1
    for number in list_of_numbers:
        mul_of_number *= number
    return(mul_of_number)


list_of_numbers = [1, 2, 3, 4]
print('Sum of Numbers:', list_of_numbers, 'is', sum(list_of_numbers))
print('Multiple of Numbers:', list_of_numbers, 'is', multiply(list_of_numbers))
