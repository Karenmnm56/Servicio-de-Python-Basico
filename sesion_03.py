#Loops
mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El nuevo numero es:", i)

    resultado = 0
    for i in mi_lista:
        resultado+= i

        print ("El resultado de la suma de mi lista es: {resultado}")

        for i in range (2,9):
         print(i)

mi_lista_2=["Lunes,Martes,Miercoles,Jueves,Viernes"]
for i in mi_lista_2:
    if i != "Lunes":
        print(f"Feliz{i}!")
#Practica 2
# Dada la lista mi_lista_2 = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
#imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
#Pista:usa los dos tipos loops y for en el mismo programa para logarlo
#Resultado:
#martes
#miercoles
#jueves
#viernes
mi_lista_3 =["Lunes","Martes","Jueves","Viernes"]
for i in mi_lista_3:
   if i != "":
      print(f"{i}")
      #while loop
      i = 0

      while i < 3:
         i+=1
         for d in mi_lista_3:
            if d != "Lunes":
               print(d)


