from icalendar import Calendar, Event

g = open('D:/00_SARDARCHITECTLABS/local data/google-calendar-data/Projects_cadsvskbdp4b4a5njoeh4lp314@group.calendar.google.com.ics','rb')
gcal = Calendar.from_ical(g.read())

for component in gcal.walk():
    if component.name == "VEVENT":
        print(component['DTSTART'].dt)
        break
g.close()
