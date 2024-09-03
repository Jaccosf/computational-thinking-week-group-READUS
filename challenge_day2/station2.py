from datetime import datetime

def solution_station_2(date):
    formatted_date = datetime.strptime(date, '%Y-%m-%d')
    day = formatted_date.weekday()
    if day == 0:
        return "月曜日"
    elif day == 1:
        return "火曜日"
    elif day == 2:
        return "水曜日"
    elif day == 3:
        return "木曜日"
    elif day == 4:
        return "金曜日"
    elif day == 5:
        return "土曜日"
    elif day == 6:
        return "日曜日"