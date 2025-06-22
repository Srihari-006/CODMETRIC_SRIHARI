import os
import sys

def clear_screen():
    """Clears the console screen in a cross-platform way"""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks(filename="todo.txt"):
    """Load tasks from file with error handling"""
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        # File doesn't exist yet - will be created on first save
        pass
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks, filename="todo.txt"):
    """Save tasks to file with error handling"""
    try:
        with open(filename, 'w') as file:
            file.writelines(task + '\n' for task in tasks)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def show_tasks(tasks):
    """Display all tasks with proper numbering"""
    clear_screen()
    if not tasks:
        print("Your to-do list is empty!\n")
    else:
        print("\n=== YOUR TO-DO LIST ===\n")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task with input validation"""
    while True:
        task = input("Enter new task (or 'cancel' to abort): ").strip()
        if not task:
            print("Task cannot be empty. Try again.")
            continue
        if task.lower() == 'cancel':
            return False
        tasks.append(f"[ ] {task}")
        if save_tasks(tasks):
            print(f"Added: {task}")
        return True

def delete_task(tasks):
    """Delete a task with input validation"""
    show_tasks(tasks)
    if not tasks:
        return
    
    while True:
        try:
            choice = input("Enter task number to delete (or 'cancel'): ").strip()
            if choice.lower() == 'cancel':
                return False
            
            index = int(choice) - 1
            if 0 <= index < len(tasks):
                deleted = tasks.pop(index)
                if save_tasks(tasks):
                    print(f"Deleted: {deleted}")
                return True
            print(f"Please enter a number between 1-{len(tasks)}")
        except ValueError:
            print("Please enter a valid number.")

def mark_task(tasks, complete=True):
    """Mark/unmark a task with input validation"""
    show_tasks(tasks)
    if not tasks:
        return
    
    action = "complete" if complete else "uncomplete"
    while True:
        try:
            choice = input(f"Enter task number to {action} (or 'cancel'): ").strip()
            if choice.lower() == 'cancel':
                return False
            
            index = int(choice) - 1
            if 0 <= index < len(tasks):
                task = tasks[index]
                if complete and "[ ]" in task:
                    tasks[index] = task.replace("[ ]", "[x]")
                elif not complete and "[x]" in task:
                    tasks[index] = task.replace("[x]", "[ ]")
                else:
                    status = "completed" if complete else "uncompleted"
                    print(f"Task is already {status}")
                    return False
                
                if save_tasks(tasks):
                    print(f"Task marked as {'completed' if complete else 'uncompleted'}!")
                return True
            print(f"Please enter a number between 1-{len(tasks)}")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main program loop"""
    tasks = load_tasks()
    
    while True:
        clear_screen()
        print("=== TO-DO LIST MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Mark Task Uncomplete")
        print("6. Exit")
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            if choice == '1':
                show_tasks(tasks)
                input("\nPress Enter to continue...")
            elif choice == '2':
                add_task(tasks)
                input("\nPress Enter to continue...")
            elif choice == '3':
                delete_task(tasks)
                input("\nPress Enter to continue...")
            elif choice == '4':
                mark_task(tasks, complete=True)
                input("\nPress Enter to continue...")
            elif choice == '5':
                mark_task(tasks, complete=False)
                input("\nPress Enter to continue...")
            elif choice == '6':
                print("\nGoodbye! Your tasks are saved.")
                break
            else:
                print("Invalid choice. Please enter 1-6.")
                input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Handle any unexpected errors
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
