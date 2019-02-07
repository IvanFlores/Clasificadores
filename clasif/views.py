from django.shortcuts import render

def Tareas_list(request):
    return render(request, 'ClasifWeb/Tareas_list.html', {})