from datetime import datetime


# this function takes a string and returns True as text if the string is a valid time in the format "hh:mm-dd-mm-yyyy" otherwise it returns the time in the wanted format
def timeInText(textv):
    text = textv.replace(" ", "")
    if len(text) < 16:
        # current_time = datetime.now()
        # hour = str(current_time.hour)
        # minutes = str(current_time.minute)
        # day = str(current_time.day)
        # month = str(current_time.month)
        # year = str(current_time.year)
        # return hour + ":" + minutes + "-" + day + "-" + month + "-" + year
        date = datetime.now()
        t = date.strftime("%H:%M-%d-%m-%Y")
        return t
    sliced = text[0:16]
    try:
        hourandminutes, day, month, year = sliced.split("-")
        hour, minutes = hourandminutes.split(":")
        hour = int(hour)
        minutes = int(minutes)
        day = int(day)
        month = int(month)
        year = int(year)
        if (
            hour > 23
            or hour < 0
            or minutes > 59
            or minutes < 0
            or day > 31
            or day < 1
            or month > 12
            or month < 1
            or year < 1000
        ):
            timeInText(text[1:])
        return sliced
    except:
        return timeInText(text[1:])


def convert_to_DaterTime(time):
    dt = datetime.strptime(time, "%H:%M-%d-%m-%Y")
    return dt


print(timeInText("cw6:23-12-10-2012wernirf"))
convert_to_DaterTime("6:23-12-10-2012")
