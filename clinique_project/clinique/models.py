# On a importé les outils de base de Django
from django.db import models

# On importe le modèle User integré à Django
# C'est lui qui gère les comptes
from django.contrib.auth.models import User
# MODELE 1 : SPECIALITE
class Specialite(models.Model):
    
    nom=models.CharField(max_length=100)
    # VARCHAR(100) NOT NULL+++++++++++++++++++
    description=models.TextField(blank=True)
    # description TEXT
    
    class Meta:
        verbose_name="Spécialité"
        verbose_name_plural="Spécialités"

# MODELE 2: MEDECIN

class Medecin(models.Model):
    #OneToneField : un médecin = un seul compte User, et vice-vers
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    telephone=models.CharField(max_length=20,blank=True)
    photo=models.ImageField(upload_to='medecins/',blank=True,null=True)
    specialites=models.ManyToManyField(Specialite,blank=True)
    class Meta:
        verbose_name="Médecin"
        verbose_name_plural="Médecins"

# MODELE 3: Patient:
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_naissance=models.DateField()
    GROUPE_SANGUIN_CHOICES=[
        ('A+','A+'),('A-','A-'),
        ('B+','B+'),('B-','B-'),
        ('AB+','AB+'),('AB-','AB-'),
        ('O+','O+'),('O-','O-'),
    ]
    groupe_sanguin=models.CharField(max_length=5,choices=GROUPE_SANGUIN_CHOICES,blank=True)
    adresse=models.TextField(blank=True)
    telephone=models.CharField(max_length=20,blank=True)
    class Meta:
        verbose_name="Patient"
        verbose_name_plural="Patients"

# MODELE 4: RENDEZ VOUS
class RendezVous(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='rendez_vous')
    medecin=models.ForeignKey(Medecin,on_delete=models.CASCADE,related_name='rendez_vous')
    date=models.DateField()
    heure=models.TimeField()
    motif=models.CharField(max_length=255)
    STATUT_CHOICES=[
        ('planifie','Planifié'),
        ('confirme','Confirmé'),
        ('annule','Annulé'),
        ('terminé','Terminé'),
    ]    
    statut=models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='planifié'
    )
    # Django va remplir ce champ automatiquement avec la date du jour
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Rendez-vous"
        verbose_name_plural="Rendez-vous"
        ordering=['date','-heure']

# MODELE 5 : Consultation

class Consultation(models.Model):
    rendez_vous=models.OneToOneField(RendezVous,on_delete=models.CASCADE,
                                     related_name='consultation')
    diagnostic=models.TextField()
    traitement=models.TextField(blank=True)
    
    notes=models.TextField(blank=True)
    prix_consultation=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Consultation"
        verbose_name_plural="Consultations"
    
    
    