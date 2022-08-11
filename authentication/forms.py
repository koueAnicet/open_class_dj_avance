from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label=" Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')#widget masque info

    """
    PasswordInput  cache automatiquement la saisie en utilisant un  
    <input>  HTML avec l’attribut  type="password"
    """