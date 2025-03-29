#Plantee el pseudocódigo de un algoritmo que permita resolver mediante muestreos aleatorios computacionales el ejercicio 6.a) 
# para cada una de las distribuciones P(B), p(B/A) y P(AB), y 6.b), para cada indicador. 
# Implemente cada pseudocódigo planteado.

#Considere que de los cubitos del problema anterior se extraen dos al azar con restitución. Si se definen las siguientes variables aleatorias o estocásticas:
#A  = suma de caras coloreadas 		B  = máximo de caras coloreadas 
#       encuentre:
#las distribuciones de probabilidades: P(A), P(B), P(B/A)<--, P(A/B)<--, p(A,B) 
#los promedios y desviaciones estándar de las distribuciones de A y de B
#el factor de correlación y la covarianza 
#un estimador del valor de B a partir de A mediante regresión lineal



import numpy as np
import random

e = 0.0001

def obtener_caras_pintadas():
    probaacum = [6 / 26, 18 / 26, 1]
    r = random.random()
    for i in range(3):
        if r < probaacum[i]:
            return i + 1  # Solucionamos sin sumarle 1

def converge(prob_ant, prob_act):
    for i in range(2, 7):
        for j in range(1, 4):
            if abs(prob_ant[i, j] - prob_act[i, j]) > e:
                return False
    return True

def Calcular_Prob_AB():
    N = 0
    exitos = np.full((7, 4), 0, dtype=float)
    prob_ant = np.full((7, 4), -1, dtype=float)
    prob_act = np.full((7, 4), 0, dtype=float)

    while not converge(prob_ant, prob_act) or N < 10000:
        cubito1 = obtener_caras_pintadas()
        cubito2 = obtener_caras_pintadas()
        B = max(cubito1, cubito2)
        A = cubito1 + cubito2
        exitos[A, B] += 1
        N += 1
        for i in range(2, 7):
            for j in range(1, 4):
                prob_ant[i, j] = prob_act[i, j]
                prob_act[i, j] = exitos[i, j] / N

    # Calcular probabilidades marginales P(A) y P(B)
    P_A = np.sum(prob_act, axis=1)  # Sumar por filas para obtener P(A)
    P_B = np.sum(prob_act, axis=0)  # Sumar por columnas para obtener P(B)

    # Calcular las probabilidades condicionales
    P_A_given_B = np.zeros_like(prob_act)  # Inicializar matriz P(A|B)
    P_B_given_A = np.zeros_like(prob_act)  # Inicializar matriz P(B|A)

    for i in range(2, 7):
        for j in range(1, 4):
            if P_B[j] > 0:
                P_A_given_B[i, j] = prob_act[i, j] / P_B[j]
            if P_A[i] > 0:
                P_B_given_A[i, j] = prob_act[i, j] / P_A[i]

    return prob_act, P_A_given_B, P_B_given_A

# Ejecutar y mostrar resultados
prob_AB, P_A_given_B, P_B_given_A = Calcular_Prob_AB()

print("Probabilidades conjuntas P(A, B):")
print(prob_AB)

print("\nProbabilidades condicionales P(A|B):")
print(P_A_given_B)

print("\nProbabilidades condicionales P(B|A):")
print(P_B_given_A)