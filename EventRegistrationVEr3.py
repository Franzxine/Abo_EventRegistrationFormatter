from datetime import datetime

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
enter_year = input("Enter the year of the event (YYYY): ")
enter_month = input("Enter the month of the event (MM): ")
enter_day = input("Enter the day of the event (DD): ")

clean_first_name = first_name.strip().title()
clean_last_name = last_name.strip().title()
clean_full_name = f"{clean_first_name} {clean_last_name}"
name_code = clean_full_name.upper()
clean_section = section.strip().upper()
clean_event_name = event_name.strip().title()

date_string = f"{enter_year}-{enter_month}-{enter_day}"
event_date = datetime.strptime(date_string, "%Y-%m-%d")

print("\nStudent Event Registration Summary")
print(f"Name: {clean_full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {clean_section}")
print(f"Event: {clean_event_name}")
print(f"Event Date: {event_date.strftime('%B %d, %Y')}")
print("Language Used: Python")
print("String Method/Function Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")