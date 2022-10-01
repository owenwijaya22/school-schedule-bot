import datetime
import yagmail
import json

class Courses:
    def __init__(self, courses):
        self.courses = courses

    def get_today_info(self):
        # get today's info
        today = datetime.datetime.now()
        self.hour = float(today.time().hour)
        self.day = self.today.strftime("%A")

    def get_courses_info(self):
        for course, course_infos in self.courses.items():
            for course_info in course_infos:
                # check todays date if it matches with the day or course
                if self.day == course_info["day"]:
                    course_hour_starts = course_info["time"]["time_starts"]
                    # check one hour before class starts
                    if self.hour == float(course_hour_starts) - 1:
                        # get class details to be send from gmail
                        course_hour_ends = course_info["time"]["time_ends"]
                        course_type = course_info["type"]
                        zoom_link = course_info["zoom_link"]
                        # construct message
                        self.message = f"""
                        <p>Course: {course} {course_type}</p>
                        <p>Starts at: {course_hour_starts}.00</p>
                        <p>Ends at: {course_hour_ends}</p>
                        <p><a href="{zoom_link}">zoom link</a></p>
                        """
    def send_gmail(self, sender, recipient, password):
        with yagmail.SMTP(self.sender, self.password) as yag:
            yag.send(to=self.recipient, subject="schedule", contents=self.message)

