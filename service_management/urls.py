from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myserviceapp import views as myserviceapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', myserviceapp_views.login_request, name='login'),
    path('logout/', myserviceapp_views.logout_request, name='logout'),
    path('register/', myserviceapp_views.register_request, name='register'),
    path('', myserviceapp_views.home, name='home'),
    path('service/<int:id>/', myserviceapp_views.service_detail, name='service_detail'),
    path('add_service/', myserviceapp_views.add_service, name='add_service'),
    path('service/update/<int:service_id>/', myserviceapp_views.service_update, name='service_update'),
]
