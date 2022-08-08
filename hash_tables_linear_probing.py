class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LinearProbing:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity cannot be zero or less")
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.load_factor = 0.4
        self.threshold = self.load_factor * self.capacity
        self.size = 0

    def hashfunc(self, key):
        return (key & 0x7FFFFFFF) % self.capacity

    def probing(self, index):
        x = 1
        while self.table[index] != None:
            if self.table[index] == "RIP":
                return index
            index = (index + x) % self.capacity
            x += 1
        return index

    def insert(self, key, value):
        if self.getIndex(key) != None:
            index = self.getIndex(key)
            self.table[index].value = value
            return
        new_entry = Entry(key, value)
        index = self.hashfunc(key)
        index = self.probing(index)
        if self.table[index] == "RIP":
            self.size -= 1
        self.table[index] = new_entry
        self.size += 1
        if self.size >= self.threshold:
            self.resize()
        
    def getIndex(self, key):
        index = self.hashfunc(key)
        x = 1
        RIPtrack = []
        while self.table[index] != None:
            current_entry = self.table[index]
            if current_entry == "RIP":
                RIPtrack.append(index)
            if current_entry != "RIP" and current_entry.key == key:
                if RIPtrack != [] and index != RIPtrack[0]:
                    index_new = RIPtrack[0]
                    self.table[index_new] = current_entry
                    self.table[index] = "RIP"
                    index = index_new
                return index
            index = (index + x) % self.capacity
            x += 1
        return None

    def get(self, key):
        index = self.getIndex(key)
        if index != None:
            return self.table[index].value
        return index

    def remove(self, key):
        index = self.getIndex(key)
        if index != None:
            self.table[index] = "RIP"

    def resize(self):
        old_capacity = self.capacity
        self.capacity = 2 * old_capacity
        old_table = self.table
        self.table = [None] * self.capacity
        self.threshold = self.load_factor * self.capacity
        for i in range(old_capacity):
            if old_table[i] != None:
                if old_table[i] == "RIP":
                    self.size -= 1
                else:
                    current_entry = old_table[i]
                    key = current_entry.key
                    index = self.hashfunc(key)
                    index = self.probing(index)
                    self.table[index] = current_entry
        old_table = None
    
    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0

if __name__ == "__main__":
    ht = LinearProbing(10)
    ht.insert(1, "Suhas1")
    ht.insert(2, "Suhas2")
    ht.insert(3, "Suhas3")
    print("Getting key 1:", ht.get(1))
    print(ht.size)
    ht.insert(21, "Suhas21")
    print(ht.size)
    print(ht.getIndex(21))
    print(ht.table)
    ht.remove(1)
    print(ht.table)
    print(ht.get(21))
    print(ht.table)
    ht.clear()
    print(ht.table)