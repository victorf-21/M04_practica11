"""
Funció que li demanarà a l’usuari l’edat i els ingressos que té mensuals. Si l’edat és ser igual o major de 18 anys i
els ingressos son majors de 1200, el missatge per consola serà: “És necessari que facis la declaració d’hisenda” En cas
que alguna de les dues opcions no es compleixi, el missatge serà: “Encara no pots fer la declaració”.
"""
def x():
    edad = int(input("Introduce tu edad: "))
    ingressos = int(input("Introduce tus ingresos: "))

    if(edad >= 18 and ingressos > 1200):
        return "És necessari que facis la hisenda"

    else:
        return "Encara no pots fer la declaració"
print(x())