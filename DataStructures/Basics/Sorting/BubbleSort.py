import random


def bubble_sort(items):
    # Loop for till the length of list
    for i in range(len(items)):
        swapped = False
        # Run another loop in reducing fashion, Swap the alternate element and push largest to the end
        # Each iteration will put the max element to the end
        for j in range(1, len(items) - i):
            # If current element is greater than previous then swap
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                swapped = True

        # Check if any swap happened, if not List is already sorted
        if not swapped:
            break;

    return items


# items = [90, 80, 37, 31, 15, 10]      # Average case
# items = [10, 35, 31, 37, 80]          # Already sorted  - Worst case
items = [random.randint(0, 100) for i in range(10)]  # Generate a random List
print(items)
print("Sorted : {}".format(bubble_sort(items)))
