"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views 
import blog.views
from django.contrib.auth.views import LoginView

"""
*LogoutView  (vue de déconnexion) — vous pouvez supprimer la vue   
*logout_user  que nous avions construite une fois que c’est fait.

$PasswordChangeView  (vue de changement de mot de passe)

*PasswordChangeDoneView  (vue de changement de mot de passe accompli)
**N’oubliez pas de consulter documentation Django officielle 
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),#Étape 4 : Ajoutez le modèle d’URL
    path('logout/', authentication.views.logout_user, name="logout"),
    path('home/', blog.views.home, name='home'),
]
