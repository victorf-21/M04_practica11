#Funció on demanarà a l’usuari que inserti 2 números i el programa li dirà quin és el més gran i quin el més petit. Si son iguals sortirà que son iguals.
num1 = int(input("Insertar primer número"))
num2 = int(input("Insertar segundo número"))
if num1 > num2:
  print('El primer número es mayor: ')
if num1 < num2:
  print('El segundo número es mayor')
if num1 == num2:
  print('Son iguales')