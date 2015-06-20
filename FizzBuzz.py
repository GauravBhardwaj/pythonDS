__author__ = 'gbhardwaj'
'''
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
'''

def fizzbuzz(number):
    if(number%15 ==0):
        return "Fizz Buzz"
    elif(number%3==0):
        return "Fizz"
    elif(number%5==0):
        return "Buzz"

    return number



