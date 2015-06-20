__author__ = 'gbhardwaj'

class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def setNext(self,newNext):
        self.next = newNext

    def setData(self,newdata):
        self.data = newdata

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class LinkedList(object):
     def __init__(self):
         self.length = 0
         self.head = None

     def printList(self):
         temp = self.head
         while(temp!=None):
             print temp.getData()
             temp = temp.getNext()

     def addList(self,new_node_data): # case-

     # 1 if list is empty , make this as head
         newNode = Node(new_node_data)
         if(self.length==0):
             print "1st element, make it head"
             self.head = newNode
             self.length+=1
         else:
             temp = self.head
             print "List is not empty, add it to head"
             newNode.next = temp
             self.head = newNode
             self.length+=1

l1 = LinkedList()
print l1.length # no length

#add one node
l1.addList(3)
print l1.length # length =1
l1.addList(5)
print l1.length
l1.addList(7)
print l1.length
l1.addList(67)
print l1.length
l1.addList(77)
print l1.length
l1.printList()
