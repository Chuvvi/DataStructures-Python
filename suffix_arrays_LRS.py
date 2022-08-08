class Suffix:
    def __init__(self, s):
        self.string = s
        self.sa = self.__suffixArray(s)
        self.lcp = self.__lcp(self.sa)
        self.lrs = self.__lrs(self.sa, self.lcp)

    def __suffixArray(self, s):
        sa = []
        for i in range(len(s)):
            sa.append(s[i:])
        sa.sort()
        return sa

    def __lcp(self, sa):
        lcp = [0]
        for i in range(len(sa) - 1):
            count = 0
            j = 0
            while j < len(sa[i]) and j < len(sa[i + 1]):
                if sa[i][j] != sa[i + 1][j]:
                    break
                count += 1
                j += 1
            lcp.append(count)
        return lcp

    def __lrs(self, sa, lcp):
        val = max(lcp)
        index = []
        for i in range(len(lcp)):
            if lcp[i] == val:
                index.append(i)
        lrs = []
        for j in index:
            lrs.append(sa[j - 1][:val])
        return lrs

if __name__ == '__main__':
    s = "ABABBAABAA"
    sa = Suffix(s)
    print(sa.sa)
    print(sa.lcp)
    print(sa.lrs)