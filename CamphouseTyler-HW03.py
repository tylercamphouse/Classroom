def is_leap_year(year):
  """Checks if a given year is a leap year."""
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False
def get_day_of_week(month, day, year):
  """Calculates the day of the week for a given date."""
  if not 1 <= month <= 12:
    return "Invalid month."
  if not 1 <= day <= 31:
    return "Invalid day."
  if not 1900 <= year <= 2100:
    return "Invalid year."
  if month == 2:
    if is_leap_year(year):
      if day > 29:
        return "Invalid day for February in a leap year."
    else:
      if day > 28:
        return "Invalid day for February."
  y = year - 1
  jan_first_day = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
  days_passed = 0
  for i in range(1, month):
    if i in [1, 3, 5, 7, 8, 10, 12]:
      days_passed += 31
    elif i == 2:
      if is_leap_year(year):
        days_passed += 29
      else:
        days_passed += 28
    else:
      days_passed += 30
  days_passed += day - 1
  day_of_week = (jan_first_day + days_passed) % 7
  days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  return days_of_week[day_of_week]
date_str = input("Enter a date in MM/DD/YYYY format: ")
month, day, year = map(int, date_str.split("/"))
result = get_day_of_week(month, day, year)
print(result)