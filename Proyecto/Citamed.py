dni= input("Introduzca su dni:")
mes= input("Introduzca el mes :")
dia= input("Introduzca el dia:")
hora= input("Introduzca la hora:")
especialidad= input("Introduzca la especialidad.:")


citas=open('Banco.csv', 'a+')
citas.write(dni + ";" + mes + ";"+ dia + ";" + hora + ";"+ especialidad + "\n")
citas.close 


#valores=['Dni', 'Mes', 'Dia', 'Hora', 'Especialidad']

#for valores in citas:
#    valores.append(int(valores))
#print(valores) 
