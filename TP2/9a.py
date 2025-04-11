#9) Una señal de sonido periódica varía en el tiempo y puede tomar valores discretos en el rango [–127, 128]. Proponga el pseudocódigo de un algoritmo que permita calcular, a partir de los datos generados por la señal (asumir que están disponibles en un archivo):
#a)  la probabilidad de primera recurrencia, en n pasos, para el valor 0 de señal 
#b)  la media de recurrencia para los diferentes valores de señal





import random


file = open("TP3/Practico 2_Datos-Ej9.txt", mode="r")
lines_list = file.readlines()
T_min = 2000
e = 0.0001

def converge(prob_ant, prob_act):
    for i in range(0,300):
        if abs(prob_ant[i] - prob_act[i]) < e :
            return True
    return False

def obtener_senial(i):
    line = lines_list[i]
    return int(lines_list[i].strip())

def prob_recurrencia (simbolo):
    i = 1
    retornos = [0] * 300
    fi_ant = [-1] * 300
    fi = [0] * 300
    ult_ret = 0
    t_actual = 0
    total_retornos = 0
    while (not converge(fi,fi_ant) or (t_actual < T_min)) and (i < len(lines_list) ):
        s=obtener_senial(i)
        t_actual+=1
        if (s == simbolo):
            n = t_actual - ult_ret
            retornos[n]+=1
            total_retornos+=1
            fi_ant = fi
            for j in range(0,300):
                fi[j] = retornos[j]/total_retornos
            ult_ret = t_actual
        i+=1
    file.close()
    return fi  


print(prob_recurrencia(0))
