from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Courses #болле краткая запись после импорта
from .models import Categorys

# Create your views here.
def index(request):
    courses = Courses.objects.all()
    #return HttpResponse(''.join([str(course) + '<br>' for course in courses])) #объединение последовательности списков в строку с табуляцией
    #return HttpResponse(courses)
    return render(request, 'shop/courses.html', {'courses': courses})

def single_course(request, course_id):
    #Option 1
    # try:
    #     course = Courses.objects.get(pk = course_id)
    #     return render(request, "shop/single_course.html", {"course": course})
    # except Courses.DoesNotExist:
    #     raise Http404 #404 если не такого курса
    #Option 2
    course = get_object_or_404(Courses, pk = course_id) #404 если не такого курса
    return render(request, "shop/single_course.html", {"course": course})

    