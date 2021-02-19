def domain_with_max_messages_sent(given_file):
    """
    Printing the domain with maximum messages sent
    :param given_file : .txt
    :return: void
    """
    # name = input('Enter file:')
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()

    simple_dictionary_counter = dict()
    for line in file_to_handle:
        line = line.split()
        if "From:" in line:
            # Extracting the domain from the line
            line = line[1].split("@")
            line = line[1]
            simple_dictionary_counter[line] = simple_dictionary_counter.get(line, 0) + 1
            continue
    maximum_value = None
    maximum_key = None
    # Finding the key with maximum value
    for word, count in simple_dictionary_counter.items():
        if maximum_value is None or count > maximum_value:
            maximum_key = word
            maximum_value = count

    print(simple_dictionary_counter)
    print(" \n The domain with maximum messages sent is",maximum_key,"with", maximum_value, "messages")
