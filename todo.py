import argparse
import pickle
import re
from datetime import datetime, timedelta
from dateutil.parser import parse
from parsedatetime import Calendar
from tabulate import tabulate  # For formatting the table

class Task:
    """Representation of a task
    Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    """
    def __init__(self, name, due_date=None, priority=1):
        self.created = datetime.now()
        self.completed = None
        self.name = name
        self.unique_id = None  # Unique ID needs to be set when adding to Tasks
        self.priority = priority
        self.due_date = due_date

class Tasks:
    """A list of `Task` objects."""
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('.todo.pickle', 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            pass  # File doesn't exist, start with an empty list

    def pickle_tasks(self):
        with open('.todo.pickle', 'wb') as file:
            pickle.dump(self.tasks, file)

    def list_tasks(self):
        # Implement the method to list tasks
        # Filter out completed tasks
        incomplete_tasks = [task for task in self.tasks if task.completed is None]
        
        # Sort tasks by due date and priority
        sorted_tasks = sorted(
            incomplete_tasks,
            key=lambda task: (
                task.due_date if task.due_date else datetime.max.date(),
                -task.priority,
                task.unique_id  # Add unique_id to maintain stable sorting
            ),
        )

        # Display the tasks in a tabulated format
        table_headers = ["ID", "Age", "Due Date", "Priority", "Task"]
        table_data = [
            [
                task.unique_id,
                f"{(datetime.now() - task.created).days}d",
                task.due_date.strftime('%m/%d/%Y') if task.due_date else "-",
                task.priority,
                task.name,
            ]
            for task in sorted_tasks
        ]

        print(tabulate(table_data, headers=table_headers, tablefmt="grid")) # print list table


    def report_tasks(self):
        # Implement the method to report tasks
        # Sort all tasks by creation date
        all_tasks = sorted(self.tasks, key=lambda task: task.created)
        # Sort tasks by due date and priority
        sorted_tasks = sorted(
            all_tasks,
            key=lambda task: (
                task.due_date if task.due_date else datetime.max.date(),
                -task.priority,
                task.unique_id  # Add unique_id to maintain stable sorting
            ),
        )

        # Display all tasks in a tabulated format
        table_headers = ["ID", "Age", "Due Date", "Priority", "Task", "Created", "Completed"]
        table_data = [
            [
                task.unique_id,
                f"{(datetime.now() - task.created).days}d",
                task.due_date.strftime('%m/%d/%Y') if task.due_date else "-",
                task.priority,
                task.name,
                task.created.strftime('%a %b %d %H:%M:%S %Z %Y'),
                task.completed.strftime('%a %b %d %H:%M:%S %Z %Y') if task.completed else "-",
            ]
            for task in sorted_tasks
        ]

        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


    def done_task(self, task_id):
        # Find the task with the specified unique_id
        task_to_complete = None
        for task in self.tasks:
            if task.unique_id == task_id:
                task_to_complete = task
                break

        # Check if the task was found
        if task_to_complete:
            # Mark the task as completed
            task_to_complete.completed = datetime.now()
            print(f"Completed task {task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found.")


    def delete_task(self, task_id):
        # Implement the method to delete a task
        # Find the task with the specified unique_id
        task_to_delete = None
        for task in self.tasks:
            if task.unique_id == task_id:
                task_to_delete = task
                break

        # Check if the task was found
        if task_to_delete:
            # Remove the task from the list
            self.tasks.remove(task_to_delete)
            print(f"Deleted task {task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found.")


    def query_tasks(self, query_terms):
        '''Query tasks'''
        # Filter out completed tasks
        incomplete_tasks = [task for task in self.tasks if task.completed is None]

        # Filter tasks based on query terms
        filtered_tasks = []
        for term in query_terms:
            filtered_tasks.extend(
                [task for task in incomplete_tasks if re.search(term, task.name, re.IGNORECASE)]
            )

        # Sort tasks by due date and priority
        sorted_tasks = sorted(
            filtered_tasks,
            key=lambda task: (task.due_date if task.due_date else datetime.max.date(), -task.priority, task.unique_id),
        )

        # Display the tasks in a tabulated format
        table_headers = ["ID", "Age", "Due Date", "Priority", "Task"]
        table_data = [
            [
                task.unique_id,
                f"{(datetime.now() - task.created).days}d",
                task.due_date.strftime('%m/%d/%Y') if task.due_date else "-",
                task.priority,
                task.name,
            ]
            for task in sorted_tasks
        ]

        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


    def add_task(self, name, due_date=None, priority=None):
        '''Implement the method to add a task'''
        # Generate a unique identifier for the task
        unique_id = 1 if not self.tasks else max(task.unique_id for task in self.tasks) + 1
        
        # Validate and parse due date
        if due_date:
            cal = Calendar() 
            time_struct, parse_status = cal.parse(due_date)

            if parse_status == 0: # already in machine readable format
                try:
                    due_date = parse(due_date).date()
                except ValueError:
                    print("Error: Invalid due date format. Please use a valid date format.")
                    return
            else:
                # allows human readable strings to date (ie tommorrow)
                due_date = parse(str(time_struct.tm_year) + '-' + str(time_struct.tm_mon) + '-' + str(time_struct.tm_mday)).date()

        # Validate and set priority
        if priority is None :
            priority = 1 # default
        elif priority not in [1, 2, 3]: # invalid input
            print("Error: Invalid priority. Priority should be 1, 2, or 3.")
            return

        # Create a new Task object
        new_task = Task(name, due_date, priority)
        new_task.unique_id = unique_id

        # Add the task to the list of tasks
        self.tasks.append(new_task)

        print(f"Created task {unique_id}")


def main():
    '''Parse input and save to pickle file'''
    parser = argparse.ArgumentParser(description="Command Line Task Manager")
    parser.add_argument('--add', type=str, help="Add a new task")
    parser.add_argument('--delete', type=int, help="Delete a task by ID")
    parser.add_argument('--list', action='store_true', help="List tasks")
    parser.add_argument('--report', action='store_true', help="Report all tasks")
    parser.add_argument('--query', type=str, required=False, nargs='+', help="Search tasks with query terms") # allows multiple search items
    parser.add_argument('--done', type=int, help="Mark a task as done by ID")
    parser.add_argument('--due', type=str, help='Due date for the task')
    parser.add_argument('--priority', type=int, help='Priority of the task, default is 1')

    args = parser.parse_args() # parse

    tasks_manager = Tasks() # call tasks class

    if args.add and not args.add.isdigit(): # name could only be string
        tasks_manager.add_task(args.add, due_date=args.due, priority=args.priority)
    elif args.delete:
        tasks_manager.delete_task(args.delete)
    elif args.list:
        tasks_manager.list_tasks()
    elif args.report:
        tasks_manager.report_tasks()
    elif args.query:
        tasks_manager.query_tasks(args.query)
    elif args.done:
        tasks_manager.done_task(args.done)
    else:
        print("There was an error in creating your task. Run 'todo -h' for usage instructions.") # Invalid arguments

    tasks_manager.pickle_tasks()  # Save tasks to file

if __name__ == "__main__":
    main()