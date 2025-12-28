# Simple Command-Line To-Do List 📝

A minimalist, Python-based To-Do List application that runs in the command line. This project is designed for users who need a quick and easy way to manage tasks without a graphical user interface or external database.

# Features ✨

 Add Task: Easily append new tasks to your list.

  View Tasks: Display all current tasks with their corresponding numbers.

 Delete Task: Remove a completed or unwanted task by its number.

   Simple Interface: Intuitive, text-based menu for navigation.

# Prerequisites 🛠️

To run this application, you only need:

   Python 3.x (The code is written in standard Python and requires no external libraries).

# Installation and Setup 🚀

   Save the Code: Save the provided Python code into a file named todo_list.py.

   Open Terminal: Navigate to the directory where you saved the file using your terminal or command prompt.

   Run the Application: Execute the script using the Python interpreter:
   
    Bash

    python todo_list.py

# How to Use 💡

Once the application starts, you will be presented with the main menu:

To-Do List Menu
1. Add Task
2. Delete Task
3. View Tasks
4. Exit
Choose an option:

Options

Option	Description	Action
1	Add Task	Prompts you to enter the new task text and adds it to the list.
2	Delete Task	Prompts for the number of the task you want to delete (as shown in the View Tasks list).
3	View Tasks	Displays your entire list with numbered items.
4	Exit	Closes the application.

# Project Structure 🧑‍💻

The application is structured into clear, modular functions:

   display_menu(): Shows the user the available options.

   add_task(tasks): Handles adding a new task to the list (the tasks list).

   delete_task(tasks): Handles removing a task by its index.

   view_tasks(tasks): Prints the current list of tasks.

   main(): The primary execution loop that manages user input and calls the corresponding functions.

# Future Enhancements (Ideas) 💡

   Adding functionality to save and load tasks to/from a file (e.g., CSV or JSON) so the list persists after exiting.

   Adding a feature to mark tasks as complete (e.g., with a [DONE] tag).

   Implementing input validation to handle non-integer inputs gracefully.
