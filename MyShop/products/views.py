from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q

def product_list(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')
    tags = request.GET.getlist('tags')

    filters = Q()

    # Apply the filters for Query, Category, and Tags
    if query:
        filters &= Q(name__icontains=query) | Q(description__icontains=query)
        
    if category:
        filters &= Q(category__id=category)

    if tags:
        filters &= Q(tags__id__in=tags)

    products = Product.objects.filter(filters).distinct()

    categories = Category.objects.all()
    all_tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': all_tags,
        'selected_category': category,
        'selected_tags': tags,
        'query': query,
    }
    return render(request, 'product_list.html', context)

