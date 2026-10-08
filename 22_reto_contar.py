import csv
import sys
#Nombre del archivo que le voy a pasar en este caso un archivo CSV
registros = "lecturas.csv"
#En caso de que haya pasado un archivo al momento de compilar.
if len(sys.argv) > 1 :
    registros=sys.argv[1]
#Diccionario que utilizare para contar
contador={}
#Variable que contara los errores
dmg=0
#Aqui empezara la funcion que puede fallar, es decir que puede tener un error al recibir un dato por ejemplo.
try:
    with open(registros,newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            try:
                if not fila["maquina"]:
                    raise ValueError("No hay maquina")
                float(fila["temp_c"])
                int(fila["errores"])
            except (ValueError,TypeError):
                dmg+=1
                continue
            m=fila["maquina"]
            contador[m]=contador.get(m,0)+1    

except FileNotFoundError:
    print(f"No existe {registros}")
    sys.exit()

print(f"Archivo:{registros}")
for maquina in sorted(contador):
    print(maquina, contador[maquina])
print(f"Filas con errores:{dmg}")    