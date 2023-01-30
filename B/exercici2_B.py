"""
En aquest codi s’hi crearà una funció on demanarà a l’usuari que indica un número
i aquest li indicarà si és parell o senar.
"""
numero = (int(input("Introddueix un número: ")))
if numero % 2 == 0:
    print("El teu número és parell")
else:
    print("El teu número és senar")