def x_d_spam_confidence_average(given_file):
    """
    Calculating the average X-DSPAM value
    :param given_file: .txt
    :return: void
    """
    file_to_handle = None
    try:
        file_to_handle = open(given_file)
    except:
        print('File cannot be opened:', given_file)
        exit()
    number_of_times_x_dspam_appeared = 0
    sum_of_x_d_spam = 0
    for line in file_to_handle:
        line = line.split()
        # Finding the line with X-DSPAM
        if "X-DSPAM-Confidence:" in line:
            number_of_times_x_dspam_appeared += 1
            # Converting the file to Float
            sum_of_x_d_spam = sum_of_x_d_spam + float(line[1])
            continue
    try:
        # Calculating the sum divided by the number of appearances
        print("The average of D-Spam is ", sum_of_x_d_spam/number_of_times_x_dspam_appeared)
    except ZeroDivisionError:
        print("No X-DSPAM-Confidence found, so cannot divide by zero")