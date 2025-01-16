from salesFunnel.models import SalesFunnelStage

def create_pre_course_sales_funnel_stages():
    stages = [
        {"name": "Первичный контакт", "order": 1},  # Клиент узнал о школе или связался впервые
        {"name": "Запрос информации", "order": 2},  # Клиент запросил информацию о курсах
        {"name": "Консультация", "order": 3},  # Проведение консультации по курсам
        {"name": "Запись на пробный урок", "order": 4},  # Клиент записался на пробное занятие
        {"name": "Посещение пробного урока", "order": 5},  # Клиент посетил пробное занятие
        {"name": "Принятие решения", "order": 6},  # Клиент раздумывает над записью на курс
        {"name": "Запись на курс", "order": 7},  # Клиент записался на курс
    ]

    for stage in stages:
        SalesFunnelStage.objects.get_or_create(name=stage["name"], order=stage["order"])
    print("Этапы до начала обучения успешно созданы.")
