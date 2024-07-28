class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed task: {task}")
        else:
            print(f"Task not found: {task}")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("No tasks in the to-do list.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Read a book")
    todo_list.display_tasks()
    todo_list.remove_task("Buy groceries")
    todo_list.display_tasks()
