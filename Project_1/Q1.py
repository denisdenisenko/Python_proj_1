import re


def number_of_messages_in_inbox(given_file):
    """
    Counting the number of messages in the inbox
    :param given_file: .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    simple_counter = 0
    # Iterating over each line and if there "From " in the line -> increase counter
    for line in file_to_handle:
        line = line.rstrip()
        if re.search('^From:', line):
            # print(line)
            simple_counter += 1
            continue
    print("Number of messages in inbox: ", simple_counter)
