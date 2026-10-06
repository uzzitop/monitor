def promedio(numeros):
    return sum(numeros) / len(numeros)


def esta_fuera_de_rango(temp, minimo=8, maximo=14):
    return temp < minimo or temp > maximo


def contar_alertas(temps):
    cuenta = 0
    for t in temps:
        if esta_fuera_de_rango(t):
            cuenta = cuenta + 1
    return cuenta


def nombre_corto(maquina):
    return maquina.upper()[0:3]


def saludar(nombre, entusiasmo=1):
    return "Hola, " + nombre + "!" * entusiasmo


temps = [10.5, 11.2, 9.8, 14.7, 11.0]
print(round(promedio(temps), 2))
print(esta_fuera_de_rango(14.7))
print(contar_alertas(temps))
print(nombre_corto("m02-norte"))
print(saludar("Uzzi", 3))