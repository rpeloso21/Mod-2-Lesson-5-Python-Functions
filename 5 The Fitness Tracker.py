

activities = []
durations = []

# Task 1
def log_activity():
    while True:
        activity = input("What activity would you like to log?")
        activities.append(activity)

        duration = input(f"How long did you do your {activity} for?  Please list time in minutes.")
        durations.append(duration)
        if input("Would you like to add another activity?").lower() == "yes":
            continue
        else:
            break

# Task 2
def calorie_counter():
    total_calories_burned = 0

    for x in durations:
        calories_burned = float(x) * 3.5
        total_calories_burned += calories_burned
    
    return total_calories_burned

# Task 3
def summary():
    input("Would you like to see your workout summary?")
    x = 0
    for y in activities:
        print(f"You completed your {activities[x]} for {durations[x]}.")
        x += 1

    print(f"You burned {calorie_counter()} calories!  Congratulations!")

log_activity()
calorie_counter()
summary()