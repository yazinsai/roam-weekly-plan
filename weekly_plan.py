import sys
import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def next_week():
    today = datetime.date.today()
    next_sunday = today + datetime.timedelta(days=-today.weekday()-1, weeks=1)
    return [
        custom_strftime("%B {S}, %Y", next_sunday + datetime.timedelta(days=i))
        for i in range(0, 7)
    ]


def generate_template():
    week = next_week()
    template = """
Week:: [[{sunday}]]
## Top Weekly Goals
## [[Weekly Habits]]
    
## Daily Goals
    Sunday: [[{sunday}]]
    Monday: [[{monday}]]
    Tuesday: [[{tuesday}]]
    Wednesday: [[{wednesday}]]
    Thursday: [[{thursday}]]
    Friday: [[{friday}]]
    Saturday: [[{saturday}]]
    """.format(
        sunday=week[0],
        monday=week[1],
        tuesday=week[2],
        wednesday=week[3],
        thursday=week[4],
        friday=week[5],
        saturday=week[6],
    )
    return template


s = generate_template()
sys.stdout.write(s)
