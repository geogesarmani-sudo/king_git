# Exercice semaine5_Calculatrice
# ELENGA François Armani*

def addition(a, b):
    return a + b
def soustraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return'Erreur: Calcul impossible'
    return a / b

# structure de la calculatrice
def calculatrice():
    print('=== Calculatrice ===')
    print('     1. Addition ')
    print('     2. Soustraction ')
    print('     3. Multiplication ')
    print('     4. Division ')

    Choix = input('Choisir une opération (1-4):')
    
    while Choix not in ('1','2','3','4'):
        print('Choix non disponible.')
        print('Veuillez Choisir 1, 2, 3 ou 4')
        Choix = input('Choisir une opération (1-4):')

    if Choix in ('1','2','3','4'):
      Nb_1 = float(input('Saissisez le premier nombre: '))
      Nb_2 = float(input('Saissisez le second nombre: '))
    if Choix == '1':
             resultat = addition(Nb_1, Nb_2)
    elif Choix == '2':
                resultat = soustraction(Nb_1, Nb_2)    
    elif Choix == '3':
                resultat = multiplication(Nb_1, Nb_2)
    elif Choix == '4':
                resultat = division(Nb_1, Nb_2)        

    
    print(f'Résultat = {resultat}')      
    
calculatrice()
   


