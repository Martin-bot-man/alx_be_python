



print("This program will help you manage your daily tasks based on their priority and time sensitivity.")
    
Task = input("Enter your task: ")    
Time_Bound = input("Is it time-bound? (yes / no): ")
priority = input("Priority (high / medium / low): ")


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
           
    