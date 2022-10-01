import courses
import json
with open("../../data/config.json", "r") as file:
    configs = json.load(file)
    sender = configs["sender"]
    password = configs["password"]
    recipient = configs["recipient"]

all_courses = [courses.C01_C, courses.L04, courses.CE1_0, courses.L03, courses.T02, courses.TE1, courses.C02, courses.T01, courses.CE1_1, courses.C01_J, courses.T90]

for course in all_courses:
    course.send_email(sender, password, recipient)