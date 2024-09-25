    class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self, value=None):
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
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contain(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False


tree = BinarySearchTree(2)
# print("With no value: ", tree.root)
# trees = BinarySearchTree(1)
# print("with value: ", trees.root.value)

tree.insert(3)
tree.insert(1)

# print(tree.root.value)
# print(tree.root.right.value)
# print(tree.root.left.value)




print(tree.contain(2))
print(tree.contain(3))
print(tree.contain(1))
print(tree.contain(0))

        