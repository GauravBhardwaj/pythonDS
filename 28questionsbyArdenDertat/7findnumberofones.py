def count_numberof_ones(x):
    '''
    Given interger find ones in it.
    '''
    count = 0
    while x > 0:
        if x%2 !=0:
            count += 1
        x = x/2
    return count

def find_numberof_ones1(n):
    '''
    Given a binary number find number of one in it, using bit manipulations
    '''
    count = 0
    while n:
        count += n & 1
        n = n >> 1

    return count


def int_to_bin(num, bits=8):
    r = ''
    while bits:
        r = ('1' if num&1 else '0') + r
        bits = bits - 1
        num = num >> 1
    return r

print count_numberof_ones(233)
print find_numberof_ones1(233)
print "binary representation, ", int_to_bin(23)
