from django.contrib import admin
from app_book.models import Ingredient, IngredientName, Category, Recipe


class IngredientsAdmin(admin.TabularInline):
    """ Show ingredients in recipe """

    model = Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ Recipe administrator """

    list_display = ['title', 'author', 'content', 'category']
    list_filter = ['category']
    search_fields = ['category__name', 'title']
    raw_id_list_displayfields = ['user']
    user_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'content', 'image', 'author', 'category')
        }),
    )
    inlines = [IngredientsAdmin]

    def save_model(self, request, obj, form, change):
        """ Overriding for save user """

        if form.is_valid():
            if not request.user.is_superuser or not form.cleaned_data["user"]:
                obj.user = request.user
                obj.save()
            elif form.cleaned_data["user"]:
                obj.user = form.cleaned_data["user"]
                obj.save()

    def preprocess_list_display(self, request):
        """ Override to remove user field for regular user """

        if 'user' not in self.list_display:
            self.list_display.insert(self.list_display.__len__(), 'user')
        if not request.user.is_superuser:
            if 'user' in self.list_display:
                self.list_display.remove('user')

    def preprocess_search_fields(self, request):
        """ Override to remove search by user for regular user """

        if 'user__username' not in self.search_fields:
            self.search_fields.insert(self.search_fields.__len__(), 'author')
        if not request.user.is_superuser:
            if 'user__username' in self.search_fields:
                self.search_fields.remove('author')

    def changelist_view(self, request, extra_context=None):
        """ Override changelist """

        self.preprocess_list_display(request)
        self.preprocess_search_fields(request)
        return super(RecipeAdmin, self).changelist_view(request)

    def get_queryset(self, request):
        """ Override to get only user's recipes """

        if request.user.is_superuser:
            return super(RecipeAdmin, self).get_queryset(request)
        else:
            qs = super(RecipeAdmin, self).get_queryset(request)
            return qs.filter(user=request.user)

    def get_fieldsets(self, request, obj=None):
        """ Supeuser's fieldsets """

        if request.user.is_superuser:
            return super(RecipeAdmin, self).get_fieldsets(request, obj)
        return self.user_fieldsets


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category administration """

    list_display = ('name', 'description')
    list_filter = ('name', 'description')


@admin.register(IngredientName)
class IngredientNameAdmin(admin.ModelAdmin):
    """ IngredientName administration """

    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Ingredient administration """

    list_display = ('name', 'grams', 'recipe')
    list_filter = ('name', 'recipe')
