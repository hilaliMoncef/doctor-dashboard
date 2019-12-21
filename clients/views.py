from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Clients
from .forms import ClientForm

@login_required
def index(request):
    clients = Clients.objects.all()
    return render(request, 'clients/index.html', locals())

@login_required
def add(request):
    form = ClientForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, '{} {} a été ajouté à la liste des patients.'.format(form.cleaned_data['nom'], form.cleaned_data['prenom']))
            return redirect('clients')

    return render(request, 'clients/add.html', locals())

@login_required
def edit(request, id):
    client = get_object_or_404(Clients, pk=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le patient {} {} a été modifié.'.formt(form.cleaned_data['nom'], form.cleaned_data['prenom']))
            return redirect('clients')

    form = ClientForm(instance=client)
    return render(request, 'clients/edit.html', locals())

@login_required
def delete(request, id):
    client = get_object_or_404(Clients, pk=id)
    messages.success(request, 'Le patient {} {} a été supprimé.'.format(client.nom, client.prenom))
    client.delete()

    return redirect('clients')