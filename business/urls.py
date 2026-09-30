# business/urls.py
from django.urls import path
from . import views

app_name = 'business'  # ← این خط باید وجود داشته باشد

urlpatterns = [
    path('menu/<slug:slug>/', views.menu_view, name='menu'),
    # سایر مسیرها
]


urlpatterns = [
    path(
    "",
    views.home,
    name="home"
),

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

path('menu/', views.menu_view, name='menu'),

]