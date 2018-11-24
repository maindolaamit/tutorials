import DataStructures
from DataStructures.LinkedList import DoubleLinkedList
from DataStructures.LinkedList import LinkedList


def test_single_linkedlist():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(20)
    list.insert(24)
    list.insert(34)

    print(list)
    print(list.get(4))

    list.remove(1)
    print(list)
    list.insert(50)
    print(list)

    list.removeAt(3)
    print(list)
    list.insertAt(3, 10)
    print(list)

    # Test with String
    list = LinkedList()
    list.insert('A')
    list.insert('m')
    list.insert('m')
    print(list)
    list.removeAt(2)
    list.insert('i')
    list.insert('t')
    print(list)


def test_double_linkedlist():
    list = DoubleLinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(20)
    list.insert(24)
    list.insert(34)

    print(list)
    print(list.get(4))

    list.remove(1)
    print(list)
    list.insert(50)
    print(list)

    list.remove_at(3)
    print(list)
    list.insert_at(3, 10)
    print(list)


# Main program starts here
print("Testing Single Linked List....")
test_single_linkedlist()

print("\nTesting Double Linked List....")
test_double_linkedlist()
