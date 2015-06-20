__author__ = 'gbhardwaj'

def unique_in_order(iterable):
    '''
    Make two counters , keep second moving until its doesnt match first
    if stops matching store the value where it matched and now move the first counter
    :param iterable:
    :return:
    '''
    inputList = list(iterable)
    returnList = []
    length=len(inputList)
    first = 0
    second = 1
    while (length > 0): #012345
        print first,second, length


        if(inputList[first]==inputList[second]):
            second=second+1
            #returnList.append(trailSecond)


        else:
            #trailSecond = second
            returnList.append(inputList[first])
            print inputList[first]
            first = second
            second=second+1
            if(second == (len(inputList))-1):
                returnList.append(inputList[first])


    #returnList.append()
        length=length-1

    return returnList

print unique_in_order('AAAABBBCCDAABBB')
