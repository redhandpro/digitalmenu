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
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def qr_code_view(request, slug):

    business = get_object_or_404(
        Business,
        slug=slug
    )

    url = request.build_absolute_uri(
        f"/menu/{business.slug}/"
    )

    qr = qrcode.make(url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    return HttpResponse(
        buffer.getvalue(),
        content_type="image/png"
    )