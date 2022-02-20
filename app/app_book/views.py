from django.views.generic import ListView
from app_book.models import Recipe, IngredientName
from app_book.utils import generate_queryset


class MainPageView(ListView):
    """ Main page view """

    paginate_by = 3
    model = Recipe
    context_object_name = 'queryset'
    template_name = 'app_book/index.html'

    def get_context_data(self, **kwargs):
        """ Overriding this method to add a second queryset to the context """

        context = super(MainPageView, self).get_context_data(**kwargs)
        context.update(
            {'ingredients': IngredientName.objects.all()}
        )
        return context

    def get_queryset(self):
        """ Overriding this method for filtering """

        queryset = Recipe.objects.prefetch_related('ingredients').all().order_by('-created_at')
        title = self.request.GET.get('name')
        ingredients = self.request.GET.getlist('ingredients')
        if title:
            title_queryset = Recipe.objects.filter(title__icontains=title)
            if title_queryset and ingredients:
                queryset = list(set(generate_queryset(title_queryset, ingredients)))
            else:
                queryset = title_queryset
        elif ingredients:
            queryset = list(set(generate_queryset(queryset, ingredients)))
        return queryset