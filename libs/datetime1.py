from datetime import datetime as dt

course_start = dt(2024, 3, 30, 12)
current = dt.now()
course_end = dt.strptime('15:00 14.07.2024', '%H:%M %d.%m.%Y')

# >>> course_start
# datetime.datetime(2024, 3, 30, 12, 0)
# >>>
# >>> current
# datetime.datetime(2024, 5, 18, 12, 51, 55, 602823)
# >>>
# >>> course_end
# datetime.datetime(2024, 7, 14, 15, 0)

# >>> current - course_start
# datetime.timedelta(days=49, seconds=3115, microseconds=602823)
# >>>
# >>> course_end - current
# datetime.timedelta(days=57, seconds=7684, microseconds=397177)

