# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 2 - Mini-Projet : Module Fondateur
# ============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========
# Convention Python : les constantes s'ecrivent en MAJUSCULES

TAUX_EUR_FCFA               = 655.957  # float : taux fixe zone CFA (immuable)
TAUX_USD_FCFA               = 600.0    # float : taux approximatif 2025
SEUIL_OMS_DENSITE_MEDICALE  = 2.3     # float : medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0    # float : % couverture vaccinale minimum OMS
SEUIL_MORTALITE_ALERTE      = 2.0     # float : % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS   = 30      # int   : jours minimum de stock avant alerte

DEPARTEMENTS_CONGO = [  # 12 departements de la Republique du Congo
    
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# === SECTION B : VARIABLES DES 5 HOPITAUX ===================
# Prefixe h1_ a h5_ pour eviter la confusion de noms entre hopitaux
# Montants en FCFA => float | Comptages (lits, medecins) => int

# Hopital 1 — CHU de Brazzaville
h1_nom             = 'CHU de Brazzaville'  # str
h1_ville           = 'Brazzaville'         # str
h1_departement     = 'Brazzaville'         # str
h1_type            = 'CHU'                 # str : CHU / Hopital General / Hopital de District / Centre de Sante
h1_nb_lits         = 320                   # int
h1_nb_lits_occupes = 284                   # int
h1_nb_medecins     = 47                    # int
h1_nb_infirmiers   = 123                   # int
h1_population_zone = 1_800_000             # int : habitants desservis
h1_budget_fcfa     = 250_000_000.0         # float : budget trimestriel estimatif

# Hopital 2 — Hopital General de Pointe-Noire
h2_nom             = 'Hopital General Pointe-Noire'  # str
h2_ville           = 'Pointe-Noire'                  # str
h2_departement     = 'Kouilou'                        # str
h2_type            = 'Hopital General'                # str
h2_nb_lits         = 180                              # int
h2_nb_lits_occupes = 143                              # int
h2_nb_medecins     = 22                               # int
h2_nb_infirmiers   = 58                               # int
h2_population_zone = 128_000                          # int
h2_budget_fcfa     = 87_450_000.0                     # float

# Hopital 3 — Hopital de Dolisie
h3_nom             = 'Hopital de Dolisie'   # str
h3_ville           = 'Dolisie'              # str
h3_departement     = 'Niari'                # str
h3_type            = 'Hopital de District'  # str
h3_nb_lits         = 120                    # int
h3_nb_lits_occupes = 94                     # int
h3_nb_medecins     = 14                     # int
h3_nb_infirmiers   = 37                     # int
h3_population_zone = 95_000                 # int
h3_budget_fcfa     = 54_000_000.0           # float

# Hopital 4 — Hopital de District d'Owando
h4_nom             = 'Hopital District Owando'  # str
h4_ville           = 'Owando'                   # str
h4_departement     = 'Cuvette'                  # str
h4_type            = 'Hopital de District'       # str
h4_nb_lits         = 80                          # int
h4_nb_lits_occupes = 61                          # int
h4_nb_medecins     = 8                           # int
h4_nb_infirmiers   = 24                          # int
h4_population_zone = 72_000                      # int
h4_budget_fcfa     = 38_000_000.0                # float

# Hopital 5 — Centre de Sante d'Impfondo
h5_nom             = 'Centre de Sante Impfondo'  # str
h5_ville           = 'Impfondo'                   # str
h5_departement     = 'Likouala'                   # str
h5_type            = 'Centre de Sante'            # str
h5_nb_lits         = 40                           # int
h5_nb_lits_occupes = 29                           # int
h5_nb_medecins     = 3                            # int
h5_nb_infirmiers   = 12                           # int
h5_population_zone = 48_000                       # int
h5_budget_fcfa     = 18_500_000.0                 # float

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================
# stock_actuel et seuil_rupture => int (unites)
# cout_unitaire => float (FCFA / unite)
# consomm_mensuelle => int (unites consommees par mois)

# Medicament 1 — Artemether-Lumefantrine (antipaludeen essentiel)
m1_nom               = 'Artemether-Lumefantrine'  # str
m1_categorie         = 'Antipaludeen'             # str
m1_stock_actuel      = 8450                       # int : unites disponibles
m1_seuil_rupture     = 2000                       # int : seuil d'alerte PNA
m1_cout_unitaire     = 3500.0                     # float : FCFA / unite
m1_consomm_mensuelle = 1200                       # int : unites consommees/mois

# Medicament 2 — Amoxicilline 500mg (antibiotique)
m2_nom               = 'Amoxicilline 500mg'  # str
m2_categorie         = 'Antibiotique'        # str
m2_stock_actuel      = 3200                  # int
m2_seuil_rupture     = 800                   # int
m2_cout_unitaire     = 850.0                 # float
m2_consomm_mensuelle = 650                   # int

# Medicament 3 — Paracetamol 500mg (analgesique)
m3_nom               = 'Paracetamol 500mg'  # str
m3_categorie         = 'Analgesique'        # str
m3_stock_actuel      = 12000                # int
m3_seuil_rupture     = 3000                 # int
m3_cout_unitaire     = 150.0                # float
m3_consomm_mensuelle = 2500                 # int

# Medicament 4 — Serum de Rehydratation Orale (SRO)
m4_nom               = 'Serum de Rehydratation Orale'  # str
m4_categorie         = 'Rehydratation'                  # str
m4_stock_actuel      = 15600                            # int
m4_seuil_rupture     = 5000                             # int
m4_cout_unitaire     = 125.0                            # float
m4_consomm_mensuelle = 3800                             # int

# Medicament 5 — Vaccin Antipaludeen RTS,S
m5_nom               = 'Vaccin Antipaludeen RTS,S'  # str
m5_categorie         = 'Vaccin'                      # str
m5_stock_actuel      = 2800                          # int
m5_seuil_rupture     = 500                           # int
m5_cout_unitaire     = 12000.0                       # float
m5_consomm_mensuelle = 400                           # int

# === SECTION D : CALCULS D'INITIALISATION ===================

# Agregats nationaux (somme des 5 hopitaux)
total_medecins   = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_infirmiers = h1_nb_infirmiers + h2_nb_infirmiers + h3_nb_infirmiers + h4_nb_infirmiers + h5_nb_infirmiers
total_lits       = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occ   = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

# KPI 1 — Densite medicale : medecins pour 1000 habitants
densite_medicale_nat = round(total_medecins / total_population * 1000, 2)

# KPI 2 — Taux d'occupation moyen (tous hopitaux confondus)
taux_occupation_moy  = round(total_lits_occ / total_lits * 100, 1)

# KPI 3 — Valeur totale du stock de medicaments : stock * prix unitaire
valeur_stock_total = (
    m1_stock_actuel * m1_cout_unitaire +
    m2_stock_actuel * m2_cout_unitaire +
    m3_stock_actuel * m3_cout_unitaire +
    m4_stock_actuel * m4_cout_unitaire +
    m5_stock_actuel * m5_cout_unitaire
)  # float : FCFA

# === SECTION E : RAPPORT D'INVENTAIRE =======================
print('=' * 62)
print(f'  MODULE FONDATEUR - PROJET SANTE PUBLIQUE')
print(f'  Akieni Academy | Etat initial — Semaine 2')
print('=' * 62)

# Perimetre geographique
print(f'\n  PERIMETRE : {len(DEPARTEMENTS_CONGO)} departement du CONGO')
print(f'{", ".join(DEPARTEMENTS_CONGO[:6])}')
print(f'{", ".join(DEPARTEMENTS_CONGO[6:])}')

# Inventaire des 5 hopitaux
print(f'\n{"─" * 62}')
print(f'INVENTAIRE HOPITAUX — {5} etablissements')
print(f'{"─" * 62}')
hopitaux_liste = [
    (h1_nom, h1_type, h1_nb_lits, h1_nb_lits_occupes, h1_nb_medecins),
    (h2_nom, h2_type, h2_nb_lits, h2_nb_lits_occupes, h2_nb_medecins),
    (h3_nom, h3_type, h3_nb_lits, h3_nb_lits_occupes, h3_nb_medecins),
    (h4_nom, h4_type, h4_nb_lits, h4_nb_lits_occupes, h4_nb_medecins),
    (h5_nom, h5_type, h5_nb_lits, h5_nb_lits_occupes, h5_nb_medecins),
]
if (nom, typ, lits, occ, med) in hopitaux_liste:
    print(f'{nom:<35} | {typ:<20} | Lits: {occ}/{lits} | Med: {med}')

# KPIs globaux
print(f'\n{"─" * 62}')
print(f'  KPIs GLOBAUX')
print(f'{"─" * 62}')
print(f'  Densite medicale    : {densite_medicale_nat} medecins/1000 hab  [OMS >= {SEUIL_OMS_DENSITE_MEDICALE}]')
print(f'  Taux occupation moy : {taux_occupation_moy}%                    [Optimal : 70-85%]')
print(f'  Valeur stock total  : {valeur_stock_total:>15,.0f} FCFA')

# Inventaire des 5 medicaments
print(f'\n{"─" * 62}')
print(f'  INVENTAIRE MEDICAMENTS — {5} essentiels')
print(f'{"─" * 62}')
medicaments_liste = [
    (m1_nom, m1_categorie, m1_stock_actuel, m1_seuil_rupture, m1_consomm_mensuelle),
    (m2_nom, m2_categorie, m2_stock_actuel, m2_seuil_rupture, m2_consomm_mensuelle),
    (m3_nom, m3_categorie, m3_stock_actuel, m3_seuil_rupture, m3_consomm_mensuelle),
    (m4_nom, m4_categorie, m4_stock_actuel, m4_seuil_rupture, m4_consomm_mensuelle),
    (m5_nom, m5_categorie, m5_stock_actuel, m5_seuil_rupture, m5_consomm_mensuelle),
]
if (nom, cat, stock, seuil, conso) in medicaments_liste:
    mois_restants = round(stock / conso, 1)
    statut        = 'OK' if stock > seuil else '! ALERTE'
    print(f'  {nom:<35} | {cat:<15} | Stock: {stock:>6} | {mois_restants} mois | {statut}')

# Alerte nationale
print(f'\n{"─" * 62}')
if densite_medicale_nat < SEUIL_OMS_DENSITE_MEDICALE:
    print(f'[CRITIQUE] Densite medicale nationale : {densite_medicale_nat} / 1000 hab')
    print(f'Norme OMS : {SEUIL_OMS_DENSITE_MEDICALE} — Deficit majeur a combler')
else:
    print(f'Densite medicale dans les normes OMS.')
print('=' * 62)