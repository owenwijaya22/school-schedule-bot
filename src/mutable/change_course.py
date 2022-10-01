import json


def get_courses():
    with open("./data/data.json", "r+") as file:
        courses = json.load(file)
    return courses


def change_course(courses):
    add_or_change = input("add or change?: ").lower()
    if add_or_change == "c":
        old_course = input("Old course: ")
        courses.pop(old_course)
    new_course = input("New Course: ")
    new_day = input("Day: ")
    new_time = {
        "time starts": input("Time starts: "),
        "time ends": input("Time ends: "),
    }
    new_type = input("Course type: ")
    new_building = input("Building: ")
    new_zoom_link = input("zoom link: ")
    courses.update(
        {new_course: [new_day, new_time, new_type, new_building, new_zoom_link]}
    )
    return courses


courses = get_courses()
courses_now = change_course(courses)
print(courses_now)
