class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class doublyLinkedlist:
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
            
    def printList(self):
        if self.head is None:
            return None
        
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def popfirst(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        temp.next = None
        self.length -= 1 
        
        return temp
    
    def pop(self):
        if self.head is None:
            return None
        
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
                
        return temp
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
        
        if self.length - 1 == index:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        after = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = after
        after.prev = new_node
        
        self.length += 1
        return True
    
    
doubly = doublyLinkedlist(5)
doubly.append(9)
doubly.append(10)
doubly.append(11)
doubly.append(12)
doubly.printList()

# print(doubly.get(1))
# print(doubly.get(4))

print("Change")
# doubly.popfirst()
# doubly.pop()

doubly.insert(2,100)
doubly.printList()