"""
В этом задании вам нужно реализовать вьюху, которая возвращает IP входящего запроса в виде строки.

Вот тут есть информация о том, как узнать IP:
https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.META
"""

from django.http import HttpResponse, HttpRequest


def show_user_ip_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse([request.META['REMOTE_ADDR'], "\n", request.META['HTTP_USER_AGENT']])

    # [23/Mar/2026 16:11:07] "GET /me/ip/ HTTP/1.1" 200 9
    # 127.0.0.1
