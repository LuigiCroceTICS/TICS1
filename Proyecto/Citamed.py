dni= int(input("Introduzca su dni:"))

citas=open('Banco.csv', 'a+')
citas.close 

valores=['Dni', 'Mes', 'Dia', 'Hora', 'Especialidad']

for valores in citas:
    valores.append(int(valores))
print(valores)

citas.write(dni)


 
