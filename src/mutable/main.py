from mutable_class import Courses
from change_course import get_courses

def main():
    courses = get_courses()

    Bot = Courses(courses)
    Bot.get_config()
    Bot.get_today_info()
    Bot.get_courses_info()
    Bot.send_gmail()


if __name__ == "__main__":
    main()
