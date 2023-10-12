"""
URL configuration for pro project.

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
from pro.views import home
from pro.views import fc
from pro.views import eb
from pro.views import eb1
from pro.views import eb2
from pro.views import eb3
from pro.views import eb4
from pro.views import eb5
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',eb1),
    path('Tech-World/',eb1),
    path("Tech-World/course_details.html",home),
    path('Tech-World/freeCourse.html',fc),
    path('Tech-World/Ebook.html',eb),
    path('Tech-World/index.html',eb1),
    path('Tech-World/program_details.html',eb2),
    path('Tech-World/programminghub.html',eb3),
    path('Tech-World/signup.html',eb4),
    path('Tech-World/login.html',eb5),

]
