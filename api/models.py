from tastypie.resources import ModelResource
from shop.models import Categorys, Courses

class CategoryResourse(ModelResource):
    class Meta: 
        queryset = Categorys.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class CourseResourse(ModelResource):
    class Meta: 
        queryset = Courses.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']