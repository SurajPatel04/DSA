class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

        
    def printLinkedList(self):
        temp = self.head
        value = []
        while temp is not None:
            value.append(str(temp.value))
            temp = temp.next
        return " -> ".join(value)
            
            
    def appendLinkedlist(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
                
    def preappend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def popFirst(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        print(temp.value)
        
        if self.head is None:
            self.tail = None
        
        self.length -= 1
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(1,index):
            temp = temp.next
        
        return temp

    def setvalue(self, index, value):
        if index < 0 or self.length > index:
            return None
        temp = self.head
        for _ in range(1, index):
            temp = temp.next
        
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.preappend(value)
        if self.length == index:
            return self.appendLinkedlist(value)
        
        new_node = Node(value)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node
        
        self.length +=1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.popFirst()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)  # Get the node just before the one to remove
        temp = prev.next            # The node to remove

        prev.next = temp.next        # Bypass the node to remove
        temp.next = None             # Optional: Break the link to the next node

        self.length -= 1

        return temp  # Optionally return the removed node or its value
    
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        afetr = temp.next
        before = None
        
        for _ in range(self.length):
            afetr = temp.next
            temp.next = before 
            before = temp
            temp = afetr
    
    def sortedinsert(self, value):
        new_node = Node(value)
        temp = self.head
        while temp.value < new_node.value:
            after = temp
            temp = temp.next
            
            
        new_node.next = after.next
        after.next = new_node
        self.length += 1
        return True
    
    def dubplicate(self):
        temp = self.head
        after = temp.next
        while after is not None:
            if temp.value == after.value:
                after = after.next
                temp.next = after
            else:
                temp = after
                after = temp.next
            
        return "Done"
    
    def valu(self, val):
        # If the list is empty, return None
        if self.head is None:
            return None
        
        # Handle the case where the head node itself needs to be removed
        while self.head is not None and self.head.value == val:
            self.head = self.head.next  # Move head to the next node
        
        temp = self.head
        
        # Iterate through the list
        while temp is not None and temp.next is not None:
            if temp.next.value == val:
                # Remove the next node
                temp.next = temp.next.next
            else:
                # Move to the next node
                temp = temp.next

        return self.head 
            
            
                
                
        
    

                

li = LinkedList(1)
li.appendLinkedlist(2)
li.appendLinkedlist(6)
li.appendLinkedlist(3)
li.appendLinkedlist(4)
li.appendLinkedlist(5)
li.appendLinkedlist(6)
li.sortedinsert(0)
# li.greaterRightRemove()
li.valu(6)
print(li.printLinkedList())



# myLinkedlIST = LinkedList(4)
# myLinkedlIST.appendLinkedlist(10)
# # print(myLinkedlIST.printLinkedList())
# # print(myLinkedlIST.pop())
# # print("After pop: ", myLinkedlIST.printLinkedList())
# myLinkedlIST.preappend(11)
# # print(myLinkedlIST.printLinkedList())
# # print(myLinkedlIST.popFirst())

# # print(myLinkedlIST.printLinkedList())

# print(myLinkedlIST.setvalue(3,5))
# print(myLinkedlIST.printLinkedList())
# myLinkedlIST.insert(1,100)
# myLinkedlIST.insert(2,101)
# myLinkedlIST.insert(0,10)
# myLinkedlIST.insert(6,10111)

# print(myLinkedlIST.printLinkedList())

# myLinkedlIST.remove(2)

# print(myLinkedlIST.printLinkedList())
# # myLinkedlIST.reverse()
# # print("Reverse: ",myLinkedlIST.printLinkedList())

# print("lenght: ", myLinkedlIST.length)

# l1 = LinkedList(1)
# l1.appendLinkedlist(2)
# print(l1.printLinkedList())

# l2 = LinkedList(1)
# l2.appendLinkedlist(2)
# print(l2.printLinkedList())



# print(l1.head.value)

# l3 = LinkedList()
# # l3.appendLinkedlist(1)
# # print(l3.printLinkedList())

# l1.appendLinkedlist(3)
# l1.appendLinkedlist(4)
# l1.appendLinkedlist(5)
# l2.appendLinkedlist(3)
# l2.appendLinkedlist(4)
# l2.appendLinkedlist(5)

# sum = 0



# temp1 = l1.head
# temp2 = l2.head



# print("temp2: ", temp2)
# for i in range(l1.length):
#     sum = temp1.value + temp2.value
#     l3.appendLinkedlist(sum)
#     temp1 = temp1.next
#     temp2 = temp2.next
    
    
# print(l1.printLinkedList())
# print(l3.printLinkedList())


# temp1 = l1.head
# temp2 = l2.head
# sum1 = 0
# for i in range(l1.length):
#     sum1 += temp1.value + temp2.value
#     temp1 = temp1.next
#     temp2 = temp2.next
    
# result = str(sum1)

# slow = l3.head
# fast = l3.head

# l3.appendLinkedlist(11)

# while fast is not None and fast.next is not None:
#     slow = slow.next
#     fast = fast.next.next
# print(l3.printLinkedList())
# print(slow.value)


