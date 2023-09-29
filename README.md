# workhours-calculator
Simple python script to calculate worked hours in a day, because I'm too lazy to do simple math at the end of a workday.

## Example
![example](./img/example.png)

## How it works
*Requires python and datetime module.*

Simply run:
```
python3 ./calc.py
```
Then answer prompted questions.

## If changes are necessary
You can change default workday and default lunchtime in the script on line 3 & 4.
```
default_workday = datetime.timedelta(hours=8)
default_lunch_time = datetime.timedelta(hours=1)
```
These are set by default to 8 hour workday with 1 hour lunch.