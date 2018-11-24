"""
Two friends decide to meet between 8 A.M and 9 A.M. Once one of the friends arrives at the destination,
he waits for 10 minutes for his friend to show up. So if Friend1 comes at 8.40 he will wait till 8.50 and then leaves.
Friend2 doesnt know if Friend1 was waiting for him. Both of the friends agreed if they arrive at 8.55 then they will
wait only till 9 A.M not till 9.05 A.M.

What is the probability the two friends will meet.
"""

import random

# Define the Number of events to Simulate
N = 400000
# Get random minutes from 0 to 60
friend1 = [random.randint(0, 60) for i in range(N)]
friend2 = [random.randint(0, 60) for i in range(N)]

# Check in how many instances the friends meet
met = [(x, y) for (x, y) in zip(friend1, friend2) if abs(x - y) < 10]
not_met = [(x, y) for (x, y) in zip(friend1, friend2) if abs(x - y) >= 10]

print("Number of times Friends met : {}".format(len(met)))
print("Number of times Friends not met : {}".format(len(not_met)))
print("The probability of meeting two Friends is {:.2f}".format(float(len(met) / N)))
