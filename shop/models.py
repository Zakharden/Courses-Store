from django.db import models
from django.utils import timezone

class Categorys(models.Model):
    title = models.CharField(max_length=255) #значение в виде строки
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE) #курс будет принадлежать только одной категории #при удалении категории будет удален курс
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title