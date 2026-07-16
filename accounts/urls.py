from django.urls import path
from . import views


urlpatterns = [

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
        "create-business/",
        views.create_business,
        name="create_business"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "add-category/",
        views.add_category,
        name="add_category"
    ),

    path(
        "add-product/",
        views.add_product,
        name="add_product"
    ),


path(
    "delete-product/<int:id>/",
    views.delete_product,
    name="delete_product"
),

path(
    "edit-product/<int:id>/",
    views.edit_product,
    name="edit_product"

),
path(
    "toggle-product/<int:id>/",
    views.toggle_product,
    name="toggle_product"
),
path(
    "settings/",
    views.settings_business,
    name="settings_business"
),
]

