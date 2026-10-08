lineas = [
# Una lista de textos: 1 encabezado, 4 filas buenas y 3 dañadas (le falta una columna, «abc» como temperatura, y una vacía).
    "fecha_hora,maquina,temp_c,errores",
    "2026-09-26 00:00,M01,9.93,0",
    "2026-09-26 00:00,M02,9.92,1",
    "2026-09-26 00:05,M02",
    "2026-09-26 00:05,M03,abc,0",
    "2026-09-26 00:10,M01,10.05,2",
    ",,,",
    "2026-09-26 00:10,M02,10.12,0",
]
with open("lecturas_danado.csv", "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(lineas) + "\n")
print("Creé lecturas_danado.csv con 3 filas dañadas a propósito")
# Avisa que ya está.

