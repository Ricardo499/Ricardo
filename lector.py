#!/usr/bin/python3
import argparse
import sys
#importacion de librerias

def leer_archivo( archivo ):
   ''' fc = open(archivo,"r") # r = reading: lectura 
    texto = fc.read() 
    lineas = texto.splitlines()  
    texto_limpio = " ".join(lineas) 
    return texto_limpio '''
   try:
        with open(archivo, "r") as fh:
           texto = fh.read()
           linens = texto.splitlines()
           texto_limpio=" ".join(linens)
   except:
        texto_limpio=" "
   return texto_limpio

def leer_stopwords(archivo): 
    print(archivo)
    try: 
        with open(archivo,"r") as fh:
             print("Antes de leer") 
             lineas = fh.readlines()
             print("Despues de leer") 
             lista  = [p.strip("\n") for p in lineas]
             print("Despues de la lista") 
             set_sw = set(lista)
             print("Despues de set") 
    except IOError as e:
        #print (e)
        print (sys.exc_info)
        print("Hubo un error") 
        set_sw = set() 
    return set_sw 


def eliminar_palabras(dp, palabras):
      diccionario={}
      for (k,v) in dp.items():
        if k not in palabras:
          diccionario[k]= v      
      return diccionario
 
def contar_palabras( texto ):
    palabras = texto.split(" ") 
    dp = dict() 
    for palabra in palabras: 
        p = palabra.lower().strip(",.") 
        if p in dp: 
           dp[p]+= 1
        else: 
          dp[p] = 1 
        if "" in dp:
          del(dp[""])
    return dp

def imprime_diccionario(dp, minimo):
    lista = [ (k,v) for k,v in dp.items() if v >= minimo ]
    lista_ordenada = sorted(lista, key = lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
        print(tupla[0],"= ", tupla[1])
    return

def main( archivo, minimo, stopwords ):
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    set_stopwords = leer_stopwords(stopwords)
    print (set_stopwords)
    diccionario =eliminar_palabras(dip, set_stopwords)
    print(len(dip))
    print(len(diccionario))
    #print(dip)
    imprime_diccionario(diccionario,minimo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-m', '--minimo', dest='minimo', help="minimo", required=False, default = 3, type= int)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help="stopwords", required=False, default = "Spanish_Stopwords.txt")
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    stopwords = args.stopwords
    main(archivo, minimo, stopwords)