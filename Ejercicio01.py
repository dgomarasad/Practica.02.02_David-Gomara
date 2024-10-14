#Escribir un programa que pregunte el nombre del usuario en la consola y un
#número entero e imprima por pantalla en líneas distintas el nombre del 
#usuario tantas veces como el número introducido.
Nombre = input("Como te llamas ")
numero = int(input("Escribe un numero "))
print((Nombre + '\n')* numero)