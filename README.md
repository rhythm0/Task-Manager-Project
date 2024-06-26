# mpcs-50101-autumn-2023-finalproject

# Your Task Manager

This is an object oriented task manager application that will allow you to enter tasks, save them to a file, and retrieve them ... all without moving your hands from the keyboard.

# Running the program
Run the program completely from the command line passing in commands and arguments that will alter the behavior of the program.

The commands are `--add` (with `--due`, `--priority`), `--delete`, `--list`, `--report`, `--query`, and `--done`.  

- usage: 
`todo.py [-h] [--add ADD] [--delete DELETE] [--list] [--report] [--query QUERY [QUERY ...]] [--done DONE] [--due DUE] [--priority PRIORITY]`

## Rules
Below are the general rules the tasks would follow in this program:

- Each task is uniquely identified from all other tasks by a numeric identifier, ID.
- Tasks are assigned a priority level of 1, 2 or 3 to indicate the importance (3 is the highest priority).
- A Task object should store the date they were created and completed.
- The task manager should allows for different types of tasks: a task with no due date and a task with a due date.


## Task Add
Add a new task by using the --add command. Sub commands are --due (optional) and --priority (default set as 1). 
#### Input Format: `--add name --due date --priority level`
Data type:
- name - string (should not be digits)
- date - mm/dd/yy or human readable date
- priority - level of 1,2,3

Examples of adding tasks are shown below.

`$ python todo.py --add "Walk Dog" --due 4/17/2018 --priority 1` >>> Created task 1

`$ python todo.py --add "Buy milk and eggs" --due friday --priority 2` >>> Created task 3

`$ python todo.py --add "Cook eggs"` >>> Created task 4

## Task List Command
#### Input Format: `--list`
Display a list of the not completed tasks sorted by the due date. 

If tasks have the same due date, sort by decreasing priority (1 is the highest priority). 

If tasks have no due date, then sort by decreasing priority.

Only tasks that are not completed should be listed with this command. 

The Age in the table is the number of days since the task was created.

Follow the formatting shown below.

`$ python todo.py --list`

![image](https://github.com/rhythm0/mpcs-50101-autumn-2023-finalproject-rhythm0/assets/66907386/ae8023a9-1f48-4b4b-808d-ce9de8e5e673)


## Task Done Command
#### Input Format: `--done task_id`
Complete a task by passing the done argument and the unique identifier. The following example complete tasks 1 and 2. Remember that you are not deleting a task, you are just marking it as complete. Your --list methods should ensure that it is no longer printed to the terminal.

`$ python todo.py --done 2` >>> Completed task 2

`$ python todo.py --list`

![image](https://github.com/rhythm0/mpcs-50101-autumn-2023-finalproject-rhythm0/assets/66907386/fae55cf1-89b1-481b-ab97-57875c96a951)


## Task Delete Command
#### Input Format: `--delete task_id`
Delete a task by passing the `--delete` command and the unique identifier.

`$ python todo.py --delete 9`>>> Deleted task 9

`$ python todo.py --list`

![image](https://github.com/rhythm0/mpcs-50101-autumn-2023-finalproject-rhythm0/assets/66907386/ba1c8d4c-664d-4de7-8386-0dbbe4aa88a0)

## Task List Command Using a Query Term
#### Input Format: `--query term1 term2 ...`
Search for tasks that match a search term using the `--query` command. Only return tasks are not completed in your results. Multiple terms should be able to be searched.

`$ python todo.py --query eggs`

![image](https://github.com/rhythm0/mpcs-50101-autumn-2023-finalproject-rhythm0/assets/66907386/febb5867-b0c6-49e0-ad9d-67937c6a06e6)


`$ python todo.py --query eggs study`

![image](https://github.com/rhythm0/mpcs-50101-autumn-2023-finalproject-rhythm0/assets/66907386/8608e6ad-2286-49a1-86bd-8cc124407f75)


## Task Report Command
#### Input Format: `--report`
List all tasks, including both completed and incomplete tasks, using the report command. Follow the formatting shown below for the output. Follow the same reporting order as the `--list` command.

`$ python todo.py --report`

![image](https://github.com/rhythm0/mpcs-50101-autumn-2023-finalproject-rhythm0/assets/66907386/307976cf-27c8-4817-ae5a-769181b58c7c)

## Help Command 
Once an exception occurs, i.e., invalid input, the program warns the user to run "python todo.py -h" for usage instructions. 
- Example: 

`$ python todo.py -h`

`Command Line Task Manager`

`optional arguments:`

`  -h, --help            show this help message and exit`

  `--add ADD             Add a new task`

  `--delete DELETE       Delete a task by ID`

  `--list                List tasks`

  `--report              Report all tasks`

  `--query QUERY [QUERY ...] Search tasks with query terms`

  `--done DONE           Mark a task as done by ID`

  `--due DUE             Due date for the task`

  `--priority PRIORITY   Priority of the task, default is 1`
  

## Error Handling
- Example warning user:
`$ python todo.py --add 2 --due 4/17/2018 --priority 1`

`There was an error in creating your task. Run "python todo.py -help" for usage instructions.`
