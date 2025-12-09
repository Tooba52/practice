class Queue: #array based queue
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


queue = Queue(3)

print("Array Based")
print(queue.isFull())
print(queue.isEmpty())
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
queue.dequeue()
print(queue.queue)
queue.enqueue(6)
queue.enqueue(1)
queue.enqueue(14)
print(queue.queue)
print(queue.front())
print(queue.size())
print(queue.isEmpty())
print(queue.isFull())
