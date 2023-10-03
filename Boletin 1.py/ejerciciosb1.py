#Ejercicio 1 escribir la cadena Hola, Mundo
print("Hola , Mundo")


#Ejercicio 2
x = "Hola, Mundo"
print(x)



#Ejercicio 3
print("Bienvenido")
nombre=input("por favor, introduce tu nombre: ")
print("Hola ¿Que tal?", nombre)


#ejercicio 4
print(((3+2)/(2*5))**2)



#ejercicio 5
print("¡Hola,Bienvenido!, Calculemos cuanto te Deben.")
horas=int(input("¿Cuantas Horas Trabajas?:"))
coste=int(input("¿Cual es el coste Por Hora?:"))

print("El Total es=", coste*horas)



#Ejercicio 6
print("Bienvenido")
n=int(input("Introduzca un numero Positivo"))
suma= (n*(n+1))/2

print("La operacion es:")
print("*****************************")
print(suma)

print("Calculemos tu IMC")

peso=int(input("Introduce Tu Peso en KG"))

altura=int(input("Ahora Introduce tu Estatura en M"))

resultado= peso/altura

print(resultado)




#ejercicio 7

print("Calculemos tu IMC")

peso=int(input("Introduce Tu Peso en KG"))

altura=float(input("Ahora Introduce tu Estatura en M"))

resultado= peso/altura**2

print("Tu IMC es:")
print(resultado)



#ejercicio 8

print("Vamos a Calcular esta division:")

n1=int(input("Introduce el Primer Numero"))
n2=int(input("Introduce el Segundo Numero"))

resultado= n1/n2
resto=n1%n2

print("La división de ", n1,"entre",n2,"da un cociente de", resultado, "y un resto de ",resto)
