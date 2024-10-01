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
            self.tail.next = self.head
            self.length = 1
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        
        poped_value = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            
        self.length -= 1
        return poped_value
    
    def popFirst(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.tail.next = self.head
            
        self.length -= 1
        return temp
        
                    
    
    def printLinkedList(self):
        if self.head is None:
            return None
        
        temp = self.head
        
        while True:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set(self,index, value):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.get(index)
        temp.value = value
        
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
        
        if self.length== index:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        after = temp.next
        
        temp.next = new_node
        new_node.next = after
        
        self.length += 1
        
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.popFirst()
        
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index-1)
        remove = temp.next
        after = remove.next
        temp.next = after
        
        self.length -= 1
        return 
    
    def reverse(self):
        if self.head is None:
            return None
                
        self.tail.next = None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
            
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        self.tail.next = self.head
        
        return True
    
        
l1 = CircularLinkedList(1)
l1.append(2)
l1.append(3)
l1.prepend(0)

l1.printLinkedList()

print("Change: ")
# l1.set(3,222)
# l1.set(2,22)
# l1.remove(2)

l1.reverse()
l1.printLinkedList()

print("Tail next: ",l1.tail.next.value)