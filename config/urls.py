# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # پنل ادمین
    path('admin/', admin.site.urls),
    
    # صفحه اصلی → هدایت به لاگین خودت
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    
    # اپ accounts
    path('accounts/', include('accounts.urls')),
    
    # اپ business (منو، QR و ...)
    path('', include('business.urls')),
]


# فایل‌های رسانه (عکس‌ها) در حالت توسعه
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )