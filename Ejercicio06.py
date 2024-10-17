#Escribir un programa que pida al usuario que introduzca una frase en la 
#consola y una vocal, y después muestre por pantalla la misma frase pero con
#la vocal introducida en mayúscula.
Frase = input('Dime una frase ')
Vocal = input('Dime una vocal ')
print(Frase.replace(Vocal, Vocal.upper()))
