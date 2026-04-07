# Ces imports viennent de Django
from django.shortcuts import render, get_object_or_404, redirect
# render          : combine un template HTML avec des données et retourne une réponse
# get_object_or_404 : cherche un objet en BD, retourne une page 404 si introuvable
# redirect        : envoie l'utilisateur vers une autre URL

from django.contrib.auth.decorators import login_required
# login_required : un "décorateur" qui bloque l'accès si l'utilisateur n'est pas connecté

from django.contrib import messages
# messages : système de notifications temporaires (succès, erreur, info...)

from django.contrib.auth import login, logout, authenticate
# login      : connecte un utilisateur (crée la session)
# logout     : déconnecte l'utilisateur
# authenticate : vérifie username + password, retourne l'User si correct

from .models import Medecin, Patient, RendezVous, Consultation, Specialite
from .forms import RendezVousForm, ConsultationForm
# On importera ces formulaires à l'étape suivante


# ─────────────────────────────────────────────
# VUE 1 : Page d'accueil
# ─────────────────────────────────────────────
def accueil(request):
    # On récupère des statistiques à afficher sur la page d'accueil
    # .count() fait un SELECT COUNT(*) — plus efficace que len()
    nb_medecins = Medecin.objects.count()
    nb_patients = Patient.objects.count()
    nb_rdv      = RendezVous.objects.count()

    # On récupère les 3 derniers rendez-vous (le "-" = ordre décroissant)
    derniers_rdv = RendezVous.objects.order_by('-date', '-heure')[:3]

    # Le "contexte" = dictionnaire de données envoyées au template
    # Dans le template, on pourra écrire {{ nb_medecins }}, {{ derniers_rdv }}...
    contexte = {
        'nb_medecins': nb_medecins,
        'nb_patients': nb_patients,
        'nb_rdv': nb_rdv,
        'derniers_rdv': derniers_rdv,
    }

    # render() cherche le fichier templates/clinique/accueil.html
    return render(request, 'clinique/accueil.html', contexte)


# ─────────────────────────────────────────────
# VUE 2 : Connexion
# ─────────────────────────────────────────────
def connexion(request):

    # request.method indique si c'est une visite normale (GET)
    # ou une soumission de formulaire (POST)
    if request.method == 'POST':

        # request.POST contient les données du formulaire soumis
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate vérifie les identifiants en base de données
        # Retourne l'objet User si correct, None si incorrect
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login() crée la session : l'utilisateur est maintenant connecté
            login(request, user)

            # messages.success : une notification verte qui apparaît une seule fois
            messages.success(request, f'Bienvenue, {user.first_name} !')

            # On redirige vers le tableau de bord
            return redirect('tableau_de_bord')
        else:
            # Identifiants incorrects : on affiche une erreur
            messages.error(request, 'Identifiants incorrects.')

    # Si GET (première visite) ou si POST échoue : on affiche le formulaire
    return render(request, 'clinique/connexion.html')


# ─────────────────────────────────────────────
# VUE 3 : Déconnexion
# ─────────────────────────────────────────────
def deconnexion(request):
    logout(request)  # supprime la session
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('connexion')


# ─────────────────────────────────────────────
# VUE 4 : Tableau de bord
# ─────────────────────────────────────────────

# @login_required : si l'utilisateur n'est pas connecté,
# Django le redirige automatiquement vers login_url
@login_required(login_url='connexion')
def tableau_de_bord(request):

    # On détecte si l'utilisateur est un médecin ou un patient
    # hasattr vérifie si l'attribut existe sans lever d'erreur
    est_medecin = hasattr(request.user, 'medecin')
    est_patient = hasattr(request.user, 'patient')

    contexte = {}

    if est_medecin:
        medecin = request.user.medecin

        # filter() = WHERE en SQL
        # On récupère uniquement les RDV de CE médecin
        rdv_a_venir = RendezVous.objects.filter(
            medecin=medecin,
            statut__in=['planifie', 'confirme']  # statut IN ('planifie', 'confirme')
        ).order_by('date', 'heure')

        contexte = {
            'role': 'medecin',
            'medecin': medecin,
            'rdv_a_venir': rdv_a_venir,
            'nb_patients': rdv_a_venir.values('patient').distinct().count(),
        }

    elif est_patient:
        patient = request.user.patient

        rdv_a_venir = RendezVous.objects.filter(
            patient=patient,
            statut__in=['planifie', 'confirme']
        ).order_by('date', 'heure')

        rdv_passes = RendezVous.objects.filter(
            patient=patient,
            statut='termine'
        ).order_by('-date')

        contexte = {
            'role': 'patient',
            'patient': patient,
            'rdv_a_venir': rdv_a_venir,
            'rdv_passes': rdv_passes,
        }

    return render(request, 'clinique/tableau_de_bord.html', contexte)


# ─────────────────────────────────────────────
# VUE 5 : Liste des médecins
# ─────────────────────────────────────────────
@login_required(login_url='connexion')
def liste_medecins(request):

    # On récupère TOUS les médecins
    medecins = Medecin.objects.all()

    # Recherche : si l'URL contient ?q=cardiologie
    # ex : /medecins/?q=cardiologie
    recherche = request.GET.get('q', '')
    # request.GET.get('q', '') : récupère le paramètre "q" de l'URL
    # le deuxième argument '' est la valeur par défaut si "q" n'existe pas

    if recherche:
        # icontains = LIKE '%...%' en SQL, insensible à la casse
        medecins = medecins.filter(
            specialites__nom__icontains=recherche
        )
        # specialites__nom__icontains : on traverse la relation ManyToMany
        # pour filtrer sur le nom de la spécialité

    contexte = {
        'medecins': medecins,
        'recherche': recherche,
        'specialites': Specialite.objects.all(),
    }
    return render(request, 'clinique/liste_medecins.html', contexte)


# ─────────────────────────────────────────────
# VUE 6 : Détail d'un médecin
# ─────────────────────────────────────────────
@login_required(login_url='connexion')
def detail_medecin(request, medecin_id):
    # get_object_or_404 : cherche Medecin avec pk=medecin_id
    # Si introuvable → page 404 automatique. Jamais de crash.
    medecin = get_object_or_404(Medecin, pk=medecin_id)

    contexte = {
        'medecin': medecin,
        'specialites': medecin.specialites.all(),
    }
    return render(request, 'clinique/detail_medecin.html', contexte)


# ─────────────────────────────────────────────
# VUE 7 : Prendre un rendez-vous
# ─────────────────────────────────────────────
@login_required(login_url='connexion')
def prendre_rdv(request, medecin_id):
    medecin = get_object_or_404(Medecin, pk=medecin_id)

    # On vérifie que l'utilisateur est bien un patient
    if not hasattr(request.user, 'patient'):
        messages.error(request, 'Seuls les patients peuvent prendre un rendez-vous.')
        return redirect('liste_medecins')

    patient = request.user.patient

    if request.method == 'POST':
        # On instancie le formulaire avec les données POST
        form = RendezVousForm(request.POST)

        if form.is_valid():
            # commit=False : on crée l'objet en mémoire SANS le sauvegarder
            # Ça nous permet d'ajouter les champs manquants avant
            rdv = form.save(commit=False)

            # On complète les champs qui ne viennent pas du formulaire
            rdv.patient = patient
            rdv.medecin = medecin
            rdv.statut  = 'planifie'

            # Maintenant on sauvegarde vraiment en base de données
            rdv.save()

            messages.success(request, 'Votre rendez-vous a bien été enregistré !')
            return redirect('tableau_de_bord')
    else:
        # Première visite : formulaire vide
        form = RendezVousForm()

    contexte = {
        'form': form,
        'medecin': medecin,
    }
    return render(request, 'clinique/prendre_rdv.html', contexte)


# ─────────────────────────────────────────────
# VUE 8 : Détail d'un rendez-vous + consultation
# ─────────────────────────────────────────────
@login_required(login_url='connexion')
def detail_rdv(request, rdv_id):
    rdv = get_object_or_404(RendezVous, pk=rdv_id)

    # On essaie de récupérer la consultation liée (elle n'existe peut-être pas)
    # try/except évite une erreur si la consultation n'est pas encore créée
    try:
        consultation = rdv.consultation  # accès via le related_name OneToOne
    except Consultation.DoesNotExist:
        consultation = None

    # Seul le médecin du RDV peut saisir une consultation
    peut_consulter = (
        hasattr(request.user, 'medecin') and
        request.user.medecin == rdv.medecin
    )

    if request.method == 'POST' and peut_consulter:
        # Si une consultation existe déjà on la modifie, sinon on en crée une
        form = ConsultationForm(request.POST, instance=consultation)

        if form.is_valid():
            c = form.save(commit=False)
            c.rendez_vous = rdv  # on lie la consultation au rendez-vous
            c.save()

            # On met aussi à jour le statut du rendez-vous
            rdv.statut = 'termine'
            rdv.save()

            messages.success(request, 'Consultation enregistrée.')
            return redirect('detail_rdv', rdv_id=rdv.pk)
    else:
        form = ConsultationForm(instance=consultation)

    contexte = {
        'rdv': rdv,
        'consultation': consultation,
        'form': form,
        'peut_consulter': peut_consulter,
    }
    return render(request, 'clinique/detail_rdv.html', contexte)