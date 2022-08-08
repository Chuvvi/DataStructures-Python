class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = node()
        self.length = 0

    def push(self, data):
        current_node = self.head
        new_node = node(data)
        if current_node.data == None:
            current_node.data = data
            self.length = 1
        else:
            new_node.next = current_node
            self.head = new_node
            self.length += 1

    def pop(self):
        current_node = self.head
        if self.length == 0:
            print("Error : Stack is empty")
        elif self.length == 1:
            d = current_node.data
            current_node.data = None
            self.length = 0
            return d
        else:
            pop_node = current_node
            self.head = current_node.next
            self.length -= 1
            return pop_node.data
    
    def peek(self):
        current_node = self.head
        return current_node.data

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
    s = stack()
    print(s)
    s.push(10)
    s.push(9)
    s.push(8)
    s.push(7)
    s.push(6)
    s.push(5)
    s.push(4)
    print(s)
    print(s.peek())
    print(s.length)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s, s.peek(), s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s)