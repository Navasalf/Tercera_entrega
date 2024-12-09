from django.urls import path
from app_coder import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    
    path("cursos-formularios", views.formulario_curso, name="curso-formulario"),
    path("profesor-formularios", views.formulario_profesor, name="profesor-formulario"),
    path("estudiante-formularios", views.formulario_estudiante, name="estudainte-formulario"),
]