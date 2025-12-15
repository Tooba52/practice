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
        pass


    #Delete - No ordering property for binary tree




# Create nodes
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

# root.preorder()
# root.inorder()
# root.postorder()
# root.levelorder()
print(root.height())
print(root.count_nodes())
print(root.count_leaves())
print(root.search_bt(7))
print(root.search_bt(9))