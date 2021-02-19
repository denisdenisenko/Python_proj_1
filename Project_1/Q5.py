import re


def day_with_max_messages(given_file):
    """
    Printing the day with most messages
    :param given_file : .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    simple_dictionary_counter = dict()
    try:
        for line in file_to_handle:
            if "Author" in line:
                for second_line in file_to_handle:
                    # Extracting the Days
                    if re.search('^Date:', second_line):
                        second_line = second_line.rstrip()
                        second_line = second_line.split("(")
                        day_element = second_line[1].split(",")[0]
                        simple_dictionary_counter[day_element] = simple_dictionary_counter.get(day_element, 0) + 1
                        break
    except:
        print("One or more parameters were corrupt")
    maximum_value = None
    maximum_key = None
    # Extracting the day with max messages sent
    for word, count in simple_dictionary_counter.items():
        if maximum_value is None or count > maximum_value:
            maximum_key = word
            maximum_value = count

    print(simple_dictionary_counter, "\n")
    print("The day when received most messages is :", maximum_key)
    print("With", maximum_value, " messages")


def month_with_max_messages(given_file):
    """
    Printing the day with most messages
    :param given_file : .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    simple_dictionary_counter = dict()
    for line in file_to_handle:
        if "Author" in line:
            for second_line in file_to_handle:
                # Extracting the month
                if re.search('^Date:', second_line):
                    second_line = second_line.rstrip()
                    second_line = second_line.split("(")
                    try:
                        month_element = second_line[1].split(",")[1].split()[1]
                        simple_dictionary_counter[month_element] = simple_dictionary_counter.get(month_element, 0) + 1
                        break
                    except:
                        # print("Cannot extract Month")
                        break
    maximum_value = None
    maximum_key = None
    # Extracting the Month with max messages sent
    for word, count in simple_dictionary_counter.items():
        if maximum_value is None or count > maximum_value:
            maximum_key = word
            maximum_value = count

    print(simple_dictionary_counter, "\n")
    print("The month when recieved most messages is :", maximum_key)
    print("With", maximum_value, " messages")


def hour_with_max_messages(given_file):
    """
    Printinh the hour with max messages sent
    :param given_file : .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    dictionary_counter = dict()
    for line in file_to_handle:
        if "Author" in line:
            for second_line in file_to_handle:
                # Extracting the Hour
                if re.search('^Date:', second_line):
                    second_line = second_line.rstrip()
                    second_line = second_line.split("(")
                    try:
                        hour_element = second_line[0].split(":")[1].split(" ")[2]
                        dictionary_counter[hour_element] = dictionary_counter.get(hour_element, 0) + 1
                        break
                    except:
                        print("Cannot extract Hour")
                        break
    maximum_value = None
    maximum_key = None
    # Extracting the Hour with max messages sent
    for word, count in dictionary_counter.items():
        if maximum_value is None or count > maximum_value:
            maximum_key = word
            maximum_value = count

    print("The hour when recieved most messages is :", maximum_key)
    print("With", maximum_value, " messages")
