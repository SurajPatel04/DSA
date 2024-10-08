class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value=None):
        if value is None:
            self.top = None
            self.height =0
        else:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
            
    def printStack(self):
        if self.top is None:
            return None
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        
        self.height -=1
        return temp.value
    
    def is_empty(self):
        if self.height == 0:
            return "Stack is empty"
        else:
            return "Stack is not empty"
        
    def peek(self):
        if self.height == 0:
            return None
        else:
            return self.top.value
        
    def size(self):
        return self.height
    
    def clear(self):
        if self.height == 0:
            return None
        while self.top is not None:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            
        self.height = 0
        
        
stac1 = Stack()
stac2 = Stack(2)
stac2.push(4)
# print(stac2.pop())
# # print("Empty Stack: ", stac1)
# print("Non empty Stack: ")
# stac2.printStack()

# print(stac1.is_empty())
# print(stac2.is_empty())
# print(stac1.peek())
# print(stac2.peek())

# print(stac1.size())

stac2.clear()
stac2.printStack()
print(stac2.is_empty())



