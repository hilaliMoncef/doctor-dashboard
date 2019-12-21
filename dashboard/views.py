from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import ConnexionForm
from clients.models import Clients
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect
import pandas as pd
import datetime

@login_required
def index(request):
    client_count = Clients.objects.count()
    if client_count != 0:
        male_count = Clients.objects.filter(sexe='H').count() / client_count * 100
        female_count = 100 - male_count
        age_list = pd.DataFrame(list(Clients.objects.all().values('naissance')))
        age_list = pd.to_datetime(age_list['naissance'], errors='coerce')
        age_list = age_list.apply(calculate_age)
        age_list = age_list.groupby(age_list).count()
        ages = age_list.index
        num_ages = age_list.values
    else:
        male_count = 0
        female_count = 0
        age_list = 0
        ages = []
        num_ages = []
    last_clients = Clients.objects.all().order_by('-id')[:5]

    return render(request, 'index.html', locals())

def search(request):
    url_parameter = request.GET.get("q")

    clients = Clients.objects.filter(nom__icontains=url_parameter) | Clients.objects.filter(prenom__icontains=url_parameter)
    html = render_to_string(
        template_name="clients-results-partial.html",
        context={"clients": clients}
    )

    data = {
        'html': html
    }
    return JsonResponse(data)

def calculate_age(bday):
    d = datetime.date.today()
    return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))


@login_required
def cctv(request):
    return render(request, 'cctv.html', locals())


def login(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Une erreur s\'est produite. Veuillez réessayer.')
    else:
        form = ConnexionForm()

    return render(request, 'login.html', locals())

def logout(request):
    auth_logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('login')