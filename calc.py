#!/usr/bin/env python3
import datetime

default_workday = datetime.timedelta(hours=8)
default_lunch_time = datetime.timedelta(hours=1)

start_time_str = input("Enter the start time (HH:MM): ")
start_time = datetime.datetime.strptime(start_time_str, "%H:%M")

end_time_str = input("Enter the end time (HH:MM): ")
end_time = datetime.datetime.strptime(end_time_str, "%H:%M")

time_elapsed = end_time - start_time

lunch_time_minutes = int(input("Enter the length of your lunch break (in minutes): "))
remaining_lunch = default_lunch_time - datetime.timedelta(minutes=lunch_time_minutes)

total_worktime = (time_elapsed - default_lunch_time) + remaining_lunch
flex_time = total_worktime - default_workday

total_worktime_str = str(total_worktime).split(":")[:2]
formatted_total_worktime = ":".join(total_worktime_str)

if flex_time < datetime.timedelta(0):
    flex_time_str = str(-flex_time).split(":")[:2]
    formatted_flex_time = "-" + ":".join(flex_time_str)
else:
    flex_time_str = str(flex_time).split(":")[:2]
    formatted_flex_time = ":".join(flex_time_str)

print("-" * 50)
print(f"Total Time Worked: {formatted_total_worktime}")
print(f"Flex Time: {formatted_flex_time}")
print("-" * 50)
