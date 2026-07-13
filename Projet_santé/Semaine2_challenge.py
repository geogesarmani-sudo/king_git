# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 2 - Challenge Entreprise : Rapport Comparatif
# 3 Hopitaux du Departement du Pool
# Destinataire : Dr. ELENGA Pascal, Directeur DSS
# Nom : Elenga François Armani
# Date : 23/06/2026
# ============================================================

# --- SECTION 1 : HOPITAL 1 — District de Kinkala ---
h1_nom             = 'Hopital District Kinkala'  # str
h1_budget_fcfa     = 12_500_000                  # int : budget trimestriel FCFA
h1_consultations   = 1847                        # int : consultations externes
h1_hospitalisations= 312                         # int : hospitalisations
h1_deces           = 8                           # int : deces hospitaliers
h1_lits_total      = 45                          # int : capacite totale
h1_lits_occupes    = 41                          # int : lits occupes
h1_medecins        = 3                           # int : medecins permanents
h1_population      = 85_000                      # int : population desservie

# --- SECTION 2 : HOPITAL 2 — CMS de Vindza ---
h2_nom             = 'CMS de Vindza'             # str
h2_budget_fcfa     = 6_800_000                   # int
h2_consultations   = 923                         # int
h2_hospitalisations= 87                          # int
h2_deces           = 2                           # int
h2_lits_total      = 20                          # int
h2_lits_occupes    = 14                          # int
h2_medecins        = 1                           # int
h2_population      = 42_000                      # int

# --- SECTION 3 : HOPITAL 3 — Hopital de Kindamba ---
h3_nom             = 'Hopital de Kindamba'       # str
h3_budget_fcfa     = 9_200_000                   # int
h3_consultations   = 1234                        # int
h3_hospitalisations= 201                         # int
h3_deces           = 11                          # int
h3_lits_total      = 35                          # int
h3_lits_occupes    = 33                          # int
h3_medecins        = 2                           # int
h3_population      = 67_000                      # int

# --- SECTION 4 : CALCULS KPIs — HOPITAL 1 ---

# Cout moyen par patient : budget / (consultations + hospitalisations)
h1_cout_moyen      = round(h1_budget_fcfa / (h1_consultations + h1_hospitalisations), 2)

# Taux d'occupation : lits occupes / lits totaux * 100
h1_taux_occupation = round(h1_lits_occupes / h1_lits_total * 100, 2)

# Densite medicale : medecins / population * 1000
h1_densite         = round(h1_medecins / h1_population * 1000, 2)

# Taux de mortalite : deces / hospitalisations * 100
h1_mortalite       = round(h1_deces / h1_hospitalisations * 100, 2)

# --- SECTION 5 : CALCULS KPIs — HOPITAL 2 ---
h2_cout_moyen      = round(h2_budget_fcfa / (h2_consultations + h2_hospitalisations), 2)
h2_taux_occupation = round(h2_lits_occupes / h2_lits_total * 100, 2)
h2_densite         = round(h2_medecins / h2_population * 1000, 2)
h2_mortalite       = round(h2_deces / h2_hospitalisations * 100, 2)

# --- SECTION 6 : CALCULS KPIs — HOPITAL 3 ---
h3_cout_moyen      = round(h3_budget_fcfa / (h3_consultations + h3_hospitalisations), 2)
h3_taux_occupation = round(h3_lits_occupes / h3_lits_total * 100, 2)
h3_densite         = round(h3_medecins / h3_population * 1000, 2)
h3_mortalite       = round(h3_deces / h3_hospitalisations * 100, 2)

# --- SECTION 7 : BONUS — Budget suffisant pour 5 medecins chacun ? ---
budget_total       = h1_budget_fcfa + h2_budget_fcfa + h3_budget_fcfa  # int
cout_medecin_trim  = 1_200_000   # int : cout d'un medecin par trimestre (FCFA)
medecins_actuels   = h1_medecins + h2_medecins + h3_medecins           # int : total actuel
medecins_cibles    = 5 * 3                                              # int : 5 par hopital
medecins_manquants = medecins_cibles - medecins_actuels                 # int
cout_recrutement   = medecins_manquants * cout_medecin_trim             # int : cout total
budget_suffisant   = budget_total >= cout_recrutement                   # bool

# --- SECTION 8 : AFFICHAGE RAPPORT ---
print('=' * 65)
print(f'  RAPPORT COMPARATIF - DEPARTEMENT DU POOL')
print(f'  A : Dr. ELENGA Pascal, Directeur de la DSS')
print(f'  Date : 08 janvier 2026 — Confidentiel')
print('=' * 65)

# Boucle sur les 3 hopitaux pour affichage uniforme
hopitaux = [
    (h1_nom, h1_cout_moyen, h1_taux_occupation, h1_densite, h1_mortalite),
    (h2_nom, h2_cout_moyen, h2_taux_occupation, h2_densite, h2_mortalite),
    (h3_nom, h3_cout_moyen, h3_taux_occupation, h3_densite, h3_mortalite),
]

for (nom, cout, occ, dens, mort) in hopitaux:
    print(f'\n  {nom}')
    print(f'  {"-" * 50}')
    print(f'  Cout moyen / patient  : {cout:>10,.0f} FCFA')
    print(f'  Taux occupation lits  : {occ:>9.2f} %')
    print(f'  Densite medicale      : {dens:>9.2f} medecins / 1000 hab [OMS >= 2.3]')
    print(f'  Taux de mortalite     : {mort:>9.2f} %                [Seuil : 2%]')

    # Identification de la situation critique
    if mort > 2.0 or dens < 0.05:
        print(f'  >>> SITUATION CRITIQUE : mortalite = {mort}% | densite = {dens} <<<')
    else:
        print(f'  Statut : Sous surveillance reguliere')

#   Bonus challenge
print(f'\n{"=" * 65}')
print(f'  Bonus challenge')
print(f'{"=" * 65}')
print(f'  Budget total des 3 hopitaux  : {budget_total:_} FCFA')
print(f'  Medecins actuels             : {medecins_actuels} (objectif : {medecins_cibles})')
print(f'  Medecins manquants           : {medecins_manquants}')
print(f'  Cout recrutement             : {cout_recrutement:_} FCFA')

if budget_suffisant:
    surplus = budget_total - cout_recrutement
    print(f'  FAISABLE : budget suffisant (surplus : {surplus:_} FCFA)')
else:
    deficit = cout_recrutement - budget_total
    print(f'  IMPOSSIBLE : deficit de {deficit:_} FCFA')
print('=' * 65)
