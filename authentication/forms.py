from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label=" Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')#widget masque info

    """
    PasswordInput  cache automatiquement la saisie en utilisant un  
    <input>  HTML avec l’attribut  type="password"
    """
    
    """_summary_
    Étape 1 : Spécialisez UserCreationForm
        UserCreationForm est un ModelForm qui possède trois champs :username,password1,et password2. 
        Comme nous demandons également d’autres champs à l’utilisateur, 
        nous allons devoir spécialiser ce formulaire.
        **get_user_model, qui vous permet d’obtenir le modèle  Usersans l’importer directement
    """
    
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()#utilise leuser model prsonalisé
        fields = ('username','email', 'first_name','last_name', 'role')
        
class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )