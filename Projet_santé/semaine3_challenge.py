# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 3 - Challenge Entreprise : Tableau de Bord Sanitaire
# 5 Hopitaux — Pour le Conseil des Ministres
# Destinataire : Secretaire General du Ministere de la Sante
# Notions S2 : variables, types, operateurs, f-strings
# Notions S3 : if/elif/else, conditions composees and/or
# Nom : Elenga François Armani
# Date : 23/06/2026
# ============================================================

# --- SECTION 1 : HOPITAL 1 — CHU de Brazzaville ---
h1_nom          = 'CHU Brazzaville'   # str
h1_lits_total   = 320                 # int
h1_lits_occupes = 298                 # int
h1_nb_medecins  = 47                  # int
h1_nb_ruptures  = 2                   # int : SRO, Vaccin
h1_nb_alertes   = 2                   # int : Artemether, Amoxicilline

# --- SECTION 2 : HOPITAL 2 — Hopital General Pointe-Noire ---
h2_nom          = 'Hopital Pointe-Noire'  # str
h2_lits_total   = 180                     # int
h2_lits_occupes = 143                     # int
h2_nb_medecins  = 22                      # int
h2_nb_ruptures  = 0                       # int
h2_nb_alertes   = 1                       # int : Amoxicilline

# --- SECTION 3 : HOPITAL 3 — Hopital de Dolisie ---
h3_nom          = 'Hopital Dolisie'   # str
h3_lits_total   = 95                  # int
h3_lits_occupes = 91                  # int
h3_nb_medecins  = 8                   # int
h3_nb_ruptures  = 1                   # int : SRO
h3_nb_alertes   = 2                   # int : Artemether, Vaccin

# --- SECTION 4 : HOPITAL 4 — Hopital de District Owando ---
h4_nom          = 'Hopital Owando'    # str
h4_lits_total   = 45                  # int
h4_lits_occupes = 32                  # int
h4_nb_medecins  = 3                   # int
h4_nb_ruptures  = 3                   # int : SRO, Vaccin, Artemether
h4_nb_alertes   = 0                   # int

# --- SECTION 5 : CMS Impfondo ---
h5_nom          = 'CMS Impfondo'      # str
h5_lits_total   = 20                  # int
h5_lits_occupes = 19                  # int
h5_nb_medecins  = 1                   # int
h5_nb_ruptures  = 2                   # int : SRO, Amoxicilline
h5_nb_alertes   = 1                   # int : Vaccin

# --- SECTION 6 : CALCULS TAUX D'OCCUPATION (S2 reutilise) ---
h1_taux_occ = round(h1_lits_occupes / h1_lits_total * 100, 1)  # float
h2_taux_occ = round(h2_lits_occupes / h2_lits_total * 100, 1)
h3_taux_occ = round(h3_lits_occupes / h3_lits_total * 100, 1)
h4_taux_occ = round(h4_lits_occupes / h4_lits_total * 100, 1)
h5_taux_occ = round(h5_lits_occupes / h5_lits_total * 100, 1)

# --- SECTION 7 : NIVEAU D'OCCUPATION DES LITS (S3 nouveau) ---
# Source : Regle 2 DSS — seuils OMS occupation lits

# Hopital 1
if h1_taux_occ > 95:
    h1_niv_occ = '[CRI]'   # str : CRITIQUE — saturation
elif h1_taux_occ > 85:
    h1_niv_occ = '[ALT]'   # str : ALERTE ELEVEE
elif h1_taux_occ > 70:
    h1_niv_occ = '[OK ]'   # str : OPTIMAL
else:
    h1_niv_occ = '[BAS]'   # str : SOUS-UTILISATION

# Hopital 2
if h2_taux_occ > 95:
    h2_niv_occ = '[CRI]'
elif h2_taux_occ > 85:
    h2_niv_occ = '[ALT]'
elif h2_taux_occ > 70:
    h2_niv_occ = '[OK ]'
else:
    h2_niv_occ = '[BAS]'

# Hopital 3
if h3_taux_occ > 95:
    h3_niv_occ = '[CRI]'
elif h3_taux_occ > 85:
    h3_niv_occ = '[ALT]'
elif h3_taux_occ > 70:
    h3_niv_occ = '[OK ]'
else:
    h3_niv_occ = '[BAS]'

# Hopital 4
if h4_taux_occ > 95:
    h4_niv_occ = '[CRI]'
elif h4_taux_occ > 85:
    h4_niv_occ = '[ALT]'
elif h4_taux_occ > 70:
    h4_niv_occ = '[OK ]'
else:
    h4_niv_occ = '[BAS]'

# Hopital 5
if h5_taux_occ > 95:
    h5_niv_occ = '[CRI]'
elif h5_taux_occ > 85:
    h5_niv_occ = '[ALT]'
elif h5_taux_occ > 70:
    h5_niv_occ = '[OK ]'
else:
    h5_niv_occ = '[BAS]'

# --- SECTION 8 : NIVEAU D'ALERTE GLOBAL (S3 nouveau) ---
# Source : Regles de classification — Secretariat General Ministere Sante
# Conditions composees : or / and selon la regle

# Hopital 1
if h1_nb_ruptures >= 2 or h1_taux_occ > 95:
    h1_alerte = '[CRITIQUE]'
    h1_recommandation = 'Mobiliser reserve PNA + transferts patients urgents'
elif h1_nb_ruptures >= 1 or h1_taux_occ > 85 or (h1_nb_alertes >= 2 and h1_nb_medecins < 5):
    h1_alerte = '[PREOCCUPANT]'
    h1_recommandation = 'Commande urgente medicaments + renforcement personnel'
else:
    h1_alerte = '[SATISFAISANT]'
    h1_recommandation = 'Maintenir surveillance standard'

# Hopital 2
if h2_nb_ruptures >= 2 or h2_taux_occ > 95:
    h2_alerte = '[CRITIQUE]'
    h2_recommandation = 'Mobiliser reserve PNA + transferts patients urgents'
elif h2_nb_ruptures >= 1 or h2_taux_occ > 85 or (h2_nb_alertes >= 2 and h2_nb_medecins < 5):
    h2_alerte = '[PREOCCUPANT]'
    h2_recommandation = 'Commande urgente medicaments + renforcement personnel'
else:
    h2_alerte = '[SATISFAISANT]'
    h2_recommandation = 'Maintenir surveillance standard'

# Hopital 3
if h3_nb_ruptures >= 2 or h3_taux_occ > 95:
    h3_alerte = '[CRITIQUE]'
    h3_recommandation = 'Mobiliser reserve PNA + transferts patients urgents'
elif h3_nb_ruptures >= 1 or h3_taux_occ > 85 or (h3_nb_alertes >= 2 and h3_nb_medecins < 5):
    h3_alerte = '[PREOCCUPANT]'
    h3_recommandation = 'Commande urgente medicaments + renforcement personnel'
else:
    h3_alerte = '[SATISFAISANT]'
    h3_recommandation = 'Maintenir surveillance standard'

# Hopital 4
if h4_nb_ruptures >= 2 or h4_taux_occ > 95:
    h4_alerte = '[CRITIQUE]'
    h4_recommandation = 'Mobiliser reserve PNA + transferts patients urgents'
elif h4_nb_ruptures >= 1 or h4_taux_occ > 85 or (h4_nb_alertes >= 2 and h4_nb_medecins < 5):
    h4_alerte = '[PREOCCUPANT]'
    h4_recommandation = 'Commande urgente medicaments + renforcement personnel'
else:
    h4_alerte = '[SATISFAISANT]'
    h4_recommandation = 'Maintenir surveillance standard'

# Hopital 5
if h5_nb_ruptures >= 2 or h5_taux_occ > 95:
    h5_alerte = '[CRITIQUE]'
    h5_recommandation = 'Mobiliser reserve PNA + transferts patients urgents'
elif h5_nb_ruptures >= 1 or h5_taux_occ > 85 or (h5_nb_alertes >= 2 and h5_nb_medecins < 5):
    h5_alerte = '[PREOCCUPANT]'
    h5_recommandation = 'Commande urgente medicaments + renforcement personnel'
else:
    h5_alerte = '[SATISFAISANT]'
    h5_recommandation = 'Maintenir surveillance standard'

# --- SECTION 9 : COMPTEURS NATIONAUX ---
nb_hopitaux_critiques = 0  # int
nb_ruptures_national  = 0  # int : total ruptures sur les 5 hopitaux

# Comptage niveaux critiques
if h1_alerte == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h2_alerte == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h3_alerte == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h4_alerte == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h5_alerte == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1

# Comptage ruptures nationales
nb_ruptures_national = (
    h1_nb_ruptures + h2_nb_ruptures + h3_nb_ruptures +
    h4_nb_ruptures + h5_nb_ruptures
)

# BONUS : cout commandes urgentes (450 000 FCFA par rupture)
cout_commande_express = 450_000              # int : FCFA par commande express
cout_total_urgences   = nb_ruptures_national * cout_commande_express  # int

# --- SECTION 10 : AFFICHAGE TABLEAU DE BORD ---
print('=' * 64)
print(' TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE')
print(' Date : 16 janvier 2026 | Pour le Conseil des Ministres')
print('=' * 64)
print(f' {"HOPITAL":<25} {"OCCUPATION":<14} {"ALERTES":<12} {"NIVEAU GLOBAL"}')
print('-' * 64)
print(f' {h1_nom:<25} {str(h1_taux_occ)+"%":<6} {h1_niv_occ}  {str(h1_nb_ruptures)+"R + "+str(h1_nb_alertes)+"A":<12} {h1_alerte}')
print(f' {h2_nom:<25} {str(h2_taux_occ)+"%":<6} {h2_niv_occ}  {str(h2_nb_ruptures)+"R + "+str(h2_nb_alertes)+"A":<12} {h2_alerte}')
print(f' {h3_nom:<25} {str(h3_taux_occ)+"%":<6} {h3_niv_occ}  {str(h3_nb_ruptures)+"R + "+str(h3_nb_alertes)+"A":<12} {h3_alerte}')
print(f' {h4_nom:<25} {str(h4_taux_occ)+"%":<6} {h4_niv_occ}  {str(h4_nb_ruptures)+"R + "+str(h4_nb_alertes)+"A":<12} {h4_alerte}')
print(f' {h5_nom:<25} {str(h5_taux_occ)+"%":<6} {h5_niv_occ}  {str(h5_nb_ruptures)+"R + "+str(h5_nb_alertes)+"A":<12} {h5_alerte}')
print('-' * 64)
print(f' {nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE')
print(f' {nb_ruptures_national} ruptures de stock identifiees a l echelle nationale')
print(f' BONUS — Cout commandes urgentes : {cout_total_urgences:_} FCFA')

# Recommandation nationale conditionnelle
if nb_hopitaux_critiques >= 3:
    print(f' RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA')
elif nb_hopitaux_critiques >= 1:
    print(f' RECOMMANDATION : Renforcement cible des hopitaux en situation critique')
else:
    print(f' RECOMMANDATION : Maintenir la surveillance standard')

print('=' * 64)
