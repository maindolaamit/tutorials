communication = [[] for m in range(4)]
for m in range(4):
    while len(communication) == 0 or len(
            communication[m]) != 2:  # and len(communication[m]) != 2:  # or communication[m][0] == communication[m][1]:
        communication[m] = ([int(i) for i in input("{} - sender receiver : ".format(m + 1)).split() if
                              1 <= int(i) <= 5])
        print(m, communication[m], len(communication[m]))
    print("Incrementing...")

print(communication)
