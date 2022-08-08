class unionFind():
    def __init__(self):
        self.array = []
        self.dictionary = {}
        self.index = 0

    def add(self, element):
        self.dictionary[element] = self.index
        self.array.append(self.index)
        self.index += 1

    def isasub(self, element1, element2):
        element1_index = self.dictionary[element1]
        element2_index = self.dictionary[element2]
        if self.array[element1_index] == self.array[element2_index]:
            return True
        else:
            return False


    def findparent(self, element):
        if element not in self.dictionary:
            return "KeyError : " + element
        element_root = self.path_compress(element)
        for i in self.dictionary:
            if self.dictionary[i] == element_root:
                return i
        return False

    def path_compress(self, element):
        element_index = self.dictionary[element]
        copy = element_index
        element_root = None
        while True:
            if element_index == self.array[element_index]:
                element_root = element_index
                break
            element_index = self.array[element_index]
        for i in range(len(self.array)):
            if self.array[i] == copy:
                self.array[i] = element_root
        return element_root
        

    def union(self, element1, element2):
        if element1 not in self.dictionary:
            print("KeyError : " + element1)
            exit()
        if element2 not in self.dictionary:
            print("KeyError : " + element2)
            exit()
        if self.isasub(element1, element2) == False:
            element1_root = self.path_compress(element1)
            element2_root = self.path_compress(element2)
            for i in range(len(self.array)):
                if self.array[i] == element2_root:
                    self.array[i] = element1_root

if __name__ == "__main__":
    uf = unionFind()
    uf.add("A")
    uf.add("B")
    uf.add("C")    
    uf.add("D")
    uf.add("E")
    uf.add("F")
    uf.union("A", "B")
    uf.union("B", "C")
    uf.union("D", "E")
    uf.union("F", "B")
    print(uf.dictionary)
    print(uf.array)
    print(uf.findparent("C"))
    print(uf.findparent("O"))