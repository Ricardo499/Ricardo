#!/usr/bin/python3
import argparse
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
 
def contar_palabras( texto ):
    palabras = texto.split(" ") 
    dp = dict() 
    for palabra in palabras: 
        p = palabra.strip(",.") 
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

def main( archivo, minimo ):
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    #print(dip)
    imprime_diccionario(dip,minimo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-m', '--minimo', dest='minimo', help="minimo", required=False, default = 3, type= int)
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    main(archivo, minimo)

