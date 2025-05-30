


def daily_reminder():
    print("This program will help you manage your daily tasks based on their priority and time sensitivity.")
    print("You will be asked to input your task, its priority (high, medium, low), and whether it is time-sensitive (yes, no).")
    print("Based on your inputs, the program will suggest when you should complete your task.")
    print("Let's get started!")
    print("Please enter the details of your task:")

    Task= input("What is your task for today? ")    
    priority = input("what is the priority of your task? (high / medium / low) ")
    Time_sensitivity = input("Is your task time-sensitive? (yes / no) ")
    if priority.lower() == "high" and Time_sensitivity.lower() =="yes":
        print("You should complete this task today. ")
    elif priority.lower() == "high" and Time_sensitivity.lower() =="no":
        print("You should complete this task within the next few days. ")
    elif priority.lower() == "medium" and Time_sensitivity.lower() =="yes":
        print("You should complete this task within the next few days. ")
    elif priority.lower() == "medium" and Time_sensitivity.lower() =="no":
        print("You should complete this task within the next week. ")
    elif priority.lower() == "low" and Time_sensitivity.lower() =="yes":
        print("You should complete this task within the next week. ")
    elif priority.lower() == "low" and Time_sensitivity.lower() =="no":
        print("You can complete this task whenever you have time. ")
    else:
        print("Invalid input. Please try again.")
    print("Thank you for providing the details of your task.")
    print("Welcome to the Daily Reminder Program!")
    daily_reminder()
    while True:
        another_task = input("Do you have another task to add? (yes / no) ")
        if another_task.lower() == "yes":
            daily_reminder()
        elif another_task.lower() == "no":
            print("Thank you for using the Daily Reminder Program!")
            break
        else:
            print("Invalid input. Please try again.")    
def main():
    daily_reminder()
if __name__ == "__main__":
    main()
# This program helps users manage their daily tasks based on priority and time sensitivity.
