#4) Una fuente puede emitir 3 símbolos y la elección del próximo símbolo a partir del emitido antes está dada por el siguiente grafo de transición: 
#a) Plantee la matriz que caracteriza a la fuente (cuando 
#corresponda, suponga equiprobabilidad)
#b) Determine la distribución de probabilidades estacionarias 
#c) Para cada símbolo, calcule la probabilidad que se emitan 2 símbolos símbolos consecutivos iguales (en estado estacionario)


import random

e = 0.01


def primer_simb():
    probaacum=[1/3,2/3,1]
    r= random.random()
    for i in range(3):
        if r < probaacum[i]:
            return i 
        
def sig_dado_anterior(s_ant):
    matriz_prob_acum= [1/2,1/3,0],[1,2/3,1],[0,1,0]
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