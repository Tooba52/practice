class StackArray: #array based stack
    def __init__(self,capacity:int):
        self.stack = [] 
        self.capacity = capacity

    def push(self, data): # Push - insert data at the top of the stack
        self.stack.append(data)

    def pop(self): # Pop - Deletes last inserted element from the stack and returns it 
        if self.isEmpty():
            return None
        return self.stack.pop()

    def top(self): # Top/Peek - returns the last element without removing it
        if self.stack == []:
            return None
        return self.stack[-1]
    
    def size(self): # Size - returns the number of elements in the stack
        return len(self.stack)
    
    def isEmpty(self): # isEmpty - returns True if stack is empty, otherwise False
        return(len(self.stack) == 0)
    
    def isFull(self): # isFull - returns True if stack is full, otherwise False
        return(len(self.stack) == self.capacity) 

    def clear(self): # Clear - removes all elements in the stack
        self.stack = []

class Node:
    def __init__(self,data:int):
        self.data = data 
        self.next = None

class StackLinkedList: #linkedlist based stack
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

arrayStack = StackArray(3)
llStack = StackLinkedList()

print("Array Based")
arrayStack.push(2)
print(arrayStack.stack)
arrayStack.push(5)
print(arrayStack.stack)
print(arrayStack.pop())
print(arrayStack.stack)
print(arrayStack.top())
print(arrayStack.size())
print(arrayStack.isEmpty())
print(arrayStack.isFull())
arrayStack.push(6)
arrayStack.push(8)
print(arrayStack.stack)
print(arrayStack.isFull())
arrayStack.clear()
print(arrayStack.stack)


print("Linked List Based")
llStack.push(2)
print(llStack)
llStack.push(5)
print(llStack)
print(llStack.pop())
print(llStack)
print(llStack.top())
print(llStack.size())
print(llStack.isEmpty())
print(llStack.isFull())
llStack.push(6)
llStack.push(8)
print(llStack)
print(llStack.isFull())
llStack.clear()
print(llStack)
