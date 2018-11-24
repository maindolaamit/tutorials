"""
View the Problem statement from the below link
https://www.codechef.com/problems/CERSOL
"""

# Define variables
num_test_cases = 0
# Get the Number of Test cases
while not 1 <= num_test_cases <= 500:
    num_test_cases = int(input("1<= Test cases <= 500\nEnter the number of Test Cases : "))

print()
for t in range(num_test_cases):
    num_soldiers, num_comm_link, num_classes = 0, 0, 0
    # Get the Number of Soldiers, Communication Link and Soldier's classes
    while not (1 <= num_soldiers <= 2500 and num_comm_link == (num_soldiers - 1) and 1 <= num_classes <= 10):
        num_soldiers, num_comm_link, num_classes = [int(i) for i in input(
            "1 <= soldiers <= 2500\n0 <= communication links\n1 <= classes <= 10\ne.g. : 10 9 8\nEnter the number of "
            "Soldiers, Communication links and classes : ").split(" ", 3)]

    print("Soldiers : {} - Communication Links : {} - Classes : {}\n".format(num_soldiers, num_comm_link, num_classes))
    # Get the Soldier's classes
    classes = []
    while not len(classes) == num_soldiers:
        classes = [int(i) for i in input("Enter Array of class for each Soldier : ").split() if
                   1 <= int(i) <= num_classes]
    print(classes)
    communication = []
    for m in range(num_comm_link):
        while len(communication) == 0 or len(communication[m]) != 2:  # or communication[m][0] == communication[m][1]:
            communication.append([int(i) for i in input("{} - sender receiver : ".format(m + 1)).split() if
                                  1 <= int(i) <= num_soldiers])
            print(communication)

    print(communication)
