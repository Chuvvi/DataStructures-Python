class Node:
    def __init__(self, Data = None):
        self.Data = Data
        self.Next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node.Data == None:
            current_node.Data = new_node.Data
            self.length = 1
        else:
            self.tail.Next = new_node
            self.tail = new_node
            self.length += 1

    def insert(self, index, data):
        if index < 0:
            print("Index can not be negative")
        elif index > self.length:
            print("Index overflow")
        else:
            if index == self.length:
                self.append(data)
            else:
                new_node = Node(data)
                current_node = self.head
                current_index = 0
                last_node = current_node
                while current_index != index:
                    last_node = current_node
                    current_node = current_node.Next
                    current_index += 1
                new_node.Next = last_node.Next
                last_node.Next = new_node
                self.length += 1
    
    def get(self, index):
        if index < 0:
            print("Index can not be less than zero")
        elif index >= self.length:
            print("Index overflow")
        else:
            current_node = self.head
            current_index = 0
            while current_index != index:
                current_node = current_node.Next
                current_index += 1
            print(current_node.Data)

    def replace(self, index, new_data):
        if index < 0:
            print("Index can not be less than zero")
        elif index >= self.length:
            print("Index overflow")
        else:
            current_node = self.head
            current_index = 0
            while current_index != index:
                current_node = current_node.Next
                current_index += 1
            current_node.Data = new_data

    def deleteend(self):
        current_node = self.head
        last_node = current_node
        while current_node.Next != None:
            last_node = current_node
            current_node = current_node.Next
        last_node.Next = None
        self.tail = last_node
        self.length -= 1

    def delete(self, index):
        if index < 0:
            print("Index can not be less than zero")
        elif index >= self.length:
            print("Index overflow")
        else:
            if index == self.length - 1:
                self.deleteend()
            else:
                current_node = self.head
                current_index = 0
                while current_index != index:
                    last_node = current_node
                    current_node = current_node.Next
                    current_index += 1
                last_node.Next = current_node.Next
                self.length -= 1

    def __str__(self):
        current_node = self.head
        a = ""
        if current_node.Data == None:
            return "[]"
        while current_node.Next != None:
            a += str(current_node.Data) + " "
            current_node = current_node.Next
        a += str(current_node.Data)
        f = "[" + a + "]"
        return f

if __name__ == '__main__':
    k = SinglyLinkedList()
    k.append(0)
    k.append(1)
    k.append(2)
    print(k)
    print(k.length)
    k.deleteend()
    print(k)
    k.append(3)
    k.append(4)
    k.append(5)
    k.append(6)
    print(k)
    k.delete(3)
    k.append(10)
    print(k)
    k.insert(6, 99)
    print(k)
    k.insert(2, 69)
    print(k)
    k.get(2)
    k.replace(2, 96)
    print(k)
    k.append(990)
    print(k)
    print(k.length)