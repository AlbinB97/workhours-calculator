#!/usr/bin/env python3
import datetime
import inquirer
import colorama

project_one = "R&D"
project_two = "Ops"
project_three = "Consulting"

default_workday = datetime.timedelta(hours=8)
default_lunch_time = datetime.timedelta(hours=1)
reset_color = colorama.Style.RESET_ALL

start_time_str = input(colorama.Fore.CYAN + "Enter the start time (HH:MM) > " + reset_color)
start_time = datetime.datetime.strptime(start_time_str, "%H:%M")

end_time_str = input(colorama.Fore.CYAN + "Enter the end time (HH:MM) > " + reset_color)
end_time = datetime.datetime.strptime(end_time_str, "%H:%M")

time_elapsed = end_time - start_time

lunch_time_minutes = int(input(colorama.Fore.CYAN + "Enter the length of your lunch break (in minutes) > " + reset_color))
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

print(colorama.Fore.LIGHTBLACK_EX + ("-" * 50) + reset_color)
print(f"Total Time Worked: {formatted_total_worktime}")
print(f"Flex Time: {formatted_flex_time}")
print(colorama.Fore.LIGHTBLACK_EX + ("-" * 50) + reset_color)

projects = [
    inquirer.Checkbox('projects',
                      message='Select projects you worked on',
                      choices=[project_one, project_two, project_three])
]
answers = inquirer.prompt(projects)
selected_projects = answers['projects']

for project in selected_projects:
    hours_worked_on_project = input(colorama.Fore.CYAN + "How many hours did you work on " + colorama.Fore.LIGHTBLUE_EX + f"{project}" + colorama.Fore.CYAN + " (H:M) > " + reset_color)
    answer_hours, answer_minutes = map(int, hours_worked_on_project.split(":"))
    if project == project_one:
        projone_time = datetime.timedelta(hours=answer_hours, minutes=answer_minutes)
    elif project == project_two:
        projtwo_time = datetime.timedelta(hours=answer_hours, minutes=answer_minutes)
    elif project == project_three:
        projthree_time = datetime.timedelta(hours=answer_hours, minutes=answer_minutes)

total_internal_time = total_worktime

for project in selected_projects:
    if project == project_one:
        total_internal_time = total_internal_time - projone_time
    elif project == project_two:
        total_internal_time = total_internal_time - projtwo_time
    elif project == project_three:
        total_internal_time = total_internal_time - projthree_time

total_internal_time_str = str(total_internal_time).split(":")[:2]
formatted_total_internal_worktime = ":".join(total_internal_time_str)

print(colorama.Fore.LIGHTBLACK_EX + ("-" * 50) + reset_color)
print(f"Internal Time Worked: {formatted_total_internal_worktime}")

for project in selected_projects:
    if project == project_one:
        total_projone_time_str = str(projone_time).split(":")[:2]
        formatted_projone_time = ":".join(total_projone_time_str)
        print(f"{project_one} Time Worked: {formatted_projone_time}")
    elif project == project_two:
        total_projtwo_time_str = str(projtwo_time).split(":")[:2]
        formatted_projtwo_time = ":".join(total_projtwo_time_str)
        print(f"{project_two} Time Worked: {formatted_projtwo_time}")
    elif project == project_three:
        total_projthree_time_str = str(projthree_time).split(":")[:2]
        formatted_projthree_time = ":".join(total_projthree_time_str)
        print(f"{project_three} Time Worked: {formatted_projthree_time}")

print(colorama.Fore.LIGHTBLACK_EX + ("-" * 50) + reset_color)
