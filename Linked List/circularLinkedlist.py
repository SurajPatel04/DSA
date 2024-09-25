class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self, value = None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            
        self.length += 1
        return True
    
    def printLinkedList(self):
        if self.head is None:
            return None
        
        temp = self.head
        
        while temp.next != self.head:
            print(temp.value)
            temp = temp.next
        
l1 = CircularLinkedList(1)
l1.append(2)
l1.append(3)
l1.printLinkedList()