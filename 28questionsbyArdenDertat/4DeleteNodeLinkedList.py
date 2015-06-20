#Given a linkedlist of integers and an integer value,
#delete every node of the linkedlist containing that value.
class Node(object):
    def __init__(self, init_data, next=None):
        self.data = init_data
        self.next = next


class Linkedlist(object):
    def __init__(self, head):
        self.head = head

    def delete_value(self,delete_data):
        '''
        compare Given value with all nodes and if found delete it and return the new head
        https://www.cs.bu.edu/teaching/c/linked-list/delete/
        '''
        if not self.head:
            return

        while self.head and self.head.data == delete_data:
            #this handles the consecutive duplicates at the begining
            self.head = self.head.next

        curr = self.head
        prev = None

        while curr:
            if curr.data == delete_data:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

    def delete(self, data):
        '''
        This will delete the first occurence of element encountered
        '''
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


    def print_list(self):
        print "printing list content"
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

#sample list
head = Node(4,Node(4,Node(1,Node(4,Node(4,Node(9,None))))))
l = Linkedlist(head)
#delete value at tail
#l.delete_value(9)
#l.print_list()
#delete value at head
l.delete_value(4)
l.print_list()
#delete duplicate value at mid
l.delete_value(9)
l.print_list()
