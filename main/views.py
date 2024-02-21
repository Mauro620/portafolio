from django.shortcuts import render
from .models import projects, habilidades
from .utils import calcula_edad, calcular_semestre


def index(request):
    Projects = projects.objects.all()
    Habilidades = habilidades.objects.all()
    edad = calcula_edad("2003-06-20")
    semestre = calcular_semestre("2022-01-20")

    context = {
        "projects": Projects,
        "edad": edad,
        "semestre": semestre,
        "habilidades": Habilidades,
    }
    return render(request, "index.html", context)


# Create your views here.
