ano= int(input("Introduce EL Año en el Que naciste:"))
        
signo=["El Mono", "El Gallo", "El Perro", "El Cerdo", " La Rata", "El Buey", "El Tigre", "El Conejo", "El Dragon", " La Serpiente", "El Caballo", "La Cabra"]
zodiaco= ano % 12 

print ("Tu Signo Del Zodiaco es", signo[zodiaco])