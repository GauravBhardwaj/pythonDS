__author__ = 'Gaurav'
import LinkedListNode
from UnorderedList import UnorderedList

#driver code to test logic

linked_list = UnorderedList()

#add at head of linked list
linked_list.add_at_head(4)
linked_list.add_at_head(4)
linked_list.add_at_head(4)
linked_list.add_at_head(4)
linked_list.add_at_head(56)
linked_list.add_at_head(58)
linked_list.add_at_head(4)
linked_list.add_at_head(58)
#add at the tail of linked list
linked_list.add_at_tail(33)

#delete some element
linked_list.delete_element_at(0)

#print contents of linked list
linked_list.print_list()

#delete the duplicate
linked_list.remove_duplicates_with_buffer()
#print contents of linked list
linked_list.print_list()

#length of linked list
print "length of list is: " + str(linked_list.length)

#reverse a linked list
linked_list.reverse_linkedlist()
linked_list.print_list()
#detect a loop in linked list
