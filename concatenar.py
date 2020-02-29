#!/usr/bin/python3
#./concatenar -n /tmp/episodio1.txt -n /tmp/episodio2.txt -o Ep1yEp2.txt
#o es output

import lector
import argparse

def main(nombres, output):
  listado=[]
  for nombre in nombres:
    texto = lector.leer_archivo(nombre)
    listado.append(texto)
  textote = "\n". join(listado)
  
  file = open(output,"w")
   
  file.write(textote)
  file.close()
  print("Se creo el archivo " + output)
      
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nombre', dest='nombres', help="nombre de personajes", action="append", required=True)
    parser.add_argument('-o', '--output', dest='output', help="archivo de salida", \
                        required= True)
    args = parser.parse_args()
    nombres = args.nombres
    output = args.output
    main(nombres, output)
