from django.shortcuts import render, get_object_or_404
from .models import Business


def menu_view(request, slug):
    business = get_object_or_404(
        Business,
        slug=slug
    )

    categories = business.categories.all()

    return render(
        request,
        "menu.html",
        {
            "business": business,
            "categories": categories
        }
    )