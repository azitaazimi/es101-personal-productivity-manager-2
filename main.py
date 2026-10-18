app_name = "Productivity manager"
app_version = 0.4


def show_heading() -> None:
    print("=" * 60)
    print(app_name)
    print(app_version)
    print("=" * 60)


def show_menu():
    print("1. Create or update current task")
    print("2. View current task")
    print("3. Mark task as completed")
    print("4. Show work plan")
    print("0. Exit")


def show_goodbye_message():
    print("Thank you for using the app!")


def create_or_update_task() -> tuple[str, int, float, int, bool]:
    task_completed = False
    task_name = input("Task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return "", 3, 0.0, 0, False

    priority_level = int(input("Priority level (1-3): ").strip())
    if priority_level < 1 or priority_level > 3:
        print("Priority must be a number 1 to 3. ")
        return "", 3, 0.0, 0, False

    estimated_hours = float(input("Estimated hours: ").strip())
    if estimated_hours == 0:
        print("Estimated hours must be a number.")
        return "", 3, 0.0, 0, False

    planned_focus_sessions = int(input("Planned focus sessions: "))
    if planned_focus_sessions == 0:
        print("Planned focus sessions must be greater than zer0")
        return "", 3, 0.0, 0, False

    print("Current task created/updated successfully")
    return (
        task_name,
        priority_level,
        estimated_hours,
        planned_focus_sessions,
        task_completed,
    )


def display_current_task(
    task_n: str,
    priority_l: int,
    estimated_h: float,
    planned_focus: int,
    completed: bool,
):
    if not task_n:
        print("No current task has been created.")
    else:
        print("Task name: ", task_n)
        print("Priority level: ", priority_l)
        print("Estimated hours: ", estimated_h)
        print("Planned focus sessions: ", planned_focus)
        print("Completed: ", completed)


def mark_task_completed(task_name: str) -> bool:
    if not task_name:
        print("A task must exist before it can be completed! ")
        return False
    else:
        print("Task mark as completed. ")
        return True


def show_work_plan(task_name: str, planned_focus_time: int):
    if not task_name:
        print("No current task has been created.")
    else:
        print("Work plan for", task_name)
        for session_number in range(1, planned_focus_time + 1):
            print("Session: ", session_number)


def main():
    running = True
    current_task_name = ""
    current_task_priority = 3
    current_task_estimated_hours = 0.0
    planned_focus_sessions = 0
    task_completed = False

    while running:
        show_heading()
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task, priority, hours, focus_sessions, completed = create_or_update_task()
            if task:
                current_task_name = task
                current_task_priority = priority
                current_task_estimated_hours = hours
                planned_focus_sessions = focus_sessions
                task_completed = completed

        elif choice == "2":
            display_current_task(
                current_task_name,
                current_task_priority,
                current_task_estimated_hours,
                planned_focus_sessions,
                task_completed,
            )
        elif choice == "3":
            task_completed = mark_task_completed(current_task_name)

        elif choice == "4":
            show_work_plan(current_task_name, planned_focus_sessions)
        elif choice == "0":
            running = False
            show_goodbye_message()
        else:
            print("Invalid option. Please try again!")


if __name__ == "__main__":
    main()
