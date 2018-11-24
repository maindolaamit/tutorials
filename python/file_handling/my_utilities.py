"""
    Module : file_utils
    This Module has various utilities for File Handling operations.
"""

import sys


def srch_str(substr, filename):
    """ Search a substring in the file, like grep command"""
    lines = open(filename, "r").readlines()
    # Create a format specifier
    fmt = ""
    for i, line in enumerate(lines):
        if line.find(substr) != -1:
            print("{} : {}".format(i, line.rstrip())


def wc(file):
    """ Returns the number of Characters, words and lines in a file
    The result is a tuple """
    data = open(file, "rb").read()
    return len(data), len(data.split()), len(data.splitlines())


def wc_large(file):
    """ Returns the number of Characters, words and lines in a large file
    The result is a tuple """

    num_chars = num_words = num_lines = 0
    for line in open(file, "rb"):
        num_chars += len(line)
        num_words += len(line.split())
        num_lines += 1

    return (num_chars, num_words, num_lines)


def split(orig_file, num_splits=2):
    """
    This method will split the given File into the provided number of sub-Files.
    If number of files to be slitted into is not given default value of 2 will be considered.
    """
    from os import path as path

    # Check if Parameters are passed
    if orig_file is None:
        print("Please pass the full filename")
        exit(0)

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
