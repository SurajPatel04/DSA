class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def left_child(self,index):
        return 2 * index +1
    
    def right_child(self, index):
        return 2* index + 2
    
    def parent(self, index):
        return (index -1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def insert(self, value):
        self.heap.append(value)
        
        current = len(self.heap) -1 
        
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
            
            
    def sink_down(self,index):
        max_index = index
        right_child = self.right_child(max_index)
        left_child = self.left_child(max_index)
        if left_child < len(self.heap) and self.heap[max_index] < self.heap[left_child]:
            max_index = left_child
        if right_child < len(self.heap) and self.heap[max_index] < self.heap[right_child]:
            max_index = right_child
            
        if max_index != index:
            self.swap(max_index,index)
            self.sink_down(max_index)
    
    def remove(self):
        if self.heap is None:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self.sink_down(0)
        
        return max_value
    
    
    def heapify(self, arr):
        self.heap = arr
        for i in range(len(arr)//2-1, -1 , -1):
            self.sink_down(i)
            
    
            
heap = MaxHeap()   
# heap.insert(95)
# heap.insert(75)
# heap.insert(80)
# heap.insert(55)

# heap.insert(60)

# heap.insert(50)
# heap.remove()

arr = [54,53,55,52,50]

heap.heapify(arr)
print(heap.heap)