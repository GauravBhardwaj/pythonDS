#There is an array of non-negative integers.
#A second array is formed by shuffling the elements of the first array and
#deleting a random element.Given these two arrays, find which element is
#missing in the second array
import timeit


def find_missing_element1(arr1,arr2):
    '''
    brute force, check if element in first is in others
    Time complexity: O(n2) but considering the complexity of search in list as O(n)
    Space complexity: O(1)
    '''
    for num in arr1:
        if not num in arr2:
            return num

def find_missing_element2(arr1, arr2):
    '''
    create set of both list and find the substraction, its like using inbuilt methods
    Time complexity: O(n) as set diffrence says, its depends on len(s)
    Space complexity: O(1)
    '''
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set1-set2

    return set3

def find_missing_element3(arr1, arr2):
    '''
    since all array numbers are positive , diffrence of sum of both array
    Time complexity: O(n), depends on sum function actually
    Space complexity: O(1)
    '''
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    return sum1-sum2

def find_missing_element4(arr1, arr2):
    '''
    Time complexity: O(n), depends on sum function actually
    Space complexity: O(1)
    '''
    result = 0
    for num in arr1+arr2:
        result ^= num
    return result




arr1 = [4,1,0,2,9,6,8,7,5,3]
arr2 = [6,4,7,2,1,0,8,3,9]
#test 1
print find_missing_element1(arr1, arr2)
t1 = timeit.Timer("find_missing_element1([4,1,0,2,9,6,8,7,5,3], [6,4,7,2,1,0,8,3,9])","from __main__ import find_missing_element1")
print "algo1: ", t1.timeit()
#test 2
print find_missing_element2(arr1, arr2)
t2 = timeit.Timer("find_missing_element2([4,1,0,2,9,6,8,7,5,3], [6,4,7,2,1,0,8,3,9])","from __main__ import find_missing_element2")
print "algo2: ", t2.timeit()
#test3
print find_missing_element3(arr1, arr2)
t3 = timeit.Timer("find_missing_element3([4,1,0,2,9,6,8,7,5,3], [6,4,7,2,1,0,8,3,9])","from __main__ import find_missing_element3")
print "algo3: ", t3.timeit()

#test4
print find_missing_element4(arr1, arr2)
t4 = timeit.Timer("find_missing_element4([4,4,1,0,2,9,6,8,7,5,3], [6,4,4,7,2,1,0,8,3,9])","from __main__ import find_missing_element4")
print "algo4: ", t4.timeit()


#algo1:  1.05260896683
#algo2:  1.42342090607
#algo3:  0.73545217514
#algo4:  1.49461483955

#conclusion says algo3 is fastest but it doesnt handles duplicate, which is a drawback,
#so the bit manipulation works best in duplicate handling
