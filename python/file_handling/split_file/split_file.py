"""
    This script will split the given File into the provided number of Files.
    If number of files to be slitted into is not given default value of 2 will be considered.

    The below execution will split file "a.txt" into 3 files - a_0.txt a_1.txt a_2.txt
    python split_file.py a.txt 3

"""

# Import the Libraries
import sys
from os import path as path

# Check if Parameters are passed
if len(sys.argv) < 2:
    print "Please pass the full filename"
    exit(0)

# Get the Parameters
orig_file = sys.argv[1]
num_splits = int(sys.argv[2]) if len(sys.argv) > 2 else 2  # Default split is 2

orig_file_name = path.basename(orig_file)
orig_fp = open(orig_file, 'r')
file_length = len(orig_fp.readlines())
start_pos = end_pos = 0
num_lines = file_length / num_splits  # Set the number of lines to write for each file

print "Splitting File {0} of length {1} into {2} files".format(orig_file_name, file_length, num_splits)
for i in range(num_splits):
    orig_fp.seek(start_pos)  # Reset file to start position
    end_pos = (file_length if i + 1 == num_splits else start_pos + num_lines)  # Set the End Position
    # print 'start_pos : {} , end_pos : {}'.format(start_pos, end_pos)
    # Get the new File Name
    new_file = "{0}_{1}.{2}".format('.'.join(orig_file_name.split('.')[:-1]), str(i), orig_file_name.split('.')[-1])
    # Create a new file to write the contents
    new_fp = open(new_file, 'w')
    new_fp.writelines(orig_fp.readlines()[start_pos: end_pos])  # Write the Lines
    new_fp.close()  # Close the file after writing
    print "Created file {0}, number of lines {1}".format(new_file, len(open(new_file, 'r').readlines()))
    start_pos += num_lines  # Reset the start Position

# Close the Original File
orig_fp.close()
