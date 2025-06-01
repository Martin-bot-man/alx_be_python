



print("This program will help you manage your daily tasks based on their priority and time sensitivity.")
    
Task = input("Enter your task: ")    
is_time_bound_str = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")


reminder_message = f"Reminder: '{task}' is a "

# Process the task based on priority using match-case
match priority.lower():
    case 'high':
        reminder_message += "high priority task"
        if is_time_bound:
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Aim to complete it as soon as possible."
    case 'medium':
        reminder_message += "medium priority task"
        if is_time_bound:
            reminder_message += " that should be addressed today."
        else:
            reminder_message += ". Try to get to it soon."
    case 'low':
        reminder_message += "low priority task"
        if is_time_bound:
            reminder_message += ". It's time-bound, so try to tackle it today."
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _: # Handles any invalid priority input
        reminder_message = f"Note: '{task}' has an unknown priority level. "
        if is_time_bound:
            reminder_message += "It's time-bound, so you might want to clarify its urgency."
        else:
            reminder_message += "No immediate action might be required."

    