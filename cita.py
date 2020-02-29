#!/usr/bin/python3
import argparse
import lector
import contar_palabras

def obten_cita(texto, inicio, cuenta):
  lista = texto.split(" ")
  longitud  = len(lista)
  if ((inicio+cuenta) <longitud):
    lista_palabras = lista[inicio:inicio+cuenta]
    cita = " ".join(lista_palabras)
  else:
      cita = ""
  return cita


def main(archivo , archivo_stopwords, incio, cuenta):
   texto = lector.leer_archivo(archivo)
   cita = obten_cita(texto, inicio, cuenta)
   print("cita:", cita)
   stopwords = lector.leer_stopwords (archivo_stopwords)
   contar_palabras.contar(cita, archivo_stopwords)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-s', '--stopwords', dest='archivo_stopwords', help="stopwords", required=False, default = "Spanish_Stopwords.txt")
    parser.add_argument('-i', '--inicio', dest='inicio', help= 'inicio de la cita', required=False, default=10, type = int)
    parser.add_argument('-c', '--cuenta', dest= 'cuenta', help ='longitud en palabras', required=False, default=10, type= int)
    args = parser.parse_args()
    archivo = args.archivo
    inicio = args.inicio
    cuenta = args.cuenta 
    archivo_stopwords = args.archivo_stopwords
    main(archivo, archivo_stopwords, inicio, cuenta)
