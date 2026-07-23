from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from business.models import Business, Category, Product
from .forms import BusinessForm, CategoryForm, ProductForm, BusinessUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("login")

    return render(request, "accounts/register.html", {
        "form": form
    })


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
    })


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
    })

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