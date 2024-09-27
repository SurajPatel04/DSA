class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    

class BinarySearchTree:
    def __init__(self, value= None):
        if value is None:
            self.root = None
        else:
            new_node = Node(value)
            self.root = new_node
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    tem
                
        
    