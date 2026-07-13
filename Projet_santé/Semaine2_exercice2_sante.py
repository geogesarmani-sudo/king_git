# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 2 - Exercice 2 : Convertisseur de Devises et KPIs Sanitaires OMS
# Hopital General de Pointe-Noire — Trimestre Q4 2025
# Nom : Elenga François Armani
# Date : 23/06/2026
# ============================================================

# --- SECTION 1 : DONNEES BRUTES ---
budget_fcfa          = 87_450_000  # int  : budget trimestriel (underscore pour lisibilite)
nb_consultations_ext = 4823        # int  : consultations externes Q4
nb_hospitalisations  = 1247        # int  : hospitalisations Q4
nb_deces             = 18          # int  : deces hospitaliers Q4
nb_lits_total        = 180         # int  : capacite totale en lits
nb_lits_occupes      = 143         # int  : lits occupes en moyenne ce trimestre
nb_medecins          = 22          # int  : medecins permanents
nb_infirmiers        = 58          # int  : infirmiers permanents
population_dept      = 128_000     # int  : population departement Kouilou
taux_eur_fcfa        = 655.957     # float: taux fixe zone CFA (immuable)
taux_usd_fcfa        = 600.0       # float: taux approximatif 2025

# --- SECTION 2 : CONVERSIONS DE DEVISES ---

# Division : budget FCFA / taux => montant en devise etrangere
budget_eur = round(budget_fcfa / taux_eur_fcfa, 2)  # float : euros
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2)  # float : dollars

# --- SECTION 3 : INDICATEURS OMS ---

# OMS 1 — Densite medicale : nb medecins pour 1000 habitants
densite_medicale = round((nb_medecins / population_dept) * 1000, 1)  # float

# OMS 2 — Taux de mortalite hospitaliere : deces / hospitalisations * 100
taux_mortalite = round((nb_deces / nb_hospitalisations) * 100, 1)    # float

# OMS 3 — Taux d'occupation des lits : lits occupes / lits totaux * 100
taux_occupation = round((nb_lits_occupes / nb_lits_total) * 100, 1)  # float

# --- SECTION 4 : OPERATEURS AVANCES (// % **) ---

# Division entiere // : nombre de jours de stock couverts par le budget medicaments
budget_medicaments   = int(budget_fcfa * 0.35)  # int : 35% du budget alloue aux medicaments
cout_journalier_meds = 450_000                  # int : cout journalier en FCFA
jours_stock          = budget_medicaments // cout_journalier_meds  # int : division entiere
jours_restants       = budget_medicaments % cout_journalier_meds   # int : reste en FCFA (modulo)

# Modulo % : pair ou impair (utile pour les rapports bi-mensuels)
parite_consultations = nb_consultations_ext % 2  # int : 0 = pair, 1 = impair
statut_parite        = 'pair' if parite_consultations == 0 else 'impair'

# Puissance ** : projection budget N+2 avec croissance de 8%/an pendant 2 ans
budget_n_plus_2 = round(budget_fcfa * (1.08 ** 2), 1)  # float

# --- SECTION 5 : AFFICHAGE RAPPORT ---     
print('=' * 60)
print(f' RAPPORT TRIMESTRIEL Q4 2025 - Hopital General de Pointe-Noire')
print('=' * 60)

print(f'\nBUDGET')
print(f'  Depenses Q4      : {budget_fcfa:_} FCFA')
print(f'  En euros         : {budget_eur:,.2f} EUR')
print(f'  En dollars       : {budget_usd:,.2f} USD')

print(f'\nINDICATEURS OMS')
print(f'  Densite medicale : {densite_medicale} medecins / 1000 hab   [Norme OMS : >= 2.3]')
print(f'  Taux mortalite   : {taux_mortalite}%                        [Seuil alerte : > 2%]')
print(f'  Taux occupation  : {taux_occupation}%                       [Optimal : 70-85%]')

print(f'\nANALYSE PHARMACIE')
print(f'  Budget medicaments : {budget_medicaments:_} FCFA')
print(f'  Jours de stock     : {jours_stock} jours')
print(f'  jours_restants     : {jours_restants:_}')

print(f'\nPROJECTION BUDGETAIRE')
print(f'  Budget N+2 (8%/an) : {budget_n_plus_2:_} FCFA')

# --- SECTION 6 : ALERTES CONDITIONNELLES ---

if densite_medicale < 2.3:
    print(f'ALERTE : Densite medicale CRITIQUE  :{densite_medicale} / 1000 hab - norme OMS : 2.3')
if taux_mortalite > 2.0:
    print(f'[ALERTE] Taux mortalite   :{taux_mortalite}% (seuil : 2%)')
if taux_occupation > 85.0:
    print(f'[ALERTE]   Surcharge lits :{taux_occupation}% (optimal max : 85%)')
if densite_medicale >= 2.3 and taux_mortalite <= 2.0 and taux_occupation <= 85.0:
    print(f'Aucune alerte — tous les indicateurs sont dans les normes.')
print('=' * 62)
