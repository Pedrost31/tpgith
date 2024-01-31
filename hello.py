nombre = input("Veuillez saisir un nombre : ")
print("Le nombre que vous avez saisi est :", nombre)

print("Les multiples de", nombre, "sont :")
for i in range(1, 11):
    multiple = nombre * i
    print(nombre, "x", i, "=", multiple)