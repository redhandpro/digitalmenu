from django.shortcuts import render, get_object_or_404
from .models import Business
import qrcode
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404




def menu_view(request, slug):

    business = get_object_or_404(
        Business,
        slug=slug
    )

    categories = business.categories.all()

    return render(
        request,
        "business/menu.html",
        {
            "business": business,
            "categories": categories
        }
    )
from django.shortcuts import render, get_object_or_404
from .models import Business


def qr_code_view(request, slug):

    business = get_object_or_404(
        Business,
        slug=slug
    )

    return render(
        request,
        "business/qr.html",
        {
            "business": business
        }
    )
def qr_view(request, slug):

    business = get_object_or_404(
        Business,
        slug=slug
    )

    return render(
        request,
        "business/qr.html",
        {
            "business": business
        }
    )



def qr_image(request, slug):

    business = get_object_or_404(
        Business,
        slug=slug
    )


    link = request.build_absolute_uri(
        f"/menu/{business.slug}/"
    )


    qr = qrcode.make(link)


    buffer = BytesIO()

    qr.save(buffer, "PNG")


    return HttpResponse(
        buffer.getvalue(),
        content_type="image/png"
    )