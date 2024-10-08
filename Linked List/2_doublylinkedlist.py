class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    
class DoublyLinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length =0
        else:
            new_node = Node(value)
            self.tail = new_node
            self.head = new_node
            self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length +=1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        
        
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -=1
        
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp.value
    
    def printList(self):
        if self.head is None:
            return None
        
        temp = self.head
        
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
            
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length +=1 
        return True
    
    def popFirst(self):
        if self.head is None:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
        
        temp.next = None
        self.length -= 1
        return temp    

    def get(self,index):
        if index < 0 or index >= self.length:
             return None
        temp = self.head
        if index<self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
            
        return temp
        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >self.length:
            return False
        
        if self.length == index:
            return self.append(value)
        
        if index == 0:
            return self.prepend(value)
        
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.popFirst()
        
        if index == self.length-1:
            return self.pop()
        
        before = self.get(index-1)
        temp = before.next
        after = temp.next
        
        before.next = after
        after.prev = before
        
        # or
        
        # temp  = self.get(index)
        # temp.next.prev = temp.prev
        # temp.prev.next = temp.next
        # temp.next = None
        # temp.prev = None
        
        self.length -= 1
        return temp.value
        
    def reverse(self):
        if self.head is None:
            return None
        temp =self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp.prev = after
            temp = after
    
    def sortedinsert(self, value):
        new_node = Node(value)
        temp = self.head
        while temp.next.value < value:
            temp = temp.next
        
        temp.next.prev = new_node
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp
        
        self.length += 1

l1 = DoublyLinkedList(1)
l1.append(2)
l1.append(4)
l1.sortedinsert(3)

# l1.popFirst()
# l1.prepend(0)
# l1.popFirst()
l1.printList()
        
            
            
        
