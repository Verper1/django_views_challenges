"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest
from faker import Faker
from django.http import FileResponse
from io import BytesIO


def generate_file_with_text_view(request: HttpRequest) -> FileResponse | HttpResponse:
    length = request.GET.get("length")

    try:
        length = int(length)
        if length < 5 or length > 500:
            return HttpResponse(status=403)
    except (TypeError, ValueError):
        return HttpResponse(status=403)

    fake = Faker("ru_RU")
    fake_text = fake.text(max_nb_chars=length)

    buffer = BytesIO()
    buffer.write(fake_text.encode("utf-8"))
    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename="generated_text.txt"
    )
