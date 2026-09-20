# variables > data types
#task_name > string
#priority_level > integer
#estimated_hours > float
#study_days_available > int

task_name = input("Enter the task name: ")
priority_level = int(input("Enter priority level (1-3): "))
estimated_hours = float(input("Enter estimated hours to complete the task: "))
study_available_days= int(input("Enter available study days: "))

daily_hours_target = estimated_hours / study_available_days

print("You have", study_available_days, " days and you need ", estimated_hours, "hours to finish your task: ", task_name)
print("The time you should spend every day: ", daily_hours_target)
