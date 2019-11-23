
from django.contrib import admin
from products import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
]
