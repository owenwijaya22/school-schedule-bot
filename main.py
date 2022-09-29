import datetime
import json
import yagmail
import webbrowser

#get today's info
today = datetime.datetime.now()
hour = float(today.time().hour)
day = today.strftime("%A")
message = ""
with open("./data/data.json", "r+") as file:
    courses = json.load(file)

#get app password for api auth
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
                #get class details to be send from gmail
                course_hour_ends = course_info["time"]["time_ends"]
                lesson_type = course_info["type"]
                zoom_link = course_info["zoom_link"]
                #construct message
                message += f"lu ad {course} {lesson_type} jam {course_hour_starts}\n selesai jam {course_hour_ends}\n nih zoom link {zoom_link} (udh auto buka juga sih di laptop)\n"
                #auto buka zoom tab
                webbrowser.open_new_tab(zoom_link)
                # send gmail
                with yagmail.SMTP(sender, password) as yag:
                    yag.send(to=recipient, subject="schedule", contents=message)
