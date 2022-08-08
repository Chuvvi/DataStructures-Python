class maxHeap():
    def __init__(self):
        self.heap = []

    def leftChild(self, i):
        return (2*i) + 1

    def rightChild(self, i):
        return (2*i) + 2

    def parent(self, i):
        return (i-1)//2

    def length(self):
        return len(self.heap)

    def getValue(self, i):
        return self.heap[i]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        if self.length() == 0:
            return None
        return self.heap[0]

    def add(self, data):
        index = self.length()
        self.heap.append(data)
        while (index != 0):
            p = self.parent(index)
            parent_value = self.getValue(p)
            child_value = self.getValue(index)
            if parent_value < child_value:
                self.swap(p, index)
            index = p

    def maxHeapify(self, i):
        left = self.leftChild(i)
        right = self.rightChild(i)
        if (left <= self.length() - 1 and self.getValue(left) > self.getValue(i)):
            largest = left
        else:
            largest = i
        if (right <= self.length() - 1 and self.getValue(right) > self.getValue(largest)):
            largest = right
        if (largest != i):
            self.swap(largest, i)
            self.maxHeapify(largest)

    def poll(self):
        if self.length() == 0:
            return None
        largest = self.heap[0]
        del self.heap[0]
        self.maxHeapify(0)
        return largest

    def __str__(self):
        if self.length() == 0:
            return "[]"
        a = ""
        for i in self.heap:
            a += str(i)
        f = "[" + a +"]"
        return f

class minHeap():
    def __init__(self):
        self.heap = []

    def rightChild(self, i):
        return 2*i + 1
    
    def leftChild(self, i):
        return 2*i + 2

    def parent(self, i):
        return (i - 1) // 2
    
    def length(self):
        return len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def getValue(self, i):
        return self.heap[i]

    def add(self, i):
        index = self.length()
        self.heap.append(i)
        while (index != 0):
            parent_index = self.parent(index)
            parent_value = self.getValue(parent_index)
            child_value = self.getValue(index)
            if parent_value > child_value:
                self.swap(parent_index, index)
            index = parent_index

    def minHeapify(self, i):
        left_child = self.leftChild(i)
        right_child = self.rightChild(i)
        if (left_child <= self.length() - 1 and self.getValue(left_child) < self.getValue(i)):
            smallest = left_child
        else:
            smallest = i
        if (right_child <= self.length() - 1 and self.getValue(right_child) < self.getValue(smallest)):
            smallest = right_child
        if (smallest != i):
            self.swap(smallest, i)
            self.minHeapify(smallest)

    def poll(self):
        if self.length() == 0:
            return
        smallest = self.getValue(0)
        del self.heap[0]
        self.minHeapify(0)
        return smallest

    def __str__(self):
        if self.length() == 0:
            return "[]"
        a = ""
        for i in self.heap:
            a += str(i)
        f = "[" + a + "]"
        return f

if __name__ == '__main__':
    '''
    mh = maxHeap()
    mh.add(1)
    mh.add(2)
    mh.add(3)
    mh.add(4)
    mh.add(5)
    mh.add(6)
    mh.add(7)
    mh.add(8)
    mh.add(9)
    mh.add(10)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    '''
    mh = minHeap()
    mh.add(1)
    mh.add(2)
    mh.add(3)
    mh.add(4)
    mh.add(5)
    mh.add(6)
    mh.add(7)
    mh.add(8)
    mh.add(9)
    mh.add(10)
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)
    print(mh.poll())
    print(mh)