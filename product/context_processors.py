
from .models import Category

def categories_processors(request):
    return {
         'categories':Category.objects.filter(parent=None)
    }

