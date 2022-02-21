from typing import List
from django.db.models import QuerySet
from app_book.models import Recipe

def generate_queryset(queryset: QuerySet[Recipe], ingredients: List[str]):
    """ This function generates recipes with ingredients from the filter """

    for item in queryset:
        for ingredient in item.ingredients.all():
            if ingredient.name.name in ingredients:
                yield item