import requests
import random as r
url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
webContent = requests.get(f"{url}")
personaje = webContent.json()
valores = list(personaje[0].values())
cita = valores[0]
nombre = valores[1]
print(nombre)

def rellenarNombre(nombre):
    palabra = ""
    for i in range(len(nombre)):
        if nombre[i] == " ":
            palabra += " "
        else:
            palabra += "_"
    return palabra

def letras(nombre):
    letra = []
    pos = 0
    for i in range(int(len(nombre)/4)):
        pos = r.randint(0,len(nombre)-1)
        letra.append(nombre[pos])
    return letra

def nuevoNombre(nombre, letras):
    palabra = ""
    for i in range(len(nombre)):
        if nombre[i] == " ":
            palabra += " "
        elif nombre[i] in letras:
            palabra += nombre[i]
        else:
            palabra += "_"
    return palabra

continuar = True
print(cita)
cont = 0
nint = 1
print(rellenarNombre(nombre))
letras_viejas = []
while continuar:
    print("Adivina el autor de la cita ")
    intento = input(f"Intento {nint}: ").lower().capitalize()
    if intento == nombre.lower().capitalize():
        print("¡Enhorabuena!")
        continuar = False
    elif cont<2:
        letrasNombre = letras(nombre)
        for letra in letrasNombre:
            if letra not in letras_viejas:
                letras_viejas.append(letra)
        print(nuevoNombre(nombre, letras_viejas))
        cont += 1
    else:
        print(f"Has perdido... El personaje es: {nombre}")
        continuar = False
    nint+=1
