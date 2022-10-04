
def add_course():
    courses = {}
    for _ in range(int(input("How many courses are you going to add?: "))):
        course_name = input("course name: ")
        if course_name == "":
            break
        courses[course_name] = []
    return courses


def add_course_info(courses):
    index_dict = {
        0: "first",
        1: "second",
        2: "third",
        3: "fourth",
        4: "fifth",
        5: "sixth",
    }

    for index, course_name in enumerate(courses):
        course_type = input(f"{course_name} {index_dict.get(index)} class type (lecture, lab, tutorial): ")
        day = input("day: ")
        time_starts = input("time starts: ")
        time_ends = input("time ends: ")
        building = input("building: ")
        zoom_link = input("zoom link: ")
        courses[course_name] = [
            {
                "day": day,
                "time": {"time_starts": time_starts, "time_ends": time_ends},
                "course_type": course_type,
                "building": building,
                "zoom_link": zoom_link,
            }
        ]
        return courses

#to be implemented/refactored later
def change_course(courses):
    add_or_change = input("add or change?: ").lower()
    if add_or_change == "c":
        old_course = input("Old course: ")
        courses.pop(old_course)
    course_name = input("course name: ")
    course_type = input("course type: ")
    day = input("day: ")
    building = input("building: ")
    zoom_link = input("zoom link: ")
    time_starts = input("time starts: ")
    time_ends = input("time ends: ")
    courses[course_name] = [
        {
            "day": day,
            "time": {"time_starts": time_starts, "time_ends": time_ends},
            "course_type": course_type,
            "building": building,
            "zoom_link": zoom_link,
        }
    ]
    return courses
