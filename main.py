running = True
current_task_name = ""
current_task_priority = 3
current_task_estimated_hours = 0.0
planned_focus_sessions = 0
task_completed = False

while running:
    print("1. Create or update current task")
    print("2. View current task")
    print("3. Mark task as completed")
    print("4. Show work plan")
    print("0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Task name: ")
        priority_text = int(input("Priority level (1-3): "))
        hours_text = input("Estimated hours: ")
        sessions_text = input("Planned focus sessions: ")
        if not task_name:
            print("Task name cannot be empty. ")
            continue
        if priority_text < 1 or priority_text > 3:
            print("Priority must be between 1-3.")
            continue

        current_task_name = task_name
        current_task_priority = priority_text
        current_task_estimated_hours = hours_text
        planned_focus_sessions = int(sessions_text)
        task_completed = False
        print("Current task updated/created successfully!")

    elif choice == "2":
        if not current_task_name:
            print("No current task has been created.")
        else:
            print("Task name: ", current_task_name)
            print("Priority: ", current_task_priority)
            print("Estimated hours: ", current_task_estimated_hours)
            print("Focus: ", planned_focus_sessions)
            print("is Task completed: ", task_completed)
            if current_task_priority == 1 and not task_completed:
                print("Immediate attention recommended!")
    elif choice == "3":
        if not current_task_name:
            print("No current task has been created.")
        else:
            task_completed = True
            print("Task marked as completed.")
    elif choice == "4":
        if not current_task_name:
            print("No current task has been created.")
        else:
            print("Work plan for", current_task_name)
            for session_number in range(1, planned_focus_sessions + 1):
                print("Session: ", session_number)

    elif choice == "0":
        running = False
        print("Thank you for using the app!")
    else:
        print("Invalid option. Please try again!")
