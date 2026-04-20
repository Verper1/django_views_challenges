"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from django.http import HttpRequest, JsonResponse
import requests


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> JsonResponse:
    url = f"https://api.github.com/users/{github_username}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10"
    }
    response = requests.get(url=url, headers=headers)
    response_status = response.status_code
    response = response.json()

    if not response_status == 404:
        name_from_git = {'name': response['name']}  # 127.0.0.1:8000/user/github/defunkt или AndyZej/full-name/
    else:
        name_from_git = {}  # 127.0.0.1:8000/user/github/AndyZej12121212/full-name/

    return JsonResponse(data=name_from_git, status=response_status)
