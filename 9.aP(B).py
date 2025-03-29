#Plantee el pseudocódigo de un algoritmo que permita resolver mediante muestreos aleatorios computacionales el ejercicio 6.a) 
# para cada una de las distribuciones P(B), p(B/A) y P(AB), y 6.b), para cada indicador. 
# Implemente cada pseudocódigo planteado.

#Considere que de los cubitos del problema anterior se extraen dos al azar con restitución. Si se definen las siguientes variables aleatorias o estocásticas:
#A  = suma de caras coloreadas 		B  = máximo de caras coloreadas 
#       encuentre:
#las distribuciones de probabilidades: P(A), P(B)<--, P(B/A), P(A/B), p(A,B) 
#los promedios y desviaciones estándar de las distribuciones de A y de B
#el factor de correlación y la covarianza 
#un estimador del valor de B a partir de A mediante regresión lineal




import random

e = 0.0001


def obtener_caras_pintadas():
    probaacum=[6/26,18/26,1]
    r= random.random()
    for i in range(3):
        if r < probaacum[i]:
            return i+1 #Arreglo va de 0 a 2, como hago para solucionarlo sin sumarle 1 
        

        
def converge(prob_ant, prob_act):
    for i in range(1,4):
        if abs(prob_ant[i] - prob_act[i]) > e:
            return False
    return True


def Calcular_Prob_B ():

    exitos = [0] * 4
    N = 0
    prob_ant= [-1] * 4
    prob_act =[0] * 4

    while(not converge(prob_ant, prob_act) or N < 10000):
        cubito1 = obtener_caras_pintadas()
        cubito2 = obtener_caras_pintadas()
        B=max(cubito1,cubito2)
        exitos[B]+=1
        N+=1
        for i in range(1,4):
            prob_ant[i] = prob_act[i]
            prob_act[i] = exitos[i] / N
    return prob_act

print (Calcular_Prob_B())