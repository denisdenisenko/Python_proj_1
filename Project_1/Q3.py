import re


def number_of_messages_by_domain(given_file):
    """
    Print the number of messages by each domain
    :param given_file: .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()

    simple_counting_dictionary = dict()
    for line in file_to_handle:
        line = line.rstrip()
        if re.search('^From:', line):
            line = line.split(" ")
            line = line[1].split("@")
            item = line[1]
            simple_counting_dictionary[item] = simple_counting_dictionary.get(item, 0) + 1
            continue
    print(simple_counting_dictionary)
