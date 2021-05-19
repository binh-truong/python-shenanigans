import os
import time
from datetime import datetime
from datetime import timedelta

def countdown(shutdownTime):
    """
    countdown counts down until a time has reached

    :param shutdownTime: datetime object when the count down should stop
    """ 
    print('\nCommencing countdown timer!')

    while datetime.now() < shutdownTime:
        timeRemaining = shutdownTime - datetime.now()
        # split is used to remove the microseconds from the timedelta string
        print("shutting down in " + str(timeRemaining).split(".")[0], end='\r')
        time.sleep(1)

def main():
    shutdownInput = input('Enter minutes or a time (hh:mm) to shut down: ')

    # initialize our time variables at the same time
    now = shutdownTime = datetime.now()

    # use the given input time format to distinguish between the two use cases
    if ':' in shutdownInput:
        hourMinutes = shutdownInput.split(':')
        shutdownHour = int(hourMinutes[0])
        shutdownMinutes = int(hourMinutes[1])

        # new datetime object with the user's input 
        # example input = 13:37 | 03.05.2021 12:00 -> 03.05.2021 13:37
        shutdownTime = now.replace(hour = shutdownHour, minute = shutdownMinutes, second = 0)

        # we have to change to the next day if the input time is after a date change
        # example input = 02:00, now is 16:00 | 03.05.2021 02:00 -> 04.05.2021 02:00
        if shutdownTime < now:
            shutdownTime = shutdownTime + timedelta(days=1)
    else:
        # calculate the shutdown time by adding using user input minutes
        minutesUntilShutdown = int(shutdownInput)
        shutdownTime = now + timedelta(minutes=minutesUntilShutdown)

    # pretty print and count down
    formattedShutdownTime = shutdownTime.strftime('\nThe system will be shut down at %d.%m.%Y %H:%M')
    print(formattedShutdownTime)

    countdown(shutdownTime)

    # kill it
    os.system("shutdown /s /t 00")

if __name__ == "__main__":
    main()