import os
import time
from datetime import datetime
from datetime import timedelta

## FUNCTION DEFINITIONS
def countdown(shutdownTime):
    timeDifference = shutdownTime - datetime.now()
    totalSeconds = timeDifference.seconds

    print('\nCommencing countdown timer!')
    while totalSeconds:
        remainingHours, remainingSeconds = divmod(totalSeconds, 3600)
        remainingMinutes, remainingSeconds = divmod(remainingSeconds, 60)
        print("shutting down in " + str(remainingHours) + 'h '+ str(remainingMinutes) + 'm '+ str(remainingSeconds) + 's ', end='\r')
        time.sleep(1)
        totalSeconds -= 1


## MAIN START
shutdownInput = input('Enter minutes or a time (hh:mm) to shut down: ')

secondsUntilShutdown = 0
now = shutdownTime = datetime.now()

if ':' in shutdownInput:
    # split up hh:mm into separate values
    hourMinutes = shutdownInput.split(':')
    shutdownHour = int(hourMinutes[0])
    shutdownMinutes = int(hourMinutes[1])

    # new datetime object with the user's input
    shutdownTime = now.replace(hour = shutdownHour, minute = shutdownMinutes, second = 0)

    # assume next day shutdown if the shutdown time is before 'now'
    if shutdownTime < now:
        shutdownTime = shutdownTime + timedelta(days=1)
    timedifference = shutdownTime - now
    secondsUntilShutdown = timedifference.seconds
else:
    minutesUntilShutdown = int(shutdownInput)
    shutdownTime = now + timedelta(minutes=minutesUntilShutdown)

formattedShutdownTime = shutdownTime.strftime('\nThe system will be shut down at %d.%m.%Y %H:%M')
print(formattedShutdownTime)

countdown(shutdownTime)
os.system("shutdown /s /t")
