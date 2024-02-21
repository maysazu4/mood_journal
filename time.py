from datetime import datetime

def timeInText(text):
    if len(text) < 16:
        current_time = datetime.now()
        hour = str(current_time.hour)
        minutes = str(current_time.minute)
        day = str(current_time.day)
        month = str(current_time.month)
        year = str(current_time.year)
        return hour+":"+minutes+"-"+day+"-"+month+"-"+year
    sliced =text[0:16]
    try:
        hourandminutes, day, month, year = sliced.split('-')
        hour,minutes = hourandminutes.split(':')
        hour = int(hour)
        minutes = int(minutes)
        day = int(day)
        month = int(month)
        year = int(year)
        if(hour > 23 or hour<0 or minutes > 59 or minutes < 0 or day > 31 or day < 1 or month > 12 or month < 1 or year < 0):
            timeInText(text[1:])
        return datetime(year, month, day, hour, minutes).strftime("%A, %d %B %Y %I:%M %p")
    except:
        return timeInText(text[1:])

print(timeInText("cw16:23-12-10-2012wernirf"))