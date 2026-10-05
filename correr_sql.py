import sqlite3
import sys

archivo = sys.argv[1]
consulta = open(archivo, encoding="utf-8").read()

conexion = sqlite3.connect("monitor.db")
cursor = conexion.execute(consulta)
columnas = [c[0] for c in cursor.description]
filas = cursor.fetchall()

anchos = [len(c) for c in columnas]
for fila in filas:
    for i, valor in enumerate(fila):
        anchos[i] = max(anchos[i], len(str(valor)))

print("  ".join(c.ljust(anchos[i]) for i, c in enumerate(columnas)))
print("  ".join("-" * a for a in anchos))
for fila in filas:
    print("  ".join(str(v).ljust(anchos[i]) for i, v in enumerate(fila)))
print(f"Filas: {len(filas)}")
conexion.close()