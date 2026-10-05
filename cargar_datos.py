import csv
import sqlite3

conexion = sqlite3.connect("monitor.db")
cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS lecturas")
cursor.execute(
    "CREATE TABLE lecturas ("
    "fecha_hora TEXT, maquina TEXT, temp_c REAL, errores INTEGER)"
)

with open("lecturas.csv", newline="", encoding="utf-8") as archivo:
    filas = csv.DictReader(archivo)
    for fila in filas:
        fecha = fila["fecha_hora"]
        maquina = fila["maquina"]
        temp = float(fila["temp_c"])
        errores = int(fila["errores"])
        cursor.execute(
            "INSERT INTO lecturas VALUES (?, ?, ?, ?)",
            (fecha, maquina, temp, errores),
        )

conexion.commit()
total = cursor.execute("SELECT COUNT(*) FROM lecturas").fetchone()[0]
print(f"Cargué {total} lecturas en monitor.db")
conexion.close()