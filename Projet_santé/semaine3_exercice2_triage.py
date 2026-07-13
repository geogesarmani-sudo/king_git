# ============================================================
# AKIENI ACADEMY - Projet de Sante Publique
# Semaine 3 - Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# Nom : Elenga François Armani
# ============================================================

print('=' * 55)
print(' SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE')
print(' Protocole Manchester adapte — DSS Congo 2026')
print('=' * 55)
print()

# --- SECTION 1 : SAISIE DES DONNEES PATIENT ---
# S2 (reutilise) : input(), conversion de types float() et int()

nom_patient  = input(' Nom du patient                          : ')  # str
age_patient  = int(input(' Age (annees)                            : '))  # int
temperature  = float(input(' Temperature (degres C, ex: 38.4)        : '))  # float
spo2         = float(input(' Saturation O2 en % (ex: 96.0)           : '))  # float
tension_syst = int(input(' Tension systolique en mmHg (ex: 135)    : '))  # int
douleur      = int(input(' Douleur /10 (0=aucune, 10=insupportable) : '))  # int

# --- SECTION 2 : VALIDATION DES PLAGES ---
# S3 (nouveau) : conditions simples pour detecter les saisies impossibles

saisie_valide = True  # bool : devient False si une valeur est hors plage

if temperature < 35.0 or temperature > 43.0:
    print(' ERREUR : Valeur de temperature impossible — verifier la saisie')
    saisie_valide = False

if spo2 < 50.0 or spo2 > 100.0:
    print(' ERREUR : SpO2 hors plage — verifier le capteur')
    saisie_valide = False

if tension_syst < 50 or tension_syst > 250:
    print(' ERREUR : Tension hors plage — verifier le brassard')
    saisie_valide = False

if douleur < 0 or douleur > 10:
    print(' ERREUR : Douleur doit etre entre 0 et 10')
    saisie_valide = False

if age_patient < 0 or age_patient > 120:
    print(' ERREUR : Age invalide — verifier la saisie')
    saisie_valide = False

# --- SECTION 3 : TRIAGE (si saisie valide) ---
# S3 (nouveau) : conditions composees avec or (UNE seule condition suffit)
# IMPORTANT : ordre du plus critique au moins critique — du plus restrictif au plus large
# Source : Protocole Manchester adapte — Chef urgences Dr. NKOUNKOU Aristide

if saisie_valide:

    # Niveau 1 — IMMEDIAT : au moins UNE condition critique suffit (or)
    if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
        niveau_triage = '1 — IMMEDIAT'
        couleur_triage = '[ROUGE]'
        delai_pec      = '0 minute'
        action_triage  = 'Medecin present immediatement — code ROUGE active'

    # Niveau 2 — URGENT : conditions moins critiques mais toujours urgentes
    elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
        niveau_triage  = '2 — URGENT'
        couleur_triage = '[ORANGE]'
        delai_pec      = '< 10 minutes'
        action_triage  = 'Appel medecin senior — surveillance rapprochee'

    # Niveau 3 — URGENT DIFFERE : fievre moderee ou douleur importante
    elif temperature > 37.5 or douleur > 6:
        niveau_triage  = '3 — URGENT DIFFERE'
        couleur_triage = '[JAUNE]'
        delai_pec      = '< 30 minutes'
        action_triage  = 'Infirmier — surveillance continue'

    # Niveau 4 — MOINS URGENT : tous les parametres dans les normes
    else:
        niveau_triage  = '4 — MOINS URGENT'
        couleur_triage = '[VERT]'
        delai_pec      = '< 120 minutes'
        action_triage  = 'File d attente standard'

    # --- SECTION 4 : STATUT PAR PARAMETRE VITAL ---
    # S3 (nouveau) : operateur ternaire pour statut inline dans f-string
    # Permet d'identifier le motif principal qui a declenche le niveau

    statut_temperature = '[ANORMAL — > 39.5]' if temperature > 39.5 else (
                         '[ANORMAL — > 38.5]' if temperature > 38.5 else (
                      '[ANORMAL — > 37.5]' if temperature > 37.5 else '[NORMAL]'))

    statut_spo2        = '[ANORMAL — < 90]'  if spo2 < 90  else (
                         '[ANORMAL — < 94]'  if spo2 < 94  else '[NORMAL]')

    statut_tension     = '[ANORMAL — > 180]' if tension_syst > 180 else (
                         '[ANORMAL — > 140]' if tension_syst > 140 else '[NORMAL]')

    statut_douleur     = '[ANORMAL — > 6]'   if douleur > 6 else '[NORMAL]'

    # --- SECTION 5 : IDENTIFICATION DU MOTIF PRINCIPAL ---
    # S3 (nouveau) : conditions pour identifier quelle valeur a declenche l'alerte

    if temperature > 39.5:
        motif_principal = f'Temperature {temperature} C > seuil 39.5 C'
    elif spo2 < 90:
        motif_principal = f'SpO2 {spo2}% < seuil 90%'
    elif tension_syst > 180:
        motif_principal = f'Tension {tension_syst} mmHg > seuil 180 mmHg'
    elif temperature > 38.5:
        motif_principal = f'Temperature {temperature} C > seuil 38.5 C'
    elif spo2 < 94:
        motif_principal = f'SpO2 {spo2}% < seuil 94%'
    elif tension_syst > 140:
        motif_principal = f'Tension {tension_syst} mmHg > seuil 140 mmHg'
    elif temperature > 37.5:
        motif_principal = f'Temperature {temperature} C > seuil 37.5 C'
    elif douleur > 6:
        motif_principal = f'Douleur {douleur}/10 > seuil 6/10'
    else:
        motif_principal = 'Tous les parametres dans les normes'

    # --- SECTION 6 : AFFICHAGE FICHE TRIAGE ---
    # S2 (reutilise) : f-strings structurees
    print()
    print('=' * 55)
    print(f' RESULTAT TRIAGE — {nom_patient.upper()}')
    print('=' * 55)
    print(f' PARAMETRES VITAUX')
    print(f' Temperature    : {temperature} C  {statut_temperature}')
    print(f' Saturation O2  : {spo2} %          {statut_spo2}')
    print(f' Tension systol.: {tension_syst} mmHg  {statut_tension}')
    print(f' Douleur        : {douleur} / 10        {statut_douleur}')
    print('-' * 55)
    print(f' NIVEAU DE TRIAGE : {niveau_triage}')
    print(f' COULEUR          : {couleur_triage}')
    print(f' PRISE EN CHARGE  : {delai_pec}')
    print(f' ACTION           : {action_triage}')
    print('-' * 55)
    print(f' Motif principal  : {motif_principal}')
    print('=' * 55)
