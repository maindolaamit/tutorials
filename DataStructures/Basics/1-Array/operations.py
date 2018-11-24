class Array:
    """This class Implements the basic Array functionality"""

    def __init__(self, list):
        """Constructor Method of the class"""
        self.list = list
        self.occupied_pos = len(list)

    def __init__(self):
        self.list = []
        self.occupied_pos = 0

    def __repr__(self):
        output = "{"
        if len(self.list) > 0:
            for i in range(len(self.list)):
                if i > 0:
                    output += ","
                output += str(self.list[i])
        else:
            output += "List is empty"
        output += "}"
        print(self.list)

    def insert_at(self, pos=0, data=0):
        """ Insert the element at the given index"""
        if pos < len(self.list):
            self.list.append(None)
            for i in range(len(self.list) - 2, pos, -1):
                self.list[i + 1] = self.list[i]
            self.list[pos] = data
        else:
            print("Invalid index {} : Maximum : {}".format(pos, len(self.list)))

    def insert(self, value):
        """ Insert the element in the List at the end"""
        self.list.append(value)

    def remove_at(self, pos):
        """ Remove value at the given Index """
        if pos < len(self.list):
            for i in range(pos, len(self.list)):
                self.list[i] = self.list[i + 1]
        else:
            print("Invalid index {} : Maximum : {}".format(pos, len(self.list)))

    def remove(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                self.remove_at(i)
                print("Removed {}".format(value))
                return
        print("Value not in the list {}".format(value))


a = Array()
a.insert(5)
a.insert(6)
print(a)
a.insert_at(2, 4)
print(a)
