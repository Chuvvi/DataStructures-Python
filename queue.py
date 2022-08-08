class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.head = node()
        self.tail = self.head
        self.length = 0

    def enqueue(self, data):
        current_node = self.head
        new_node = node(data)
        if current_node.data == None:
            current_node.data = data
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def dequeue(self):
        current_node = self.head
        if self.length == 0:
            return "Error: The queue is empty"
        elif self.length == 1:
            return_data = current_node.data
            current_node.data = None
            self.length = 0
            return return_data
        else:
            return_data = current_node.data
            self.head = current_node.next
            self.length -= 1
            return return_data

    def peek(self):
        current_node = self.head
        return current_node.data

    def contains(self, data):
        current_node = self.head
        while current_node.next != None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        if current_node.data == data:
            return True
        return False

    def remove(self, data):
        if self.contains(data) == True:
            current_node = self.head
            if current_node.data == data:
                if current_node.next == None:
                    current_node.data = None
                    self.length -= 1
                else:
                    self.head = current_node.next
                    self.length -= 1
            previous_node = current_node
            current_node = current_node.next
            while current_node.next != None:
                if current_node.data == data:
                    previous_node.next = current_node.next
                    current_node = current_node.next
                    self.length -= 1
                else:
                    previous_node = current_node
                    current_node = current_node.next
            if current_node.data == data:
                previous_node.next = None
                self.length -= 1        
        else:
            print(data, "does not exist in the given queue")

    def isempty(self):
        if self.length == 0:
            return True
        else:
            return False

    def __str__(self):
        current_node = self.head
        a = ""
        if current_node.data == None:
            return "[]"
        else:
            while current_node.next != None:
                a += str(current_node.data) + " "
                current_node = current_node.next
            a += str(current_node.data)
            f = "[" + a + "]"
            return f

if __name__ == '__main__':
    q = queue()
    print(q)
    print(q.peek())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.contains(1))
    print(q.contains(5))
    q.remove(1)
    print(q)
    print("Peek", q.peek())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print("Length is ", q.length)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.length)
    print(q.peek())
    print(q, q.length)