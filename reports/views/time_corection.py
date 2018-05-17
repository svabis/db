# -*- coding: utf-8 -*-

# DST
def dst(time):
    import calendar
    import datetime
    date = time.date()
    year = date.year

    dst_start = max(week[-1] for week in calendar.monthcalendar(year, 10))
    dst_end   = max(week[-1] for week in calendar.monthcalendar(year, 3))
    date_dst_start = datetime.date(year, 10, dst_start)
    date_dst_end = datetime.date(year, 3, dst_end)

    if date_dst_end <= date <= date_dst_start:
        return 3
    else:
        return 2
