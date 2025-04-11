#3) Considere una fuente markoviana que emite símbolos {0,1,2} según la siguiente matriz de pasaje:
#a) Considerando que el símbolo emitido inicialmente es 0, obtenga la distribución de probabilidades de emisión en los pasos 1, 2 y 3




import random

e = 0.01

def primer_simb():
    probaacum=[1/3,2/3,1]
    r= random.random()
    for i in range(3):
        if r < probaacum[i]:
            return i 
        
def sig_dado_anterior(s_ant):
    matriz_prob_acum= [1/4,3/4,0],[3/4,1,1/2],[1,0,1]
    r= random.random()
    for i in range(3):
        if r < matriz_prob_acum[i][s_ant]:
            return i 
        
def converge(prob_ant, prob_act):
    for i in range(0,3):
        if abs(prob_ant[i] - prob_act[i]) < e :
            return True
    return False


def calcular_vector_estado_partiendo_de_simb_inic(t,s0):

    emisiones= [0] * 3
    v_estacionario= [0] * 3
    v_estacionario_ant= [-1] * 3
    cant_simbolos = 0
    while(not converge(v_estacionario_ant, v_estacionario) or cant_simbolos < 10000):
        s=sig_dado_anterior(s0)

        for i in range(1,t): #hacemos como un t-1 porque la primera iteracion se hace arriba(sabiendo que el primero es 0 )
            s = sig_dado_anterior(s)
        v_estacionario_ant = v_estacionario
        emisiones[s]+=1
        cant_simbolos+=1
        for i in 0,1,2:
            v_estacionario[i] = emisiones[i] / cant_simbolos
    return v_estacionario
print("Vector de estado t=1")
print (calcular_vector_estado_partiendo_de_simb_inic(1,0))
print("Vector de estado t=2")
print (calcular_vector_estado_partiendo_de_simb_inic(2,0))
print("Vector de estado t=3")
print (calcular_vector_estado_partiendo_de_simb_inic(3,0))