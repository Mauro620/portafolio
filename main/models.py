from django.db import models
from django.db.models.fields import CharField, URLField, IntegerField
from django.db.models.fields.files import ImageField
from datetime import datetime


# Create your models here.
class projects(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="static/img/portafolio/")
    url = URLField(blank=True)
    url2 = URLField(blank=True)


class habilidades(models.Model):
    title = CharField(max_length=30)
    porcentaje = IntegerField()
