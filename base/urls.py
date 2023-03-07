"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from api.models import CategoryResourse, CourseResourse
from tastypie.api import Api

api = Api(api_name = 'v1')
course_resource = CourseResourse()
category_resource = CategoryResourse()
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('shop/', include('shop.urls')),
    path('', include('shop.urls')), #для стер shop для того, чтобы сделать стартовой страницей
    # path('api/', include(course_resource.urls)), #было до подключения api.register
    # path('api/', include(category_resource.urls))
    path('api/', include(api.urls))
]
