# ModelForm: Django Genere automatiquement un formulaire
# à partir d'un modele. On n'écrit pas chaque champ à la main

from django import forms
from .models import RendezVous, Consultation

class RendezVousForm(forms.ModelForm):
    # La classe Meta idndiqe à Django quel modele utiliser
    class Meta:
        model=RendezVous
        # fields : quels champs inclure dans le formulaire
        fields=['date','heure','motif']
        # widgets: On personnalise l'apparence des champs HTML
        widgets={
            'date':forms.DateInput(
                attrs={
                    'type':'date',
                    'class':'form-control'
                    # input type="date" class="form-control"
                }
            ),
            'heure':forms.TimeInput(
                    # input type="time" class="form-control"
                attrs={
                    'type':'time',
                    'class':'form-control'
                }
            ),
            'motif':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Décrivez le motif de votre consultation...'
                }
            ),
        }
class ConsultationForm(forms.ModelForm):
    class Meta:
        model=Consultation
        fiels=['diagnostic','traitement','notes','prix_consultation']
        widgets={
            'diagnostic':forms.Textarea(
                attrs={
                    'class':"form-control",
                    'rows':4,
                    'placeholder':'Diagnostic médical ...'
                }
            ),
            'traitement':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3,
                    'placeholder':'Traitement prescrit...'
                }
            ),
            'notes':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':2,
                    'placeholder':'Notes complémentaires...'
                }
            ),
            'prix_consultation':forms.NumberInput(
                attrs={'class':'form-control'}
            ),
        }