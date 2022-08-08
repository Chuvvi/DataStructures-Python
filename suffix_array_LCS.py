#INCOMPLETE

class Suffix:
    def __init__(self, a):
        self.string = ""
        self.lex = ["#", "$", "%", "!", "&", "(", ")", "*", "+", ",", "-", ".", "/"]
        for i in range(len(a)):
            self.string += a[i] + self.lex[i]
        self.sa = self.__sa(self.string)[len(a):]
        self.lcp = self.__lcp(self.sa)

    def __sa(self, s):
        a = []
        for i in range(len(s)):
            a.append(s[i:])
        a.sort()
        return a

    def __lcp(self, a):
        lcpa = [0]
        for i in range(len(a) - 1):
            count = 0
            j = 0
            while j < len(a[i]) and j < len(a[i + 1]):
                if a[i][j] != a[i + 1][j]:
                    break
                count += 1
                j += 1
            lcpa.append(count)
        return lcpa

if __name__ == '__main__':
    s = Suffix(["abca", "bcad", "daca"])
    print(s.string)
    print(s.sa)
    print(s.lcp)