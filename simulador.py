# Simulador del monitor de maquinas expendedoras
# Crea lecturas.csv con una semana de historial y luego sigue creando lecturas nuevas en vivo.
# Solo usa Python estandar: no hay que instalar nada mas.
#
# Uso:  python simulador.py            (lecturas nuevas cada 2 segundos)
# Parar: Ctrl + C
#
# Columnas de lecturas.csv: fecha_hora, maquina, temp_c, errores
# Rango normal de temperatura: de 8 a 14 grados.

import csv
import math
import os
import random
import sys
import time
from datetime import datetime, timedelta

ARCHIVO = "lecturas.csv"
MAQUINAS = ["M01", "M02", "M03", "M04", "M05"]
INICIO = datetime(2026, 9, 26, 0, 0)     # el historial empieza aqui
FIN_HIST = datetime(2026, 10, 3, 19, 0)  # y termina justo antes de esta hora
PASO = timedelta(minutes=5)              # una lectura cada 5 minutos
EJEMPLO = {  # las 3 primeras lecturas en vivo de M02 (igual que en la leccion 1)
    "2026-10-03 19:00": (11.19, 1),
    "2026-10-03 19:05": (11.33, 0),
    "2026-10-03 19:10": (11.47, 2),
}


def entre(t, a, b):
    return datetime.strptime(a, "%Y-%m-%d %H:%M") <= t < datetime.strptime(b, "%Y-%m-%d %H:%M")


def lectura(t, m, azar):
    """Devuelve (temp_c, errores), o None si esa lectura no llego."""
    hora = t.hour + t.minute / 60
    temp = 11.0 + 1.2 * math.sin((hora - 6) / 24 * 6.2832) + azar.gauss(0, 0.15)
    err = 1 if azar.random() < 0.03 else 0
    # Fallas escondidas del historial (ver solucion_NO_ABRIR.txt)
    if m == "M02" and entre(t, "2026-09-29 02:00", "2026-09-29 07:00"):
        return None
    if m == "M04" and entre(t, "2026-09-30 14:00", "2026-09-30 18:00"):
        return (0.0, err)
    if m == "M01" and entre(t, "2026-10-01 08:00", "2026-10-01 20:00"):
        horas = (t - datetime(2026, 10, 1, 8, 0)).seconds / 3600
        temp += 0.55 * horas
    if m == "M03" and entre(t, "2026-10-02 10:00", "2026-10-02 13:00"):
        err = azar.randint(4, 9)
    if m == "M05" and t == datetime(2026, 10, 2, 3, 20):
        temp = 31.5
    return (round(temp, 2), err)


def historial():
    azar = random.Random(2026)
    filas = []
    t = INICIO
    while t < FIN_HIST:
        for m in MAQUINAS:
            r = lectura(t, m, azar)
            if r is None:
                continue
            fila = [t.strftime("%Y-%m-%d %H:%M"), m, "%.2f" % r[0], r[1]]
            filas.append(fila)
            if m == "M01" and entre(t, "2026-09-28 12:00", "2026-09-28 12:30"):
                filas.append(list(fila))  # lectura duplicada
        t += PASO
    return filas


def escribir_solucion():
    with open("solucion_NO_ABRIR.txt", "w", encoding="utf-8") as f:
        f.write("Las 6 fallas escondidas (no abrir hasta intentar encontrarlas):\n")
        f.write("1. M02 sin lecturas el 2026-09-29 de 02:00 a 07:00 (hueco de conexion)\n")
        f.write("2. M04 temperatura exactamente 0.00 el 2026-09-30 de 14:00 a 18:00 (sensor pegado)\n")
        f.write("3. M01 se calienta poco a poco el 2026-10-01 de 08:00 a 20:00 (sobrecalentamiento)\n")
        f.write("4. M03 con 4 a 9 errores de lector el 2026-10-02 de 10:00 a 13:00\n")
        f.write("5. M05 pico de 31.5 grados una sola vez, el 2026-10-02 a las 03:20\n")
        f.write("6. M01 lecturas duplicadas el 2026-09-28 de 12:00 a 12:30\n")


def main():
    espera = 2.0
    if not os.path.exists(ARCHIVO):
        filas = historial()
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["fecha_hora", "maquina", "temp_c", "errores"])
            w.writerows(filas)
        escribir_solucion()
        print("Cree %s con %d lecturas (del 26 de septiembre al 3 de octubre, 5 maquinas)." % (ARCHIVO, len(filas)))
    else:
        print("Ya existe %s: agrego lecturas nuevas al final." % ARCHIVO)
    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        ultima = list(csv.reader(f))[-1][0]
    t = datetime.strptime(ultima, "%Y-%m-%d %H:%M") + PASO
    azar = random.Random()
    print("Lecturas nuevas cada %d segundos. Para parar: Ctrl + C\n" % espera)
    print("fecha_hora        maquina  temp_c  errores")
    try:
        while True:
            with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                for m in MAQUINAS:
                    clave = t.strftime("%Y-%m-%d %H:%M")
                    if m == "M02" and clave in EJEMPLO:
                        temp, err = EJEMPLO[clave]
                    else:
                        temp, err = lectura(t, m, azar)
                    w.writerow([clave, m, "%.2f" % temp, err])
                    print("%s  %s      %5.2f   %d" % (clave, m, temp, err))
            t += PASO
            time.sleep(espera)
    except KeyboardInterrupt:
        print("\nListo. Se detuvo el simulador. Tus datos estan en %s" % ARCHIVO)


if __name__ == "__main__":
    main()
