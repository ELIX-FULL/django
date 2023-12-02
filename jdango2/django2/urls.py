
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from jdango2.products.views import index_page, send_form, ShopPageView, AboutPageView, ShopDetailView, register_user
from jdango2.django2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('shop', ShopPageView.as_view(), name='shop'),
    path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('abouts', AboutPageView.as_view(), name='about'),
    path('form', send_form),
    path('accounts/', include('allauth.urls')),
    path('register/', register_user)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
