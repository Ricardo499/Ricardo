#!/usr/bin/python3
import lector
import argparse
import random
import contar_palabras

def extraer_palabra(texto):
    lista_palabras = texto.split(" ")
    for palabra in lista_palabras:         
        palabra_aleatoria = random.choice(lista_palabras)
        if len(palabra_aleatoria) > 1:
            palabra_seleccionada = palabra_aleatoria 
    return palabra_seleccionada
    
def main(texto, numero):
    texto = lector.leer_archivo(archivo)
    lista_palabras_aleatorias = []
    for i in range(numero):
        lista_palabras_aleatorias.append(extraer_palabra(texto))
    print(lista_palabras_aleatorias)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-n', '--numero', dest='numero', help="numero", required=False, type = int)
    args = parser.parse_args()
    archivo = args.archivo
    numero = args.numero
    main(archivo, numero)