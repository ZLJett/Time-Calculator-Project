# put help statment here

# import for testing
import unittest

def add_time(start, duration, start_day=None):
  # break up start input and store starting am/pm
  split_start_input = start.split() 
  start_ampm = split_start_input[1]
  # break up hours/minutes into their own vars and converts each from string to int
  split_start_time = split_start_input[0].split(":")
  start_hours = int(split_start_time[0])
  start_minutes = int(split_start_time[1])

  # convert hours to 24hr clock
  if start_ampm == "PM":
    start_hours += 12

  # convert start time to minutes
  start_in_minutes = start_hours * 60 + start_minutes

  # break up duration into hours/minutes then convert time to minutes
  duration_hours, duration_minutes = duration.split(":")
  duration_in_minutes = (int(duration_hours) * 60) + int(duration_minutes)

  # total all input time, both start and duration to get total_minutes
  total_minutes = start_in_minutes + duration_in_minutes

  # find total hours and days
  total_hours = total_minutes // 60
  days_elapsed = total_hours // 24 

  # find remaining time
  remaining_hours = total_hours - (days_elapsed * 24)
  remaining_minutes = total_minutes - (total_hours * 60)

  # set am/pm based on 24 hour time
  if remaining_hours < 12:
     final_ampm = "AM"
  else:
    final_ampm = "PM"

  # deal time = zero hundred hours so can convert to 12 hour time
  if remaining_hours == 0: 
    remaining_hours += 12
  # convert back to 24 hour time
  if remaining_hours > 12:
    remaining_hours -= 12

  # set up days later
  if days_elapsed > 0:
    add_days_to_result = True
    if days_elapsed == 1:
      number_days_later = "(next day)"
    else:
      number_days_later = "(" + str(days_elapsed) + " days later)"
  else:
    add_days_to_result = False

  # determine day of week to add, if any 
  if start_day is not None:
    # set a dictionary to assign each day a number, Monday is first day of week
    weekdays_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    # checks if valid input using map() to make all keys in weekday_dict lower case so can compare to input
    if start_day.lower() not in map(lambda weekday: weekday.lower(), weekdays_dict.keys()):
      return "Invaild day entered. Is your spelling correct?"
    # find what day to return
    else: 
      add_weekday_to_result = True
      # determine current day, or rather set vaild input to coresponding key for weekdays_dict
      for weekday in weekdays_dict.keys():
        if weekday.lower() == start_day.lower():
          start_weekday = weekday
      if days_elapsed == 0:
       current_weekday = start_weekday
      else:
        total_days = weekdays_dict[start_weekday] + days_elapsed
        weeks_elapsed = total_days // 7
        final_weekday_number = total_days - (weeks_elapsed * 7)
        # Values from weekdays_dict are equivalent to the index of the list, so using final day's number as index to get weekday from list of weekdays_dict keys
        current_weekday = list(weekdays_dict.keys())[final_weekday_number]
  else:
    add_weekday_to_result = False
  
  # check if remaining_minutes is only sigle digit, i.e. 6 instead of 06, and add zero
  if remaining_minutes < 10:
    fixed_remaining_minutes = "0" + str(remaining_minutes)
  else:
    fixed_remaining_minutes = str(remaining_minutes)
  # determine correct format of return string based on if weekday input and # of days passed
  final_time = str(remaining_hours) + ":" + fixed_remaining_minutes + " "+ final_ampm
  if add_weekday_to_result and add_days_to_result:
    new_time = final_time + ", " + current_weekday + " " + number_days_later
  elif add_days_to_result:
    new_time = final_time + " " + number_days_later
  elif add_weekday_to_result:
    new_time = final_time + ", " + current_weekday
  else:
    new_time = final_time

  return new_time


if __name__ == "__main__":
  print(add_time("11:06 PM", "2:02"))
  unittest.main(module='test_module', exit=False)
  