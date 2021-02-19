import re


def number_of_modified_arguments(given_file):
    """
    Printing all Modified values
    :param given_file: .txt
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
        line = line.rstrip()
        # Finding a line with "Modified"
        if "Modified" in line:
            for second_line in file_to_handle:
                # Beraking the loop if reached out of Modified
                if re.search('^Log', second_line):
                    break
                # Extracting the last value in Path
                second_line = second_line.split("/")
                item = second_line[-1].rstrip()
                dictionary_counter[item] = dictionary_counter.get(item, 0) + 1
                continue
    print(dictionary_counter)
    print("\n The list above is a list with all Modified values and the number they were used")
