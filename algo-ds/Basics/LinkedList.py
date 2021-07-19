class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node  # Only for Double Linked List

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    """Single Linked List Implementation"""

    # Constructor method
    def __init__(self):
        self.head = None
        self.size = 0

    # Print method for Class
    def __repr__(self):
        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(repr(tmp))
            tmp = tmp.next_node
        return "[" + ", ".join(nodes) + "] - {" + self.size.__str__() + "}"

    # Get the size
    def get_size(self):
        return self.size

    # is Empty
    def is_empty(self):
        return self.size == 0

    def get(self, key):
        # Get element at the given key
        if (int(key) < 0):
            print("IInvalid Key : {}, should be greater than or equal to 0".format(key))
        elif int(key) > self.size - 1:
            print("Invalid Key : {}, should be an Integer between 0 and {}".format(key, self.size - 1))
        else:
            tmp, pos = self.head, 0
            while tmp and pos < int(key):
                pos, tmp = pos + 1, tmp.next_node
            # Return Data
            return tmp.data

    # Inset method, at the end
    def insert(self, data=None):
        # Assign a value to Head Node if Null
        if self.head is None:
            self.head = Node(data)
            self.size = 1
        else:
            tmp = self.head
            while tmp.next_node is not None:
                tmp = tmp.next_node
            tmp.next_node = Node(data)
            self.size += 1

    # Remove an element from list
    def remove(self, data):
        if data is None:
            print("Invalid data : {}, Should be an Element from List".format(data))
        else:
            tmp, tmp_prev = self.head, None
            while tmp.data != data:
                tmp_prev = tmp
                tmp = tmp.next_node
            if tmp_prev is None:
                self.head = self.head.next_node
            else:
                tmp_prev.next_node = tmp.next_node
            self.size -= 1

    # Insert an element at a given position
    def insertAt(self, at=0, data=None):
        if at > self.size - 1:
            print("Invalid position, cannot exceed size : {}".format(self.size))
        elif at == 0:
            new = Node(data, self.head)
            self.head = new
        else:
            # Traverse to the position
            tmp, i = self.head, 0
            while i < at - 1:
                i += 1
                tmp = tmp.next_node
            new = Node(data, tmp.next_node)
            tmp.next_node = new
            self.size += 1

    # Remove an element at a given position
    def removeAt(self, at=0):
        """Removes an element from the List a given Position"""
        if at > self.size - 1:
            print("Invalid position {}, cannot exceed : {}".format(at, self.size - 1))
        elif at == 0:
            self.size -= 1
            self.head = self.head.next_node
        else:
            tmp, i = self.head, 0
            while i < at - 1:
                i += 1
                tmp = tmp.next_node
            tmp.next_node = tmp.next_node.next_node
            self.size -= 1


class DoubleLinkedList:
    """Double Linked List Implementation"""

    # Constructor method
    def __init__(self):
        self.head = None
        self.size = 0

    # Print method for Class
    def __repr__(self):
        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(repr(tmp))
            tmp = tmp.next_node
        return "[" + ", ".join(nodes) + "] - {" + self.size.__str__() + "}"

    # Get the size
    def get_size(self):
        return self.size

    # is Empty
    def is_empty(self):
        return self.size == 0

    # Get element at the given key
    def get(self, key):
        if (int(key) < 0):
            print("IInvalid Key : {}, should be greater than or equal to 0".format(key))
        elif int(key) > self.size - 1:
            print("Invalid Key : {}, should be an Integer between 0 and {}".format(key, self.size - 1))
        else:
            tmp, pos = self.head, 0
            while tmp and pos < int(key):
                pos, tmp = pos + 1, tmp.next_node
            # Return Data
            return tmp.data

    # Inset method, at the end
    def insert(self, data=None):
        # Assign a value to Head Node if Null
        if self.head is None:
            self.head = Node(data)
            self.size = 1
        else:
            tmp = self.head
            while tmp.next_node is not None:
                tmp = tmp.next_node
            tmp.next_node = Node(data)
            tmp.next_node.prev_node = tmp
            self.size += 1

    # Remove an element form List
    def remove(self, data):
        if data is None:
            print("Invalid data : {}, Should be an Element from List".format(data))
        else:
            tmp = self.head
            print(tmp.data)
            while tmp.data != data:
                print(tmp.data)
                tmp = tmp.next_node
            if tmp == self.head:
                self.head = self.head.next_node
                self.head.prev_node = None
            else:
                tmp.next_node.prev_node = tmp.prev_node
                tmp.prev_node.next_node = tmp.next_node
            self.size -= 1

    # Insert an element at a given position
    def insert_at(self, at=0, data=None):
        if at > self.size - 1:
            print("Invalid position, cannot exceed size : {}".format(self.size))
        elif at == 0:
            new = Node(data, self.head)
            self.head = new
        else:
            # Traverse to the position
            tmp, i = self.head, 0
            while i < at - 1:
                i += 1
                tmp = tmp.next_node
            new = Node(data, tmp.next_node)
            tmp.next_node = new
            new.prev_node = tmp
            self.size += 1

    # Remove an element at a given position
    def remove_at(self, at=0):
        """Removes an element from the List a given Position"""
        if at > self.size - 1:
            print("Invalid position {}, cannot exceed : {}".format(at, self.size - 1))
        elif at == 0:
            self.size -= 1
            self.head = self.head.next_node
        else:
            tmp, i = self.head, 0
            while i < at - 1:
                i += 1
                tmp = tmp.next_node
            tmp.next_node = tmp.next_node.next_node
            tmp.next_node.prev_node = tmp
            self.size -= 1
