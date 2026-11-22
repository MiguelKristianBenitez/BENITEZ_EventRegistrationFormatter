# Student Event Registration
# Version 3 - Added Date Formatting

from datetime import date

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()

year = int(input("Enter event year: "))
month = int(input("Enter event month (1-12): "))
day = int(input("Enter event day: "))

full_name = (first_name + " " + last_name).title()
event_date = date(year, month, day)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.upper())
print("Event:", event_name.title())
print("Event Date:", event_date.strftime("%B %d, %Y"))
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("\nRegistration record created successfully.")
