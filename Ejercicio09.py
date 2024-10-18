#Escribir un programa que pregunte al usuario la fecha de su nacimiento en
#formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar
#el programa anterior para que también funcione cuando el día o el mes se
#introduzcan con un solo carácter.
Fecha_de_nacimiento = input("Dime tu fecha de ncimiento en formato (dd/mm/aaaa) ")
Fecha_de_nacimiento = Fecha_de_nacimiento.split("/")
print("Dia:", Fecha_de_nacimiento[0])
print("Mes: ", Fecha_de_nacimiento[1])
print("Año : ", Fecha_de_nacimiento[2])
                    