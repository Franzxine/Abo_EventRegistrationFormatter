first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
enter_year = input("Enter the year of the event (YYYY): ")
enter_month = input("Enter the month of the event (MM): ")
enter_day = input("Enter the day of the event (DD): ")

full_name = f"{first_name} {last_name}"
date_string = f"{enter_year}-{enter_month}-{enter_day}"

print("\nStudent Event Registration Summary")
print(f"Name: {full_name}")
print(f"Name Code: {full_name}")
print(f"Section: {section}")
print(f"Event: {event_name}")
print(f"Event Date: {date_string}")
print("Language Used: Python")
print("String Method/Function Used: none yet")
print("Date/Time Feature Used: none yet")
print("Registration record created successfully.")