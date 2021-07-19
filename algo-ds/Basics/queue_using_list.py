class queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.MAX = 100

    def insert(self, data):
        if data is None:
            print('Enter a valid  Number')
        else:
            if self.MAX == self.front:
                print('Queue overflow...')
            else:
                self.front = 0
                self.rear += 1
                self.queue.append(data)

    def remove(self):
        if self.front != 0:
            print('Queue is Empty')
        else:
            print("front {} real {}".format(self.front, self.rear + 1))
            self.queue = self.queue[1:self.rear + 1]  # Remove first element from the queue
            self.rear -= 1
            if self.rear < 0:
                self.front = -1  # List is empty now

    def __repr__(self):
        if self.front == 0:
            return ", ".join(self.queue)


# Create a new Stactk
q = queue()
while 1 == 1:
    choice = int(input("Enter an Option\n1.\tInsert\t2.\tRemove\t3.\tPrint\t4.\tExit\n"))
    if 1 == choice:
        data = input("Enter data : ")
        q.insert(data)
    elif 2 == choice:
        q.remove()
    elif 3 == choice:
        print(q)
    elif 4 == choice:
        exit()
