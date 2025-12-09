
class Node:
    def __init__(self,data:int):
        self.data = data 
        self.next = None

class Queue: #linkedlist based queue
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

queue = Queue()

print("Linked List Based")
print(queue.isEmpty())
print(queue.isFull())
queue.enqueue(3)
print(queue)
print(queue.size())
queue.enqueue(2)
queue.enqueue(7)
print(queue)
print(queue.size())
print(queue.isEmpty())
print(queue.isFull())
queue.clear()
print(queue)

