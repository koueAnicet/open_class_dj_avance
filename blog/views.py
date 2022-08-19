from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from blog import forms
from blog import models
from authentication import forms as auth_forms

@login_required # decorateur Restreigne l’accès à la page d’accueil
def home(request):
    
    #Pour voir les photos qui ont été chargées, vous devez les récupérer dans la vue.
    photos = models.Photo.objects.all()

    return render(request, "blog/home.html", context={'photos': photos})

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        """
            vu que vous transférez une image, vous devez 
            aussi lui donner 
            tout fichier envoyé avec la requête. Faites-le en
            passant égalementrequest.FILESen argument.
        """
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            """
                Vous pouvez créer l’objet  Photo  sans le sauvegarder dans la base de données, en 
                enregistrant le formulaire avec l’argumentcommit=False
            """
            photo = form.save(commit=False)
            # définissez le téléchargeur sur l'utilisateur avant d'enregistrer le modèle
            photo.uploader = request.user
            print("############")
            print(photo.uploader)
            #actu on peut sover
            photo.save()
            return redirect('home', photo.uploader)
    return render(request, 'blog/photo_upload.html', context={'form': form})