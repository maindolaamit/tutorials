import random


def merge(list_1, list_2):
    """ This method will merge the given two items and return the sorted output """
    l1, l2 = len(list_1), len(list_2)  # Store the length of each list
    merged_output = [None for i in range(l1 + l2)]
    i, j = 0, 0
    # Compare each element of the two lists till one of them is exhausted
    while i < l1 and j < l2:
        if list_1[i] <= list_2[j]:
            merged_output[i + j] = list_1[i]
            i += 1
        else:
            merged_output[i + j] = list_2[j]
            j += 1

    # Check if list_1 is exhausted, add remaining element to the output
    for j in range(j, l2):
        merged_output[i + j] = list_2[j]

    # Check if list_2 is exhausted, add remaining element to the output
    for i in range(i, l1):
        merged_output[i + j] = list_1[i]

    # print(merged_output)
    return merged_output


def merge_sort(items):
    """ This method will Divide the input list until only 1 item remains
    """
    # print(items)
    # Divide the unsorted list until only 1 element remains
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    # Merge sort recursively on both hl1ves
    left, right = merge_sort(items[0:mid]), merge_sort(items[mid:])
    # print(left, right)
    # Return the merged output
    return merge(left, right)


# items = [random.randint(0, 100) for i in range(10)]
# items = [65, 3, 80, 84, 22, 55, 100, 5, 26, 32]
items = [3, 5, 7, 3, 2, 4, 1, 9, 10, 5, 4, 4]

sorted_item = merge_sort(items)
print(sorted_item)
