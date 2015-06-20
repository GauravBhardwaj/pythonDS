#Given an integer array, output all pairs that sum up to a specific value k
#Valid questions to ask: 1. array contains duplicate ?, shall reverse be considered as valid output ?
import math
import timeit
def pair_sum1(arr,sum):
    '''
    This method will simply take one element and sum up with all other values to check if equals k,
    Time Complexity: O(n^2)
    Space Complexity:O(1), ignore that i am using an extra list of tuples to return the output data,
    it can be ignored to save space
    '''
    if len(arr) < 2:
        return
    retlist = []
    for i in range(0,len(arr)):
        for k in range(1,len(arr)):
            if arr[i]+arr[k]==sum:
                tup = (arr[i],arr[k])
                retlist.append(tup)
    return retlist


def pair_sum2(arr,sum):
    '''
    we will first sort the array and traverse the array from both ends,
    if the sum of first element + last element comes more than K,
    we will decrease the last pointer,
    if it comes less than k we will increase first pointer.
    Time Complexity: O(nlogn) [due to sorting]
    Space Complexity: O(1) [ignore the retlist]
    '''
    if len(arr) < 2:
        return
    sorted_arr = sorted(arr)
    length = len(arr)
    retlist = []
    first = 0
    last = length-1

    for i in range(0,length):

        if sorted_arr[first]+sorted_arr[last] == sum:
            tup = sorted_arr[first],sorted_arr[last]
            retlist.append(tup)
            #print first,last
            first += 1
        elif sorted_arr[first]+sorted_arr[last] < sum:
            first += 1
        elif sorted_arr[first]+sorted_arr[last] > sum:
            last -= 1

    return retlist


def pair_sum3(arr,k):
    '''
    we will use an extra data structure to store the diffrence (k-element) and
    later search to see if that element exists in the arr.
    Time Complexity: O(n)
    Space Complexity:O(n)
    '''
    if len(arr) < 2:
        return
    retlist = []
    diff = []
    for i in range(0,len(arr)):
        if k-(arr[i]) in arr:
            tup = (arr[i], k-(arr[i]))
            retlist.append(tup)

    return retlist


#print pair_sum1(arr,6)
#test with 1
t1 = timeit.Timer("pair_sum1([2,3,9,23,-3,-5,34,3,22,10],6)", "from __main__ import pair_sum1")
print "algo1: ", t1.timeit()
#test with 2
#print pair_sum2([2,3,9,23,-3,-5,34,22,10],6)
t2 = timeit.Timer("pair_sum2([2,3,9,23,-3,-5,34,3,22,10],6)", "from __main__ import pair_sum2")
print "algo2:",t2.timeit()

#test with 3
#print pair_sum3([2,3,9,23,-3,-5,34,22,10],6)
t3 = timeit.Timer("pair_sum3([2,3,9,23,-3,-5,34,3,22,10],6)", "from __main__ import pair_sum3")
print "algo3: ", t3.timeit()

#results:
#algo1:  11.2225921154
#algo2: 4.0871899128
#algo3:  2.69490194321
# algo 3 is the fastest 
