def findMinElementInList(inputlist):
    minimumInteger = inputlist[0]

    for element in inputlist:
        if(element < minimumInteger):
            minimumInteger = element
        else:
            pass
    return minimumInteger

print findMinElementInList([5,13,8,22,14,9,89,900])
#print findMinElementInList([0,1,2,3,4,5,6,7])