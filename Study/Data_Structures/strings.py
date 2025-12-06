s="example"

#Retrieval
print(f"Retrieval: {s}  ->  {s[0]}") #returns "e"

#Traversal
print("Traversal:")
for char in s: # returns each character in the string
    print(char)

#Searching
print(f"Searching: amp in {s}  ->  {s.find("amp")}, {"amp" in s}") #returns index when found, #returns true or false if it was found

#Concatenation
print(f"Concatenation: {s}  ->  {s + " of string" + " being concatenated"}") # returns as one string 

#Slicing
print(f"Slicing: {s}  ->  {s[2:5]}") # returns characters in the index range

#Replacement
print(f"Replacement: {s}  ->  {s.replace("ex","Ex")}")# replaces first parameter with second

#Case Transformation
print(f"Case Transformation: {s}  ->  {s.upper()}, {s.lower()}") #turns all characters in a string to upper case or lower case 

#Stripping
s1 = "  hello  world  "
print(f"Stripping: {s1}  ->  {s1.strip()}") #removes white space at the beginning and end of a string

#Splitting
s2 = "a,b,c"
print(f"Splitting: {s2}  ->  {s2.split(",")}") #seperates string into substrings using a delimiter 

#Joining
s3 = ["a", "b", "c"]
print(f"Joining: {s3}  ->  {",".join(s3)}") #combines list of string into one 