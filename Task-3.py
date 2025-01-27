class Task:
    def __init__(self, task_id, name, description):
        self.task_id = task_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Name: {self.name}, Description: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, name, description):
        new_task = Task(self.next_id, name, description)
        self.tasks.append(new_task)
        self.next_id += 1
        print(f"Task '{name}' created successfully!")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, name=None, description=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if name:
                    task.name = name
                if description:
                    task.description = description
                print(f"Task ID {task_id} updated successfully!")
                return
        print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} deleted successfully!")
                return
        print(f"Task ID {task_id} not found.")


def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            manager.create_task(name, description)
        elif choice == "2":
            manager.read_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                name = input("Enter new task name (or leave blank to keep current): ")
                description = input("Enter new task description (or leave blank to keep current): ")
                manager.update_task(task_id, name or None, description or None)
            except ValueError:
                print("Invalid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
