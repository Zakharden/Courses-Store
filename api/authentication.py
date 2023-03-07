from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == "GET":
            return True #если метод get, то аутентификация не нужна
        
        return super().is_authenticated(request, **kwargs)