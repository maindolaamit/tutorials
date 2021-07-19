from DataStructures.LinkedList import LinkedList, Node


class Set:
    """Implementation of Set"""

    # Constructor Method
    def __init__(self, data=None):
        self.head = None
        self.size = 0
        if data is not None:
            if isinstance(data, list):
                for i in data:
                    self.insert(i)
            else:
                print("Pass a valid List of values")

    # Print the
    def __repr__(self):
        if self.size == 0:
            return "[Empty Set]"

        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(repr(tmp))
            tmp = tmp.next_node
        return "[" + ", ".join(nodes) + "] - {" + self.size.__str__() + "}"

    # Insert an element in the set
    def insert(self, data):
        if data is None:
            print("Invalid data : {}, Should be an Int value".format(data))
        else:
            if self.size == 0:
                self.head = Node(data)
            else:
                tmp = self.head
                while tmp.data < data and tmp.next_node:
                    tmp = tmp.next_node

                if tmp.data > data:
                    new = Node(data, tmp, tmp.prev_node)
                    # Check if getting inserted at the top
                    if tmp.prev_node is None:
                        self.head = new
                    else:
                        tmp.prev_node.next_node = new
                    tmp.prev_node = new
                elif tmp.data < data:
                    new = Node(data, tmp.next_node, tmp)
                    tmp.next_node = new
                else:
                    return
            self.size += 1

    # Remove an element from the set
    def remove(self, data):
        if data is None:
            print("Invalid data : {}, Should be an Int value".format(data))
        else:
            if self.size == 0:
                print("Set is Empty")
            else:
                tmp = self.head
                while not tmp.data == data and tmp.next_node:
                    tmp = tmp.next_node
                if (data == tmp.data):
                    if tmp.prev_node is None:
                        self.head = tmp.next_node
                    else:
                        # set only if next element exists
                        if tmp.next_node is not None: tmp.next_node.prev_node = tmp.prev_node
                        tmp.prev_node.next_node = tmp.next_node  # Reset previous node
                    self.size += -1
                else:
                    print("{} : Element not present in Set".format(data))

    # Union of Set
    def union(self, s2):
        tmp = s2.head
        while tmp:
            self.insert(tmp.data)
            tmp = tmp.next_node

    # Subtract of set
    def subtract(self, s2):
        if self.size == 0:
            print("Set is Empty")
        else:
            s2_node = s2.head
            while s2_node:
                # Loop for element in Set
                tmp = self.head
                while not tmp.data == s2_node.data and tmp.next_node:
                    tmp = tmp.next_node
                if s2_node.data == tmp.data:
                    if tmp.prev_node is None:
                        self.head = tmp.next_node
                    else:
                        # set only if next element exists
                        if tmp.next_node is not None:
                            tmp.next_node.prev_node = tmp.prev_node
                        tmp.prev_node.next_node = tmp.next_node  # Reset previous node

                    self.size += -1
                s2_node = s2_node.next_node

    # Intersect of set
    def intersect(self, s2):
        if self.size == 0:
            print("Set is Empty")
        else:
            s2_node = s2.head
            while s2_node:
                # print("Checking for {}".format(s2_node.data))
                # Loop for element in Set
                node = self.head
                while node and node.data < s2_node.data:
                    if node.prev_node is None:
                        self.head = node.next_node
                    else:
                        # set only if next element exists
                        if node.next_node is not None:
                            node.next_node.prev_node = node.prev_node
                        node.prev_node.next_node = node.next_node  # Reset previous node

                    self.size += -1
                    node = node.next_node
                # print(self)
                s2_node = s2_node.next_node


# Test
s = Set()
s.insert(2)
s.insert(1)
s.insert(3)
s.insert(10)
s.insert(4)
s.insert(6)
s.insert(9)
s.insert(9)
s.insert(9)
s.insert(12)
s.remove(9)
s.remove(1)
s.remove(12)
print(s)

s1 = Set([0, 8, 4, 3])
print(s1)
print("\nTesting Intersect...")
s1.intersect(s)
print(s1)
