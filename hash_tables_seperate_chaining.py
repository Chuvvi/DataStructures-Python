class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hashvalue = None

class HashTableSeperateChaining:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity cannot be 0 or less")
        self.capacity = capacity
        self.table = [None]*capacity
        self.size = 0
    
    def hashfunc(self, key):
        return (key & 0x7FFFFFFF) % self.capacity

    def hashh(self, new_entry):
        key = new_entry.key
        hash_value = self.hashfunc(key)
        new_entry.hashvalue = hash_value
        return hash_value

    def findsize(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0

    def haskey(self, key):
        hashkey = self.hashh(key)
        if self.table[hashkey] == None:
            return False
        for j in self.table[hashkey]:
            if j == key:
                return True
        return False

    def insert(self, key, value):
        new_entry = Entry(key, value)
        index = self.hashh(new_entry)
        if self.table[index] == None:
            self.table[index] = [new_entry]
        else:
            self.table[index].append(new_entry)
        self.size += 1

    def get(self, key):
        index = self.hashfunc(key)
        if self.table[index] == None:
            return "Key does not exist"
        for i in range(len(self.table[index])):
            current_entry = self.table[index][i]
            if current_entry.key == key:
                return current_entry.value
        return "Key does not exist"
    
    def remove(self, key):
        index = self.hashfunc(key)
        if self.get(key) != False:
            length = len(self.table[index])
            if length == 1:
                self.table[index][0] = None
                self.size -= 1
            else:
                for i in range(length):
                    current_entry = self.table[index][i]
                    if current_entry.key == key:
                        break
                del self.table[index][i]
                self.size -= 1
                return "Key removed"
        else:
            return "Key not present"

    def resize(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity cannot be 0 or less")
        old_capacity = self.capacity
        self.capacity = capacity 
        self.old_table = self.table
        self.table = [None] * self.capacity
        self.size = 0
        for i in range(old_capacity):
            if self.old_table[i] != None:
                length = len(self.old_table[i])
                for j in range(length):
                    current_entry = self.old_table[i][j]
                    key = current_entry.key
                    value = current_entry.value
                    self.insert(key, value)
        self.old_table = None


if __name__ == '__main__':
    a = HashTableSeperateChaining(10)
    print(a.table)
    print(a.isempty())
    print(a.findsize())
    a.insert(69, "Suhas")
    a.insert(9, "Chuvvi")
    a.insert(1, "Hello")
    a.insert(2, "World")
    a.insert(13, "Check")
    print(a.findsize())
    print(a.isempty())
    #a.clear()
    print(a.isempty())
    print(a.get(69))
    print(a.remove(69))
    print(a.get(69))
    print(a.table)
    print(a.get(9))
    print(a.findsize())
    print(a.capacity)
    a.resize(12)
    print(a.get(13))