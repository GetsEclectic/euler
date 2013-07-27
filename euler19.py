import datetime

# sunday
startDate = datetime.date(1901, 1, 6)

endDate = datetime.date(2000, 12, 31)

currentDate = startDate
numSundays = 0
while currentDate <= endDate:
    if currentDate.day == 1:
        numSundays += 1
    currentDate += datetime.timedelta(7)

print numSundays