import datetime
import json
import yagmail
import webbrowser


class Courses:
    def __init__(
        self, course_name, course_type, day, time_starts, time_ends, building, zoom_link=None
    ):
        self.course_name = course_name
        self.course_type =  course_type
        self.day = day
        self.time_starts = time_starts
        self.time_ends = time_ends
        self.building = building
        self.zoom_link = zoom_link
    
    def send_email(self, sender, password, recipient):
        today = datetime.datetime.now()
        hour = 14
        self.day = "Friday"
        # hour = float(today.time().hour)
        # day = today.strftime("%A")
        if today == self.day:
            if hour == int(self.time_starts[:2])-1:
                message =  f"""
                    <p>Course: {self.course_name} {self.course_type}</p>
                    <p>Starts at: {self.time_starts}.00</p>
                    <p>Ends at: {self.time_ends}</p>
                    <p><a href="{self.zoom_link}">zoom link</a></p>        
                    """
                with yagmail.SMTP(sender, password) as yag:
                    yag.send(to=recipient, subject="schedule", contents=message)
                  

    
    


C01_C = Courses(
    "CS1302",
    "lecture"
    "Monday",
    "12:00",
    "16:50",
    "YEUNG LT-2",
    "https://cityu.zoom.us/j/97540196724?pwd=d0E1eVpHOXZna3UyL2o1ZDhUNHVHZz09&uname=Owen+VALENTINUS",
)

L04 = Courses(
    "CS1302",
    "lab"
    "Monday",
    "16:00",
    "16:50",
    "LI 4400",
    "https://cityu.zoom.us/j/99053961777?pwd=cWMvVVpxbzF4MXEwNytGLy9FMGRKdz09&uname=Owen+VALENTINUS",
)


CE1_0 = Courses(
    "MA1200",
    "lecture",
    "Tuesday",
    "10:00",
    "11:50",
    "YEUNG LT-5",
    "https://cityu.zoom.us/j/96115175728?pwd=VGR5ekRzMWRBdHFzaElpcUlzalZidz09&uname=Owen+VALENTINUS",
)
L03 = Courses(
    "PHY1201",
    "lab",
    "Tuesday",
    "15:00",
    "17:50",
    "YEUNG G5-317"
)
T02 = Courses(
    "JC2066",
    "tutorial",
    "Wednesday",
    "09:00",
    "09:50",
    "YEUNG LT-2",
    "https://cityu.zoom.us/j/97748439786?uname=Owen+VALENTINUS"


)
TE1 = Courses(
    "MA1200",
    "tutorial",
    "Wednesday",
    "13:00",
    "13:50",
    "YEUNG B5-210"
)


C02 = Courses(
    "PHY1201",
    "Wednesday",
    "16:00",
    "17:50",
    "YEUNG LT-1",
    "https://cityu.zoom.us/j/93998400956?uname=Owen+VALENTINUS",
)

T01 = Courses(
    "PHY1201",
    "Thursday",
    "11:00",
    "11:50",
    "YEUNG LT-2",
    "https://cityu.zoom.us/j/92199559650?uname=Owen+VALENTINUS",
)

CE1_1 = Courses(
    "MA1200",
    "lecture",
    "Thursday",
    "15:00",
    "16:50",
    "YEUNG LT-5",
    "https://cityu.zoom.us/j/99899247499?pwd=TVByckx2U1U2S0YvV0xpbFVqYWJvZz09&uname=Owen+VALENTINUS",
)

C01_J = Courses(
    "JC2066",
    "lecture",
    "Friday",
    "09:00",
    "11:50",
    "YEUNG LT-2",
    "https://cityu.zoom.us/j/97748439786?uname=Owen+VALENTINUS",    
)

T90 = Courses(
    "GE1401",
    "tutorial",
    "Friday",
    "15:00",
    "17:50",
    "YEUNG B5-209"
)
