def sum(list1):
    sum_of_list1=0
    for ele in list1:
        sum_of_list1+=ele
    return(sum_of_list1)

def multiply(list2):
    mul_of_list2=1
    for ele in list2:
        mul_of_list2*=ele
    return(mul_of_list2)

print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))