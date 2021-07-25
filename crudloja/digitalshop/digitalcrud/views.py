from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404


class CalcadoForm(ModelForm):
    class Meta:
        model = Calcados
        fields = ['nome', 'materialinterno', 'materialsola', 'modelo', 'marca', 'cor', 'ocasiao', 'tamanho']


def calcado_lista(request, template_name='calcado_list.html'):
    calcado = Calcados.objects.all()
    calcados = {'lista': calcado}
    return render(request, template_name, calcados)


def calcado_novo(request, template_name='calcado_form.html'):
    form = CalcadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_calcados')
    return render(request, template_name, {'form': form})


def calcado_editar(request, pk, template_name='calcado_form.html'):
    calcado = get_object_or_404(Calcados, pk=pk)
    if request.method == "POST":
        form = CalcadoForm(request.POST, instance=calcado)
        if form.is_valid():
            calcado = form.save()
            return redirect('listar_calcados')
    else:
        form = CalcadoForm(instance=calcado)
    return render(request, template_name, {'form': form})

def calcado_remove(request, pk):
    calcado = Calcados.objects.get(pk=pk)
    if request.method == "POST":
        calcado.delete()
        return redirect('listar_calcados')
    return render(request, 'calcado_delete.html', {'calcado': calcado})