#append(x) - O(1)
print("Append:")
numbers = [1,2,3,4,5,6]
print(numbers)
numbers.append(7) #adds 7 at the end of the list
print(numbers)

#pop/pop(i) - O(1)/O(n)
print("Pop:")
numbers = [1,2,3,4,5,6]
print(numbers)
numbers.pop(3) #removes value 4 at index 3
numbers.pop() #removes last value in the list 6
print(numbers)

#insert(i.x) - O(n)
print("Insert:")
numbers = [1,2,3,4,5,6]
print(numbers)
numbers.insert(0,10) #inserts value 10 at index 0 
print(numbers)

#remove(x) - O(n)
print("Remove:")
numbers = [1,2,3,4,5,6]
print(numbers)
numbers.remove(2) #iremoves first value 2 from list
print(numbers)

#count(x) - O(n)
print("Count:")
numbers = [1,2,3,4,5,6,6,6]
print(numbers.count(6)) #counts occurances of a value in the list

#index(x) - O(n)
print("Index:")
numbers = [1,2,3,4,5,6,6,6]
print(numbers.index(4)) #returns index of value specified

#sort() - O(n log n)
print("Sorted:")
numbers = [6,3,2,4,1,5]
numbers.sort()
print(numbers)

#reverse() - O(n)
print("Reverse:")
numbers = [1,2,3,4,5,6]
numbers.reverse()
print(numbers)

#min() - O(n)
print("Min:")
numbers = [1,2,3,4,5,6]
numbers.reverse()
print(min(numbers))

#max() - O(n)
print("Max:")
numbers = [1,2,3,4,5,6]
print(max(numbers))

#slicing arr[i:j] - O(k)
print("Slicing:")
numbers = [1,2,3,4,5,6]
print(numbers[2:]) # returns from index 2 onwards
print(numbers[:2]) # returns until index 2 
print(numbers[1:4]) # returns from index 1 until index 4