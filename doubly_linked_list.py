class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.back = None

class DoublyLinkedList():
    def __init__(self):
        self.head = node()
        self.tail = self.head
        self.inter = self.head #to keep a track of "back" pointer
        self.length = 0
    
    def append(self, data):
        current_node = self.head
        new_node = node(data)
        if current_node.data == None:
            current_node.data = data
            self.inter.back = current_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.back = self.inter.back
            self.inter.back = new_node
            self.tail = new_node
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
                current_node = current_node.next
                current_index += 1
            print(current_node.data)

    def insertbeginning(self, data):
        if self.length == 0:
            self.append(data)
        else:
            current_node = self.head
            new_node = node(data)
            current_node.back = new_node
            new_node.next = current_node
            self.head = new_node
            self.length += 1

    def deletebeginning(self):
        if self.length == 0:
            print("Error : The current list has no elements")
        elif self.length == 1:
            current_node = self.head
            current_node.data = None
            self.length = 0
        else:
            current_node = self.head
            next_node = current_node.next
            next_node.back = None
            self.head = next_node
            self.length -= 1

    def deleteend(self):
        if self.length == 0:
            print("Error : The current list has no elements")
        elif self.length == 1:
            current_node = self.head
            current_node.data = None
            self.length = 0
        else:
            last_node = self.tail
            second_last_node = last_node.back
            second_last_node.next = None
            self.tail = second_last_node
            self.length -= 1

    def insert(self, index, data):
        if index < 0 :
            print("Index can not be less than zero")
        elif index > self.length:
            print("Index overflow")
        elif index == 0:
            self.insertbeginning(data)
        elif index == self.length:
            self.append(data)
        else:
            current_node = self.head
            current_index = 0
            new_node = node(data)
            while current_index != index:
                current_node = current_node.next
                current_index += 1
            previous_node = current_node.back
            new_node.next = current_node
            current_node.back = new_node
            new_node.back = previous_node
            previous_node.next = new_node
            self.length += 1

    def replace(self, index, new_data):
        if index < 0 :
            print("Index can not be less than zero")
        elif index > self.length:
            print("Index overflow")
        else:
            current_node = self.head
            current_index = 0
            while current_index != index:
                current_node = current_node.next
                current_index += 1
            current_node.data = new_data

    def __str__(self):
        current_node = self.head
        a = ""
        if current_node.data == None:
            return "[]"
        while current_node.next != None:
            a += str(current_node.data) + " "
            current_node = current_node.next
        a += str(current_node.data)
        f = "[" + a + "]"
        return f

if __name__ == '__main__':
    
    k = DoublyLinkedList()
    k.append(9)
    k.append(10)
    k.append(11)
    print(k)
    k.deleteend()
    k.deletebeginning()
    print(k)
    k.append(1)
    k.append(2)
    k.append(3)
    k.append(4)
    k.append(5)
    print(k)
    k.insert(3, 0)
    k.append(9)
    print(k)
    k.replace(3, 99)
    print(k)