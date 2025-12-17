class TreeNode:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None


    #Preorder = root -> left -> right
    def preorder(self):
        print(self.value) #print root

        if self.left:
            self.left.preorder() #go left
        if self.right:
            self.right.preorder() #go right


    #Inorder = left -> root -> right
    def inorder(self):
        if self.left:
            self.left.inorder() # go left

        print(self.value) #print root


        if self.right:
            self.right.inorder() #go right


    #Postorder = left -> right -> root
    def postorder(self):
        if self.left:
            self.left.postorder() # go left
        if self.right:
            self.right.postorder() #go right

        print(self.value) #print root


    #Levelorder = top -> bottom, left -> right
    def levelorder(self):
        queue = [self] #start at root

        while queue: #we there are still nodes in the queue to print
            node = queue.pop(0) #remove the node in the queue
            print(node.value) #print the removed node

            if node.left:
                queue.append(node.left) #add the left child of the removed node to the queue

            if node.right:
                queue.append(node.right) #add the right child of the removed node to the queue


    #Height
    def height(self):
        left_height = self.left.height() if self.left else -1 #if there is a left child calculate the height of that child
        right_height = self.right.height() if self.right else -1 #if there is a right child calculate the height of that child
        return 1 + max(left_height,right_height) #return the longer subtree and increment 1 to include the root


    #Count nodes
    def count_nodes(self):
        left_count = self.left.count_nodes() if self.left else 0 #count nodes of left subtree
        right_count = self.right.count_nodes() if self.right else 0 #count nodes of right subtree
        return 1 + left_count + right_count #return both counts and increment 1 for the root


    #Count leaves
    def count_leaves(self):
        if not self.left and not self.right: # if tree is a single node return 1
            return 1
    
        left_count = self.left.count_leaves() if self.left else 0 #count leaves of left subtree
        right_count = self.right.count_leaves() if self.right else 0 #count leaves of right subtree
        return left_count + right_count #return both counts and increment 1 for the root


    #Search - No ordering property for binary tree
    def search_bt(self,target):
        if self.value==target: # if target is found at root return True immiditaley
            return True
        if self.left and self.left.search_bt(target): #if the value is found in left subtree return True
            return True
        if self.right and self.right.search_bt(target): #if the value is found in right subtree return True
            return True
        return False #not found


    #Insert - No ordering property for binary tree
    def insert_bt(self,value):
        queue = [self] #start at root

        while queue: #while there are still nodes in the queue to print
            node = queue.pop(0) #remove the node in the queue and store

        if node.left == None: # if left child empty → insert
            node.left = TreeNode(value)
            return

        if node.right == None: # if right child empty → insert
            node.right = TreeNode(value)
            return
            


    #Delete - No ordering property for binary tree
    def delete_bt(self,target):
        queue = [self]
        node_to_delete = None
        last = None

        while queue: #loop through to find the node to delete
            last = queue.pop(0)

            if last.value == target: #if we find node to delete update variable
                node_to_delete = last

            if last.left: #if there is a left subtree add the node to the queue
                queue.append(last.left)

            if last.right: #if there is a right subtree add the node to the queue
                queue.append(last.right)


        if node_to_delete: #if we found the node to delete remove it 
            node_to_delete.value = last.value
            last.value = None


    def search_bst(self, target):
        if self.value == target: #if we find the value return True
            return True

        if target < self.value: #if the value is less then the nodes value then we move left
            if self.left: #check if subtree exists, then recursively search it
                return self.left.search_bst(target)
            else:
                return False
        else:  #if it is greater then we move right
            if self.right: #check if subtree exists, then recursively search it
                return self.right.search_bst(target)
            else:
                return False
            

    def insert_bst(self,value):
        if value < self.value: # if the value is smaller then the nodes value move left
            if self.left: #check if subtree exists, then recursively move through till we find an empty space and insert
                self.left.insert_bst(value)
            else:
                self.left = TreeNode(value)
        elif value > self.value: #if it is greater then we move right
            if self.right: #check if subtree exists, then recursively move through till we find an empty space and insert
                self.right.insert_bst(value)
            else:
                self.right = TreeNode(value)
        

    def find_min(self): #helper function to find the minimum value node in a subtree 
        current = self
        while current.left:
            current = current.left
        return current
    

    def delete_bst(self, value): # 3 cases
        if value < self.value: # if the value is smaller then the nodes value move left
            if self.left: #check if subtree exists, then recursively move through it
                self.left = self.left.delete_bst(value)
        elif value > self.value: #if it is greater then we move right
            if self.right: #check if subtree exists, then recursively move through it
                self.right = self.right.delete_bst(value)

        else: # node to delete is found

            # Case 1: No children
            if not self.left and not self.right:
                return None

            # Case 2: One child
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self.right.find_min()
            self.value = successor.value
            self.right = self.right.delete_bst(successor.value)

        return self



# Create nodes
root = TreeNode(5)
for v in [3, 7, 2, 4, 8]:
    root.insert_bst(v)
print(root.search_bst(4))  
print(root.search_bst(10)) 
root.insert_bst(6)
print(root.inorder())
root.delete_bst(3)
print(root.inorder())


