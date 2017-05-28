#
# Manuelita es un porgrama colaborativo.
# No pretende ser útil pero tiene propósitos nobles.
#
import sys

def selfie(archivo):

    fuente = open(archivo)

    for linea in fuente:
        print(linea[:-1])

    fuente.close()
    return


print("Hola, así soy realmente:")

selfie(sys.argv[0])
