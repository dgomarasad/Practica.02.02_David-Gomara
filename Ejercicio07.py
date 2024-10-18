#Escribir un programa que pregunte el correo electrónico del usuario en la
#consola y muestre por pantalla otro correo electrónico con el mismo nombre
#(la parte delantera de la arroba @) pero con dominio ceu.es.
Correo_electronico = input('Dime tu correo electronico:')
print(Correo_electronico[Correo_electronico.replace('@')] + '@ceu.es')