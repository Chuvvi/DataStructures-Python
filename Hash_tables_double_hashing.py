class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hashvalue = None

class DoubleHashing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.load_factor = 0.4
        self.threshold = int(self.capacity * self.load_factor)