# Shira Choen 212079875
# Shira Erel 213173636

def task_manager():
    tasks = {}
    
    def add_task(task_name, status="incomplete"):
        tasks[task_name] = status
    
    def get_tasks():
        return tasks

    def complete_task(task_name):
        if task_name in tasks:
            tasks[task_name] = "complete"
        else:
            print(f"task '{task_name}' not found.")
    
    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }

# Checking the task manager
# Create a new task manager
tasks_manager = task_manager()
# Add tasks
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")
# Get the list of tasks
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
# Should print: {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework':'incomplete'}

# Mark a task as complete
tasks_manager['complete_task']("Write email")

# Get the list of tasks after marking and deleting
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
# Should print: {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}