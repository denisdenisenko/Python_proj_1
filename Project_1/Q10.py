import re


def new_revision_average(given_file):
    """
    Calculating the average New Revision value
    :param given_file: .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    number_of_new_revision_appeared = 0
    sum_of_new_revision = 0
    for line in file_to_handle:
        line = line.rstrip()
        # Finding the line with "New Revision"
        if re.search('^New Revision:', line):
            line = line.split()
            number_of_new_revision_appeared += 1
            sum_of_new_revision = sum_of_new_revision + float(line[2])
            continue
    try:
        # Calculating the sum divided by the number of appearances
        print("The average of New Revision is ", sum_of_new_revision / number_of_new_revision_appeared)
    except ZeroDivisionError:
        print("No Revision found, so cannot divide by zero")
