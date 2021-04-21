def overlapping(list1,list2):
    for ele1 in list1:
        for ele2 in list2:
            if(ele1==ele2):
                return True
    return False

list1=[1,2,3,4]
list2=[4,5,6,7]

print(overlapping(list1,list2))