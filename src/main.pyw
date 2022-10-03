from courses import Course
import json

with open("./data/data.json", "r+") as file:
    courses = json.load(file)

with open("./data/config.json", "r") as file:
    configs = json.load(file)
    sender = configs["sender"]
    password = configs["password"]
    recipient = configs["recipient"]

for course_name, course_infos in courses.items():
    for course_info in course_infos:
        course = Course(course_info, course_name)
        if course.is_near():
            course.send_email(sender, recipient, password)
            course.open_zoom()
