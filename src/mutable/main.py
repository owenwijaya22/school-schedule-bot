from class_attempt import Courses
from course_adder import get_courses
import json

def get_config():
    with open("./data/config.json", "r") as file:
        configs = json.load(file)
        sender = configs["sender"]
        recipient = configs["recipient"]
        password = configs["password"]
    return sender, recipient, password

def main(courses, sender, recipient, password):
    sender, recipient, password = get_config()
    courses = get_courses()

    Bot = Courses(courses)
    Bot.get_today_info()
    Bot.get_courses_info()
    Bot.send_gmail(sender, recipient, password)

if __name__ == "__main__":
    main()