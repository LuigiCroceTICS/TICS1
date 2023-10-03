#ejercicio 3

n=int(input("Introduce un numero entero positivo:"))

#control de errores
if n < 0:
    print("Error. el numero introducido no es entero.")
else:
    for i in range(1,n+1, 2):
        print(i)
        
        