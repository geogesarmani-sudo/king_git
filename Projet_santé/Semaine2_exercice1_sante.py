# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 2 - Exercice 1 : Fiche Patient CHU Brazzaville
# Nom : Elenga François Armani
# Date : 23/06/2026
# =============================================================

#  --- SECTION 1 : VARIABLES PATIENT ---
nom_patient = 'MAVOUNGOU Celestine' #str
age_patient =  42 #int
sexe_patient = 'F' #str
departement_patient = 'Brazzaville' #str
couverture_sociale = 'CNSS' #str

# --- SECTION 2 : VARIABLES CONSULTATION ---
type_consultation = 'Urgences' #str
cout_consultation_fcfa = 15000.0 #float
nb_consultations = 1 #int
remise_cnss_pct = 30.0 #float
diagnostic_principal = 'Paludisme grave' #str


# --- SECTION 3 : VARIABLES HOPITAL ---
nom_hopital = 'CHU de Brazzaville' #str
ville_hopital = 'Brazzaville' #str
nb_lits_total = 320 #int
nb_lits_occupes = 284 #int
nb_medecins_actifs = 47 #int 

#  --- SECTION 4 : CALCULS ---
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
taux_occupation_pct = round(nb_lits_occupes / nb_lits_total * 100, 1)
nb_consultations_hopital = 120 #int
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)

# --- SECTION 5 : AFFICHAGE ---
print('='*60)
print(f' FICHE PATIENT - {nom_patient}')
print('='*60)
print(f'Age            : {age_patient} ans ')
print(f'Sexe           : {sexe_patient}')
print(f'Departement    : {departement_patient}')
print(f'Couverture     : {couverture_sociale}')
print('-'*60)
print(f' CONSULTATION')
print(f'Type           : {type_consultation}')
print(f'Diagnostic     : {diagnostic_principal}')
print(f'Cout unitaire  : {cout_consultation_fcfa:.0f} FCFA')
print(f'Remise CNSS    : {remise_cnss_pct}%')
print(f'COUT TOTAL     : {cout_total_fcfa} FCFA')
print('-'*60)
print(f'HOPITAL        : CHU de Brazzaville')
print(f'Ville          : {ville_hopital}')
print(f'Lits occupes   : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)')
print(f'Medecins actifs: {nb_medecins_actifs}')
print(f'Ratio consult. : {ratio_consultations_medecin} consultations / medecin ce matin')
print('='*60)
print(f'STATUT : Prise en charge validee')
print('='*60)