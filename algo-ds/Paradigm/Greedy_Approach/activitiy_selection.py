def print_max_activity(activity):
    activity_len = len(activity)
    print("Size of Acitvities : {}\n".format(len(activity)))
    # First activity always gets selected
    i, activity_selected = 0, [activity[0]]
    # Loop for all activities
    for j in range(1, activity_len):
        if activity[j][0] > activity_selected[i][1]:
            activity_selected.append(activity[j])
            i += 1
    print("{} activities are selected :\n{}".format(len(activity_selected), activity_selected))


# Create a tuple of start and End time
activity = [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
# Sort the Activity
activity.sort(key=lambda x: x[1])

print("Start sequence : {}".format(list(s[0] for s in activity)))
print("End sequence   : {}".format(list(s[1] for s in activity)))
print_max_activity(activity)
