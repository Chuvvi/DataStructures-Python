class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class QuadraticProbing:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity cannot be zero or less")
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.load_factor = 0.4
        self.threshold = self.load_factor * self.capacity
        self.size = 0

    def hashfunc(self, index):
        return (index & 0x7FFFFFFF) % self.capacity
    
    def probfunc(self, x):
        return int((x*x + x) / 2)

    def probing(self, index):
        x = 1
        while self.table[index] != None:
            if self.table[index] == "RIP":
                return index
            index = (index + self.probfunc(x)) % self.capacity
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
                    new_index = RIPtrack[0]
                    self.table[new_index] = current_entry
                    self.table[index] = "RIP"
                    index = new_index
                return index
            index = (index + self.probfunc(x)) % self.capacity
            x += 1
        return None
    
    def get(self, key):
        index = self.getIndex(key)
        if index != None:
            return self.table[index].value
        return None

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
            current_entry = old_table[i]
            if current_entry != None:
                if current_entry == "RIP":
                    self.size -= 1
                else:
                    key = current_entry.key
                    index = self.hashfunc(key)
                    index = self.probing(index)
                    self.table[index] = current_entry
        old_table = None
    
    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0

if __name__ == '__main__':
    ht = QuadraticProbing(8)
    ht.insert(1, "Suhas1")
    ht.insert(2, "Suhas2")
    ht.insert(3, "Suhas3")
    print(ht.table)
    ht.insert(17, "Suhas17")
    ht.insert(23, "Suhas23")
    ht.remove(1)
    print(ht.table)
    print("___________________________")
    print(ht.get(17))
    print(ht.table)
