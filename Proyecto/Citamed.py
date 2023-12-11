dni= input("Introduzca su dni:")
otra= input("Introduzca otra:")

citas=open('Banco.csv', 'a+')
citas.write(dni + ";" + otra + "\n")
citas.close 


#valores=['Dni', 'Mes', 'Dia', 'Hora', 'Especialidad']

#for valores in citas:
#    valores.append(int(valores))
#print(valores) 
