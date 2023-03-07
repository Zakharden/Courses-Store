from tastypie.resources import ModelResource
from shop.models import Categorys, Courses
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization

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
        excludes = ['reviews_qty', 'created_at'] #что изключить из получаемого json
        authentication = CustomAuthentication()
        Authorization = Authorization()
    
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle #позволяет вставить budle 'category_id'
    
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
    
    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper() #получение через API (у названий - заглавные буквы)