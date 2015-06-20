__author__ = 'gbhardwaj'

def Fibbonacci1(number):
    '''
    Check if the number is a fibooncchi number
    :return: True or False
    '''
    if number < 1:
        return 1
    else:
        return Fibbonacci1(number-1)+Fibbonacci1(number-2)


def Fibbonacci2(number):
    '''
    :param number:
    :return:
    '''
    retList = {0:0, 1:1}
    if number in retList:
        return retList[number]
    retList[number] = Fibbonacci2(number-1)+Fibbonacci2(number-2)
    return retList[number]

def Fibbonacci3(number):
    '''
    :param number:
    :return:
    '''
    a = 0
    b = 1
    for _ in range(number):
        a, b = a, a+b
    return a

print Fibbonacci2(10)
print Fibbonacci3(10)

