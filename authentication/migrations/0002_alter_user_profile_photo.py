# Generated by Django 4.0.5 on 2022-08-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='photo_profile', verbose_name='Photo de profil'),
        ),
    ]