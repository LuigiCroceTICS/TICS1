#pedimos la palabra al usuario
palabra=input("Introduce Una Palabra:")
p2i=""

#calculamos el tamaño de la palabra 
#print(len(palabra))

#recorremos la palabra 
for i in range(len(palabra),0,-1):
    #print(palabra[i-1])

    p2i= p2i+palabra[i-1]
print(p2i)

if palabra==p2i:
    print("Es un Palindromo")
else:
    print("No es Palindromo")




