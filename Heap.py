class MaxHeap:
    def __init__ (self):
        self.heap = []
        
    def _lef_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def _sink_down(self, index):
        max_index = index
        while True:
            left_child = self._lef_child(index)
            right_child = self._right_child(index)
            if left_child < len(self.heap) and self.heap[max_index] < self.heap[left_child]:
                max_index = left_child
            if right_child < len(self.heap) and self.heap[max_index] < self.heap[right_child]:
                max_index = right_child
            
            if max_index != index:
                self._swap(max_index, index)
                index = max_index
            else:
                return
        
    def remove(self):
        if self.heap is None:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self._sink_down(0)
        
        return max_value
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current,self._parent(current))
            current = self._parent(current)
    
heap = MaxHeap()

heap.insert(95)
heap.insert(75)
heap.insert(80)
heap.insert(55)

heap.insert(60)

heap.insert(50)
print(heap.heap)
heap.insert(100)
print(heap.heap)