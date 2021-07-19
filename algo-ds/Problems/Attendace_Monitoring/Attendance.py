class EmpNode:
    """ Employee Class Node to store the Employee details"""

    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.attendance_count = 1
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        if self.emp_id is None:
            return "Empty Node"
        else:
            return "({}:{})".format(self.emp_id, self.attendance_count)

    def swipe(self):
        self.attendance_count += 1


class AttendanceTree:
    """Binary Tree to Hold the Employee Attendance"""

    NodeList = []

    def __init__(self):
        """Default Constructor"""
        self.root = None

    def __repr__(self):
        """Default Print method"""
        if self.root is None:
            return
        else:
            # Empty the list
            self.NodeList.clear()
            # Prepare the list
            self.print_inorder(self.root, 0)
            self.NodeList.sort(key=lambda value: value[0])
            return_str = ""
            # Loop till Height of Tree
            # print(self.NodeList)
            for i in range(self.get_tree_height()):
                str = "{} : ".format(i)
                # Pick Nodes of specific height
                h_nodes = list(filter(lambda x: x[0] == i, self.NodeList))
                for nodes in h_nodes:
                    str += "{} ".format(nodes[1])
                return_str += str + "\n"

        return return_str

    @staticmethod
    def insert(emp_id, node):
        """Recursive Method to insert data in the tree"""
        # Check if Employee Id is less or greater
        if emp_id < node.emp_id:
            if node.left_node is None:
                node.left_node = EmpNode(emp_id)
                # print("<--Assigned Left")
            else:
                # print("<--")
                AttendanceTree.insert(emp_id, node.left_node)
        elif emp_id > node.emp_id:
            if node.right_node is None:
                node.right_node = EmpNode(emp_id)
                # print("-->Assigned Right")
            else:
                # print("-->")
                AttendanceTree.insert(emp_id, node.right_node)
        else:
            # print("Swiped {}".format(emp_id))
            node.swipe()

    def search(self, emp_id, node):
        """Search for an Employee in the Tree"""
        if node is None or emp_id == node.emp_id:
            return node
        elif emp_id > node.emp_id:
            return self.search(emp_id, node.right_node)
        elif emp_id < node.emp_id:
            return self.search(emp_id, node.left_node)

    @staticmethod
    def print_inorder(node, height=0):
        """Print Tree in In-Order """
        if node is not None:
            AttendanceTree.print_inorder(node.left_node, height + 1)  # Traverse left
            AttendanceTree.NodeList.append([height, node])  # Insert Node info in the tuple form
            # print("Height {} : ({},{})".format(height, node.emp_id, node.attendance_count))  # Print the value
            AttendanceTree.print_inorder(node.right_node, height + 1)  # Traverse right
        else:
            # height -= 1
            return

    @staticmethod
    def get_num_nodes(node):
        """This method will count the Total no. of Employees Present in the Tree"""
        total = 0
        if node is None:
            return total
        if node.left_node:
            total += AttendanceTree.get_num_nodes(node.left_node)
        if node.right_node:
            total += AttendanceTree.get_num_nodes(node.right_node)
        return total + 1

    @staticmethod
    def get_height(node):
        """Method to view a node's height in the tree"""
        if node is None:
            return 0
        else:
            return max(AttendanceTree.get_height(node.left_node), AttendanceTree.get_height(node.right_node)) + 1

    def print_tree_info(self):
        """Method to print the Information about the Tree"""
        print("Total no. of Nodes in the Tree : {}".format(self.get_num_nodes(self.root)))
        print("Height of the Tree : {}\n".format(self.get_height(self.root)))

    def get_tree_height(self):
        """Method to view the Tree height"""
        return self.get_height(self.root)

    def _search_id_rec(self, emp_id):
        """Wrapper Search method"""
        if self.root is None:
            print("Tree is Empty")
            return None
        else:
            return self.search(emp_id, self.root)

    def insert_emp(self, emp_id):
        """Wrapper Insert method"""
        if self.root is None:
            self.root = EmpNode(emp_id)
            # print("Assigned Root")
        else:
            self.insert(emp_id, self.root)

    def read_employees_rec(self):
        """Method to read the data from inputPS!.txt file """
        file_name = "inputPS1.txt"
        try:
            f = open(file_name, 'r')
            for line in f.readlines():
                # Condition to prevent any
                if len(line) > 0:
                    self.insert_emp(int(line))
            f.close()
        except FileNotFoundError:
            print("File does not Exists")

    def headcount_rec(self):
        """Method to count the Number of Employees in the Tree"""
        file_name = "outputPS1.txt"
        count = self.get_num_nodes(self.root)
        print("Total no. of Employees today : {}".format(count))
        try:
            f = open(file_name, 'w')
            f.writelines("Total no. of Employees Present today : {}\n".format(self.get_num_nodes(self.root), 0))
            f.close()
        except IOError as e:
            print("Error : {}".format(e))

    def search_id_rec(self):
        """Method to Output the Employee's attendance"""
        input_file = "promptsPS1.txt"
        output_file = "outputPS1.txt"
        with open(input_file, 'r') as fp:
            op = open(output_file, 'a')
            for line in fp.readlines():
                if line.split(":")[0] == "searchId":
                    emp_id = int(line.split(":")[1])
                    # print("Searching for emp_id {}".format(emp_id))
                    if self._search_id_rec(emp_id) is not None:
                        op.writelines("Employee id {} is present today.\n".format(emp_id))
                    else:
                        op.writelines("Employee id {} is absent today.\n".format(emp_id))
            print("Published search results in {}".format(output_file))
            op.writelines("\n")
            op.close()

    def how_often(self):
        """Method to Output the Employee's swipe Information"""
        input_file = "promptsPS1.txt"
        output_file = "outputPS1.txt"
        with open(input_file, 'r') as fp:
            op = open(output_file, 'a')
            for line in fp.readlines():
                if line.split(":")[0] == "howOften":
                    emp_id = int(line.split(":")[1])
                    # print("Tallying swipe for emp_id {}".format(emp_id))
                    node = self._search_id_rec(emp_id)
                    if node is not None:
                        op.writelines(
                            "Employee id {} swiped {} times today and is currently {} office.\n".format(emp_id,
                                                                                                        node.attendance_count,
                                                                                                        "outside" if node.attendance_count % 2 == 0 else "in"))
                    else:
                        op.writelines("Employee id {} did not swipe today.\n".format(emp_id))
            print("Published howOften results in {}".format(output_file))
            op.writelines("\n")
            op.close()

    def traverse_visitor(self, node, max_swipe=(None, 0)):
        """Print Tree and look for max swipe count"""
        if node is None:
            return max_swipe
        else:
            # print(node)
            max_swipe = max_swipe if max_swipe[1] >= node.attendance_count else (node.emp_id, node.attendance_count)
            # print("Comparing max {} ....\n".format(max_swipe[1]))
            left_max_swipe = self.traverse_visitor(node.left_node, max_swipe)
            right_max_swipe = self.traverse_visitor(node.right_node, max_swipe)
            return left_max_swipe if left_max_swipe[1] >= right_max_swipe[1] else right_max_swipe

    def frequent_visitor(self):
        """Method to find the Employees Swiped most"""
        output_file = "outputPS1.txt"
        max_swipe = self.traverse_visitor(self.root)
        print("Maximum swipes {}".format(max_swipe))
        if max_swipe is not None:
            with open(output_file, 'a') as fp:
                fp.writelines(
                    "Employee id {} swiped the most number of times toady with a count of {}\n".format(max_swipe[0],
                                                                                                       max_swipe[1]))

    def print_range_present(self, start_id, end_id):
        """Method to print the Employees in the range"""
        output_file = "outputPS1.txt"
        # Open the file and start writing for the employees found in the range
        with open(output_file, 'a') as fp:
            fp.writelines("Range: {} to {}\n".format(start_id, end_id))
            fp.writelines("Employee Attendance:\n")
            for i in range(start_id, end_id):
                # Search the Node
                emp_node = self._search_id_rec(i)
                if emp_node is not None:
                    # print(emp_node)
                    fp.writelines("{}, {}, {}\n".format(emp_node.emp_id, emp_node.attendance_count,
                                                        "out" if emp_node.attendance_count % 2 == 0 else "in"))

            print("Files written Successfully")


# Test the program
attn_201906 = AttendanceTree()
# attn_201906.insert_emp(139553)
# attn_201906.insert_emp(139554)
# attn_201906.insert_emp(139552)
# attn_201906.insert_emp(139554)
# attn_201906.insert_emp(139551)
# attn_201906.insert_emp(139557)
# attn_201906.insert_emp(139557)
# attn_201906.insert_emp(139557)
# attn_201906.insert_emp(139560)
# attn_201906.insert_emp(139550)
#

attn_201906.read_employees_rec()
attn_201906.print_tree_info()

attn_201906.headcount_rec()

attn_201906.search_id_rec()

attn_201906.how_often()

print(attn_201906)

attn_201906.frequent_visitor()

attn_201906.print_range_present(10, 40)

