from datetime import timedelta, datetime

def display_current_datetime():
    current_date = datetime.now()

    print(f"Current date and time :{current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add: "))
    future_date  = datetime.now() + timedelta(days = days_to_add)
    print(f'Future date after adding{days_to_add} days: {future_date.strftime("%Y-%m-%d %H:%M:%S")}')
if __name__ == "__main__":
    current = display_current_datetime()
    calculate_future_date()
   