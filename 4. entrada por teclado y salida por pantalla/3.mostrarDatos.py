from platform import freedesktop_os_release


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(nombre)
print(edad)

#concatenacion
print(nombre , edad)
print("hola mi nombre es " , nombre , "y tengo" , edad , "años")

#format
print("hola {} tienes {}".format(nombre , edad))