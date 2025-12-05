class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail=None 

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def add_to_tail(self, data:int): #implement with tail pointer for O(1) TC
        n = Node(data) # create new node

        if self.head == None: #if empty rhen create node and return 
            self.head = n
            self.tail = n
            return
        
        self.tail.next = n
        n.prev=self.tail
        self.tail=n

    def add_to_head(self, data:int):
        n = Node(data) # create new node

        if self.head == None: #if empty then create node and return
            self.head = n
            self.tail=n
            return
        
        n.next=self.head
        self.head.prev = n
        self.head = n

    def add_after(self, data:int, insertAfter:int):
        n = Node(data) # create new node

        if self.head == None: #catches if list is empty
            return
        
        curr = self.head
        
        while curr.data !=None and curr.data != insertAfter: #loop through until we find where we want to insert
            curr = curr.next
        
        if curr.next == None: #insertAfter was not found
            return
    
        n.prev=curr
        n.next=curr.next
        curr.next.prev=n
        curr.next=n
        

    def delete_tail(self): # O(1) since we used self.tail otherwise it would be O(n)
        if self.head==None: # catches empty list
            return
        
        if self.head.next==None: #if there is only 1 node remove it
            self.head=None
            return 
        
        toDelete = self.tail
        self.tail=toDelete.prev
        self.tail.next =None


    def delete_head(self):
        if self.head==None: # catches empty list
            return
        
        if self.head.next==None: #if there is only 1 node remove it
            self.head=None
            return 
        
        toDelete = self.head
        self.head=toDelete.next
        self.head.prev = None
        toDelete.next = None


    def delete_after(self,deleteAfter:int):
        if self.head==None or self.head.next == None: # catches empty list or if there is only 1 node
            return
    
        curr = self.head

        while curr != None and curr.data != deleteAfter: #loops through until we find where to delete and makes sure we are within the linked list
            curr = curr.next

        if curr.next==None: #catches if deleteafter was not found
            return
        
        toDelete = curr.next
        curr.next = toDelete.next
        if toDelete.next != None: #in the case that the todelete was the tail already then there is no such node toDelete.next.prev
            toDelete.next.prev = curr
        


dll = DoublyLinkedList()
dll.add_to_head(13)
dll.add_to_tail(2)
dll.print_list()
dll.add_to_tail(9)
dll.print_list()
dll.add_to_tail(4)
dll.print_list()
dll.add_to_head(5)
dll.print_list()
dll.add_to_head(9)
dll.print_list()
dll.add_after(10,2)
dll.print_list()
dll.delete_tail()
dll.print_list()
dll.delete_head()
dll.print_list()
dll.delete_after(2)
dll.print_list()