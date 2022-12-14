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
                <p>Starts at: {self.time_starts}</p>
                <p>Ends at: {self.time_ends}</p>
                <p>Building: {self.building}</p>
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
        # assuming my laptop will never shutdown, fk i need to build my own raspeberry pi server asap, heroku is slow af
        if today == self.day:
            # if less than 30 minutes before class, send email to notify
            check = float(self.time_starts) - today_hour_minute
            if check <= 0.7 and check >= 0.41:
                self.send_email(sender, recipient, password)
                if self.zoom_link:
                    self.open_zoom()
            # i have to sort my datas if i use this method so meh
            # if today_hour_minute < float(self.time_starts):
            #         self.send_email(sender, recipient, password)
            #         self.open_zoom()
            #         return True
