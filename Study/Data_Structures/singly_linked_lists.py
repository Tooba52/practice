class Node:
    def __init__(self, data:int):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head= None
        self.tail=None # optional (adding to tail makes TC O(1) instead of O(n))

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def add_to_tail(self,data:int):
        n = Node(data) #Create new node

        if self.head == None: #if empty add the node and return
            self.head = n
            self.tail = n
            return
        
        self.tail.next = n
        self.tail = n

    def add_to_head(self,data:int): #Add node to head
        n = Node(data)#Create new node

        if self.head == None: #if empty add the node and return
            self.head = n
            self.tail=n
            return
        
        n.next = self.head
        self.head = n

    def add_after(self,data:int,insertAfter:int): #Add node to head

        if self.head == None: #if empty create the node and return
            self.head = Node(data)
            return
        
        curr = self.head #create reference
        while curr != None and curr.data != insertAfter: #loop through nodes to find where to insert and we are within the linked list
            curr = curr.next

        if curr == None: #if insertafter is never found
            return

        n = Node(data) #Create new node
        n.next = curr.next
        curr.next = n

    def delete_tail(self):
        if self.head == None: # catches if list is emty
            return 
        
        if self.head.next == None: # catches if there is 1 node in list then deletes it
            self.head = None
            return

        curr = self.head # make reference to head
        next_node = curr.next #make reference to the node after the head

        while next_node.next != None: # loop through until next_node is at the tail
            next_node = next_node.next
            curr= curr.next
        
        curr.next = None # make the node before the end the new tail

    def delete_head(self):
        if self.head == None: # catches if list is emty
            return 
        
        if self.head.next == None: # catches if there is 1 node in list then deletes it
            self.head = None
            return

        to_delete = self.head # make reference to head
        self.head = to_delete.next


    def delete_after(self,deleteAfter:int):
        if self.head == None: # catches if list is emty
            return 
        
        curr = self.head # make reference to head 

        while curr.data != None and curr.data != deleteAfter: #loop until we find wthe node we want to delet after
            curr = curr.next

        if curr == None: #if deleteAfter is never found
            return

        if curr.next == None: #if the node we want to delete after is the tail then there is nothing to delete
            return 
        
        to_delete = curr.next
        curr.next = to_delete.next



sll = SinglyLinkedList()
sll.print_list()
sll.add_to_head(5)
sll.print_list()
sll.add_to_head(9)
sll.print_list()
sll.add_to_head(14)
sll.print_list()
sll.add_after(10,14)
sll.print_list()
sll.delete_tail()
sll.print_list()
sll.delete_head()
sll.print_list()
sll.add_to_tail(5)
sll.print_list()
sll.add_to_tail(7)
sll.print_list()
sll.delete_after(9)
sll.print_list()