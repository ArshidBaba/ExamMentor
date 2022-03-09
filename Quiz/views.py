from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Category

def category_list(request):
    MAX_OBJECTS = 20
    categories = Category.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list(categories.values("name"))
    }
    return JsonResponse(data)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = {
        "results": {
                "name": category.name,
        }
    }
    return JsonResponse(data)



















