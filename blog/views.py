from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required # decorateur Restreigne l’accès à la page d’accueil
def home(request):
    return render(request, "blog/home.html")