from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout

def logout_user(request):
    logout(request)
    return redirect('login')

def Login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            #
            user = authenticate(
                username = form.cleaned_data["username"],#recupere dans formulaire
                password = form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                # message = f"Bonjour, {user.username}! Vous êtes connecté."
                return redirect("home")
                
            else:
                message = f"Identifiants invalides."
    return render(request,
            "authentication/login.html",    
            context={"form": form, "message": message})