"""
En aquest codi es demana a l’usuari que inserti 2 números.
El programa li dirà quin és el més gran i quin el més petit.
Si en cas de que fossin iguals, no sortirà cap missatge.
"""

num1 = int(input('Introdueix per pantalla un número: '))
num2 = int(input('Introdueix un segon número: '))

if (num1>num2):
    print("El primer número que has introduït és més gran que el segon.")
    # Crearem el primer condicional

if(num1<num2):
    print("El segon número que has introduït és més gran que el primer.")
    # Crearem el segon condicional

else:
    print("")
    # Crearem un l'últim condicional per descarte.