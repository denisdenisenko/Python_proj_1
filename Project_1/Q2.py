# Importing library for sorting the dictionary list
import re
from collections import OrderedDict


def count_the_number_of_authors(given_file):
    """
    Creating a sorted list of authors by their sending activity in descending order
    and adding them to another file.
    :param given_file : .txt
    :return: .txt
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    # Creating the new file
    name_of_file_to_write = "Dictionary_of_Authors.txt"
    file_to_write = open(name_of_file_to_write, "w")
    dictionary_counter = dict()
    for line in file_to_handle:
        # Iterating throug each line where "Author" is mentioned
        line = line.rstrip()
        if re.search('^Author:', line):
            try:
                # Extracting the domain from Author
                line = line.rstrip()
                line = line.split(": ")
                line = line[1]
                dictionary_counter[line] = dictionary_counter.get(line, 0) + 1
            except Warning:
                print("Wrong Author")
                continue
    # Creating sorted list in descending order
    sorted_counts = OrderedDict(sorted(dictionary_counter.items(), key=lambda x: x[1], reverse=True))
    print(sorted_counts)
    print(" \n File was created, check in directory for Dictionary_of_Authors.txt")
    # Adding the dictionary list to new file
    for k, v in sorted_counts.items():
        file_to_write.write(str(k) + ' sent ' + str(v) + ' messages' + '\n\n')
    file_to_write.close()
