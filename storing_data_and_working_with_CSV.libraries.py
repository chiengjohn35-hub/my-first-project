#to do list
import csv

todo = {
    "monday":{
        "morning": "Revision",
        "afternoon": "Practice",
        "evening": "physical activity"
    },
    "tuesday":{
        "morning": "practice",
        "afternoon": "revision",
        "evening": "physical activity"
    },
    "wednesday": {
    "morning": "practice",
    "afternoon": "Practice",
    "evening": "revision"
    },
    "thursday": {
        "morning": "physical activity",
        "afternoon": "revision",
        "evening": "practice"
    },
    "friday": {
        "morning": "practice",
        "afternoon": "revision",
        "evening": "physical activity"
    }
}

print("       my todo list",)
for i, obj in todo.items():
    print("----------------------------")
    print(i)
    for y in obj:
        print(y  + ":", obj[y])
print(sep=" ")

while True:
    day = input("enter the day to check out your schedule on todo list: ").strip()
    if not day in todo:
        print(f"there's no {day} in todo list!")
        print("Please check your day spellings!")
    else:
        enter_time = input("Enter what time is the schedule (Morning/afternoon/evening) : ").strip().lower()
        if enter_time in todo[day]:
            print(f"Yes Sir, You have a {todo[day][enter_time]} scheduled")
            print(f"on {day} at ", enter_time, "hours.")

            with open("chieng.cvs", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(f"{day} - {enter_time}" )
            break








