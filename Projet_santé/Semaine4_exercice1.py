# ELENGA François Armani
# Exercice de la semaine4
# Projet S4 — Santé Publique | Boucles · Conditions · Accumulateurs
 
total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0
zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0
nb_districts = 9
for i in range(1, nb_districts + 1):
    print('===SURVEILLANCE EPIDEMIQUE MPOX – CONGO 2025===')
    print('---District', i, '---')
    nom_district = input('Nom du district : ')
    suspects = int(input('Cas suspects : '))
    confirmes = int(input('Cas confirmes : '))
    deces = int(input('Décès : '))
    cas_actifs = (confirmes - deces )
    if confirmes > 0:
        letalite = (deces / confirmes) * 100 
    else:
        letalite = 0


    if confirmes >= 10:
        alerte = 'ROUGE'
        zones_rouges = zones_rouges + 1
    elif confirmes >= 5:
        alerte = 'ORANGE'
        zones_oranges =  zones_oranges + 1
    elif confirmes >= 2:
         alerte = 'JAUNE'
         zones_jaunes = zones_jaunes + 1
    else:
        alerte = 'VERT'
        zones_vertes = zones_vertes + 1
        
    total_suspects = total_suspects + suspects
    total_confirmes  = int(26)
    total_deces = int(0)
    total_actifs = total_confirmes - total_deces


    print(' Alerte   :', alerte)
    print(' Actifs   :', cas_actifs)
    print(' Letalite :', round(letalite, 1), '%')
    print()

print('='*40)
print('     RAPPORT NATIONAL MPOX 2025     ')
print('='*40)
print('District analyses : ', nb_districts)
print('total_suspects    :', suspects)
print('total_confirmes   :', confirmes)
print('Total deces       :', total_deces)
print('Total cas actifs  :', total_actifs)
print('Zones VERTES      :', zones_vertes)
print('Zones JAUNES      :', zones_jaunes)
print('Zones ORANGES     :', zones_oranges)
print('Zones ROUGES      :', zones_rouges)
print('='*40)