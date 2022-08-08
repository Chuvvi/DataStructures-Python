class FenwickTree:
    def __init__(self, values):
        self.values = values
        self.tree = [0] + values
        self.length = len(values)
        for i in range(self.length):
            j = i + self.__LSB(i)
            if j <= self.length:
                self.tree[j] += self.tree[i]

    def __LSB(self, i):
        return i & -i
    
    def sum(self, i):
        s = 0
        while i != 0:
            s += self.tree[i]
            i -= self.__LSB(i)
        return s

    def rangeSum(self, i , j):
        return self.sum(j) - self.sum(i - 1)

    def update(self, index, value):
        while index <= self.length:
            self.tree[index] += value
            index += self.__LSB(index)

if __name__ == '__main__':
    values = [1,2,3,4,5,6]
    ft = FenwickTree(values)
    print(values)
    print(ft.tree)
    '''
    print(ft.sum(5))
    print(ft.rangeSum(4, 5))
    ft.update(3, 4)
    print(ft.tree)
    '''