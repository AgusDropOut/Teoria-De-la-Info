#En un juego de preguntas y respuestas se colocan 6 tarjetas boca abajo (4 con preguntas simples y 2 con preguntas difíciles). En cada turno, se elige una tarjeta al azar, se devuelve y luego de mezcladas se elige otra. Obtenga la probabilidad de que:
#ambas preguntas sean difíciles
#sólo una de las preguntas sea difícil 
#la segunda pregunta sea difícil, dado que la primera fue simple  <--

import random

e = 0.01

# 0 son simples 
# 1 son dificiles
def agarrar_segunda_carta(c1):
    probaacum=[3/5,1], [4/5,1]
    r= random.random()
    for i in range(2):
        if r < probaacum[c1] [i]:
            return i 
        

def agarrar_primera_carta():
    probaacum=[4/6,1] 
    r= random.random()
    for i in range(2):
        if r < probaacum[i]:
            return i 
        
def converge(prob_ant, prob_act):
    if abs(prob_ant - prob_act) < e :
        return True
    return False


def Calcular_Prob_Dos_preguntas_dif ():

    exitos = 0
    N = 0
    prob_ant=-1
    prob_act = 0

    while(not converge(prob_ant, prob_act) or N < 1000):
        pregunta1 = agarrar_primera_carta()
        pregunta2 = agarrar_segunda_carta(pregunta1)
        if pregunta1 == 1 and pregunta2 == 1:
            exitos+=1
        N+=1
        prob_ant = prob_act
        prob_act = exitos/N
    return prob_act

print (Calcular_Prob_Dos_preguntas_dif())
