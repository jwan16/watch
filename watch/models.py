from django.db import models
from django.core.urlresolvers import reverse
from multiupload.fields import MultiFileField

class Brand(models.Model):
    name = models.CharField(max_length=250, unique=True)
    des = models.CharField(max_length=500)
    origin =  models.CharField(max_length=100)
    logo =  models.FileField()

    def get_absolute_url(self):
        return reverse('watch:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Watch(models.Model):
    watch_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name =  models.CharField(max_length=50)
    year =  models.CharField(max_length=10)
    price = bracelet_material = models.CharField(max_length=15)
    code = models.CharField(max_length=20)
    ref_no = models.CharField(max_length=30)
    movement = models.CharField(max_length=50, choices=(('automatic', 'Automatic'),('manual', 'Manual'),('quartz', 'Quartz')))
    case_material = models.CharField(max_length=30)
    bracelet_material = models.CharField(max_length=30)
    bracelet_color = models.CharField(max_length=30)
    bracelet_length = models.CharField(max_length=30)
    pic = models.ImageField()
    large_pic = models.FileField()
    featured = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=1000)
    bg = models.FileField()