__author__ = 'gbhardwaj'

def isBalanced(symbolString):
    '''
    :param symbolString: "()()()" - balanced == True
    :return:
    '''
    retList = []
    isBalanced = True
    index = 0
    while index < len(symbolString) and isBalanced:
        if symbolString[index] in ['(','{','[']:
            retList.append(symbolString[index])
        elif(symbolString[index] in [')','}',']']):
            if retList:
                retList.pop()
        else:
            pass

        index+=1

    if(retList==[]):
        return True
    else:
        return False

print isBalanced('[{()}(])')







