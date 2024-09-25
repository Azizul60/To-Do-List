to_do = {
    "6:00 am": "Wake up",
    "8:00 am": "Prepare for office & breakfast",
    "9:00 am": "On my way to office",
    "1:30 pm": "Lunch & Prayer",
    "5:00 pm": "Heading towards home",
    "6:00 pm": "Prayer",
    "9:00 pm": "Dinner",
    "11:00 pm": "It's bed time"
}

# Ask the user for the current time to see what to do now
user = input("What time is it now (e.g., '6:00 am'): ").strip()

# Check if the input matches any key in the dictionary
if user in to_do:
    print(f"Now it's time to: {to_do[user]}")
else:
    print("No tasks scheduled for this time.")
