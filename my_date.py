def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False oterwise"""
    return (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0))

def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap_year(year):
        days_in_month[2] = 29
    
    return sum(days_in_month[1:month]) + day    

def days_in_a_year(year):
    return 366 if is_leap_year(year) else 365

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    if year1 == year2:
        return ordinal_date(year2, month2, day2) - ordinal_date(year1, month1, day1)

    total_days = 0

    for year in range(year1 + 1, year2):
        total_days += days_in_a_year(year)

    return total_days + days_in_a_year(year1) - ordinal_date(year1, month1, day1) + ordinal_date(year2, month2, day2)

DAYS_OF_WEEK = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    if month < 3:
        year -= 1
        month += 12

    percent = year // 100
    year_percent = year % 100
    
    day_cnt = (day + ((13 * (month + 1)) // 5) + year_percent +
            (year_percent // 4) + (percent // 4) - (2 * percent))
    
    day_num = day_cnt % 7
    
    return DAYS_OF_WEEK[day_num - 1]

def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    mnt_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    d_name = day_of_week(year, month, day)
    m_name = mnt_names[month]
    return f"{d_name}, {day:02d} {m_name} {year}"



