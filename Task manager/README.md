# Task Manager App

This python app will allow a team to manage the tasks assigned to the team members. 

A user will be to add a task (to any user registered on the system, so either to themself or another user), 
view all the tasks assigned to them, and view all the tasks assigned to the whole team. The added tasks are added to a
tasks text file tasks.txt. Users are able to edit tasks in the following manner: to change the due date of their assigned
tasks, to mark their own tasks as completed.

The admin user has unique user access to the following unique features of the app:
The admin user type will be able to register a unique username and password, which will add the username and password
to a textfile (users.txt). the admin will be able to generate a report that will summarise important information about the 
teams tasks from the tasks.txt file, including the number of total tasks, how many are completed, how many are overdue, 
how many are in progress. This is generated in a text file called tasks_overview.txt. Anoteher report is generated regarding
similar statistics regarding the user. The admin user is also able to view statistics relating to the tasks and users.
