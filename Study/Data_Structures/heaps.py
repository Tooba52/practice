class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min 
    
    def __str__(self):
        return str(self.heap)
    
    #helper functions
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    
    def compare(self, child, parent):
        if self.is_min:
            return child < parent
        else:
            return child > parent

        
    def peek(self): # return top value in heap
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up()

    def bubble_up(self):
        i = len(self.heap) - 1

        while i > 0:
            p = self.parent(i)

            if self.compare(self.heap[i], self.heap[p]):
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break


    def delete(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down()
        return root

    def bubble_down(self):
        i = 0
        n = len(self.heap)

        while True:
            left = self.left(i)
            right = self.right(i)
            best = i

            if left < n and self.compare(self.heap[left], self.heap[best]):
                best = left

            if right < n and self.compare(self.heap[right], self.heap[best]):
                best = right

            if best != i:
                self.heap[i], self.heap[best] = self.heap[best], self.heap[i]
                i = best
            else:
                break


heap = Heap(is_min=True)

heap.insert(7)
heap.insert(3)
heap.insert(15)
heap.insert(2)

print(heap)        # [2, 3, 15, 7]
print(heap.peek()) # 2

heap.delete()
print(heap)        # [3, 7, 15]

