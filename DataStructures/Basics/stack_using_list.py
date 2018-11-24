class stack:
    def __init__(self):
        self.top = -1
        self.MAX = 100
        self.stack = []

    def push(self, data):
        if data is None:
            print('Enter a valid number')
        else:
            if self.MAX == self.top:
                print('Stack Overflow')
            else:
                self.stack.append(data)
                self.top += 1

    def pop(self):
        if self.top >= 0:
            self.stack.pop()
            self.top -= 1
        else:
            print('Stack is empty')

    def __repr__(self):
        if self.top >= 0:
            return ",".join(self.stack)
        else:
            print('Stact is empty.')


# Create a new Stactk
s = stack()
while 1 == 1:
    choice = int(input("Enter an Option\n1.\tPush\t2.\tPop\t3.\tPrint\t4.\tExit\n"))
    if 1 == choice:
        data = input("Enter data : ")
        s.push(data)
    elif 2 == choice:
        s.pop()
    elif 3 == choice:
        print(s)
    elif 4 == choice:
        exit()
