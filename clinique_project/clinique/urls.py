from django.urls import path
from . import views

#urlpatterns : Django parcourt cette liste dans l'ordre
# et s'arrete à la premiere URL qui correspond
urlpatterns=[
    path('',views.accueil,name='accueil'),
    path('connexion/',views.connexion,name='connexion'),
    path('deconnexion/',views.deconnexion,name='deconnexion'),
    path('dashboard/',views.tableau_de_bord,name='tableau_de_bord'),
    path('medecins/',views.liste_medecins,name='medecin'),
    path('medecins/<int:medecin_id>',views.detail_medecin,name='detail_medecin'),
    path('medecins/<int:medecin_id>/rdv',views.prendre_rdv,name='prendre_rdv'),
    path('rdv/<int:rdv_id>/',views.detail_rdv,name='detail_rdv'),
]