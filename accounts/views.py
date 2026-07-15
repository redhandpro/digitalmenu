from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .forms import BusinessForm, CategoryForm

from business.models import Business



def register_view(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:
        form = UserCreationForm()


    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )
@login_required
def create_business(request):

    if request.method == "POST":

        form = BusinessForm(
            request.POST,
            request.FILES
        )
        Vif form.is_valid():

            business = form.save(commit=False)

            business.owner = request.user

            business.slug = slugify(
                business.name
            )

            business.save()

            return redirect(
                "dashboard"
            )

    else:
        form = BusinessForm()


    return render(
        request,
        "accounts/create_business.html",
        {
            "form": form
        }
    )
@login_required
def dashboard(request):

    business = get_object_or_404(
        Business,
        owner=request.user
    )

    categories = business.categories.all()


    return render(
        request,
        "accounts/dashboard.html",
        {
            "business": business,
            "categories": categories
        }
    )
@login_required
def add_category(request):

    business = get_object_or_404(
        Business,
        owner=request.user
    )


    if request.method == "POST":

        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)

            category.business = business

            category.save()

            return redirect(
                "dashboard"
            )

    else:

        form = CategoryForm()


    return render(
        request,
        "accounts/add_category.html",
        {
            "form": form
        }
    )