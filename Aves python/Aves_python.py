#Declara una lista de cadenas
aves=["Loro gris","Paloma de diamante","Coctel"]
print("Los valores de la lista antes de insertar:")
#Itera sobre la lista para imprimir los valores 
for ave in aves:
    print(ave,end=" ")
    
print("\n")

#Agregs 3 valores al final de la lista utilizando el metodo append()
aves.append("Mayna")
aves.append("Periquitos")
aves.append("Cacatua")
print("Los valores valores de la lista despues de insertar :")
#Itera sobre la lista para imprimir los valores
for ave in aves:
    print(ave,end=" ")
   
print("\n")
