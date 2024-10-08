class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self,value):
        new_node = Node(value)
        self.root = new_node
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        
        def create(current_node, new_node):
            if new_node.value == -1:
                return None

            # Try to insert in the left child first
            if current_node.left is None or current_node.left.value == -1:
                current_node.left = new_node
                return True
            # If left is occupied, move to the left child
            elif current_node.left is not None:
                if create(current_node.left, new_node):
                    return True
            
            # If left subtree insertion failed, try the right child
            if current_node.right is None or current_node.right.value == -1:
                current_node.right = new_node
                return True
            # If right is occupied, move to the right child
            elif current_node.right is not None:
                return create(current_node.right, new_node)
            
            return False  # No insertion spot found

        # Start the recursive insertion process
        create(self.root, new_node)
        return True
        
    def inorder(self):
        result = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            
            result.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return result
    
    
t = BinaryTree(1)
t.insert(2)
a = t.insert(4)
t.insert(-1)
t.insert(-1)
t.insert(5)
print(t.inorder())
