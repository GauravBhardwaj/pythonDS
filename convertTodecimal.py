__author__ = 'gbhardwaj'

retList = []

def convertParser(inputNumber):
    '''
    :param inputNumber: Convert decimal to binary
    :return:
    '''
    while inputNumber > 0:
        rem = inputNumber%2
        retList.append(rem)
        inputNumber = (inputNumber/2)

    return retList

print (convertParser(233))


