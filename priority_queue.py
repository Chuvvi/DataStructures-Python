#naive method
class priorityqueue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.append(data)
    
    def poll(self):
        length = len(self.queue)
        max_val = 0
        if length == 0:
            print("No elements to poll")
        else:
            for i in range(1, length):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            max_value = self.queue[max_val]
            del self.queue[max_val]
            return max_value

    def __str__(self):
        a = ""
        for i in self.queue:
            a += str(i) + " "
        f = "[" + a + "]"
        return f

if __name__ == '__main__':
    pq = priorityqueue()
    pq.add(1)
    pq.add(92)
    pq.add(30)
    pq.add(4)
    print(pq)
    print(pq.poll(), pq)