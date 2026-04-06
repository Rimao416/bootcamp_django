from django.contrib import admin
from .models import Specialite, Medecin, Patient, RendezVous, Consultation
# Register your models here.

#ADMIN 1 : Specialite
@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display=['nom','description']
    # search_fields: Active une barre de recherche sur les champs qu'on va mettre
    search_fields=['nom']
    
# Admin 2: Medecin
class MedecinInline(admin.StackedInline):
    model=Medecin
    can_delete=False
    verbose_name_plural="Profil Medecin"
    
@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display=['__str__','get_email','get_specialites','get_telephone']
    search_fields=['user__first_name','user__last_name','user__email']
    filter_horizontal=['specialites']
    list_filter=['specialites']
    
    filter_horizontal=['specialites']
    list_filter=['specialites']
    
    
    def get_email(self,obj):
        return obj.user.email
    get_email.short_description='Email'
    def get_telephone(self,obj):
        return obj.telephone or '-'
    get_telephone.short_description='Téléphone'
    
    def get_specialites(self,obj):
        # .all() retourne tous les objets liés
        # On  les joint en une seule chaine séparée par des virgules
        return ", ".join([s.nom for s in obj.specialites.all()])
    get_specialites.short_description="Spécialités"    
    
    
# ADMIN 3 : Patient
# Inline pour afficher les rnedez-vous d'un patient directement
class RendezVousInline(admin.TabularInline):
    # TabularInline = affichage en Table (plus compact)
    model=RendezVous
    extra=0
    fields=['medecin','date','heure','statut']
    readonly_fields=[]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['__str__','get_username','get_email','date_naissance','groupe_sanguin','telephone']
    search_fields=['user__first_name','user__last_name','user__email']

    list_filter=['groupe_sanguin']
    inlines=[RendezVousInline]
    
    def get_email(self,obj):
        return obj.user.email
    get_email.short_description='Email'
    
    def get_username(self,obj):
        return obj.user.username
    get_username.short_description='Username'

class ConsultationInline(admin.StackedInline):
    model=Consultation
    can_delete=False
    extra=0
    
@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display=['patient','medecin','date','heure','statut','motif']
    list_filter=['statut','date','medecin']
    search_fields=[
        'patient__user__first_name',
        'patient__user__last_name',
        'medecin__user__first_name',
        'motif',
    ]
    inlines=[ConsultationInline]

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display=['rendez_vous','get_patient','get_medecin','prix_consultation','updated_at']
    search_fields=['rendez_vous__patient__user__last_name',
                   'rendez_vous__medecin__user__last_name',
                   'diagnostic'
                   ]
    def get_patient(self,obj):
        return obj.rendez_vous.patient
    get_patient.short_descrption='Patient'
    def get_medecin(self,obj):
        return obj.rendez_vous.medecin
    get_medecin.short_descrption='Medecin'
    