#media aritmetica

import random

e = 0.0001  # Ajusté el valor de e a un valor más razonable


def obtener_caras_pintadas():
    probaacum = [6/26, 18/26, 1]
    r = random.random()
    for i in range(3):
        if r < probaacum[i]:
            return i + 1  # No es necesario sumarle 1; ya funciona correctamente


def converge(prob_ant, prob_act):
    # Verifica si la diferencia entre las dos probabilidades es suficientemente pequeña
    return abs(prob_ant - prob_act) < e


def Calcular_media_de_A():
    suma = 0
    N = 0
    prob_ant = -1
    prob_act = 0

    while not converge(prob_ant, prob_act) or N < 100000:
        cubito1 = obtener_caras_pintadas()
        cubito2 = obtener_caras_pintadas()
        A = cubito1 + cubito2
        N += 1
        suma += A
        prob_ant = prob_act
        prob_act = suma / N  # Media de A
    return prob_act


def Calcular_desvio_de_A(media):
    suma_cuadrados_diferencias = 0
    N = 0
    prob_ant = -1
    prob_act = 0

    while not converge(prob_ant, prob_act) or N < 100000:
        cubito1 = obtener_caras_pintadas()
        cubito2 = obtener_caras_pintadas()
        A = cubito1 + cubito2
        N += 1
        suma_cuadrados_diferencias += (A - media) ** 2  # Sumar las diferencias al cuadrado
        prob_ant = prob_act
        prob_act = (suma_cuadrados_diferencias / N) ** 0.5  # Desvío estándar
    return prob_act


# Calcular la media de A primero
media_A = Calcular_media_de_A()
print("Media de A:", media_A)

# Luego, calcular el desvío estándar usando la media calculada
desvio_A = Calcular_desvio_de_A(media_A)
print("Desvío estándar de A:", desvio_A)