from django.urls import path
from . import views


urlpatterns = [

    path(
        "menu/<slug:slug>/",
        views.menu_view,
        name="menu"
    ),

  path(
    "qr/<slug:slug>/",
    views.qr_view,
    name="qr"
),


path(
    "qr-image/<slug:slug>/",
    views.qr_image,
    name="qr_image"
),

]