class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class CircularDoublyLinkedList:
    def __init__(self, value = None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail =new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            self.length = 1
            
    def printList(self):
        if self.head is None:
            return None
        
        temp = self.head
        
        while True:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.tail.next = self.head
        self.head.prev = self.tail
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

        self.tail.next = self.head
        self.head.prev = self.tail
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            
        self.length -= 1
        
        return temp.value
    
    def popFirst(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.length  == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        
        self.length -= 1
        return temp.value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
    
        if index > self.length // 2:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
                
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if self.length == index:
            return self.append(value)
        
        if index == 0:
            return self.prepend(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        after = temp.next
        
        temp.next = new_node
        new_node.prev = temp
        
        new_node.next = after
        after.prev = new_node
        
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.popFirst()
        
        if index == self.length -1:
            return self.pop()
        
        before = self.get(index-1)
        temp = before.next
        after = temp.next
        
        before.next = after
        after.prev = before
        
        self.length -= 1
        return temp.value
    
    def reverse(self):
        if self.head is None:
            return None
        
        self.tail.next = None
        self.head.prev = None
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after
        
        self.tail.next = self.head
        self.head.prev = self.tail
        return True
    
    
l2 = CircularDoublyLinkedList()
l2.prepend(0)
l2.append(1)
l2.append(2)
l2.append(3)
l2.append(4)
l2.insert(2,22)
# l2.popFirst()

l2.printList()


print("Change")
l2.reverse()
l2.printList()
print("head prev is: ",l2.head.prev.value)
print("Tail next is: ", l2.tail.next.value)
