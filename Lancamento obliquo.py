import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

gravidade = 10
quique_porcem = 70

def calculo(v_saida,angulo):

    v_x = abs(v_saida*(math.cos(angulo)))            #80
    v_y = abs(v_saida*(math.sin(angulo)))            #60

    tempo = round((v_y//gravidade)*2,2)
    dist= round(v_x * tempo,2)
    h_max = round((v_y*(tempo/2))+0.5*-10*((tempo/2)**2),2) ## D = Vo.T + 1/2 . a.t**2
    return (dist,h_max,tempo)
    #exibicao(tempo,dist,h_max)

def exibicao(tempo,dist,h_max):
    correcao = dist/9 ### corrige o bug do smooth
    x = np.array([0, ((dist/2)/2)-correcao, dist/2, ((dist/2)/2+dist/2)+correcao, dist])
    y = np.array([0,h_max/2,h_max,h_max/2,0])

    x_smooth = np.linspace(x.min(),x.max(),50)
    y_smooth = spline(x,y, x_smooth)

    plt.plot(x_smooth,y_smooth,'--')

    ###linha do chao
    chao_x, chao_y = [-50,950], [0,0]
    plt.plot(chao_x,chao_y)

    ##### cota
    dist_cota1_x, dist_cota1_y = [0,0], [-h_max*0.10,-h_max*0.2]
    dist_cota2_x, dist_cota2_y = [dist,dist], [-h_max*0.10,-h_max*0.2]
    dist_cota3_x, dist_cota3_y = [0,dist], [-h_max*0.15,-h_max*0.15]
    plt.plot(dist_cota1_x, dist_cota1_y,'red',dist_cota2_x, dist_cota2_y,'red',dist_cota3_x, dist_cota3_y,'red')

    ### setar o limite da exibicao dos eixos
    axes = plt.gca()
    axes.set_xlim([-dist*0.1, dist+dist*0.1])
    axes.set_ylim([-h_max*0.3, h_max+h_max*0.5])

    ### Textos
    plt.text(0, h_max+h_max*0.35, 'Distancia: {}m'.format(dist), style='italic',
            bbox={'facecolor':'red', 'alpha':0.2, 'pad':10})
    plt.text(0, h_max+h_max*0.2, 'Altura Maxima: {}m'.format(h_max), style='italic',
            bbox={'facecolor':'red', 'alpha':0.2, 'pad':10})
    plt.text(0, h_max+h_max*0.05, 'Tempo: {}s'.format(tempo), style='italic',
            bbox={'facecolor':'red', 'alpha':0.2, 'pad':10})

    ### nome dos eixos
    plt.xlabel('Distancia (m)', fontsize=18)
    plt.ylabel('Altura (m)', fontsize=16)

    ## nome da linha principal
    plt.legend(['Trajetoria'], loc='best')

    ### plotar os pontos
    plt.plot([0,dist/2,dist],[0,h_max,0],'o')

    plt.show()

def run():
    v_saida = float(input('Velocidade de saida: '))  #100
    angulo = float(input('Angulo de saida: '))       #37
    primeiro = calculo(v_saida,angulo)
    tempo_quique = primeiro[2]
    v_retorno_x = abs(v_saida*0.7)       ##### SUBSTITUIR PARA A VARIAVEL CORRETA
    v_retorno_y = abs(((tempo_quique/2)*gravidade)*0.7)
    v_retorno = ((v_retorno_x**2) + (v_retorno_y**2))**0.5 ### teorema de pitagoras para encontrar o 'modulo'
    quique = calculo(v_retorno,angulo)
    print('dist {}, altura {}, tempo {}'.format(primeiro[0],primeiro[1],primeiro[2]))
    print('retorno {} , retorno x {}, retorno y {}'.format(v_retorno,v_retorno_x,v_retorno_y))
    print(quique)

run()

'''http://www3.iesam-pa.edu.br/ojs/index.php/computacao/article/viewFile/530/432  -- REFERENCIA'''
