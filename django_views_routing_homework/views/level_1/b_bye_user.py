from django.http import HttpResponse

"""
У нас есть вьюха bye_user_view, но она не привязана ни к какому пути.

Задания:
    1. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/bye/ вызывалась вьюха bye_user_view.
    2. Проверьте результат по ссылке тут http://127.0.0.1:8000/bye/
"""


def bye_user_view(request) -> HttpResponse:
    bye_message = f'Bye, {request.user}!'
    return HttpResponse(bye_message)  # [04/Mar/2026 23:48:35] "GET /bye/ HTTP/1.1" 200 19
