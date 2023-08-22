from datetime import datetime


def generate_shopping_list_text(user, ingredients):
    today = datetime.today()

    shopping_list = (
        f'Список покупок для: {user.get_full_name()}\n\n'
        f'Дата: {today:%Y-%m-%d}\n\n'
    )

    shopping_list += '\n'.join([
        f'- {ingredient["ingredient__name"]} '
        f'({ingredient["ingredient__measurement_unit"]})'
        f' - {ingredient["amount"]}'
        for ingredient in ingredients
    ])

    shopping_list += f'\n\nFoodgram ({today:%Y})'

    return shopping_list
