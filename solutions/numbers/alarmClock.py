"""
Written by Jesse Evers

This is an alarm clock. It can be set for X number of time units from
now, or for a specific time.
"""

import time
from datetime import datetime
import os


def alarmClock():

    alarmType = input("Enter 'timer' if you want an alarm for a certain amount of time, or 'alarm' if you want an alarm for a specific time: ")

    if alarmType.lower() == "timer":
        numMins = float(input("How many minutes from now do you want the alarm to go off? "))
        time.sleep(60 * numMins)
        os.system("mplayer alarm.wav")
        print("Thanks for using the alarm clock!")
    elif alarmType.lower() == "alarm":
        today = input("Is this alarm for today, or a different day? [y/n] ")

        if today.lower() == "n":
            year = int(input("Enter the year (yyyy): "))
            month = int(input("Enter the month (mm): "))
            day = int(input("Enter the day (dd): "))
        else:
            currentTime = datetime.today()
            year = currentTime.year
            month = currentTime.month
            day = currentTime.day

        hour = int(input("Enter the hour (0-23): "))
        minute = int(input("Enter the minute (0-59): "))
        alarmTime = datetime(year, month, day, hour, minute)

        while datetime.now() < alarmTime:
            time.sleep(1)

        os.system("mplayer alarm.wav")


alarmClock()