#ejercicio de repaso
num1=int(input("Por Favor Introduzca un Numero:"))
num2=int(input("Por Favor Introduzca un Numero:"))

#control de errores 
if num1<0 or num2<0 :
    print("Error")

else:
    #comienza la logica

    if num1>num2:
        print(num1, ">", num2)
    elif num2>num1:
        print(num2, ">", num1)
    else:
        print(num1, "=", num2)
        