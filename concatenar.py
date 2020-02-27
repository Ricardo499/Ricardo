#!/usr/bin/python3
import argparse

#def leer_archivo( archivo1, archivo2 ):
   
'''try:
        with open(archivo, "r") as fh:
           texto = fh.read()
           linens = texto.splitlines()
           texto_limpio=" ".join(linens)
   except:
        texto_limpio=" "
   return texto_limpio 
   archivo1 = "direccion"
   archivo2 = "direccion"
 
   lista1 = list (archivo1)
   lista2 = list (archivo2)
 
   archivo3=open('datos.txt','w')
 
   for x in range(2):
       datos.append.lista1[0]
       datos.append.lista2[0]
       archi.write(datos)
       datos = []
   return datos 


 def main(archivo):
   for nombre in nombres:
      print(nombre)
'''
def main(archivo, archivos):
   for archivo in archivos:
      print (archivo)
      texto = lectorleer_archivo(archivo)
      listado.append(texto)
   print(listado)
   textote= " ".join(listado)
if __name__ == "__main__":
   parser = argparser.Argparser()
   parser.add_argument('-n', '--archivo', dest='archivo', help="Texto unido", \
                       action="append", required= True)
   parser.add_argument('-o', '--output', dest='output', help="archivo de salida", \
                        required= True)
   args = parser.parse_args()
   archivo= args.archivos
   main(archivo)