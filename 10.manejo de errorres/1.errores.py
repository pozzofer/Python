try:
    edad = int(input("ingrese su edad: "))
    print('Tu edad es: ' , edad)
except:
    print('Ingresaste un valor erroneo')    

#para hacer que se repita hasta poner la opcion correcta podemos crear un bucle while 
while True:
        try:
            edad = int(input("ingrese su edad: "))
            print('Tu edad es: ' , edad)
            break
        except:
            print('Ingresaste un valor erroneo')  
        finally:
            print('la ejecucion ha finalizado')