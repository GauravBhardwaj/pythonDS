__author__ = 'Gaurav'

import LinkedListNode
import collections

class UnorderedList(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def add_at_tail(self,new_data):
        '''
        adds node at the end of the list, if we had tail pointer
        we could have saved the efforts of traversal, but for now suppose we dont have it
        '''
        new_node = LinkedListNode.Node(new_data)
        if self.length == 0:
            print "List is empty, making this as 1st node"
            self.head = new_node
            self.length += 1
        else:
            print "adding at the tail"
            temp = self.head
            while temp.get_next():
                temp = temp.get_next()
            temp.set_next(new_node)
            new_node.set_next(None)
            self.length += 1

    def add_at_head(self, new_data):
        new_node = LinkedListNode.Node(new_data)
        if self.length == 0:
            print "List is empty, making this as 1st node"
            self.head = new_node
            self.length += 1
        else:
            print "adding at the head of list"
            temp = self.head
            new_node.set_next(temp)
            self.head = new_node
            self.length += 1

    def delete_element_at(self, index):
        temp = self.head
        prev = None
        i = 0
        while temp and i < index:
            prev = temp
            temp = temp.get_next()
            i+=1
        if i == index:
            print "deleting element", temp.get_data()
            #prev.set_next(temp.get_next())
            if not prev:
                print "deleting head element"
                self.head = temp.get_next()
            else:
                prev.set_next(temp.get_next())
            self.length -= 1
        else:
            print "index not found"

    def print_list(self):
        print "printing list content"
        temp = self.head
        while temp:
            print temp.get_data()
            temp = temp.get_next()

    def remove_duplicates_with_buffer(self):
        temp = self.head
        prev = None
        aux_dict = collections.Counter()

        while temp:
            value_here = temp.get_data()
            if aux_dict[value_here]==0:
                #we are making sure that element is being processed only once,
                #because if its one we will simply ignore this element
                aux_dict[value_here] = 1
            else:
                #the element is duplicate
                prev.set_next(temp.get_next())

                self.length -= 1


            prev = temp
            temp = temp.get_next()
            print aux_dict

    def reverse_linkedlist_iterative(self):
        '''
        lets try with three pointers
        '''
        prev = None
        curr = self.head
        while curr:
            nxt = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = nxt

        self.head = prev



    def reverse_in_recurse(self,head,last):
        '''
        use a recursive method, but that would need head pointer in argument
        '''
        temp = head
        if not temp:
            return last
        else:
            temp = temp.get_next()
            temp.get_next() = last
            return reverse_in_recurse(self,temp, last)
        

    def detect_a_loop(self):
        '''
        detects wether this contains a loop or not
        :param head_pointer:
        :return:
        '''
        temp = self.head
        slow_pointer = temp
        fast_pointer = temp

        pass
