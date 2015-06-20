__author__ = 'gbhardwaj'

import sys
with open(sys.argv[1], 'r') as input:
     test_cases = input.read().strip().splitlines()
     print test_cases

for test_number in test_cases:
    print test_number
    retCount = 0
    while test_number>0:
        rem = int(test_number) % 2
        if(rem == 1):
            retCount += 1
        test_number = int(test_number) / 2

    print retCount
