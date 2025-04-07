from random import random
import requests
import random as r
url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
webContent = requests.get(f"{url}")
personaje = webContent.json()
valores = list(personaje[0].values())
cita = valores[0]
nombre = valores[1].lower()
print(nombre)

def llenarNombre(nombre):
    palabra = ""
    for i in range(len(nombre)):
        if nombre[i] == " ":
            palabra += " "
        else:
            palabra += "_"
    return palabra

def AgregarLetras(nombre):
    letra = ""
    pos = 0
    for i in range(3):
        pos = random.randint(0,len(nombre))
        letra = nombre[pos]

barrasbajas = llenarNombre(nombre)
cont = 0
continuar = True
print(cita)
long = list("")
for i in range(len(nombre)):
    if nombre[i]==" ":
        long+=nombre[i]
    else:
        long += "_"

cont = 0
letras = len(nombre)/3

while continuar:
    print(str(long))
    print(llenarNombre(nombre))
    intento = input("Adivina el nombre, ¡tienes 3 intentos! : ")
    if intento == nombre:
        print("Enhorabuena paquete...")
        continuar = False
    elif cont<2:
        for i in range(int(letras)):
            letra = r.randint(0,len(nombre)-1)
            while long[letra]!= "_":
                letra = r.randint(0,len(nombre)-1)
            long[letra]=nombre[letra]
        cont+=1
    elif cont>=2:
        print(f"El personaje es: {nombre}")
        continuar = False


