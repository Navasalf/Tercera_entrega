from django.shortcuts import render, redirect

from .models import Curso, Profesor
from .form import CursosFormularios, ProfesorFormulario




def inicio(request):
    return render (request, "app_coder/inicio.html")

def cursos(request):
    query = request.GET.get('q')
    if query:
        cursos = Curso.objects.filter(nombre__icontains=query)
    else:
        cursos = Curso.objects.all()
    return render (request, "app_coder/cursos.html", {"cursos":cursos})

def profesores(request):
    query = request.GET.get('q')
    if query:
        cursos = Curso.objects.filter(nombre__icontains=query)
    else:
            profesores = Profesor.objects.all()
    return render (request, "app_coder/profesores.html", {"profesores":profesores})
    
def estudiantes(request):
    return render (request, "app_coder/estudiantes.html")

def entregables(request):
    return render (request, "app_coder/entregables.html")



def formulario_curso(request):
    if request.method == "POST":
        curso_form = CursosFormularios(request.POST)
        if curso_form.is_valid():    
            info_limpia = curso_form.cleaned_data
            curso = Curso(nombre=request.POST["nombre"],camada=request.POST["camada"])
            curso.save()
            return redirect("cursos")
    else:
        curso_form = CursosFormularios()
    contexto = {"form" : curso_form}
    return render (request, "app_coder/form/curso-formulario.html", contexto)


def formulario_profesor(request):
    if request.method == "POST":
        profesor_form = ProfesorFormulario(request.POST)
        if profesor_form.is_valid():    
            info_limpia = profesor_form.cleaned_data
            profesor = Profesor (nombre=request.POST["nombre"],apellido=request.POST["apellido"], email = request.POST["email"], profesion = request.POST["profesion"])
            profesor.save()
            return redirect("profesores")
    else:
        profesor_form = ProfesorFormulario()
    contexto = {"form" : profesor_form}
    return render (request, "app_coder/form/profesor-formulario.html", contexto)

# def formulario_profesor(request):
#     return render (request, "app_coder/form/profesor-formulario.html")