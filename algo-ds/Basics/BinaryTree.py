class Node:
    def __init__(self, data=None, root_node=None):
        self.data = data
        self.root_node = root_node  # Null for Root Node
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return repr(self.data)


class Tree:
    # Constructor Class
    def __init__(self, data=None):
        self.root = Node(data)
        self.height = 1 if data is not None else 0

    # Print
    def __repr__(self):
        nodes = []
        tmp = self.root
        while tmp:
            nodes.append(tmp)
            tmp = tmp.left_node

    # Function to insert a value
    def insert(self, data, root):
        # If Root then insert at Top
        if root is None:
            self.root = Node(data)
            self.height = 1
        else:
            if data < root.data:
                # If Left Node is Null then Insert there
                if root.left_node is None:
                    root.left_node = Node(data, root)
                    self.height += 1  # Increase the height
                # Call the function recursively
                else:
                    self.insert(data, root.left_node)
            else:
                # If Left Node is Null then Insert there
                if root.right_node is None:
                    root.right_node = Node(data, root)
                # Call the function recursively
                else:
                    self.insert(data, root.right_node)

    # Function to find a value
    def find(self, data, root):
        node = self.root
        while node.data != data:
            if data > node.data:
                node = node.right_node
            else:
                node = node.left_node
        return node
