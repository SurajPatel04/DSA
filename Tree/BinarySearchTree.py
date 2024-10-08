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
        while True:
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

    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return result

    def preOrder(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result

    def postOrder(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root)
        return result

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


tree = BinarySearchTree(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)

print(tree.BFS())

print("PreOrder: ", tree.preOrder())
print("PostOrder: ", tree.postOrder())
print("Inorder: ", tree.inorder())
# print("With no value: ", tree.root)
# trees = BinarySearchTree(1)
# print("with value: ", trees.root.value)

# tree.insert(3)
# tree.insert(1)

# print(tree.root.value)
# print(tree.root.right.value)
# print(tree.root.left.value)


# print(tree.contain(2))
# print(tree.contain(3))
# print(tree.contain(1))
# print(tree.contain(0))

