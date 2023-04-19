from datetime import datetime, timedelta
from typing import List

def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> List[datetime]:
    schedule = []
    day_count = 0

    while len(schedule) < days:
        current_date = start_date + timedelta(days=day_count)
        if current_date.weekday() < 5 and day_count % (work_days + rest_days) < work_days:
            schedule.append(current_date)
        day_count += 1

    return schedule
start_date = datetime(2020, 1, 30)
schedule = generate_schedule(days=5, work_days=2, rest_days=1, start_date=start_date)
print(schedule)
