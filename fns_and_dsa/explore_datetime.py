from datetime import timedelta, datetime

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time :{current_date.strftime('%Y-%m-%d %H:%M:%S')}")
if __name__ == "__main__":
    display_current_datetime()
   