import random

aleatorio=random.randint(1,10)
print(aleatorio)

#iniciamos el programa 

numusuario=input("¡Hola! Bienvenido al Juego ¯\_(◉̃ ͜ʖ◉̃)_/¯ .\n ¿como te llamas?:")
print("Hola!", numusuario)

pregunta=input("¿Quieres jugar el juego mas divertido del mundo mundial? [s/n]")


if pregunta== "s":
    print("Estoy pensando en un numero del 1 al 10")

    if pregunta== "n":
       print("Bueno Hasta luego! cuidate......")
    

    nuser=int(input("Por favor Adivina:......."))

   
    if nuser  > aleatorio:
        print("Mas Abajo......")
        if nuser < aleatorio:
            print("mas Arriba")
            if nuser== aleatorio:
                print("Correcto!!!!!")


while nuser!= aleatorio:
 nuser=int(input("Intentalo Otra Vez:"))
 
