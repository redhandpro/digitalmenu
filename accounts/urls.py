from django.urls import path
from . import views


urlpatterns = [

    # ثبت نام
    path(
        "register/",
        views.register_view,
        name="register"
    ),

    # ساخت کسب و کار
    path(
        "create-business/",
        views.create_business,
        name="create_business"
    ),

    # داشبورد
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    # دسته بندی
    path(
        "add-category/",
        views.add_category,
        name="add_category"
    ),

    path(
        "delete-category/<int:pk>/",
        views.delete_category,
        name="delete_category"
    ),

    # محصولات
    path(
        "add-product/",
        views.add_product,
        name="add_product"
    ),

    path(
        "edit-product/<int:id>/",
        views.edit_product,
        name="edit_product"
    ),

    path(
        "delete-product/<int:id>/",
        views.delete_product,
        name="delete_product"
    ),

    path(
        "toggle-product/<int:id>/",
        views.toggle_product,
        name="toggle_product"
    ),

    path(
        "edit-product-price/<int:pk>/",
        views.edit_product_price,
        name="edit_product_price"
    ),

    # تنظیمات کسب و کار
    path(
        "settings/",
        views.settings_business,
        name="settings_business"
    ),
]