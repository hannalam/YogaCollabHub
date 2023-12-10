from django.shortcuts import render, redirect
from .models import Interaction
from .forms import InteractionForm

def interaction_list(request):
    interactions = Interaction.objects.all()
    return render(request, 'interactions/interaction_list.html', {'interactions': interactions})

def add_interaction(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interaction_list')
    else:
        form = InteractionForm()
    return render(request, 'interactions/add_interaction.html', {'form': form})

def edit_interaction(request, interaction_id):
    interaction = Interaction.objects.get(pk=interaction_id)
    if request.method == 'POST':
        form = InteractionForm(request.POST, instance=interaction)
        if form.is_valid():
            form.save()
            return redirect('interaction_list')
    else:
        form = InteractionForm(instance=interaction)
    return render(request, 'interactions/edit_interaction.html', {'form': form, 'interaction': interaction})

def delete_interaction(request, interaction_id):
    interaction = Interaction.objects.get(pk=interaction_id)
    if request.method == 'POST':
        interaction.delete()
        return redirect('interaction_list')
    return render(request, 'interactions/delete_interaction.html', {'interaction': interaction})
