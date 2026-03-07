from django.http import HttpResponseNotFound, HttpResponse
from .utils import get_month_title_by_number


"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3/ 
"""


def get_month_title_view(request, month_number: int) -> HttpResponse | HttpResponseNotFound:
    """
    Возвращает http ответ и использует функцию get_month_title_by_number из .utils.py, чтобы понять какой сезон сейчас
    по числу месяца. Если число не в приделах от 1 до 12,
    то возвращается пустая строка и здесь уже отправляется ответ 404.
    """
    response_func = get_month_title_by_number(month_number)

    if not response_func:
        return HttpResponseNotFound('Месяца с таким номером не существует')

    return HttpResponse(response_func)

    # [05/Mar/2026 00:17:05] "GET /month-title/3/ HTTP/1.1" 200 10
    # [05/Mar/2026 00:17:11] "GET /month-title/12/ HTTP/1.1" 200 8
    # Not Found: /month-title/14/
    # [05/Mar/2026 00:17:43] "GET /month-title/14/ HTTP/1.1" 404 67
