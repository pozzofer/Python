nombre ="juan"
edad = 17

if nombre == "juan":
    print("Tu no eres Juan")
elif edad >= 18:
    print("Tienes mayoria de edad")
else:
    print("tu no eres Juan")


if nombre == "juan":
    if edad >= 18:   
        print("eres juan y tienes mayoria de edad")       
    else:
        print("eres juan, pero NO tienes mayoria de edad") 
else:
    print("tu no eres juan")                     