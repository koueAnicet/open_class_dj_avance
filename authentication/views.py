from multiprocessing import context
from django.conf import settings
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View


def signup_page(request):
    form = forms.SignupForm()
    print("la method : ",request.method )
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auto-login user, login  pour connecter l’utilisateur automatiquement
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context= {'form': form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home', form)
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})



def logout_user(request):
    logout(request)
    return redirect('login')
class LoginPageView(View):
    template_name="authentication/login.html"
    class_form = forms.LoginForm

    def get(self, request):
        form = self.class_form()
        message=''
        return render(request, self.template_name, context={"form": form ,"message": message})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            #recuperation des infos
            user= authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                login(request, user)
                return redirect("home")
        message = f"Identifiants invalides!"
        return render(request, self.template_name, context={"form": form, "message": message})

# def Login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             #
#             user = authenticate(
#                 username = form.cleaned_data["username"],#recupere dans formulaire
#                 password = form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 # message = f"Bonjour, {user.username}! Vous êtes connecté."
#                 return redirect("home")
                
#             else:
#                 message = f"Identifiants invalides."
#     return render(request,
#             "authentication/login.html",    
#             context={"form": form, "message": message})