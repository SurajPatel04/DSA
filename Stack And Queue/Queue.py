class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value=None):
        if value is None:
            self.first = None
            self.last = None
            self.length = 0
        else:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length =1
        
    def printQueue(self):
        if self.first is None:
            return None
        
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1
        return True
    
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:   
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp.value
    
    
qu0 = Queue()
qu1 = Queue(1)
qu1.enqueue(2)
qu1.dequeue()
qu1.printQueue()

qu0.enqueue(10)
qu0.dequeue()
qu0.printQueue()