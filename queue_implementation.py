class my_queue:
    def __init__(self):
        self.data = []

    def length(self):
        print(len(self.data))


    def enqueue(self, n):
        if len(self.data) <= 5:
            self.data.append(n)
        else:
            print("overflowed!")

    def dequeue(self):
        if len(self.data) == 0:
            print("underflowed!")
        self.data.pop(0)


queue = my_queue()
print("enqueue start")
queue.enqueue(10)
queue.enqueue(45)
queue.enqueue(43)
print("queue till now : ", end = "")
print(queue.data)
print("dequeue start")
queue.dequeue()
queue.dequeue()
print("queue till now : ", end = "")
print(queue.data)