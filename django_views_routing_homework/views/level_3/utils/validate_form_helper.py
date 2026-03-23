"""
Сделал так, потому что через форму можно 4-ым аргументов передать "123":123 и всё равно сработает.
Можно было бы переопределить метод clean в форме, но это уже уровень повыше, чем я сейчас.
"""
class MainValidator:
    ALLOWED_REGISTERED_FROM = {"website", "mobile_app"}

    def __init__(self, data: dict[str, str | int]) -> None:
        self.data = data


class ValidateFieldsMixin:
    def check_fields(self) -> bool:
        """Проверка на то, что всего 4 поля должно быть, из которых 1 - это необязательный age."""
        all_fields = self.data.keys()

        if len(all_fields) > 4:
            return False

        required_fields = ['full_name', 'email', 'registered_from']

        if all(field in all_fields for field in required_fields):
            if len(all_fields) > 3 and 'age' not in all_fields:
                return False
            else:
                return True

        return False

class ValidateVariableMixin:
    def check_full_name(self) -> bool:
        """Проверка, что имя есть и оно от 5 до 256 символов."""
        full_name_data = self.data.get('full_name')

        if full_name_data:
            return isinstance(full_name_data, str) and 5 <= len(full_name_data) <= 256

        return False

    def check_email(self) -> bool:
        """Проверка на почту через домен."""
        email_data = self.data.get('email')

        if email_data:
            email_str = email_data.split("@")
            return email_str[1] in ["gmail.com", "mail.ru", "yandex.ru", "mail.com"]

        return False

    def check_registered_from(self) -> bool:
        """Проверка откуда пришла регистрация."""
        registered_from_data = self.data.get('registered_from')

        if registered_from_data:
            return registered_from_data in self.ALLOWED_REGISTERED_FROM

        return False

    def check_age(self) -> bool:
        """Проверка на возраст. Если нет возраста, то всё равно вернуть True."""
        age_data = self.data.get('age')

        if age_data is None:
            return True

        return isinstance(age_data, int) and age_data > 0


class ValidateForm(MainValidator, ValidateFieldsMixin, ValidateVariableMixin):
    def final_check(self) -> dict[str, bool]:
        """Проверка всего того, что пришло из POST запроса."""
        if not self.check_fields():
            return {"is_valid": False}

        if all([
            self.check_full_name(),
            self.check_email(),
            self.check_registered_from(),
            self.check_age()
        ]):
            return {"is_valid": True}

        return {"is_valid": False}
