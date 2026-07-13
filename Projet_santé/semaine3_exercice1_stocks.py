# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 3 - Exercice 1 : Classification Stocks Medicaments PNA
# Notions S2 : variables, types, operateurs, f-strings
# Notions S3 : if/elif/else, conditions composees
# Nom : Elenga François Armani
# ============================================================

# --- SECTION 1 : VARIABLES MEDICAMENTS (reimportees depuis S2) ---

m1_nom           = 'Artemether-Lumefantrine'  # str
m1_stock         = 3200                        # int : stock actuel en unites
m1_seuil_rupture = 2000                        # int : seuil d'alerte PNA
m1_cout_unitaire = 3500.0                      # float : FCFA / unite

m2_nom           = 'Amoxicilline 500mg'        # str
m2_stock         = 950                         # int
m2_seuil_rupture = 800                         # int
m2_cout_unitaire = 850.0                       # float

m3_nom           = 'Paracetamol 500mg'         # str
m3_stock         = 12400                       # int
m3_seuil_rupture = 3000                        # int
m3_cout_unitaire = 120.0                       # float

m4_nom           = 'SRO (sachets)'             # str
m4_stock         = 4200                        # int
m4_seuil_rupture = 5000                        # int
m4_cout_unitaire = 125.0                       # float

m5_nom           = 'Vaccin DTP-HepB-Hib'       # str
m5_stock         = 820                         # int
m5_seuil_rupture = 1000                        # int
m5_cout_unitaire = 8500.0                      # float

# --- SECTION 2 : CLASSIFICATION MEDICAMENT 1 — Artemether-Lumefantrine ---

if m1_stock <= m1_seuil_rupture:                    # <= inclut le seuil exact (edge case)
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:            # entre seuil et seuil * 1.5
    m1_statut  = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action  = 'Commande urgente a declencher sous 72h'
elif m1_stock <= m1_seuil_rupture * 2.0:            # entre seuil * 1.5 et seuil * 2
    m1_statut  = 'STOCK LIMITE'
    m1_couleur = '[JAUNE]'
    m1_action  = 'Surveillance renforcee — planifier commande'
else:                                               # stock > seuil * 2 => situation normale
    m1_statut  = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action  = 'Situation normale — suivi standard'

# --- SECTION 3 : CLASSIFICATION MEDICAMENT 2 — Amoxicilline 500mg ---
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action  = 'Commande urgente a declencher sous 72h'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = 'STOCK LIMITE'
    m2_couleur = '[JAUNE]'
    m2_action  = 'Surveillance renforcee — planifier commande'
else:
    m2_statut  = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action  = 'Situation normale — suivi standard'

# --- SECTION 4 : CLASSIFICATION MEDICAMENT 3 — Paracetamol 500mg ---
if m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action  = 'Commande urgente a declencher sous 72h'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = 'STOCK LIMITE'
    m3_couleur = '[JAUNE]'
    m3_action  = 'Surveillance renforcee — planifier commande'
else:
    m3_statut  = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action  = 'Situation normale — suivi standard'

# --- SECTION 5 : CLASSIFICATION MEDICAMENT 4 — SRO (sachets) ---
if m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action  = 'Commande urgente a declencher sous 72h'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = 'STOCK LIMITE'
    m4_couleur = '[JAUNE]'
    m4_action  = 'Surveillance renforcee — planifier commande'
else:
    m4_statut  = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action  = 'Situation normale — suivi standard'

# --- SECTION 6 : CLASSIFICATION MEDICAMENT 5 — Vaccin DTP-HepB-Hib ---
if m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action  = 'Commande urgente a declencher sous 72h'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = 'STOCK LIMITE'
    m5_couleur = '[JAUNE]'
    m5_action  = 'Surveillance renforcee — planifier commande'
else:
    m5_statut  = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action  = 'Situation normale — suivi standard'

# --- SECTION 7 : COMPTAGE DES ALERTES ---

nb_ruptures_critiques = 0  # int : compteur ROUGE
nb_alertes_stock      = 0  # int : compteur ORANGE
nb_stocks_limites     = 0  # int : compteur JAUNE
nb_stocks_normaux     = 0  # int : compteur VERT

# Medicament 1
if m1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
elif m1_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
elif m1_statut == 'STOCK LIMITE':
    nb_stocks_limites = nb_stocks_limites + 1
else:
    nb_stocks_normaux = nb_stocks_normaux + 1

# Medicament 2
if m2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
elif m2_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
elif m2_statut == 'STOCK LIMITE':
    nb_stocks_limites = nb_stocks_limites + 1
else:
    nb_stocks_normaux = nb_stocks_normaux + 1

# Medicament 3
if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
elif m3_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
elif m3_statut == 'STOCK LIMITE':
    nb_stocks_limites = nb_stocks_limites + 1
else:
    nb_stocks_normaux = nb_stocks_normaux + 1

# Medicament 4
if m4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
elif m4_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
elif m4_statut == 'STOCK LIMITE':
    nb_stocks_limites = nb_stocks_limites + 1
else:
    nb_stocks_normaux = nb_stocks_normaux + 1

# Medicament 5
if m5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
elif m5_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
elif m5_statut == 'STOCK LIMITE':
    nb_stocks_limites = nb_stocks_limites + 1
else:
    nb_stocks_normaux = nb_stocks_normaux + 1

# --- SECTION 8 : AFFICHAGE RAPPORT ---
print('=' * 65)
print(' RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT')
print(' Date : 15 janvier 2026')
print('=' * 65)

# Medicament 1
print(f' {m1_couleur} {m1_nom}')
print(f' Stock : {m1_stock} unites | Seuil rupture : {m1_seuil_rupture}')
print(f' Statut : {m1_statut}')
print(f' Action : {m1_action}')
print('-' * 65)

# Medicament 2
print(f' {m2_couleur} {m2_nom}')
print(f' Stock : {m2_stock} unites | Seuil rupture : {m2_seuil_rupture}')
print(f' Statut : {m2_statut}')
print(f' Action : {m2_action}')
print('-' * 65)

# Medicament 3
print(f' {m3_couleur} {m3_nom}')
print(f' Stock : {m3_stock} unites | Seuil rupture : {m3_seuil_rupture}')
print(f' Statut : {m3_statut}')
print(f' Action : {m3_action}')
print('-' * 65)

# Medicament 4
print(f' {m4_couleur} {m4_nom}')
print(f' Stock : {m4_stock} unites | Seuil rupture : {m4_seuil_rupture}')
print(f' Statut : {m4_statut}')
print(f' Action : {m4_action}')
print('-' * 65)

# Medicament 5
print(f' {m5_couleur} {m5_nom}')
print(f' Stock : {m5_stock} unites | Seuil rupture : {m5_seuil_rupture}')
print(f' Statut : {m5_statut}')
print(f' Action : {m5_action}')
print('=' * 65)

# --- SECTION 9 : BILAN FINAL ---
print(' BILAN STOCK — PNA CONGO')
print(f' Ruptures critiques : {nb_ruptures_critiques} (SRO, Vaccin DTP)')
print(f' Alertes stock      : {nb_alertes_stock} (Artemether, Amoxicilline)')
print(f' Stocks normaux     : {nb_stocks_normaux} (Paracetamol)')
print('=' * 65)

# Alerte prioritaire conditionnelle : affichee seulement si ruptures > 0
if nb_ruptures_critiques > 0:
    print(f' !! ALERTE PRIORITAIRE : {nb_ruptures_critiques} medicaments en RUPTURE CRITIQUE !!')
    print(f' Transmettre immediatement au Dr. MOUKALA (PNA)')
print('=' * 65)
