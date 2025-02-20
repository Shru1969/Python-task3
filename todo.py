import argparse
import json
import os

# Define the file to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"[{status}] {task['id']}: {task['description']}")

def update_task(task_id, new_description):
    """Update an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print("Task not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

def mark_completed(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print("Task not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI To-Do List Manager")
    parser.add_argument("action", choices=["add", "list", "update", "delete", "complete"], help="Action to perform")
    parser.add_argument("--id", type=int, help="Task ID (for update, delete, complete)")
    parser.add_argument("--desc", type=str, help="Task description (for add, update)")
    
    args = parser.parse_args()
    
    if args.action == "add" and args.desc:
        add_task(args.desc)
    elif args.action == "list":
        list_tasks()
    elif args.action == "update" and args.id and args.desc:
        update_task(args.id, args.desc)
    elif args.action == "delete" and args.id:
        delete_task(args.id)
    elif args.action == "complete" and args.id:
        mark_completed(args.id)
    else:
        print("Invalid command. Use --help for options.")
