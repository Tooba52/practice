#Hashmap created to handle collisions via chaining 
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Hashmap:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.buckets = [None] * capacity #create an empty array with set amount of buckets
        self.length=0

    def hashFunction(self,key): #return index based of hash function
        return hash(key) % self.capacity
    
    def __str__(self):
        output = []
        for i, node in enumerate(self.buckets):
            chain = []
            curr = node
            while curr:
                chain.append(f"({curr.key}: {curr.value})")
                curr = curr.next
            chain_str = " -> ".join(chain) if chain else "None"
            output.append(f"{i}: {chain_str}")
        return "\n".join(output)

    
    def put(self,key,value): #inserting a key value pair into a hashtable
        index = self.hashFunction(key)
        head = self.buckets[index]

        if head==None: #if empty then add the key value and return 
            self.buckets[index] = Node(key,value)
            self.length+=1
            return

        curr = head
        while curr.next != None:
            curr=curr.next

        curr.next = Node(key,value)
        self.length+=1
        return curr.next
    
    def get(self, key): #retrieve the value by the key
        index = self.hashFunction(key)
        curr = self.buckets[index]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None
    
    def delete(self,key): # remove a key
        index = self.hashFunction(key)
        curr = self.buckets[index]
        prev = None

        while curr: 
            if curr.key == key: # when found break out 
                break 
            prev = curr
            curr=curr.next

        if curr == None: # not found
            return None
        
        if prev == None: #if deleting the head then make the linkedlist start at the node after 
            self.buckets[index] = curr.next
            self.length-=1
        else: #delete middle or last node 
            prev.next = curr.next 
            self.length-=1
        return curr.value
    
    def contains(self,key): #returns false or true depending on whether key is found
        index = self.hashFunction(key)
        curr = self.buckets[index]

        while curr:
            if curr.key == key:
                return True
            curr=curr.next

        if curr==None:
            return False
        
    def keys(self): #return all keys
        keys = []
        
        for node in self.buckets:
            curr = node
            while curr:
                keys.append(curr.key)
                curr = curr.next

        return keys
    
    def values(self): #return all values
        values = []
        
        for node in self.buckets:
            curr = node
            while curr:
                values.append(curr.value)
                curr = curr.next

        return values
    
    def items(self): #return all key-value pairs
        items = []
        
        for node in self.buckets:
            curr = node
            while curr:
                pair = (curr.key,curr.value)
                items.append(pair)
                curr = curr.next

        return items
    

    def size(self):#returns size
        return self.length
    
    def isEmpty(self):#returns true or false depending on condition 
        return self.length == 0
    
    def clear(self): #clears hashmap
        self.buckets = [None] * self.capacity
        self.length = 0


hashmap = Hashmap(11)
print(hashmap.isEmpty())
hashmap.put("Mia", 22)
hashmap.put("Len", 20)
hashmap.put("Zoe", 26)
hashmap.put("Tim", 31)
print(hashmap)
print()
print(hashmap.keys())
print(hashmap.values())
print(hashmap.items())
print(hashmap.size())
hashmap.delete("Zoe")
print(hashmap.items())
print(hashmap.size())
print(hashmap.isEmpty())
hashmap.clear()
print(hashmap)



        



