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
from django.contrib.auth.views import LogoutView
from products.views import (ProductViewSet,home_view,contact_view, upload_view,modify_view)
from clients.views import (Customer,login_view,logout,register_view,MyTokenObtainPairView)

#REST
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename="products")
router.register(r'customers', Customer, basename="customers")

urlpatterns = [
    path('',home_view, name="home"),
    path('upload/', upload_view, name="upload"),
    path('modify/product/<int:product_id>', modify_view, name="modify"),
    path('contact/',contact_view, name="contact"),
    path('login/',login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('register/',register_view, name="register"),
    path('admin/', admin.site.urls),
    #path('clients/', CustomerViewSet.as_view(), name="clients"),
    #Tokens
    path('api/token/', MyTokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include(router.urls), name="api")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
