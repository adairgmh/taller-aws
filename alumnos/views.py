from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alumno

@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista.html', {'alumnos': alumnos})

@login_required
def crear_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        Alumno.objects.create(nombre=nombre, apellido=apellido, edad=edad)
        return redirect('lista_alumnos')
    return render(request, 'alumnos/crear.html')

@login_required
def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.nombre = request.POST['nombre']
        alumno.apellido = request.POST['apellido']
        alumno.edad = request.POST['edad']
        alumno.save()
        return redirect('lista_alumnos')
    return render(request, 'alumnos/editar.html', {'alumno': alumno})

@login_required
def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    alumno.delete()
    return redirect('lista_alumnos')
