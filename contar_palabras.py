#!/usr/bin/python3
import lector
import argparse

def contar(archivo, archivo_stopwords):
  #texto = lector.leer_archivo(archivo)
  #lista= texto.split(" ")
  #totalpalabras= len(lista)
  #return totalpalabras
  texto=lector.leer_archivo(archivo)
  lista_palabras = texto.split(" ")
  total = len(lista_palabras)
  stopwords=lector.leer_stopwords(archivo_stopwords)
  #print(stopwords)
  dpc=dict() #dicc.palabras clave
  dps=dict() #dicc.palabras stopwords

  for palabra in lista_palabras:
    p=palabra.lower().strip(".,")
    if p in stopwords: #es stopword?
      if p in dps: #ya eiste?
            dps[p] += 1 #agregamos
      else:
            dps[p]=1 #inicial con 1
    else:
      if p in dpc: #ya existe?
        dpc[p]+=1 #agregamos 1
      else:
        dpc[p]=1 #creamos con 1
          
  print("palabras clave", len(dpc))
  print("palabras stopwords", len(dps))
  
  print("Total: ", total)
          
def contar_stopwords(archivo_stopwords):
  set_texto = lector.leer_stopwords(archivo_stopwords)
  return set_texto
  
def main (archivo, archivo_stopwords):
  print("Antes de hacer el trabajo")
  contar(archivo, archivo_stopwords)
  #set_texto= contar_stopwords(archivo_stopwords)
  print("Hice el trabajo")
  #print(total)
  #print(" ")
 # print (set_texto)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help="stopwords", required=False, default = "Spanish_Stopwords.txt")
    args = parser.parse_args()
    archivo = args.archivo
    stopwords = args.stopwords
    main(archivo, stopwords)