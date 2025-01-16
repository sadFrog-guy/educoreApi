from calendar import monthrange
from datetime import date

def calculate_full_months_excluding_partial(start_date, end_date):
    now = date.today()
    month_diff = 0
    is_last_month = False
    #1. Если нет даты окончания группы, то конец даты для рассчета явлсяется сегодня
    #2. Если сегодняшний месяц не равен месяцу окончания группы, то конечная дата это сегодня, так как мы считаем
    # баланс и нам надо знать сколько должно быть заплачено от начала обучения до сегодня.
    #3. В противном случае мы считаем до установленной даты окончания группы и вычитываем 1 месяц так как последний
    # месяц оплачивается другой суммой так же как и 1 месяц, которые и так не учитывается при вычитании двух дат
    if end_date is None:
        end_date = now
    elif now.month < end_date.month:
        end_date = now
    elif now.month == end_date.month or end_date.month < now.month:
        month_diff -=1
        is_last_month = True

    # Разница в годах и месяцах
    year_diff = end_date.year - start_date.year
    month_diff += end_date.month - start_date.month

    # Общая разница в месяцах
    total_months = year_diff * 12 + month_diff

    # _, last_day_of_month = monthrange(end_date.year, end_date.month)

    return {"count": max(total_months, 0),
            "is_last_month": is_last_month}

