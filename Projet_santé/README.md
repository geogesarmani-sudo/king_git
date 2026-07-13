# Projet Fil Rouge N°1 — Sante Publique
**Akieni Academy | Programme Data Science | Cohorte 2026**

Simulation d'une mission de conseil data commanditee par le Ministere de la Sante
de la Republique du Congo. L'objectif est de collecter, nettoyer, analyser et modeliser
les donnees de sante pour aider les decideurs a allouer les ressources sanitaires
sur les 12 departements du pays.

## Structure du projet
```
projet_sante/
├── sante_variables.py              # Module fondateur enrichi (S2 Sections A-E + S3 Sections F-I)
├── semaine2_exercice1_sante.py     # Fiche patient — CHU de Brazzaville
├── semaine2_exercice2_sante.py     # KPIs OMS — Hopital General Pointe-Noire
├── semaine2_challenge.py           # Rapport comparatif — 3 hopitaux du Pool
├── semaine3_exercice1_stocks.py    # Classification stocks PNA — 5 medicaments
├── semaine3_exercice2_triage.py    # Triage patient urgences — Protocole Manchester
├── semaine3_challenge.py           # Tableau de bord sanitaire — 5 hopitaux (Conseil des Ministres)
└── README.md                       # Ce fichier
```

## Fonctionnalites S2
- Constantes OMS et 12 departements du Congo
- Variables des 5 hopitaux et 5 medicaments essentiels
- Calcul KPIs : densite medicale, taux d'occupation, valeur stock

## Fonctionnalites S3 (nouvelles)
- Classification automatique statut stocks PNA (RUPTURE CRITIQUE / ALERTE / NORMAL)
- Systeme de triage patient selon le Protocole Manchester adapte (4 niveaux)
- Tableau de bord ministeriel 5 hopitaux avec niveau d'alerte global
- Alertes conditionnelles : ruptures medicaments, saturation lits, couverture vaccinale

## Auteur
**Elenga François Armani** / Akieni Academy Cohorte 2 — Data Science
