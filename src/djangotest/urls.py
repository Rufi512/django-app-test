"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from products import views

#REST
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename="products")

urlpatterns = [
    path('',views.home_view, name="home"),
    path('upload/', views.upload_view, name="upload"),
    path('modify/product/<int:product_id>', views.modify_view, name="modify"),
    path('contact/',views.contact_view, name="contact"),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls), name="api")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)