#A partir de un estudio estadístico en una población se ha determinado que la probabilidad de que una persona posea cierta enfermedad es 0,005. 
# Se ha comprobado además que si una persona posee la enfermedad, la probabilidad de que el examen médico arroje un resultado positivo es del 95%.
#  Por otro lado, si alguien que no posee la enfermedad se somete al examen, la probabilidad de que éste dé resultado negativo es del 96%. 
#a) si alguien obtiene un resultado negativo en el examen, cuál es la probabilidad de que esté sana? 
#b) si alguien obtiene un resultado positivo, ¿cuál es la probabilidad de que realmente esté enferma? <--

import random

e = 0.001

# 1 no esta enfermo 
# 0 esta enfermo
def no_esta_enfermo():
    probaacum=[0.005,1]
    r= random.random()
    for i in range(2):
        if r < probaacum[i]:
            return i 
        
def test_positivo(f1):
    probaacum=[0.05, 0.96], [1,1]
    r= random.random()
    for i in range(2):
        if r < probaacum[i] [f1]:
            return i 
        
def converge(prob_ant, prob_act):
    if abs(prob_ant - prob_act) < e :
        return True
    return False


def Calcular_Prob ():

    exitos = 0
    N = 1
    prob_ant=-1
    prob_act = 0

    while(not converge(prob_ant, prob_act) or N < 1000):
        persona_sana = no_esta_enfermo()
        dio_positivo = test_positivo(persona_sana)
        if dio_positivo == 1:
            if persona_sana == 0 :
                exitos+=1
            N+=1
    
        prob_ant = prob_act
        prob_act = exitos/N
    return prob_act

print (Calcular_Prob())