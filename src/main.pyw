import datetime
import json
import yagmail
import webbrowser

# get today's info
today = datetime.datetime.now()
hour = float(today.time().hour)
day = today.strftime("%A")
# hour = 14
# day = "Friday"
with open("./data/data.json", "r+") as file:
    courses = json.load(file)

# get app password for api auth
with open("./data/config.json", "r") as file:
    configs = json.load(file)
    sender = configs["sender"]
    recipient = configs["recipient"]
    password = configs["password"]

for course, course_infos in courses.items():
    for course_info in course_infos:
        # check todays date if it matches with the day or course
        if day == course_info["day"]:
            course_hour_starts = course_info["time"]["time_starts"]
            # check one hour before class starts
            if hour == float(course_hour_starts) - 1:
                # get class details to be send from gmail
                course_hour_ends = course_info["time"]["time_ends"]
                course_type = course_info["type"]
                zoom_link = course_info["zoom_link"]
                # construct message
                message = f'''
                <p>Course: {course} {course_type}</p>
                <p>Starts at: {course_hour_starts}.00</p>
                <p>Ends at: {course_hour_ends}</p>
                <p><a href="{zoom_link}">zoom link</a></p>
                '''
                # auto buka zoom tab
                if zoom_link:
                    webbrowser.open(zoom_link, new=0)
                # send gmail
                with yagmail.SMTP(sender, password) as yag:
                    yag.send(to=recipient, subject="schedule", contents=message)
