# business/views.py
from django.shortcuts import render, get_object_or_404
from accounts.models import Business, Category, Product
import qrcode
from io import BytesIO
from django.http import HttpResponse


def home(request):
    """صفحه اصلی سایت"""
    return render(request, 'business/home.html')


def menu_view(request, slug):
    """نمایش منو برای مشتری"""
    business = get_object_or_404(Business, slug=slug)
    categories = Category.objects.filter(business=business, is_active=True)
    
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id, available=True)
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        products = Product.objects.filter(category__business=business, available=True)
        selected_category = None
    
    context = {
        'business': business,
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    }
    return render(request, 'business/menu.html', context)


def qr_view(request, slug):
    """صفحه‌ای که QR کد و لینک منو رو نشون میده"""
    business = get_object_or_404(Business, slug=slug)
    # ساخت لینک کامل منو
    menu_url = request.build_absolute_uri(f'/menu/{business.slug}/')
    
    context = {
        'business': business,
        'menu_url': menu_url,
    }
    return render(request, 'business/qr.html', context)


def qr_image(request, slug):
    """تولید و برگرداندن تصویر QR اختصاصی برای هر کسب‌وکار"""
    business = get_object_or_404(Business, slug=slug)
    
    # لینک اختصاصی منوی این کسب‌وکار
    menu_url = request.build_absolute_uri(f'/menu/{business.slug}/')
    
    # ساخت QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(menu_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#6b4423", back_color="white")
    
    # برگرداندن تصویر
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")