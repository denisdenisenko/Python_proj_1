#Importing all the functions
from Project_1.Menu import *
from Project_1.Q1 import *
from Project_1.Q10 import *
from Project_1.Q11 import *
from Project_1.Q2 import *
from Project_1.Q3 import *
from Project_1.Q4 import *
from Project_1.Q5 import *
from Project_1.Q9 import *



# Reading the file
FILE_TO_READ = "mbox.txt"
show_menu()
while True:
    # Get input
    print(" \n To see menu again Press 0")
    user_key_pressed = input('Enter your choice [1-11] : \n')

    # Convert string to int type #
    try:
        user_key_pressed = int(user_key_pressed)
    except:
        print("You've entered something wrong")

    # Take action as per selected menu-option ###
    if user_key_pressed == 1:
        number_of_messages_in_inbox(FILE_TO_READ)
    elif user_key_pressed == 2:
        count_the_number_of_authors(FILE_TO_READ)
    elif user_key_pressed == 3:
        number_of_messages_by_domain(FILE_TO_READ)
    elif user_key_pressed == 4:
        domain_with_max_messages_sent(FILE_TO_READ)
    elif user_key_pressed == 5:
        day_with_max_messages(FILE_TO_READ)
    elif user_key_pressed == 6:
        month_with_max_messages(FILE_TO_READ)
    elif user_key_pressed == 7:
        hour_with_max_messages(FILE_TO_READ)
    elif user_key_pressed == 8:
        x_d_spam_confidence_average(FILE_TO_READ)
    elif user_key_pressed == 9:
        new_revision_average(FILE_TO_READ)
    elif user_key_pressed == 10:
        number_of_modified_arguments(FILE_TO_READ)
    elif user_key_pressed == 0:
        show_menu()
    elif user_key_pressed == 11:
        print("Good bye")
        break

    else:  # default
        print("Invalid number. Try again...")
