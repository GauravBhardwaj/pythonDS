import sys
import timeit
__author__ = 'gbhardwaj'
def golf(number):
    '''
    should be a prime
    should be greater than input
    should be a palindrome
    '''
    max_integer = sys.maxint
    for i in xrange(number+1,max_integer):
        if(isPalindrome(i) and isPrime(i)):
            return i
        else:
            pass

def isPrime(number):
    for i in range(2,number):
        if number%i ==0:
            return False
    else:
        return True

def isPalindrome(number):
    m = number
    a =0
    while(m!=0):
        a = m % 10 + a * 10
        m = m / 10

    if(a==number):
        return True
    else:
        return False

def shortIsPalindrome(number):
    return str(number) == str(number)[::-1]

t1 = timeit.Timer("isPalindrome(38683)","from __main__ import isPalindrome")
print ("normal palindrome",t1.timeit(number=1000000),"milliseconds")


t2 = timeit.Timer("shortIsPalindrome(38683)","from __main__ import shortIsPalindrome")
print ("short palindrome",t2.timeit(number=1000000),"milliseconds")


print shortIsPalindrome(101)