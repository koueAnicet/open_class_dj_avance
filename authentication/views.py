from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View

def logout_user(request):
    logout(request)
    return redirect('login')

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