from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    This model describes the recipe category, it is available only to the administration

    Params:
        name (models.CharField): name of category
        description (models.TextField): description as desired
    """

    name = models.CharField(max_length=64, blank=False, unique=True, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Recipe(models.Model):
    """
    This model describes the recipe

    Params:
        title (models.CharField): title
        content (models.TextField): recipe content
        created_at (models.DateTimeField): date and time of creation
        image (models.ImageField): recipe photo, optional
        category (models.ForeignKey): recipe category
        user (models.ForeignKey): filled in automatically, serves to protect other people's recipes from the user
    """

    title = models.CharField(max_length=100, blank=False, verbose_name='заголовок')
    content = models.TextField(blank=False, verbose_name='содержание')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    image = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='фото')
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE, verbose_name='категория')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'


class IngredientName(models.Model):
    """
    This model describes the available ingredient, it is available only to the administration

    Params:
        name (models.CharField): name of ingredient
    """

    name = models.CharField(max_length=64, blank=False, unique=True, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'название ингредиента'
        verbose_name_plural = 'названия ингредиентов'


class Ingredient(models.Model):
    """
    This model describes the ingredient

    Params:
        grams (models.IntegerField): how many grams
        name (models.ForeignKey): name of ingredient
        recipe (models.ForeignKey): recipe
    """

    grams = models.IntegerField(null=False, verbose_name='сколько грамм')
    name = models.ForeignKey(IngredientName, on_delete=models.PROTECT, related_name='ingredients',
                             verbose_name='название', null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients', null=True,
                               verbose_name='рецепт')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
