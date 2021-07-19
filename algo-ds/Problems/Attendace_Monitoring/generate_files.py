"""
Common package to generate the Sample files for Input
"""

import random


def generate_input_file(file_name, start_id, end_id, limit):
    """
    This Method will generate a file having random Employee Ids from a given range
    Will be used by Attendance Tree for marking attendance of Employees
    :param file_name: Output Filename to which employee ids to be written
    :param start_id: Starting range of ID
    :param end_id: Ending range of Id
    :param limit: No of id required
    :return:
    """
    # Generate random
    print("Writing file {}...".format(file_name))
    f = open(file_name, 'w')
    # Write the Random Number into file
    for i in range(limit):
        f.writelines(str(random.randrange(start_id, end_id)) + "\n")
    f.close()  # Close the file
    print("File written successfully.")


def generate_prompt_file(file_name, start_id, end_id, limit):
    """
    This Method will generate a file having random random Employee Ids
    Will be used by Attendance tree to check if an Employee is present on a day
    :param file_name: Output Filename to which employee ids to be written
    :param start_id: Starting range of ID
    :param end_id: Ending range of Id
    :param limit: No of id required
    :return:
    """
    choice_list = ["searchId", "howOften"]
    unique_emp = []
    for i in range(limit):
        value = "{}:{}".format(random.choice(choice_list), (random.randrange(start_id, end_id)))
        if value not in unique_emp:
            unique_emp.append(value)
    # Generate random
    print("Writing file {}...".format(file_name))
    f = open(file_name, 'w')
    # Write the Random Number into file
    for string in unique_emp:
        f.writelines(string + "\n")
    f.close()  # Close the file
    print("File written successfully.")


# generate_input_file("inputPS1.txt", 1, 100, 50)
generate_prompt_file("promptsPS1.txt", 1, 100, 60)
