"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

import app1.views

import app2.views
urlpatterns = [
    path('admin/', admin.site.urls),
	path('employee/', app1.views.displayEmployeeForm),
	path('login/', app1.views.displayLoginForm),
    path('sess/', app1.views.displaySession),


    #path('app1/', views.displaytemplate1),
	#path('app2/', app2.views.displaytemplate2),
	#path('emp/', app2.views.employee1),
    #path('html/', app1.views.html1),
	#path('show/', app2.views.show),
]
