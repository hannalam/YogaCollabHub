from django.shortcuts import render, get_object_or_404
from .models import Material
from .forms import MaterialForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def material_detail(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    return render(request, 'materials/material_detail.html', {'material': material})

@login_required
def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            new_material = form.save(commit=False)
            # Additional logic to link the material to the current user or session if needed
            new_material.save()
            return HttpResponseRedirect('/materials/')  # Redirect to material list page
    else:
        form = MaterialForm()
    return render(request, 'materials/create_material.html', {'form': form})

@login_required
def edit_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/materials/')  # Redirect to material list page
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/edit_material.html', {'form': form})
