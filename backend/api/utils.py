from django.shortcuts import get_object_or_404

from recipes.models import Ingredient, IngredientRecipe, Tag


def collect_ingredientsrecipe_objects(ingredient_data, recipe):
    ingredients = []
    for data in ingredient_data:
        ingredient_id = data.get('ingredient', {}).get('id')
        if ingredient_id:
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            amount = data.get('amount')
            ingredients.append(IngredientRecipe(
                recipe=recipe,
                ingredient=ingredient,
                amount=amount
            ))
    return ingredients


def collect_tags(tag_data):
    tags = []
    for tag_id in tag_data:
        tag = get_object_or_404(Tag, id=tag_id)
        tags.append(tag)
    return tags