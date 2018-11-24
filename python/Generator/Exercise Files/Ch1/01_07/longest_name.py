# using generators to find the longest name
import os

print(f'Changing directory to {os.getcwd()}')
os.chdir(os.getcwd())

full_names = (name.strip() for name in open('names.txt'))
lengths = ((name, len(name)) for name in full_names)
longest = max(lengths, key=lambda x:x[1])

print(longest)
