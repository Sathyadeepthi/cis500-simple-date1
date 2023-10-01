#######################################################
# my_date
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def ordinal_date(year: int, month: int, day: int) -> int:
    """Return the number of days elapsed since the beginning of the year, including any partial days."""

    # Define the number of days in each month (non-leap year)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if it's a leap year and update February's days accordingly
    if is_leap_year(year):
        days_in_month[2] = 29

    # Calculate the ordinal date
    ordinal = day
    for i in range(1, month):
        ordinal += days_in_month[i]

    return ordinal


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    """Return the number of days that have elapsed between two dates."""

    # Define the number of days in each month for a non-leap year
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate the ordinal date for both dates
    ordinal_date1 = sum(days_in_month[:month1]) + day1
    if is_leap_year(year1) and month1 > 2:
        ordinal_date1 += 1

    ordinal_date2 = sum(days_in_month[:month2]) + day2
    if is_leap_year(year2) and month2 > 2:
        ordinal_date2 += 1

    # Calculate the number of days in year1 from the first date
    days_in_year1 = 365
    if is_leap_year(year1):
        days_in_year1 += 1

    # Calculate the number of days in year2 from the second date
    days_in_year2 = 365
    if is_leap_year(year2):
        days_in_year2 += 1

    # Calculate the number of days elapsed between the two dates
    total_days_elapsed = 0

    # Add the days remaining in year1 from the first date
    total_days_elapsed += days_in_year1 - ordinal_date1

    # Add the days passed in year2 from the second date
    total_days_elapsed += ordinal_date2

    # Add the days for the years between year1 and year2 (excluding year1 and year2)
    for year in range(year1 + 1, year2):
        total_days_elapsed += 365
        if is_leap_year(year):
            total_days_elapsed += 1

    return total_days_elapsed


def day_of_week(year: int, month: int, day: int) -> str:
    """Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day."""

    # Define the days of the week
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Calculate the number of days that have elapsed from the reference date to the given date
    total_days_elapsed = 0

    # Calculate the days in years between the reference year and the given year
    for y in range(1753, year):
        total_days_elapsed += 366 if is_leap_year(y) else 365

    # Calculate the days in months between the reference month and the given month
    for m in range(1, month):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap_year(year) and m == 2:
            days_in_month[m] = 29
        total_days_elapsed += days_in_month[m]

    # Add the day of the month
    total_days_elapsed += day

    # Find the day of the week using modulus 7
    day_index = (total_days_elapsed - 1) % 7

    return DAYS_OF_WEEK[day_index]
