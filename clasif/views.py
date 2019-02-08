from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Tareas
from .forms import TareasForm

def Tareas_list(request):
    tareas = Tareas.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ClasifWeb/Tareas_list.html', {'tareas':tareas})

def Tareas_detalle(request, pk):
    tareas = get_object_or_404(Tareas, pk=pk)
    return render(request, 'ClasifWeb/Tareas_detalle.html', {'tareas':tareas})

def Tareas_edit(request, pk):
    tareas = get_object_or_404(Tareas, pk=pk)
    if request.method == "POST":
        form = TareasForm(request.POST, instance=tareas)
        if form.is_valid():
            tareas = form.save(commit=False)
            tareas.author = request.user
            tareas.published_date = timezone.now()
            tareas.save()
            return redirect('Tareas_detalle', pk=tareas.pk)
    else:
        form = TareasForm(instance=tareas)
    return render(request, 'ClasifWeb/Tareas_edit.html', {'form': form})

def Tareas_new(request):
    if request.method == "POST":
        form = TareasForm(request.POST)
        if form.is_valid():
            tareas = form.save(commit=False)
            tareas.author = request.user
            tareas.published_date = timezone.now()
            tareas.save()
            return redirect('Tareas_detalle', pk=tareas.pk)
    else:
        form = TareasForm()
    return render(request, 'ClasifWeb/Tareas_edit.html', {'form': form})