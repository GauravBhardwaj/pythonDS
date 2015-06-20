__author__ = 'gbhardwaj'
#keep a slow pointer and a fast point
import sys
def printLoopInSequence(input_sequence):
    fast, slow = 0, 0
    length = len(input_sequence)
    while length > 0:
         print input_sequence[slow]
         print input_sequence[fast]

         fast = fast+2
         slow = slow +1
         length = length - 1


with open(sys.argv[1], 'r') as input:
    lines = input.read().strip().splitlines()
    #print lines
    for sequence in lines:
        #print list(sequence.replace(" ", ""))
        #print list(test.split())
        printLoopInSequence(list(sequence.replace(" ", "")))




