

class Node:
    def __init__(self,data:int):
        self.data = data 
        self.next = None

class Stack: #linkedlist based stack
    def __init__(self):
        self.head=None
        self.length=0

    def __str__(self):
        curr = self.head
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return " -> ".join(values) + " -> None"

    def push(self, data): # Push - insert data at the top of thr stack
        n = Node(data)
        n.next=self.head
        self.head = n
        self.length += 1

    def pop(self): # Pop - Deletes last inserted element from the stack and returns it 
        if self.head == None:
            return None
                
        curr = self.head
        self.head = self.head.next
        self.length -= 1
        return curr.data

    def top(self): # Top/Peek - returns the last element without removing it
        if self.head==None:
            return None 
        return self.head.data
    
    def size(self): # Size - returns the number of elements in the stack
        return self.length
    
    def isEmpty(self): # isEmpty - returns True if stack is empty, otherwise False
        return(self.head==None)
    
    def isFull(self): # isFull - returns True if stack is full, otherwise False
        return(False) #LinkedList based stack is never full
    
    def clear(self): # Clear - removes all elements in the stack
        self.head = None
        self.length = 0

stack = Stack()
print("Linked List Based")
stack.push(2)
print(stack)
stack.push(5)
print(stack)
print(stack.pop())
print(stack)
print(stack.top())
print(stack.size())
print(stack.isEmpty())
print(stack.isFull())
stack.push(6)
stack.push(8)
print(stack)
print(stack.isFull())
stack.clear()
print(stack)
