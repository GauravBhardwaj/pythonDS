def findNonRepeatedString(s1):
    '''
    :param s1: "tooth"
    :return: (h)
    '''
    list1 = [0]*26
    for ch in s1:
        pos1 = ord(ch)-ord('a')
        list1[pos1] = list1[pos1]+1

    i = 0
    stillOk = True
    while i <len(list1) and stillOk:
        if(i==1):
            stillOk =False

        else:
            i = i+1

    return chr((i+97))


print findNonRepeatedString("aacb")