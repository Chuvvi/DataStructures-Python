class SuffixArray:
    def __init__(self, string):
        string = string.lower()
        self.string = string
        self.array = self.__selfArray(self.string)
        self.sortedarray = self.__ssort(self.array)
        self.array = self.__selfArray(self.string)
        self.sortedarray.sort()
        self.suffixarray = self.__suffixArray(self.array, self.sortedarray)
        self.lcp = self.__lcp(self.sortedarray)
    
    def __ssort(self, array):
        array.sort()
        return array
    
    def __selfArray(self, string):
        array = []
        for i in range(len(string)):
            array.append(string[i:])
        return array
    
    def __suffixArray(self, original, sarray):
        length = len(original)
        array = [None] * length
        for i in range(length):
            for j in range(length):
                if original[i] == sarray[j]:
                    array[j] = i
                    break
        return array

    def __lcp(self, sarray):
        lcp = [0]
        for i in range(len(sarray) - 1):
            s1, s2 = sarray[i], sarray[i+1]
            count = 0
            l1, l2 = len(s1), len(s2)
            j, k = 0, 0
            while j < l1 and k < l2:
                if s1[j] != s2[k]:
                    break
                count += 1
                j += 1
                k += 1
            lcp.append(count)
        return lcp

if __name__ == '__main__':
    s = "AABBCCDDEEFFFFFFFA"
    sa = SuffixArray(s)
    '''
    print(sa.array)
    print(sa.sortedarray)
    print(sa.suffixarray)
    '''
    lcp = sa.lcp
    print(lcp)
    sum = 0
    for i in lcp:
        sum += i
    print(sum)
    n = len(s)
    unique = (n*(n + 1)/ 2) - sum
    print(unique)