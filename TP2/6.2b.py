#2) Se desea transmitir diariamente el estado del tiempo en cierta región, en la que se pueden presentar días soleados, nublados o lluviosos. Estadísticamente, se conoce que nunca se han presentado dos días soleados seguidos. Si un día está soleado, el siguiente puede estar nublado o lluvioso con igual probabilidad. Si el día se presenta con lluvia o nublado, entonces hay una probabilidad de ½ de que el siguiente día tenga las mismas características; y si cambia, entonces es igualmente probable que sea de cualquiera de las otras posibilidades.
#a)  Encuentre el grafo y la matriz de transición de transición de estados para esta fuente markoviana
#b) Determine la proporción de días que serán soleados, nublados y lluviosos en estado estacionario



import random

e = 0.01
#sol = 0
#nub = 1
#lluv = 2

def primer_simb():
    probaacum=[1/3,2/3,1]
    r= random.random()
    for i in range(3):
        if r < probaacum[i]:
            return i 
        
def sig_dado_anterior(s_ant):
    matriz_prob_acum= [0,1/4,1/4],[1/2,3/4,1/2],[1,1,1]
    r= random.random()
    for i in range(3):
        if r < matriz_prob_acum[i][s_ant]:
            return i 
        
def converge(prob_ant, prob_act):
    for i in range(0,3):
        if abs(prob_ant[i] - prob_act[i]) < e :
            return True
    return False


def calcular_vector_estacionario():

    emisiones= [0] * 3
    v_estacionario= [0] * 3
    v_estacionario_ant= [-1] * 3
    cant_simbolos = 0
    s = primer_simb()

    while(not converge(v_estacionario_ant, v_estacionario) or cant_simbolos < 10000):
        s = sig_dado_anterior(s)
        emisiones[s]+=1
        cant_simbolos+=1
        v_estacionario_ant = v_estacionario
        for i in 0,1,2:
            v_estacionario[i] = emisiones[i] / cant_simbolos
    return v_estacionario

print (calcular_vector_estacionario())