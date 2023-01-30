#Funció on demanarà que insereixin un nom dels 5 que es proposin. Depenent del nom que indiqui s’hi mostrarà, per consola, un missatge diferent. Si es passa un nom no adeqüat s’ha d’indicar que el nom no està a la llista.
mylist = ["Victor", "Albert", "Pau", "Roberto", "Maria"]
print(mylist)
nombre = str(input("Insertar nombre"))

if nombre in mylist:
    print("Si está")
else:
    print("No está")
