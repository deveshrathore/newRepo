"""
URL configuration for club_belgrovia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import home_page,contact_page,display_city,display_country,service_page,about_page,page_404,booking_page,team,testimonial,ourhotels
from accounts.views import login_page,logout_page,register_user
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page,name='home'),
    path('contact/',contact_page,name='contact'),
    path('about/',about_page,name='about'),
    path('service/',service_page,name='service'),
    path('404/',page_404,name='404'),
    path('testimonial/',testimonial,name='testimonial'),
    path('team/',team,name='team'),
    path('booking/',booking_page,name='booking'),
    path('ourhotels/',ourhotels,name='ourhotels'),
    path('display_city/<int:city_id>/',display_city,name='dcity'),
    path('display_country/<int:country_id>/',display_country,name='dcountry'),
    
    path('accounts/login/', login_page,name='login'),
    path('accounts/logout/', logout_page,name='logout'),
    path('accounts/register/', register_user,name='register'),


]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 