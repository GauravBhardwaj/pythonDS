__author__ = 'gbhardwaj'
def checkio(data):
    '''
    Calculate length, see if it has even elements or odd elements
    [1.1.3.40] , length = 4 , median = 4/2 = [3] and 2-1 = [1] median = 1+3/2
    [1,3,4,5,6], median will be
    :param data:
    :return:
    '''
    data.sort()
    length = len(data)
    #print(data,length)
    if length%2==0:
        #even elements
        return float (data[((length)/2)]+data[((length/2)-1)]) / 2

    else:
        return data[(length-1)/2]


#These "asserts" using only for self-checking and not necessary for auto-testing

print checkio([1, 2, 3, 4, 5])
print checkio([3, 1, 2, 5, 3])
print checkio([1, 300, 2, 200, 1])
print checkio([3, 6, 20, 99, 10, 15])
print("Start the long test")
print checkio(range(1000000))
print("The local tests are done.")