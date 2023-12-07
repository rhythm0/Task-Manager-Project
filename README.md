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


## Help Command 
Once an exception is occured, i,e, invalid input, the program would warn the user to run "python todo.py -h" for usage instructions. 
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