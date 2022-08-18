"""
    Étape 1 : Configurezsettings.py
    Étape 2 : Ajoutez les médias aux modèles d’URL
    Étape 3 : Créez un formulaire capable de gérer les mises en ligne d’images
    Étape 4 : Construisez la vue pour qu’elle gère les téléversements d’images
    Étape 5 : Ajoutez le gabarit
    Étape 6 : Mettez à jour les modèles d’URL
    Étape 7 : Créez un flux, ou « feed »:Pour voir les photos qui ont été chargées, 
            vous devez les récupérer dans la vue.
"""

from django import forms

from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model= models.Photo
        fields = ['image', 'caption']
    