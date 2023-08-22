from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    color = ColorField(
        format='hex',
        default='#778899',
        unique=True,
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название'
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единица измерения'
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural ='Ингридиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Ингридиент'
    )
    amount = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1, 'Минимальное значение - 1')
        ],
        verbose_name='Количество'
    )

    class Meta:
        default_related_name = 'ingridients_recipe'
        constraints = [
            UniqueConstraint(
                fields=('ingredient', 'amount'),
                name='unique_ingredient_in_recipe'),
        ]

    def __str__(self):
        return f'{self.ingredient} – {self.amount}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Название'
    )
    image = models.ImageField(
        blank=True,
        upload_to='recipes/images'
    )
    text = models.TextField(
    )
    ingredients = models.ManyToManyField(
        IngredientInRecipe,
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, 'Минимальное значение - 1')
        ],
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:
        ordering = ('user',)
        constraints = [
            UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_favourites',
            )
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в свою корзину'
