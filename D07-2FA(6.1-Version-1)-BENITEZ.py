# Student Event Registration
# Version 1 - Basic Input and Output

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = input("Enter event year: ")
month = input("Enter event month (1-12): ")
day = input("Enter event day: ")

full_name = first_name + " " + last_name

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", month + "/" + day + "/" + year)