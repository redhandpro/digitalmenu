from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # هدایت صفحه اصلی به لاگین
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    
    # مسیرهای اپ business
    path('', include('business.urls')),
    
    # مسیرهای اپ accounts
    path('accounts/', include('accounts.urls')),
]