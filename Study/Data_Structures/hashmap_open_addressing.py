class Hashmap:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.length = 0
        self.buckets = [None] * capacity #create an empty array with set amount of buckets


    def hashFunction(self,key): #return index based of hash function
        return hash(key) % self.capacity

    def __str__(self):
        output = []
        for i, slot in enumerate(self.buckets):
            if slot is None:
                output.append(f"{i}: Empty")
            else:
                key, value = slot
                output.append(f"{i}: ({key}: {value})")
        return "\n".join(output)


    
    def put(self, key, value): #inserting a key value pair into a hashtable
        index = self.hashFunction(key)

        for i in range(self.capacity):
            if self.buckets[index] is None:  #if empty slot insert pair
                self.buckets[index] = (key, value)
                self.length += 1
                return
            
            if self.buckets[index][0] == key:  #update the value if the key is the same
                self.buckets[index] = (key, value)
                return
            
            index = (index + 1) % self.capacity  #find next slot

    def get(self,key): #retrieve the value by the key
        index = self.hashFunction(key)
        if self.buckets[index] ==None:
            return None
        
        return self.buckets[index][1]
    
    def delete(self,key): # remove a key
        index = self.hashFunction(key)

        if self.buckets[index] ==None:
            return None
        
        value= self.buckets[index][1]
        self.buckets[index] = None
        self.length-=1
        return value
    
    def contains(self,key): #returns false or true depending on whether key is found
        for pair in self.buckets:
            if pair != None and pair[0] == key:
                    return True
        return False
    
    def keys(self): #return all keys
        keys = []
        for pair in self.buckets:
            if pair != None:
                keys.append(pair[0])
        return keys
    
    def values(self): #return all values
        values = []
        for pair in self.buckets:
            if pair != None:
                values.append(pair[1])
        return values
    
    def items(self): #return all key value pairs
        items = []
        for pair in self.buckets:
            if pair != None:
                items.append((pair[0],pair[1]))
        return items
    
    def size(self): #returns size
        return self.length
    
    def isEmpty(self): #returns true or false depending on condition 
        return self.length == 0
    
    def clear(self): #clears hashmap
        self.buckets = [None] * self.capacity
        self.length = 0


hashmap = Hashmap(11)
print(hashmap.isEmpty())
print(hashmap.size())
hashmap.put("Mia", 22)
hashmap.put("Len", 20)
hashmap.put("Zoe", 26)
print(hashmap.contains("Tim"))
hashmap.put("Tim", 31)
print(hashmap)
print()
print(hashmap.contains("Tim"))
print()
print(hashmap.keys())
print(hashmap.values())
print(hashmap.items())
print(hashmap.size())
print(hashmap.isEmpty())

#fix methods get and delete as they dont work with open addressing 
