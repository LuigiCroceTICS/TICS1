#ejercicio 4 

num=int(input("Introduce un Numero entero positivo:"))

#control de errores
if num < 0:
    print("Error. el numero introducido no es entero.")
else:
    for i in range(num,1,-1):
        print(i, end=", ")      