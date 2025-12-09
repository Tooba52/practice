class Stack: #array based stack
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

stack = Stack(3)

print("Array Based")
stack.push(2)
print(stack.stack)
stack.push(5)
print(stack.stack)
print(stack.pop())
print(stack.stack)
print(stack.top())
print(stack.size())
print(stack.isEmpty())
print(stack.isFull())
stack.push(6)
stack.push(8)
print(stack.stack)
print(stack.isFull())
stack.clear()
print(stack.stack)
