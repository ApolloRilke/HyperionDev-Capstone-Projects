# L1T23 Capstone Project III: program for a small business that can
# help it to manage tasks assigned to each member of the team.

# Assumptions: there can and will only ever be one admin user.
# Every user can only edit their own tasks.

#=====importing libraries=============================
import textwrap
from datetime import datetime as dt

#=====Functions=======================================
def reg_user():
    '''Registers a new user.'''
    x = True  # Set conditional that will exit regisration.
    while x:
        username_new = input("\nEnter a new username: \n")
        
        usernames = list_of_usernames()  # Check existing usernames.
        # Set new username and password.
        # Ensure new user is not already registered.
        # Enters the loop if the new user does not already 
        # exist in the system.
        if username_new not in usernames:
            password_new_1 = input("Enter a new password: \n")
            password_new_2 = input("Confirm the password: \n")
            
            # Validate if passwords entered match.
            while password_new_1 != password_new_2:
                print("Passwords do not match.")
                password_new_1 = input("Enter a new password: \n")
                password_new_2 = input("Confirm the password: \n")
            
            # When passwords match, print confirmation message.
            print("You have registered a new user.")
            x = False  # Registration successful: exit registration.

            # Write new user info to user.txt file with correct format.
            with open('user.txt', 'a') as f:  # Appending to file.
                f.write(f"\n{username_new}, {password_new_1}")
        
        # If user finds name already registered, options for proceeding:
        # User can either retry different name or return to menu.
        elif username_new in usernames:  # User already registered.
            print("Username already exists.")
            option = input("Please select one of the following options:\
                    \nm - return to the menu \
                    \nn - try register a new user again \n").lower()
            # User wants to return to menu. 
            if option == "m":
                x = False  # Stops loop.

            # User wants to retry registration.
            elif option == "n":
                continue  # Restart while loop
            
            # User will be returned to menu when option entry invalid.
            else:
                print("Error: invalid choice. Back to the menu then.")
                x = False  # Stops loop.


def add_task():
    """User can add a task to any registered user."""
    # while loop validates if assigned user exists.
    while True: 
        
        # Get information about task from user.
        name = input("Enter user to whom you're assigning the task:\n")
        
        # Get list of usernames
        usernames = list_of_usernames()

        # Check entered name exists.
        if name not in usernames:
            print("ERROR: This user does does not exist.")
            continue  # while loop repeated
        
        # User continues the add task assignment as user exists.
        else:
            break  # exit while loop.
        
    # Get information about task from user.
    title = input("What is the title of this task?: \n")
    descrip = input("Describe the details of the task: \n")
    
    # Validate user inputs a date in future and in correct format. 
    while True:
        duedate = input("When is this task due? "
                    "(date format: D/DD Mon YYYY): \n")
        try:
            dt.strptime(duedate, '%d %b %Y')
        except ValueError:
            print(" ERROR! Incorrect format: should be \"DD Mon YYYY\"")
        else:
            duedate_is_future(duedate)
            break
    
    today = dt.today().strftime('%d %b %Y')

    # Arrange all task info into a variable correctly formatted.
    new_task = f"{name}, {title}, {descrip}, {today}, {duedate}, No"
    
    # Write new task to tasks.txt file.
    with open('tasks.txt', 'a') as f:
        f.write(f"\n{new_task}")
    print(f"You've successfully assigned task \"{title}\" to {name}.")


def view_all():
    "User can view all the tasks available."
    task_count = 0  # Initialise line/task count.
    # Open tasks.txt to read task information.
    with open('tasks.txt', 'r') as f:
        for line in f:  # Loop through (lines of file or) each task.
            task_count += 1  # Count tasks.
            task_item = line.split(", ")  # Split line into list items.
            
            # Formatting and referencing the list items appropriately:
            view_all_part = "1"
            format(task_item, task_count, view_all_part)
    
    # Allow user to peruse the results without menu showing up.
    input("Hit enter when you're done with this screen. \n")


def view_mine():
    """User is able to view their tasks. From here they can also
    edit their tasks, this includes marking the task as complete,
    changing their due dates, and reassigning their task to another."""

    user_task_count = 0  # Initialise user task count/reference.     
    users_tasks = {}  # Initialise the user's task dictionary. 
    
    # Open tasks.txt to read task information.
    with open('tasks.txt', 'r') as f:
        for line in f:  # Loops through tasks/lines in tasks.txt.
            line = line.strip()  # Removes \n from end of line.
            task_item = line.split(", ")  # Split line into task list items.
            
            # Only show tasks for signed in user.
            # Validate username at sign in with first item in task list.
            if username == task_item[0]:
                user_task_count += 1  # No. of tasks assigned to user.
                
                # Formatting and referencing the list items:
                format(task_item, user_task_count, None)

                # Add task to a dict for referencing to edit by the user.
                users_tasks[user_task_count] = task_item
    
    # The user does not have current tasks assigned to them.
    if user_task_count == 0:
        print("It seems you do not have any tasks assigned to you.")
        pass

    # Provide menu to either go back to menu or edit a task.
    # User will be looped back to this menu if invalid entry. 
    elif user_task_count != 0:
        edit = input("You can edit these tasks, or go back to the menu: \
        \n m - menu\
        \n e - edit\n").lower()
    
        # User wishes to edit a task.
        if edit == "e":
            edit_tasks_func(users_tasks)
        
        # User wishes to return to the menu.
        elif edit == "m":
            pass

        else:
            print("Oops, invalid entry, try again.")
            view_mine()


def format(task_item, user_task_count, which_section):
    ''' Formatting and referencing the list items:
     Task description wraps if too long.'''

    wrapped_desc = textwrap.fill(task_item[2], width=70)
    print(u'\u2500' * 70)
    if which_section == "1":  # This is for view_all()
        print(f"Task {user_task_count}:")
    else:  # This is for individual assigned tasks in view_mine()
        print(f"Task {user_task_count} assigned to you:")
    print(u'\u2500' * 70)
    print(f"Task:\t\t\t {task_item[1]}")
    print(f"Assigned to:\t\t {task_item[0]}")
    print(f"Date assigned:\t\t {task_item[3]}")
    print(f"Due date:\t\t {task_item[4]}")
    print(f"Task complete?:\t\t {task_item[5]}")
    print(f"Task description:\n {wrapped_desc}")
    print(u'\u2500' * 70 + "\n")


def edit_tasks_func(users_tasks):
    ''' Function gets a dictionary of the task line as items 
    with intention of changing one/more of the item/s. '''

    # Get list of usernames
    usernames = list_of_usernames()

    # Loop the editing task menu, user may want to edit more than one task.
    while True:
        task_ref = int(input("Which assigned task number would you like to"
                        " edit? \n(-1 to return to menu): \n"))
        
        # Return to menu - exit while loop.
        if task_ref == -1: 
            break
        
        # Only uncompleted tasks can be edits. Check.
        elif users_tasks[task_ref][5].lower() == "no":             
            complete_edit = (input("Choose manner of editing:\
                \n c - Mark this task as complete\
                \n e - Edit the task \n")).lower()

            # User wants to mark their task completed.
            if complete_edit == "c":
                # Prepare parameters for replace_line_in_tasks function.
                # Set dictionary value into a list. 
                not_completed = list(users_tasks[task_ref])
                
                # Change the completed status of the task in the dictionary.
                users_tasks[task_ref][5] = "Yes"  
                completed = users_tasks[task_ref]
                
                # Use function to replace the uncompleted with completed.
                replace_line_in_tasks(not_completed, completed)
                break  # Takes user back to menu when done.

            # User wants to edit their task in some way.
            elif complete_edit == "e":
                edit_menu = input("What would you like to edit?:\
                    \n u - Reassign task to different user\
                    \n d - Change the due date of the task\n")

                # User wants to reassign their task to another user.
                if edit_menu == "u":
                    # Loop until reassigned or user wants to exit.
                    while True:
                        reassign = input("To whom do you want to reassign? "
                                        "(-1 to go back):\n")
                        
                        # User wants to leave this section.
                        if reassign == "-1":
                            break
                        
                        # New user exists and gets reassigned.
                        # Check if entered user is on system.
                        elif reassign in usernames:
                            # Save old list item for reference.
                            old_assign = list(users_tasks[task_ref])
                            
                            # Replace the users.
                            users_tasks[task_ref][0] = reassign
                            
                            # Must change the assigned date as well. 
                            time_ = dt.today().strftime("%d %b %Y")  
                            
                            # Replace previous assigned date.
                            users_tasks[task_ref][3] = time_  
                            
                            # Save new list for reference.
                            assign = users_tasks[task_ref]  

                            # Log reassignment in tasks.txt using function.
                            replace_line_in_tasks(old_assign, assign)
                            
                            # Print out confirmation message.
                            ref = str(users_tasks[task_ref][1])
                            print(f"You have reassigned task "
                                f"\"{ref}\" to {reassign}")
                            
                            # User gets confirmation message before
                            # going back to viewing which tasks they
                            # can edit. 
                            input("Press a key to continue.\n")
                            view_mine()
                        
                        # The user entered invalid user.
                        else:
                            print("This user does not exist. ")
                            continue
                
                # User wishes to change the due date of their task.
                elif edit_menu == "d":
                    # Set old due date list for reference.
                    old_date = list(users_tasks[task_ref])

                    # Ensure user enters correct date format.
                    date_valid = False
                    while date_valid == False:
                        date_input = input("Enter the new due date :\n"
                                "(Format: DD Mon YYYY): ")
                        
                        # If valid format, function returns True: exit loop.
                        date_valid = time_format1(date_input)
                        
                        # Ensure duedate entered is in the future. 
                        if date_valid:
                            date_valid = duedate_is_future(date_input)

                    users_tasks[task_ref][4] = date_input  # Replace old.
                    
                    #Save new duedate list for referece.
                    new_date = users_tasks[task_ref]

                    # Replace the old with new due date in tasks.txt.
                    replace_line_in_tasks(old_date, new_date)
                    
                    # Confirmation message.
                    task_ref = str(users_tasks[task_ref][1])
                    print(f"Youve change the due date for "
                        f"\"{task_ref}\" to {date_input}")

                    # User gets confirmation message before
                    # going back to viewing which tasks they
                    # can edit. The user is not rushed.
                    input("Press a key to continue.\n")
                    view_mine()

        # Message indicating completed tasks cannot be edited. 
        elif users_tasks[task_ref][5].lower() == "yes":
            print("This task has been completed and cannot be edited.")
        
        # User selected invalid menu selection. Returns to task selection.
        else:
            print("That is an invalid selection ")


def replace_line_in_tasks(old_list, new_list):
    ''' Function replaces lines in tasks.txt. Inputs are old and new 
     to find and replace.'''

    # Read the tasks.txt file. 
    with open('tasks.txt', 'r', encoding='utf-8') as file:
        data = file.read().splitlines()  # Reads all lines in data sans \n.
    string = ", ".join(old_list)  # Turn list into string.
    new_string = ", ".join(new_list)

    # Isolate old line, to replace with new line.
    if string in data:
        index = data.index(string)  # Isolate old line in data.
        data[index] = new_string  # Replace old with new in data.

    # Write the new data to the tasks file. 
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(data))
    print("This was updated in the tasks.txt file.")  # Confirmation message.
    return


def time_format1(time_input):
    '''Ensures correct format.'''
    try:
        dt.strptime(time_input, '%d %b %Y')
    except ValueError:
        print("Incorrect format: should be \"DD Mon YYYY\"")
        return False
    else:
        return True


def duedate_is_future(time_input):
    ''' Ensures new due date is in the future.'''
    time_ = dt.strptime(time_input, "%d %b %Y")
    today = dt.today() 
    if time_ < today:  # Compare the times. 
        print("New due dates cannot be in the past.")
        return False
    if time_ > today:
        return True


def generate_task_overview():
    """Writes a task summary to generate a text file."""
    # Read from tasks to count tasks.
    with open('tasks.txt', 'r', encoding="UTF-8") as g:
        total_count = 0
        empty_list = []
        for line in g:
            total_count += 1  # Counts number of lines ie number of tasks.
            line = line.strip()  # Removes \n from end of line.
            task_item = line.split(", ")  # Split line into list items.
            empty_list.append(task_item)  # Gather all of the task info.
            
    # Initialise counters.
    completed_task = 0
    uncompleted_task = 0
    overdue = 0
    inprogress = 0

    # Set time in format for comparison.
    today = dt.today()               

    # Loop through each task line's items.
    for i in empty_list:
        # Prepare due date item [4] format for comparison.
        # This takes the duedate item from i, and formats it into
        # a comparable format.
        time_check = i[4].strip()
        time_check = dt.strptime(time_check, "%d %b %Y")

        # If task is completed, find completed with "Yes".
        if i[5].capitalize() == "Yes":
            completed_task += 1
        
        # If task not completed:
        if i[5].capitalize() == "No":
            uncompleted_task += 1

            # Check if the uncompleted task is overdue.
            if (time_check < today):
                overdue += 1
            
            # Check those still in progress within due date.
            elif time_check > today:
                inprogress += 1

    # Prepare data for text_overview.txt writing.
    uncompleted_ = int(uncompleted_task / total_count * 100)
    completed_ = 100 - uncompleted_
    print_text_over = (f"Completed tasks:\t {completed_task}\n"
    f"Overdue tasks: \t\t {overdue}\n"
    f"Tasks in progress:\t {inprogress}\n"
    f"Uncompleted:\t\t {uncompleted_task}\n"
    f"Total tasks:\t\t {total_count}\n\n"
    "Of all the tasks:\n"
    f"% Uncompleted tasks:\t {uncompleted_}%\n"
    f"% Completed tasks:\t {completed_}%\n"
    f"Overdue tasks:\t\t {int(overdue / total_count * 100)}%")

    # Write/generate the file.
    with open("task_overview.txt", 'w') as r:
        r.write(print_text_over)

    # Print confirmation message.
    print("The task_overview.txt file has been generated.")


def generate_user_overview():
    """Generates a user overview report based on users."""
    # Read through user.txt text file. 
    with open('user.txt', 'r', encoding="UTF-8") as g:
        total_users = 0
        empty_lists = []
        for line in g:
            # Counts number of lines therefore number of users.
            total_users += 1  
            
            # Removes \n from end of line.
            line = line.strip()  
            
            # Split line into list items.
            user_item = line.split(", ")  
            
            # Gather all of the task info.   
            empty_lists.append(user_item)  

    # Print total number of registered users. 
    to_report1 = f"The total number of registered users is: {total_users}"

    # Read from the tasks.txt file.
    with open('tasks.txt', 'r', encoding="UTF-8") as g:
        total_task = 0
        task_list_ = []
        for line in g:
            # Counts number of lines therefore number of tasks.
            total_task += 1 
            
            # Removes \n from end of line.
            line = line.strip()  
            
            # Split line into list items.
            task_item = line.split(", ")  
            
            # Gather all of the task info.
            task_list_.append(task_item)  

    # print for report.
    to_report2 = f"The total number of tasks are:\t\t {total_task}"

    # Loops through every name with assigned task.
    # All the users with tasks assigned to them. 
    users_isolate = [m[0] for m in task_list_]

    # Loops through every name registered (without password).
    just_names = [m[0] for m in empty_lists]

    # This checks the number of completed and uncompleted tasks of the user.
    uncomplete_stat = {}
    complete_stat = {}
    # Loop through the tasks.
    for i in range(0,len(task_list_)):
        # Set username as reference variable.
        check = task_list_[i][0] 

        # Add to dictionary for every count of an uncompleted 
        # task for the user.
        if (check not in uncomplete_stat and 
                task_list_[i][5] == "No"):
            uncomplete_stat[check] = 1

        # Add 1 to count of an uncompleted task for the user.
        elif (check in uncomplete_stat and 
                task_list_[i][5] == "No"):
            uncomplete_stat[check] += 1

        # Add to dictionary for every count of a completed 
        # task for user.
        elif (check not in complete_stat and 
                task_list_[i][5] == "Yes"):
            complete_stat[check] = 1

        # Add 1 to count of a completed task for the user.
        elif (check in complete_stat and 
                task_list_[i][5] == "Yes"):
            complete_stat[check] += 1

    # If a user does not have either a completed OR a uncompleted task
    # they must still be added to the both dicts as 0.
    for i in just_names:
        if i not in complete_stat.keys():
            complete_stat[i] = 0
        if i not in uncomplete_stat.keys():
            uncomplete_stat[i] = 0
            
    # This the overdue section.
    overdue_stat = {}  # Initialise dictionary.
    # Loop through the tasks.
    for i in range(0,len(task_list_)):
        
        # Set username reference variable.
        check_name = task_list_[i][0] 
        
        # Set todays date and task due date as reference variables.
        today = dt.today()                       
        string = task_list_[i][4].strip()
        # The two date formats are in the same format
        overdue_check = dt.strptime(string, "%d %b %Y")

        # For each username, either add to dictionary or add to value.
        # AND task must not be completed, AND the due date 
        # must be earlier than today to be over due. 
        if (check_name not in overdue_stat and 
                task_list_[i][5] == "No" and 
                overdue_check < today):
            overdue_stat[check_name] = 1

        # If username already in dictionary add to its counter.
        elif (check_name in overdue_stat and 
                task_list_[i][5] == "No" and
                overdue_check < today):
            overdue_stat[check_name] += 1

    # If a user does not have either a completed OR a uncompleted task
    # i.e no tasks. they must still be added to the lists as 0.
    for i in just_names:
        if i not in overdue_stat.keys():
            overdue_stat[i] = 0

    # Get the existing usernames:
    usernames = list_of_usernames()

    # Gets all the usernames in the task file 
    users_isolate = [m[0] for m in task_list_]

    # Counts the number of times each username is in tasks.
    user_stat = {}
    for user in users_isolate:
        if user not in user_stat:
            user_stat[user] = 1
        else:
            user_stat[user] += 1

    # If user is not assigned a task but still 
    # registered on system to add onto user_stat.
    for i in just_names:
        if i not in user_stat.keys():
            user_stat[i] = 0

    # Prepare for format to write.
    print_to_user = ""

    # formats the number of tasks each user has: headings.
    headings = ("{:<15} {:<22} {:<15} {:<15} {:<15} {:<15}"\
                .format("Username",
                        "No. assigned tasks",
                        "% total tasks",
                        "% Completed",
                        "% Uncompleted",
                        "% Overdue"))

    print_to_user += headings + "\n"
    # For every user, determine their statistics.
    for i in user_stat:
        # Prepare statistics as percentages or accordingly.
        user_count = i
        user_name = user_stat[i]
        
        # If user has no tasks assigned.
        if user_name == 0:
            user_name = 1
            user_prcnt = 0
            user_completed = 0
            user_uncomplet = 0
            user_name = 0
            overdue = 0
        
        # Uer has tasks: calculations can therefore be performed. 
        else:
            user_prcnt = int((user_name) / user_name * 100)
            user_completed = int(complete_stat[i] / user_name * 100)
            user_uncomplet = int(uncomplete_stat[i] / user_name * 100)
            overdue = int(overdue_stat[i] / user_name *100)

        # Prepare data for display.
        task_display = \
                "{:<15} {:<22} {:<15} {:<15} {:<15} {:<15}"\
                .format(user_count,
                        user_name, 
                        user_prcnt,
                        user_completed,
                        user_uncomplet,
                        overdue)  

        # Prepare data to write.
        print_to_user += task_display + "\n"   

    # Sum up the first column as total. 
    total_heading = ("{:<15} {:<22}".format("Total", total_task))
    print_to_user += total_heading + "\n"

    # Generate report.
    with open("user_overview.txt", "w") as v:
        v.write(to_report1 + "\n")
        v.write(to_report2 + "\n")
        v.write(print_to_user)

    # Print the confirmation message. 
    print("The user_overview.txt report has been generated.")
    return


def statistics():
    # Print the info from the generated overview files.
    print(u'\u2500' * 25)
    print("From text_overview.txt: ")
    print(u'\u2500' * 25)
    with open("task_overview.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(line)
    print()
    print()
    print(u'\u2500' * 25)
    print("From user_overview.txt: ")
    print(u'\u2500' * 25)
    with open("user_overview.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(line)
    # Allow user to view statistics without menu popping up.
    input("Press enter when youre done with the stats.\n")
    return


def list_of_usernames():
    """Gets the updated list of usernames. This accounts for a new registered 
    user being able to immediately have a task added to them.
    """
    # Initialise empty lists.
    user_file = []
    usernames = []

    # Read file with usernames and passwords infomation.
    with open('user.txt', 'r') as f:
        for line in f:  # Loop through lines in user.txt ie each user.
            # Remove \n and put put each username and password as a list item:
            user_file.append(line.strip())

    # Isolate the usernames.
    sort_user_info = []
    for line in user_file:  # Loop through each list item in user_file.
        # Separate username and password into list items within its list item.
        sort_user_info.append(line.split(", "))

    # First item in list item is a username [i][0]. Second item in same list
    # item is a password [i][1]. 
    for i in range(0, len(sort_user_info)):
        usernames.append(sort_user_info[i][0])  # List of all usernames.

    return usernames


#=====Login Section==================================================
today = dt.today()  # Set todays date for program use. 

# Get list of usernames for reference:
usernames = list_of_usernames()

# While loop to get a successful login.
x = True  # Set conditional that will change with successful login.
while x:
    username = input("Enter username: \n")
    # Validate if entered username is a registed user.
    if username in usernames:
        pass  # User is registered.
    else:
        print("ERROR: Username does not exist.")
        continue  # Restarts the while loop.
    
    user_file = []
    # Read file with usernames and passwords infomation.
    with open('user.txt', 'r') as f:
        for line in f:  # Loop through lines in user.txt ie each user.
            # Remove \n and put put each username and password as a list item:
            user_file.append(line.strip())

    password = input("Enter password: \n")
    # Validate if password belongs to username.
    login = f"{username}, {password}"
    if login in user_file:  # If inputs are found in user.txt.
        print(f"You have successfully logged in, {username}.")
        x = False  # Successful login: exit loop.
    else:
        print("Username does not match password.")   

#=====The Menu Section================================
while True:
    if username == "admin":
        # Admin user menu.
        menu = input("\nPlease select one of the following options:\
            \n r - register user \
            \n a - add task \
            \n va - view all tasks \
            \n vm - view my tasks \
            \n gr - generate reports \
            \n ds - statistics \
            \n e - exit \n").lower()
    else:
        # Non-admin user menu.
        menu = input("\nPlease select one of the following options:\
            \n a - add task \
            \n va - view all tasks \
            \n vm - view my tasks \
            \n e - exit \n").lower()

    #=====Register New User Section===================
    if (menu == "r") and (username == "admin"):  # If admin user.
        reg_user()

    #=====Assign a Task Section=======================
    elif menu == "a":
        add_task()
        
    #=====View All Tasks Section======================
    elif menu == "va":
        view_all()
        
    #=====View Signed-in User Tasks Section============
    elif menu == "vm":
        view_mine()

    #=====Generate Reports Section====================
    elif (menu == "gr") and (username == "admin"):  # Only admin user access.
        generate_task_overview()
        generate_user_overview()

    #=====Statistics Section==========================
    elif (menu == "ds") and (username == "admin"):  # Only admin user access.
        generate_user_overview()
        generate_task_overview()
        statistics()

    #=====User exists program=========================
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #=====Error message, incorrect menu entry=========
    else:
        print("You have made a wrong choice, Please Try again.")