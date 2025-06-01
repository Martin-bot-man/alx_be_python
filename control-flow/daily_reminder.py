print("This program will help you manage your daily tasks based on their priority and time sensitivity.")
    
# Prompt for a Single Task:
# Ask the user to input a task description and save it into a task variable
task = input("Enter your task: ")    

# In a time_bound variable, Ask if the task is time-bound (yes or no)
# This variable stores the raw 'yes' or 'no' string input.
time_bound = input("Is it time-bound? (yes/no): ") 

# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
priority = input("Priority (high/medium/low): ")


# Start building the reminder message.
reminder_message = f"Reminder: '{task}' is a "

# Process the task based on priority using match-case
# === PLEASE ENSURE THIS EXACT LINE IS IN YOUR FILE ===
match priority.lower(): 
# =====================================================
    case 'high':
        reminder_message += "high priority task"
        # Directly use 'time_bound.lower() == 'yes'' for the time-bound check
        if time_bound.lower() == 'yes':
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Aim to complete it as soon as possible."
    case 'medium':
        reminder_message += "medium priority task"
        if time_bound.lower() == 'yes':
            reminder_message += " that should be addressed today."
        else:
            reminder_message += ". Try to get to it soon."
    case 'low':
        reminder_message += "low priority task"
        if time_bound.lower() == 'yes':
            reminder_message += ". It's time-bound, so try to tackle it today."
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _: # This is the wildcard case for any other/invalid priority input.
        reminder_message = f"Note: '{task}' has an unknown priority level. "
        if time_bound.lower() == 'yes':
            reminder_message += "It's time-bound, so you might want to clarify its urgency."
        else:
            reminder_message += "No immediate action might be required."

# Print the final customized reminder.
print(reminder_message)