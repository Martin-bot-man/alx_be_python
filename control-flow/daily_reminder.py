print("This program will help you manage your daily tasks based on their priority and time sensitivity.")
    
task = input("Enter your task: ")    

time_bound_str = input("Is it time-bound? (yes/no): ")

# This is crucial for the 'if is_time_bound:' checks later.
is_time_bound = time_bound_str.lower() == 'yes'

priority = input("Priority (high/medium/low): ")

# building the reminder message.
# The f-string allows easy insertion of the 'task' variable.
reminder_message = f"Reminder: '{task}' is a "

# Process the Task Based on Priority and Time Sensitivity:
# Use a Match Case statement to react differently based on the task’s priority.
match priority.lower():
    case 'high':
        reminder_message += "high priority task"
        # Within the Match Case, use an if statement to modify the reminder if the task is time-bound.
        if is_time_bound:
            # A message should be ‘that requires immediate attention today!’
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
    case _: # This is the wildcard case, catching any priority input that doesn't match 'high', 'medium', or 'low'.
        reminder_message = f"Note: '{task}' has an unknown priority level. "
        if is_time_bound:
            reminder_message += "It's time-bound, so you might want to clarify its urgency."
        else:
            reminder_message += "No immediate action might be required."

# Provide a Customized Reminder:
# Print the final reminder about the task that includes its priority level
# and whether immediate action is required based on time sensitivity.
print(reminder_message)