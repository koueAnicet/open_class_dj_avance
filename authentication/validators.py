"""
    Un validateur est une classe qui n’a besoin que de deux méthodes : 
    une méthode  'validate'  et une méthode  'get_help_text'.
"""

from django.core.exceptions import ValidationError
    
"""
    La méthode  validate  vérifie le mot de passe et provoque une  
    'ValidationError ' si le mot de passe ne remplit pas le critère. 
    La méthode  get_help_text  
    guide l’utilisateur final pour qu’il sache comment passer la validation.
"""

class ContainsLetterValidator:
    def validate(self, password,  user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'le mode pass doi conteni un lettre', code='password_no_letters'
            )
    def get_help_text(self):
        return 'Le mot de passe doit contenir au moins un lettre majuscule ou minuscule'


class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir un chiffre', code='password_no_number')

    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'