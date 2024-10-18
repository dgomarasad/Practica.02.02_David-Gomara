#Escribir un programa que pregunte por consola el precio de un producto en 
#euros con dos decimales y muestre por pantalla el número de euros y el número
#de céntimos del precio introducido.
precio = float((input('Dime el precio del producto: ')))
precio = precio.split(",")
print("euros: ", precio[0])
print("centimos: ", precio[1])