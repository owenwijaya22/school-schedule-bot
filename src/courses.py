import datetime
import webbrowser
import yagmail
import json

class Course:
    def __init__(self, course_info, course_name):
        self.course_name = course_name
        self.day = course_info["day"]
        self.time_starts = course_info["time"]["time_starts"]
        self.time_ends = course_info["time"]["time_ends"]
        self.course_type = course_info["course_type"]
        self.building = course_info["building"]
        self.zoom_link = course_info["zoom_link"]

    def send_email(self, sender, recipient, password):
        message = f"""
                <p>Course: {self.course_name} {self.course_type}</p>
                <p>Starts at: {self.time_starts}.00</p>
                <p>Ends at: {self.time_ends}</p>
                <p><a href="{self.zoom_link}">zoom link</a></p>        
                """
        with yagmail.SMTP(sender, password) as yag:
            yag.send(to=recipient, subject="schedule", contents=message)

    def open_zoom(self):
        if self.zoom_link:
            webbrowser.open(self.zoom_link)

    def is_near(self, sender, recipient, password):
        today_info = datetime.datetime.now()
        today = today_info.strftime("%A")
        today_hour_minute = float(today_info.strftime("%H.%M"))
        if today == self.day:
            # if less than 10 minutes before class, send email to notify
            if float(self.time_starts) - today_hour_minute <= 0.90:
                self.send_email(sender, recipient, password)
            # if less than 5 minutes before class, open zoom class
            if float(self.time_starts) - today_hour_minute <= 0.45:
                self.open_zoom()

