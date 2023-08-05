import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def hex_color_validator(value):
    if not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
        raise ValidationError(
            _('Введённое значение не является HEX цветом'),
        )


def username_validator(value):
    forbidden_symbols = ''.join(set(re.findall(r'[^\w.@+-]', value)))
    if forbidden_symbols:
        raise ValidationError(
            _(f'Недопустимые символы в имени пользователя:'
              f'{forbidden_symbols}'),
        )
