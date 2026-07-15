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

]