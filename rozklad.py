from datetime import datetime, timedelta
from typing import List

def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> List[datetime]:
    # Створення порожнього списку для зберігання розкладу
    schedule = []
    # Цикл для генерації розкладу на `days` днів
    for i in range(days):
        # Якщо це перший день в розкладі, додаємо `start_date`
        if i == 0:
            schedule.append(start_date)
        # Якщо це не перший день, беремо останню дату з розкладу
        else:
            prev_date = schedule[-1]
            # Якщо останній день був робочим
            if len(schedule) % (work_days + rest_days) < work_days:
                # Додати наступний робочий день
                schedule.append(prev_date + timedelta(days=1))
            # Якщо останній день був вихідним
            else:
                # Додати наступний день відпочинку
                schedule.append(prev_date + timedelta(days=rest_days))
    # Повертаємо розклад робочих днів у форматі списку дат
    return schedule
date_str = '04-19-2023'
date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
print(generate_schedule(5, 3, 1, date_object))