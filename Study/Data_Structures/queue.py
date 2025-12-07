class QueueArray: #array based queue
    def __init__(self,capacity:int):
        self.queue = [] 
        self.capacity = capacity

    def enqueue(self, data): # insert data at the back of the stack
        if self.isFull():
            return False
        self.queue.append(data)
        return True

    def dequeue(self): # Deletes first inserted element from the queue and returns it
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def front(self): # front/Peek - returns the first element without removing it
        if self.isEmpty():
            return None
        return self.queue[0]
    
    def size(self): # Size - returns the number of elements in the queue
        return len(self.queue)
    
    def isEmpty(self): # isEmpty - returns True if queue is empty, otherwise False
        return(len(self.queue) == 0)
    
    def isFull(self): # isFull - returns True if queue is full, otherwise False 
        return(len(self.queue) == self.capacity) 

    def clear(self): # Clear - removes all elements in the stack
        self.queue = []

class Node:
    def __init__(self,data:int):
        self.data = data 
        self.next = None

class QueueLinkedList: #linkedlist based queue
    def __init__(self):
        self.head=None
        self.length=0
        self.tail = None

    def __str__(self):
        curr = self.head
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return " -> ".join(values) + " -> None"

    def enqueue(self, data): # insert data at the back of the queue
        n = Node(data)
        if self.head == None:
            self.head=n 
            self.tail=n 
            self.length +=1
            return 
        
        self.tail.next = n
        self.tail = n
        self.length += 1

    def dequeue(self): #  Deletes first inserted element from the queue and returns it 
        if self.head == None:
            return None
                
        curr = self.head
        self.head = self.head.next
        self.length -= 1
        return curr.data

    def front(self): # front/Peek - returns the first element without removing it
        if self.head==None:
            return None 
        return self.head.data
    
    def size(self): # returns the number of elements in the queue
        return self.length
    
    def isEmpty(self): # returns True if queue is empty, otherwise False
        return(self.head==None)
    
    def isFull(self): # returns True if queue is full, otherwise False
        return(False) #LinkedList based queue is never full
    
    def clear(self): # removes all elements in the queue
        self.head = None
        self.length = 0

arrayQueue = QueueArray(3)
llQueue = QueueLinkedList()

print("Array Based")
print(arrayQueue.isFull())
print(arrayQueue.isEmpty())
arrayQueue.enqueue(2)
arrayQueue.enqueue(3)
print(arrayQueue.queue)
arrayQueue.dequeue()
print(arrayQueue.queue)
arrayQueue.enqueue(6)
arrayQueue.enqueue(1)
arrayQueue.enqueue(14)
print(arrayQueue.queue)
print(arrayQueue.front())
print(arrayQueue.size())
print(arrayQueue.isEmpty())
print(arrayQueue.isFull())

print("Linked List Based")
print(llQueue.isEmpty())
print(llQueue.isFull())
llQueue.enqueue(3)
print(llQueue)
print(llQueue.size())
llQueue.enqueue(2)
llQueue.enqueue(7)
print(llQueue)
print(llQueue.size())
print(llQueue.isEmpty())
print(llQueue.isFull())
llQueue.clear()
print(llQueue)

