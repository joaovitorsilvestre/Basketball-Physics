### PYTHON VERSION: 2.7

from sympy import Eq, Symbol, solve
from math import *
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from scipy.misc import imread

h_inicial = 1.5     # 1.5
h_alvo = 5          # 5
dist = 15           # 15
gravidade = 10      # 10

def calcular_vel(h_inicial,h_alvo,dist):
    vo = Symbol('vo') ## velocidade inicial, v0

    # eqn = Eq((1.5 + (vo * (sin(45)) * ((15/(vo*cos(45)))) -5*((15/(vo*cos(45)))**2) )),5) ##ORIGINAL SEM VARIAVEL
    eqn = Eq((h_inicial + (vo * (sin(45)) * ((dist/(vo*cos(45)))) -h_alvo*((dist/(vo*cos(45)))**2) )), h_alvo) #COM VARIAVELh

    return round(((solve(eqn))[1]),1)

def calculo(v_saida,angulo):

    v_x = abs(v_saida*(math.cos(angulo)))            #80
    v_y = abs(v_saida*(math.sin(angulo)))            #60

    tempo = round((v_y//gravidade)*2,2)
    dist= round(v_x * tempo,2)
    h_max = round((v_y*(tempo/2))+0.5*-10*((tempo/2)**2),2) ## D = Vo.T + 1/2 . a.t**2
    return (dist,h_max,tempo)
    #exibicao(dist,h_max,tempo)

def exibicao(dist,h_max,tempo,v_saida):

    x = np.array([0, (dist/2)+h_alvo/2,dist])
    y = np.array([h_inicial,h_max,h_alvo])

    x_smooth = np.linspace(x.min(),x.max(),10)
    y_smooth = spline(x,y, x_smooth)

    ### plotagem
    plt.plot(x_smooth,y_smooth,'--',label='Trajetoria')
    plt.plot(x,y,'-')

    ###linha do chao
    chao_x, chao_y = [-50,dist+dist*0.3], [0,0]
    plt.plot(chao_x,chao_y,color='green',linewidth=5.0)

    ##### cota
    dist_cota1_x, dist_cota1_y = [0,0], [-h_max*0.10,-h_max*0.2]
    dist_cota2_x, dist_cota2_y = [dist,dist], [-h_max*0.10,-h_max*0.2]
    dist_cota3_x, dist_cota3_y = [0,dist], [-h_max*0.15,-h_max*0.15]
    plt.plot(dist_cota1_x, dist_cota1_y,'red',dist_cota2_x, dist_cota2_y,'red',dist_cota3_x, dist_cota3_y,'red')

    ### setar o limite da exibicao dos eixos
    axes = plt.gca()
    axes.set_xlim([-dist*0.1, dist+dist*0.2])
    axes.set_ylim([-h_max*0.3, h_max+h_max])

    ### Textos
    plt.text(0, h_max+h_max*0.8, 'Altura Maxima: {}m'.format(h_max), style='italic',
            bbox={'facecolor':'red', 'alpha':0.2, 'pad':10})
    plt.text(0, h_max+h_max*0.6, 'Tempo: {}s'.format(tempo), style='italic',
            bbox={'facecolor':'red', 'alpha':0.2, 'pad':10})
    plt.text(0, h_max+h_max*0.4, 'Velocidade necessaria: {}m/s'.format(v_saida), style='italic',
            bbox={'facecolor':'red', 'alpha':0.2, 'pad':10})

    ### nome dos eixos
    plt.xlabel('Distancia (m)', fontsize=18)
    plt.ylabel('Altura (m)', fontsize=16)

    #### plotar fundo GAMBIARRA
    plt.plot([dist-dist*0.05,dist+dist*0.05,dist+dist*0.03,dist-dist*0.03,dist-dist*0.05],\
             [h_alvo,h_alvo,h_alvo-h_alvo*0.2,h_alvo-h_alvo*0.2,h_alvo],'black',linewidth=3.0) ### cesta
    plt.plot([dist+dist*0.05,dist+dist*0.05],[h_alvo+h_alvo*0.2,0],'black',linewidth=3.0)

    ### plotar os pontos
    plt.plot([0,(dist/2)+h_alvo/2,dist],[0,h_max,h_alvo],'o')

    ## nome das linhas principais
    plt.legend(loc='best')

    plt.show()

def run(dist):
    v_saida = float(calcular_vel(h_inicial,h_alvo,dist))  #100
    angulo = float(45)       #37
    primeiro = calculo(v_saida,angulo)

    ### retornos
    dist = primeiro[0]
    h_max = primeiro[1]
    tempo = primeiro[2]

    exibicao(dist,h_max,tempo,v_saida)

run(dist)

'''REFERENCIA:
http://www.tutorbrasil.com.br/forum/fisica-i/lancamento-obliquo-t22971.html
http://stackoverflow.com/questions/4449110/python-solve-equation-for-one-variable
'''
