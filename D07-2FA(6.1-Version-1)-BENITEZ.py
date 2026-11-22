# Student Event Registration
# Version 2 - Added String Formatting

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
year = input("Enter event year: ")
month = input("Enter event month (1-12): ")
day = input("Enter event day: ")

full_name = (first_name + " " + last_name).title()

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.upper())
print("Event:", event_name.title())
print("Event Date:", month + "/" + day + "/" + year)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
