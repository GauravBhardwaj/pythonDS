#Given an array of integers (positive and negative) find the largest continuous sum
#return the largest sum, start and end
import timeit
def largest_sum1(arr):
    '''
    We will keep swapping the maxsum with cureent sum while traversing the array.
    This doesnt work for negative numbers, so add an extra condition to check that.
    Time Complexity:O(n)
    Space Complexity:O(1)
    '''
    if len(arr)==0:
        return
    currsum = 0
    maxsum = 0

    for i in range(0,len(arr)):
        currsum += arr[i]
        if currsum < 0:
            currsum = 0
        elif currsum > maxsum:
            maxsum = currsum
    return maxsum

#test
print largest_sum1([-2, -3, 4, -1, -2, 1, 5, -3])
t1 = timeit.Timer("largest_sum1([-2, -3, 4, -1, -2, 1, 5, -3])", "from __main__ import largest_sum1")
print "algo1: ", t1.timeit()

#results
#algo1:  1.3080239296
