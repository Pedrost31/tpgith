nombre = input("Veuillez saisir un nombre : ")
print("Le nombre que vous avez saisi est :", nombre)

print("Les multiples de", nombre, "sont :")
for i in range(1, 11):
    multiple = nombre * i
    print(nombre, "x", i, "=", multiple)

while True:

    nombre = input("Veuillez saisir un nombre : ")
    print("Le nombre que vous avez saisi est :", nombre)

    print("Les multiples de", nombre, "sont :")
    for i in range(1, 11):
        multiple = int(nombre) * i  
        print(nombre, "x", i, "=", multiple)
    

    reponse = input("Voulez-vous recommencer le programme ? (O/N): ").strip().upper()
    
    if reponse != "O":
        print("Le programme est terminé.")
        break


   