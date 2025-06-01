



print("This program will help you manage your daily tasks based on their priority and time sensitivity.")
    
Task = input("Task? ")    
priority = input("priority ? (high / medium / low) ")
Time_Bound = input("Time Bound? (yes / no) ")
if priority.lower() == "high" and Time_Bound.lower() =="yes":
        print("You should complete this task today. ")
elif priority.lower() == "high" and Time_Bound.lower() =="no":
        print("You should complete this task within the next few days. ")
elif priority.lower() == "medium" and Time_Bound.lower() =="yes":
        print("You should complete this task within the next few days. ")
elif priority.lower() == "medium" and Time_Bound.lower() =="no":
        print("You should complete this task within the next week. ")
elif priority.lower() == "low" and Time_Bound.lower() =="yes":
        print("You should complete this task within the next week. ")
elif priority.lower() == "low" and Time_Bound.lower() =="no":
        print("You can complete this task whenever you have time. ")
else:
        print("Invalid input. Please try again.")
print("Thank you for providing the details of your task.")
print("Welcome to the Daily Reminder Program!")
    
while True:
        another_task = input("Do you have another task to add? (yes / no) ")
        if another_task.lower() == "yes":
           
    