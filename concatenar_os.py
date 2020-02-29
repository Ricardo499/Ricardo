#!/usr/bin/python3
#python3 ./contatenar_os -f /tmp/ -i episodio -t txt -o salida.txt
import argparse
import os
import lector

'''def crear_archivo(output, folder):
    with open(output,'w') as f:
        for texto in folder:
            f.write("{}\n".format(texto))'''



def juntar_archivos(folder, inicia, termina):
    textos=[]
    folder_inicial = os.listdir(folder)
    
    #archivo.endswith(termina) 
    lista_inicia= [archivo for archivo in folder_inicial if archivo.startswith(inicia)]
    lista_termina= [archivo for archivo in folder_inicial if archivo.endswith(termina)]
         
    archivos_texto=[]
         
    for archivo in lista_termina:
      texto = lector.leer_archivo(os.path.join(folder,archivo))
      archivos_texto.append(texto)
     

    return archivos_texto

def main(folder, inicia, termina, output):
   # crear_archivo(output, folder)
   
   # archivos_texto(archivos_texto, folder)
    textos= juntar_archivos(folder, inicia, termina)
   
    texto_limpio=" ".join(textos)
    with open (output, 'w') as f:
       f.write(texto_limpio) 


            
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--folder', dest='folder', help="Folder", required=True)
  parser.add_argument('-i', '--inicia', dest='inicia', help="Inicia", required=True)
  parser.add_argument('-t', '--termina', dest='termina', help="Termina", required=True)
  parser.add_argument('-o', '--output', dest='output', help="Salida", required=True)
  args = parser.parse_args()
  folder = args.folder
  inicia = args.inicia
  termina = args.termina
  output = args.output

  main(folder, inicia, termina, output)

