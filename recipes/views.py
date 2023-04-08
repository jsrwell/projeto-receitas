from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_home_page': True,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_home_page': True,
    })

# verificar bug em 32 <a href="{% url 'recipes:category' recipe.category.id %}"> aula 59


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
