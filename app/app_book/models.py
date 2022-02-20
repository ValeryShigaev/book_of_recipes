from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='заголовок')
    content = models.TextField(blank=False, verbose_name='содержание')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    image = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='фото')
    author = models.CharField(max_length=64, blank=False, verbose_name='автор')
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE, verbose_name='категория')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'


class IngredientName(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'название ингредиента'
        verbose_name_plural = 'названия ингредиентов'


class Ingredient(models.Model):
    grams = models.IntegerField(null=False, verbose_name='сколько грамм')
    name = models.ForeignKey(IngredientName, on_delete=models.CASCADE, related_name='ingredients',
                             verbose_name='название', null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients', null=True,
                               verbose_name='рецепт')

    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
