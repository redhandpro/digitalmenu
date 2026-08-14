from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from business.models import Business, Category, Product
from .forms import BusinessForm, CategoryForm, ProductForm, BusinessUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                # ذخیره کاربر و لاگین خودکار
                user = form.save()
                # برای لاگین خودکار بعد از ثبت‌نام (اختیاری)
                # login(request, user)
                messages.success(request, "ثبت‌نام با موفقیت انجام شد! حالا وارد شوید.")
                return redirect("login")
            except Exception as e:
                # در صورت بروز خطا در ذخیره‌سازی
                messages.error(request, f"خطا در ثبت‌نام: {str(e)}")
        else:
            # نمایش خطاهای فرم
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    
    return render(request, "accounts/register.html", {"form": form})

@login_required
def create_business(request):
    form = BusinessForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        business = form.save(commit=False)
        business.owner = request.user
        business.slug = slugify(business.name)
        business.save()
        return redirect("dashboard")

    return render(request, "accounts/create_business.html", {
        "form": form
    }
                  )


@login_required
def dashboard(request):

    business = Business.objects.filter(
        owner=request.user
    ).first()

    if not business:
        return redirect("create_business")

    categories = business.categories.all()

    products = Product.objects.filter(
        category__business=business
    )

    total_products = products.count()

    available_products = products.filter(
        available=True
    ).count()

    unavailable_products = products.filter(
        available=False
    ).count()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "business": business,
            "categories": categories,
            "products": products,
            "total_products": total_products,
            "available_products": available_products,
            "unavailable_products": unavailable_products,
            "total_categories": categories.count(),
        }
    )

@login_required
def add_category(request):
    business = Business.objects.get(owner=request.user)

    form = CategoryForm(request.POST or None)

    if form.is_valid():
        category = form.save(commit=False)
        category.business = business
        category.save()
        return redirect("dashboard")

    return render(request, "accounts/add_category.html", {
        "form": form
    }
                  )

@login_required
def add_product(request):

    business = Business.objects.get(
        owner=request.user
    )

    form = ProductForm(
        request.POST or None,
        request.FILES or None
    )

    form.fields["category"].queryset = Category.objects.filter(
        business=business
    )


    if form.is_valid():

        product = form.save(commit=False)
        product.save()

        return redirect("dashboard")


    return render(
        request,
        "accounts/add_product.html",
        {
            "form": form
        }
    )

@login_required
def delete_product(request, id):

    product = get_object_or_404(
        Product,
        id=id,
        categorybusinessowner=request.user
    )

    product.delete()

    return redirect("dashboard")

@login_required
def edit_product(request, id):

    product = get_object_or_404(
    Product,
    id=id,
    categorybusinessowner=request.user
)



    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "accounts/edit_product.html",
        {
            "form": form
        }
    )

@login_required
def toggle_product(request, id):

    product = get_object_or_404(
        Product,
        id=id,
        categorybusinessowner=request.user
    )

    product.available = not product.available

    product.save()

    return redirect("dashboard")

@login_required
def settings_business(request):

    business = get_object_or_404(
        Business,
        owner=request.user
    )


    form = BusinessUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=business
    )


    if form.is_valid():

        form.save()

        return redirect("dashboard")


    return render(
        request,
        "accounts/settings.html",
        {
            "form": form
        }
    )

@login_required
def edit_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )


    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )


    if form.is_valid():

        form.save()

        return redirect("dashboard")


    return render(
        request,
        "accounts/edit_product.html",
        {
            "form": form
        }
    )

@login_required
def delete_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )
    product.delete()


    return redirect("dashboard")

@login_required
def toggle_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    product.available = not product.available

    product.save()

    return redirect("dashboard")
def home(request):

    return render(
        request,
        "business/home.html"
    )
    # accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CategoryForm

# ... سایر ویوهای شما (مانند dashboard, register, login و ...)

@login_required
def manage_categories(request):
    """نمایش لیست دسته‌بندی‌های کسب‌وکار جاری"""
    business = get_object_or_404(Business, owner=request.user)
    categories = Category.objects.filter(business=business).order_by('name')
    
    return render(request, 'accounts/manage_categories.html', {
        'business': business,
        'categories': categories,
    })

@login_required
def add_category(request):
    """افزودن دسته‌بندی جدید"""
    business = get_object_or_404(Business, owner=request.user)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.business = business
            category.save()
            messages.success(request, f"دسته‌بندی '{category.name}' اضافه شد!")
            return redirect('manage_categories')
    else:
        form = CategoryForm()
    
    return render(request, 'accounts/add_category.html', {
        'form': form,
        'business': business,
    })

@login_required
def edit_category(request, pk):
    """ویرایش دسته‌بندی موجود"""
    business = get_object_or_404(Business, owner=request.user)
    category = get_object_or_404(Category, pk=pk, business=business)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f"دسته‌بندی '{category.name}' ویرایش شد!")
            return redirect('manage_categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'accounts/add_category.html', {
        'form': form,
        'business': business,
        'category': category,
        'is_edit': True,
    })

@login_required
def delete_category(request, pk):
    """حذف دسته‌بندی"""
    business = get_object_or_404(Business, owner=request.user)
    category = get_object_or_404(Category, pk=pk, business=business)
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f"دسته‌بندی '{category_name}' حذف شد!")
        return redirect('manage_categories')
    
    return render(request, 'accounts/delete_category.html', {
        'category': category,
        'business': business,
    })
    
    
@login_required  
def manage_products(request):
    business = get_object_or_404(Business, owner=request.user)
    products = Product.objects.filter(category__business=business).order_by('-created_at')
    
    return render(request, 'accounts/manage_products.html', {
        'business': business,
        'products': products,
    })
    
@login_required
def edit_product_price(request, pk):
    business = get_object_or_404(Business, owner=request.user)
    product = get_object_or_404(Product, pk=pk, category__business=business)
    
    if request.method == 'POST':
        new_price = request.POST.get('price')
        if new_price:
            product.price = new_price
            product.save()
            messages.success(request, f"قیمت '{product.name}' به {product.price} تومان تغییر کرد!")
            return redirect('manage_products')
    
    return render(request, 'accounts/edit_price.html', {
        'product': product,
        'business': business,
    })
    