__author__ = 'gbhardwaj'
def contains_magic_number(list, magic_number):
    if magic_number in list:
         #i == magic_number:
            print "This list contains the magic number."
    else:
            print "This list does NOT contain the magic number."

contains_magic_number(range(10), 5)