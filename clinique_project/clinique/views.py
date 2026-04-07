from django.shortcuts import render, get_object_or_404, redirect
# render : Combine  un template HTML avec des données et retourne une reponse
# get_object_404 : Cherche un object en BD, retourrne une 404 si introuvable
# redirect : Envoie l'utilisateur vers une autre URL

from django.contrib.auth.decorators import login_required
# login_required : un "decorateur" qui bloque l'accès si l'utilisateur n'est pas connecté

from django.contrib import messages
# messages: système de notifications temporaires (succès, erreur, info)

from django.contrib.auth import login, logout, authenticate
# login : connecte l'utilisateur
# logout : deconnecte l'utilisateur
# authenticate : vérifie les identifiants

from .models import Medecin, Patient, RendezVous, Consultation, DossierMedical, Ordonnance, Examen, Facture, Specialite
# Importation de tous les modèles de la base de données

from .forms import RendezVousForm, ConsultationForm

# vue 1 : Page d'accueil
def accueil(request):
    # On recupère des statistiques sur la page d'accueil
    # .count () SELECT COUNT(*) 
    nb_medecins=Medecin.objects.count()
    nb_patients=Patient.objects.count()
    nb_rdv=RendezVous.objects.count()

    # On recupère les 3 derniers rendez-vou
    derniers_rdv=RendezVous.objects.order_by('-date','-heure')[:3]
    # SELECT * FROM RendezVous ORDER BY date DESC, heure DESC LIMIT 3
    contexte={
        'nb_medecins':nb_medecins,
        'nb_patients':nb_patients,
        'nb_rdv':nb_rdv,
        'derniers_rdv':derniers_rdv,
    }
    return render(request,'clinique/accueil.html',contexte)

def connexion(request):
    # request.method iinique si c'est une visite normale
    # ou une soumission de formulaire
    if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        # authenticate vérifie les identifiants en base de données
        user=authenticate(request,username=username, password=password)
        if user is not None:
            #login()  crée la session : l'utilisateur est maintenant connecté
            login(request,user)
            # messages.success
            messages.success(request, f'Bienvenue {user.username}!')
            return redirect('tableau_de_bord')
        else:
            messages.error(request, "Identifiants incorrects")
    return render(request,'clinique/connexion.html')

def deconnexion(request):
    logout(request)
    messages.success(request, "Vous êtes maintenant déconnecté")
    return redirect('connexion')


# VUE 4: Tableau de bord

# @login_required : Si l'utilisateur n'est pas connecté
# Django le redirige automatiquement

@login_required(login_url='connexion')
def tableau_de_bord(request):
    # On detecte si l'utilisateur est un médecin ou un patient
    est_medecin=hasattr(request.user,'medecin')
    est_patient=hasattr(request.user,'patient')
    contexte={}
    if est_medecin:
        medecin=request.user.medecin
        rdv_a_venir=RendezVous.objects.filter(medecin=medecin, statut__in=['planifie','confirme']).order_by('date','heure') # statut IN ('planifie','confirme')
        contexte={
            'role':"medecin",
            'medecin':medecin,
            'rdv_a_venir':rdv_a_venir,
            'nb_patients':rdv_a_venir.values('patient').distinct().count()
        }
    elif est_patient:
        patient=request.user.patient
        rdv_a_venir=RendezVous.objects.filter(patient=patient,
        statut__in=['planifie','confirme']).order_by('date','heure')
        rdv_passes=RendezVous.objects.filter(
            patient=patient,
            statut='termine'
        ).order_by('-date')
        contexte={
            'role':"patient",
            'patient':patient,
            'rdv_a_venir':rdv_a_venir,
            'rdv_passes':rdv_passes,
        }

    return render(request,'clinique/tableau_de_bord.html',contexte)

# VUE 5: Liste des medecins
@login_required(login_url='connexion')
def liste_medecins(request):
    medecins=Medecin.objects.all()
    # Recherche : Si l'Url Contient ?q=cardiologie
    recherche=request.GET.get('q','')
    if recherche: 
        medecins=medecins.filter(
            specialites__nom__icontains=recherche
        )
    contexte={
        'medecins':medecins,
        'recherche':recherche,
        'specialites':Specialite.objects.all()
    }
    return render(request,'clinique/liste_medecins.html',contexte)

    


    
    