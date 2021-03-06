# Dayvson Silva
# 06/10/2021
from math import pi, cos, sin, sqrt, atan, tanh
import matplotlib.pyplot as plt
import numpy as np

########################################################################################################################
# Dados simulação
tsim = 50  # Tempo da simulação em segundos
Tc = 0.1  # Tempo de amostragem
ciclos = int(tsim / Tc)  # Ciclos nescessarios para completar simulação em x segundos
print('ciclos nescessarios para a simulação: ', ciclos)

# Definição de variaveis
x = np.zeros(ciclos, dtype=float)
y = np.zeros(ciclos, dtype=float)
z = np.zeros(ciclos, dtype=float)
psi = np.zeros(ciclos, dtype=float)

xf = np.zeros(ciclos, dtype=float)
yf = np.zeros(ciclos, dtype=float)
zf = np.zeros(ciclos, dtype=float)
psif = np.zeros(ciclos, dtype=float)

x1 = np.zeros(ciclos, dtype=float)
y1 = np.zeros(ciclos, dtype=float)
z1 = np.zeros(ciclos, dtype=float)
psi1 = np.zeros(ciclos, dtype=float)

x2 = np.zeros(ciclos, dtype=float)
y2 = np.zeros(ciclos, dtype=float)
z2 = np.zeros(ciclos, dtype=float)
psi2 = np.zeros(ciclos, dtype=float)

rof = np.zeros(ciclos, dtype=float)
alfaf = np.zeros(ciclos, dtype=float)
betaf = np.zeros(ciclos, dtype=float)

xtil = np.zeros(ciclos, dtype=float)
xtilponto = np.zeros(ciclos, dtype=float)

ytil = np.zeros(ciclos, dtype=float)
ytilponto = np.zeros(ciclos, dtype=float)

ztil = np.zeros(ciclos, dtype=float)
ztilponto = np.zeros(ciclos, dtype=float)

rotil = np.zeros(ciclos, dtype=float)
alfatil = np.zeros(ciclos, dtype=float)
betatil = np.zeros(ciclos, dtype=float)

Uvx = np.zeros(ciclos, dtype=float)
Uvy = np.zeros(ciclos, dtype=float)
Uvz = np.zeros(ciclos, dtype=float)
omega = np.zeros(ciclos, dtype=float)

xponto1 = np.zeros(ciclos, dtype=float)
yponto1 = np.zeros(ciclos, dtype=float)
zponto1 = np.zeros(ciclos, dtype=float)
psiponto1 = np.zeros(ciclos, dtype=float)

xponto2 = np.zeros(ciclos, dtype=float)
yponto2 = np.zeros(ciclos, dtype=float)
zponto2 = np.zeros(ciclos, dtype=float)
psiponto2 = np.zeros(ciclos, dtype=float)

xdoispontos1 = np.zeros(ciclos, dtype=float)
ydoispontos1 = np.zeros(ciclos, dtype=float)
zdoispontos1 = np.zeros(ciclos, dtype=float)
psidoispontos1 = np.zeros(ciclos, dtype=float)

xdoispontos2 = np.zeros(ciclos, dtype=float)
ydoispontos2 = np.zeros(ciclos, dtype=float)
zdoispontos2 = np.zeros(ciclos, dtype=float)
psidoispontos2 = np.zeros(ciclos, dtype=float)

xdes = np.zeros(ciclos, dtype=float)
ydes = np.zeros(ciclos, dtype=float)
zdes = np.zeros(ciclos, dtype=float)

rofdes = np.zeros(ciclos, dtype=float)
alfafdes = np.zeros(ciclos, dtype=float)
betafdes = np.zeros(ciclos, dtype=float)

rodes = np.zeros(ciclos, dtype=float)
alfades = np.zeros(ciclos, dtype=float)
betades = np.zeros(ciclos, dtype=float)

xdesponto = np.zeros(ciclos, dtype=float)
ydesponto = np.zeros(ciclos, dtype=float)
zdesponto = np.zeros(ciclos, dtype=float)

rodesponto = np.zeros(ciclos, dtype=float)
alfadesponto = np.zeros(ciclos, dtype=float)
betadesponto = np.zeros(ciclos, dtype=float)

psid = np.zeros(ciclos, dtype=float)
psitil = np.zeros(ciclos, dtype=float)
Ucref = np.zeros(ciclos, dtype=float)
Vcref = np.zeros(ciclos, dtype=float)
Wcref = np.zeros(ciclos, dtype=float)
erro = np.zeros(ciclos, dtype=float)
der_psi = np.zeros(ciclos, dtype=float)

vxref1 = np.zeros(ciclos, dtype=float)
vyref1 = np.zeros(ciclos, dtype=float)
vzref1 = np.zeros(ciclos, dtype=float)

vpsiref1 = np.zeros(ciclos, dtype=float)

vxref2 = np.zeros(ciclos, dtype=float)
vyref2 = np.zeros(ciclos, dtype=float)
vzref2 = np.zeros(ciclos, dtype=float)
vpsiref2 = np.zeros(ciclos, dtype=float)

Ucrefd = np.zeros(ciclos, dtype=float)
Wcrefd = np.zeros(ciclos, dtype=float)
Vcrefd = np.zeros(ciclos, dtype=float)

qdes = np.zeros((ciclos, 6))
# qpontodes = np.zeros((ciclos, 6))
# qtil = np.zeros((ciclos, 6))
q = np.zeros((ciclos, 6))
# qpontoref = np.zeros((ciclos, 6))

########################################################################################################################
# Camada de planejamento
# Inputs
# Outputs qdes, qpontodes
# Configuração da simulação
# 1 - Derivada com diff
# 2 - Derivada manual
simulacao = 2
if simulacao == 1:
    for j in range(0, ciclos, 1):
        xdes[j] = 3 + 5 * cos(3 * j * Tc)
        ydes[j] = 5 + 5 * sin(3 * j * Tc)
        zdes[j] = 20
        rodes[j] = 5
        alfades[j] = 0
        betades[j] = 0

    # Derivada das trajetórias de interesse
    for j in range(0, ciclos, 1):
        xdesponto[j] = np.diff([xdes[j - 1], xdes[j]], n=1) / Tc
        ydesponto[j] = np.diff([ydes[j - 1], ydes[j]], n=1) / Tc
        zdesponto[j] = 0
        rodesponto[j] = 0
        alfadesponto[j] = 0
        betadesponto[j] = 0

if simulacao == 2:
    for j in range(0, ciclos, 1):
        xdes[j] = 3 + 5 * cos(3 * j * Tc)
        ydes[j] = 5 + 5 * sin(3 * j * Tc)
        zdes[j] = 20
        rodes[j] = 5
        alfades[j] = 0
        betades[j] = 0
    # Derivada das trajetórias de interesse
    for j in range(0, ciclos, 1):
        xdesponto[j] = - 15  * sin(3 * j * Tc) # * (3 * Tc)
        ydesponto[j] = 15  * cos(3 * j * Tc) #* (3 * Tc)
        zdesponto[j] = 0
        rodesponto[j] = 0
        alfadesponto[j] = 0
        betadesponto[j] = 0

########################################################################################################################
#Dados dos drones
k1 = 0.8417
k2 = 0.18227
k3 = 0.8354
k4 = 0.17095
k5 = 3.966
k6 = 4.001
k7 = 9.8524
k8 = 4.7295

# Dados do robô no ponto inicial
# Posição inicial do VANT 1
x1[1] = 0
y1[1] = 0
z1[1] = 0.75
psi1[1] = 0
# Posição inicial do VANT 2
x2[1] = -2
y2[1] = 1
z2[1] = 0.75
psi2[1] = 0

# # f(x)
# # Inputs X
# # Outputs q(xf,yf,zf,rof,alfaf,betaf)
xf[1] = x1[1]
yf[1] = y1[1]
zf[1] = z1[1]
rof[1] = sqrt((x2[1] - x1[1]) ** 2 + (y2[1] - y1[1]) ** 2 + (z2[1] - z1[1]) ** 2)
alfaf[1] = atan((z2[1] - z1[1]) / (sqrt((x2[1] - x1[1]) ** 2 + (y2[1] - y1[1]) ** 2)))
betaf[1] = atan((y2[1] - y1[1]) / (x2[1] - x1[1]))

# loop de controle
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=30, azim=-140)

for k in range(1, ciclos, 1):
    print('k', k)

    ####################################################################################################################
    # f(x)
    # Inputs X
    # Outputs q(xf,yf,zf,rof,alfaf,betaf)
    xf[k] = x1[k]
    yf[k] = y1[k]
    zf[k] = z1[k]
    rof[k] = sqrt((x2[k] - x1[k]) ** 2 + (y2[k] - y1[k]) ** 2 + (z2[k] - z1[k]) ** 2)
    alfaf[k] = atan((z2[k] - z1[k]) / (sqrt((x2[k] - x1[k]) ** 2 + (y2[k] - y1[k]) ** 2)))
    betaf[k] = atan((y2[k] - y1[k]) / (x2[k] - x1[k]))
    q = np.array([xf[k], yf[k], zf[k], rof[k], alfaf[k], betaf[k]])
    ####################################################################################################################
    # Camada de controle
    # Inputs qdes(xdes,ydes,zdes), qpontodes(xpontodes,ypontodes,zpontodes)
    # Outputs qpontoref(xref, yref, zref)

    # Calculando qtil : qtil[k] = qdes[k] - q[k]
    xtil[k] = (xdes[k] - xf[k])
    ytil[k] = (ydes[k] - yf[k])
    ztil[k] = (zdes[k] - zf[k])
    rotil[k] = (rodes[k] - rof[k])
    alfatil[k] = (alfades[k] - alfaf[k])
    betatil[k] = (betades[k] - betaf[k])

    qtil = np.array([[xtil[k]],
                     [ytil[k]],
                     [ztil[k]],
                     [rotil[k]],
                     [alfatil[k]],
                     [betatil[k]]])  # , dtype='object'
    # Parametros para proposta controlador 1
    # 1 - Modelo cinematico simpllificado
    # 2 - Modelo completo( Cinematico + dinamico)
    modelo = 1
    if modelo == 1:
        L1 = np.diag([0.5, 0.5, 1, 0.5, 0.5, 0.5])# Kp
        L2 = np.diag([1, 1, 1, 1, 1, 1])   # kd
    if modelo == 2:
        L1 = np.diag([0.5, 0.5, 1, 0.5, 0.5, 0.5])# Kp
        L2 = np.diag([1, 1, 1, 1, 1, 1])   # kd

    parcial1 = np.dot(L2, qtil)
    vector = np.vectorize(float)
    parcial1 = vector(parcial1)
    parcial1[0] = tanh(parcial1[0])
    parcial1[1] = tanh(parcial1[1])
    parcial1[2] = tanh(parcial1[2])
    parcial1[3] = tanh(parcial1[3])
    parcial1[4] = tanh(parcial1[4])
    parcial1[5] = tanh(parcial1[5])

    qpontodes = np.array([[xdesponto[k]],
                          [ydesponto[k]],
                          [zdesponto[k]],
                          [rodesponto[k]],
                          [alfadesponto[k]],
                          [betadesponto[k]]])

    # vmax = np.array([[2],[2],[4],[1],[1],[1]])

    qpontoref = qpontodes + np.dot(L1, parcial1) #* vmax

    ####################################################################################################################
    # J^-1(q)
    # Inputs qpontoref(xref, yref, zref), q(xf,yf,zf,rof,alfaf,betaf)
    # Outputs xpontoref

    Jinvq = np.array([[1, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0],
                      [1, 0, 0, np.dot(-cos(alfaf[k]), cos(betaf[k])), np.dot(rof[k], np.dot(sin(alfaf[k]), cos(betaf[k]))), np.dot(rof[k], np.dot(cos(alfaf[k]), sin(betaf[k])))],
                      [0, 1, 0, np.dot(-cos(alfaf[k]), sin(betaf[k])), np.dot(rof[k], np.dot(sin(alfaf[k]), sin(betaf[k]))), np.dot(-rof[k], np.dot(cos(alfaf[k]), cos(betaf[k])))],
                      [0, 0, 1,                        sin(alfaf[k]),                         np.dot(rof[k], cos(alfaf[k])), 0]])


    jxqpontoref = np.dot(Jinvq, qpontoref)

    xpontoref = np.array([[jxqpontoref[0]],
                          [jxqpontoref[1]],
                          [jxqpontoref[2]],
                          [0],
                          [jxqpontoref[3]],
                          [jxqpontoref[4]],
                          [jxqpontoref[5]],
                          [0]])  # , dtype='object'
    ####################################################################################################################
    # K^-1
    # Inputs xpontoref
    # Outputs vref

    kinv = np.array([[cos(psi1[k]), sin(psi1[k]), 0, 0, 0, 0, 0, 0],
                     [-sin(psi1[k]), cos(psi1[k]), 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, cos(psi2[k]), sin(psi2[k]), 0, 0],
                     [0, 0, 0, 0, -sin(psi2[k]), cos(psi2[k]), 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1]])

    Vref = np.dot(kinv, xpontoref)

    ####################################################################################################################

    vxref1[k] = Vref[0]
    vyref1[k] = Vref[1]
    vzref1[k] = Vref[2]
    vpsiref1[k] = Vref[3]

    vxref2[k] = Vref[4]
    vyref2[k] = Vref[5]
    vzref2[k] = Vref[6]
    vpsiref2[k] = Vref[7]

    ####################################################################################################################
    # Tipo de modelo do drone
    # 1 - Modelo cinematico simpllificado
    # 2 - Modelo completo( Cinematico + dinamico)
    # modelo = 1

    # 1 - Modelo cinematico simpllificado
    if modelo == 1:
        ####################################################################################################################
        # Drone 1
        # inputs vxref, vyref1, vzref1, vpsi1
        # outputs x, y, z, psi

        # Calcular Xr, Yr e Psir (Ponto de controle) XPONTO
        mie1 = np.array([[vxref1[k]],
                         [vyref1[k]],
                         [vzref1[k]],
                         [vpsiref1[k]]])

        Ae1 = np.array([[cos(psi1[k]), -sin(psi1[k]), 0, 0],
                        [sin(psi1[k]), cos(psi1[k]), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

        px1 = np.dot(Ae1, mie1)

        xponto1[k] = px1[0] # Saida xponto
        yponto1[k] = px1[1] # Saida yponto
        zponto1[k] = px1[2] # Saida yponto
        psiponto1[k] = px1[3]  # Saida psip

        if k < ciclos - 1:
            x1[k + 1] = Tc * xponto1[k] + x1[k]  # x deve ser x
            y1[k + 1] = Tc * yponto1[k] + y1[k]
            z1[k + 1] = Tc * zponto1[k] + z1[k]
            psi1[k + 1] = Tc * psiponto1[k] + psi1[k]  # Saida p

        ####################################################################################################################
        # Cinematica do Drone 2
        # inputs vxref, vyref, vzref, vpsi
        # outputs x, y, z, psi
        # Calcular Xr, Yr e Psir (Ponto de controle)
        mie2 = np.array([[vxref2[k]],
                         [vyref2[k]],
                         [vzref2[k]],
                         [vpsiref2[k]]])

        Ae2 = np.array([[cos(psi2[k]), -sin(psi2[k]), 0, 0],
                        [sin(psi2[k]), cos(psi2[k]), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

        px2 = np.dot(Ae2, mie2)

        xponto2[k] = px2[0]  # Saida xponto
        yponto2[k] = px2[1]  # Saida yponto
        zponto2[k] = px2[2]  # Saida yponto
        psiponto2[k] = px2[3]  # Saida psip

        if k < ciclos - 1:
            x2[k + 1] = Tc * xponto2[k] + x2[k]  # x deve ser x
            y2[k + 1] = Tc * yponto2[k] + y2[k]
            z2[k + 1] = Tc * zponto2[k] + z2[k]
            psi2[k + 1] = Tc * psiponto2[k] + psi2[k]  # Saida p
    ####################################################################################################################
    # Modelo completo( Cinematico + dinamico)
    if modelo == 2:
        ku = np.diag([k1, k3, k5, k7])
        kv = np.diag([k2, k4, k6, k8])
        ####################################################################################################################
        # Drone 1
        # inputs Vxref(vxref1, vyref1, vzref1, vpsi1)
        # outputs x, y, z, psi

        # Calcular Xr, Yr e Psir (Ponto de controle) XPONTO
        #                uvx        uvy        uzponto    upsiponto
        mie1 = np.array([[vxref1[k]],
                         [vyref1[k]],
                         [vzref1[k]],
                         [vpsiref1[k]]])

        Ae1 = np.array([[cos(psi1[k]), -sin(psi1[k]), 0, 0],
                        [sin(psi1[k]), cos(psi1[k]), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

        px1 = np.dot(Ae1, mie1)

        xponto1[k] = px1[0] # * 1.6  # Saida xponto Velocidade do VANT
        yponto1[k] = px1[1] # * 1.1 # Saida yponto
        zponto1[k] = px1[2] # * 0.25 # Saida yponto
        psiponto1[k] = px1[3]  # Saida psip

        Xponto1 = np.array([[xponto1[k]],
                            [yponto1[k]],
                            [zponto1[k]],
                            [psiponto1[k]]])

        # Calcular Xdoispontos
        U1 = mie1

        Xdoispontos1 = np.dot(ku, U1) - np.dot(kv, Xponto1)

        xdoispontos1[k] = Xdoispontos1[0]  # Saida xponto
        ydoispontos1[k] = Xdoispontos1[1]  # Saida yponto
        zdoispontos1[k] = Xdoispontos1[2]  # Saida yponto
        psidoispontos1[k] = Xdoispontos1[3]  # Saida psip

        if k < ciclos - 1:
            x1[k + 1] = Tc * xdoispontos1[k] + x1[k]  # x deve ser x
            y1[k + 1] = Tc * ydoispontos1[k] + y1[k]
            z1[k + 1] = Tc * zponto1[k] + z1[k]
            psi1[k + 1] = Tc * psiponto1[k] + psi1[k]  # Saida p

        ####################################################################################################################
        # Drone 2
        # inputs Vxref(vxref1, vyref1, vzref1, vpsi1)
        # outputs x, y, z, psi

        # Drone 2
        # inputs vxref, vyref1, vzref1, vpsi1
        # outputs x, y, z, psi

        # Calcular Xr, Yr e Psir (Ponto de controle) XPONTO
        #                uvx        uvy        uzponto    upsiponto
        mie2 = np.array([[vxref2[k]],
                         [vyref2[k]],
                         [vzref2[k]],
                         [vpsiref2[k]]])

        Ae2 = np.array([[cos(psi2[k]), -sin(psi2[k]), 0, 0],
                        [sin(psi2[k]), cos(psi2[k]), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

        px2 = np.dot(Ae2, mie2)

        xponto2[k] = px2[0] #* 1.6 # Saida xponto Velocidade do VANT
        yponto2[k] = px2[1] #* 1.1 # Saida yponto
        zponto2[k] = px2[2] # Saida yponto
        psiponto2[k] = px2[3]  # * 0.5 # Saida psip

        Xponto2 = np.array([[xponto2[k]],
                            [yponto2[k]],
                            [zponto2[k]],
                            [psiponto2[k]]])

        # Calcular Xdoispontos
        U2 = mie2

        Xdoispontos2 = np.dot(ku, U2) - np.dot(kv, Xponto2)

        xdoispontos2[k] = Xdoispontos2[0]  # Saida xponto
        ydoispontos2[k] = Xdoispontos2[1]  # Saida yponto
        zdoispontos2[k] = Xdoispontos2[2]  # Saida yponto
        psidoispontos2[k] = Xdoispontos2[3]  # Saida psip

        if k < ciclos - 1:
            x2[k + 1] = Tc * xdoispontos2[k] + x2[k]  # x deve ser x
            y2[k + 1] = Tc * ydoispontos2[k] + y2[k]
            z2[k + 1] = Tc * zponto2[k] + z2[k]
            psi2[k + 1] = Tc * psiponto2[k] + psi2[k]  # Saida p

    ####################################################################################################################
    # f(x)
    # Inputs X
    # Outputs q(xf,yf,zf,rof,alfaf,betaf)
    # if k < ciclos - 1:
    #     xf[k + 1] = x1[k]
    #     yf[k + 1] = y1[k]
    #     zf[k + 1] = z1[k]
    #     rof[k + 1] = sqrt((x2[k] - x1[k]) ** 2 + (y2[k] - y1[k]) ** 2 + (z2[k] - z1[k]) ** 2)
    #     alfaf[k + 1] = atan((z2[k] - z1[k]) / (sqrt((x2[k] - x1[k]) ** 2 + (y2[k] - y1[k]) ** 2)))
    #     betaf[k + 1] = atan((y2[k] - y1[k]) / (x2[k] - x1[k]))
    #     q = np.array([xf[k + 1], yf[k + 1], zf[k + 1], rof[k + 1], alfaf[k - 1], betaf[k - 1]])
    ####################################################################################################################

    # Preparação dos dados para plotar
    erro[k] = sqrt((xtil[k]) ** 2 + (ytil[k]) ** 2 + (ztil[k]) ** 2)
    plt.axis('auto')
    ####################################################################################################################

    # Plot saida
    plt.cla()
    # ax.scatter(xf[0:k], yf[0:k], zf[0:k])

    ax.plot(xdes[1:k], ydes[1:k], zdes[1:k], "-r", label="Trajetoria desejada")
    plt.plot(xdes[k], ydes[k], zdes[k], "xr")

    ax.plot(x1[1:k], y1[1:k], z1[1:k], "-g", label="Trajetoria Vant 1")
    plt.plot(x1[k], y1[k], z1[k], "xg")

    ax.plot(x2[1:k], y2[1:k], z2[1:k], "-b", label="Trajetoria Vant 2")
    plt.plot(x2[k], y2[k], z2[k], "xb")

    # ax.set_aspect('equal')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.legend(loc='best')

    # ax.view_init(elev=-75,azim=-90)
    plt.pause(0.00001)
###################################


# plt.show()


# Plota dadas

plt.show(block=False)
plt.savefig('1a' + 'trajetoria3d.png')

# Teste 3d

# ax.set_aspect('equal')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

titulo = 'Vistas 3D projetadas'
fig2, axs = plt.subplots(1, 3, num=titulo, sharey=True, figsize=(15, 5))

axs[0].set_title('Trajetoria vista xz')
axs[0].axis('equal')
axs[0].set(xlabel='x[m]', ylabel='z[m]')
axs[0].plot(xdes[1:k], zdes[1:k], "-r", label="Trajetoria desejada")
axs[0].plot(x1[1:k], z1[1:k], "-g", label="Trajetoria Vant 1")
axs[0].plot(x2[1:k], z2[1:k], "-b", label="Trajetoria Vant 2")
axs[0].legend(loc='best')
axs[0].grid()

axs[1].set_title('Trajetoria vista yz')
axs[1].axis('equal')
axs[1].set(xlabel='y[m]', ylabel='z[m]')

axs[1].plot(ydes[1:k], zdes[1:k], "-r", label="Trajetoria desejada")
axs[1].plot(y1[1:k], z1[1:k], "-g", label="Trajetoria Vant 1")
axs[1].plot(y2[1:k], z2[1:k], "-b", label="Trajetoria Vant 2")
axs[1].legend(loc='best')
axs[1].grid()

axs[2].set_title('Trajetoria vista xy')
axs[2].axis('equal')
axs[2].set(xlabel='x[m]', ylabel='y[m]')

axs[2].plot(xdes[1:k], ydes[1:k], "-r", label="Trajetoria desejada")
axs[2].plot(x1[1:k], y1[1:k], "-g", label="Trajetoria Vant 1")
axs[2].plot(x2[1:k], y2[1:k], "-b", label="Trajetoria Vant 2")
axs[2].legend(loc='best')
axs[2].grid()

plt.tight_layout()

plt.savefig('1e' + titulo + '.png')
plt.show(block=False)

# Plota dados

# Trajetoria desejada - x, y , z
# Trajetoria executada - x, y, z
titulo = 'Trajetoria desejada do robô no tempo'
fig2, axs = plt.subplots(3, 1, num=titulo, figsize=(8, 6))
axs[0].plot(xdes, label="Trajetoria desejada - Eixo x")
axs[0].plot(x1, label="Trajetoria executada - Eixo x")
axs[0].set_title('Trajetoria eixo x')
axs[0].set(ylabel='[m]')
axs[0].legend(loc='best')
axs[0].grid()

axs[1].plot(ydes, label="Trajetoria desejada - Eixo y")
axs[1].set_title('Trajetoria eixo y')
axs[1].plot(y1, label="Trajetoria executada - Eixo y")
axs[1].set_title('Trajetoria eixo y')
axs[1].set(xlabel='[Ciclos de 100 ms]', ylabel='[m]')
axs[1].legend(loc='best')
axs[1].grid()

axs[2].plot(zdes, label="Trajetoria desejada - Eixo z")
axs[2].set_title('Trajetoria eixo z')
axs[2].plot(z1, label="Trajetoria executada - Eixo z")
axs[2].set_title('Trajetoria eixo z')
axs[2].set(xlabel='[Ciclos de 100 ms]', ylabel='[m]')
axs[2].legend(loc='best')
axs[2].grid()
plt.tight_layout()

plt.savefig('2' + titulo + '.png')

# Velocidade comandada - Ucref, Wcref
# Velocidade real  - U, W
titulo = 'Velocidade do robô no tempo'

fig3, axs = plt.subplots(3, 1, num=titulo, figsize=(8, 6))
axs[0].plot(vxref1, label="Veloc. linear comandada")
axs[0].plot(vxref1, label="Veloc. linear x real - Vant1")
axs[0].plot(vxref2, label="Veloc. linear x real - Vant2")
axs[0].set_title('Velocidade linear comandada x real ')
axs[0].set(ylabel='[m/s]')
axs[0].legend(loc='best')
axs[0].grid()

axs[1].plot(vyref1, label="Veloc. linear comandada")
axs[1].plot(vyref1, label="Veloc. linear y real - Vant1")
axs[1].plot(vyref2, label="Veloc. linear y real - Vant2")
axs[1].set_title('Velocidade linear comandada x real')
axs[1].set(xlabel='[Ciclos de 100 ms]', ylabel='[m/s]')
axs[1].legend(loc='best')
axs[1].grid()

axs[2].plot(vzref1, label="Veloc. linear comandada")
axs[2].plot(vzref1, label="Veloc. linear z real - Vant1")
axs[2].plot(vzref2, label="Veloc. linear z real - Vant2")
axs[2].set_title('Velocidade linear comandada x real')
axs[2].set(xlabel='[Ciclos de 100 ms]', ylabel='[m/s]')
axs[2].legend(loc='best')
axs[2].grid()


plt.tight_layout()
plt.savefig('3' + titulo + '.png')

# Pose do robô - x, y, psi
titulo = 'Posição do robô no tempo'
fig4, axs = plt.subplots(3, 1, num=titulo, figsize=(8, 6))
axs[0].plot(x1, label="posição x do Vant1")
axs[0].plot(x2, label="posição x do Vant2")
axs[0].set_title('posição x do robô no tempo')
axs[0].set(ylabel='x[m]')
axs[0].legend(loc='best')
axs[0].grid()

axs[1].plot(y1, label="posição y do Vant1")
axs[1].plot(y2, label="posição y do Vant2")
axs[1].set_title('posição y do robô no tempo')
axs[1].set(ylabel='y[m]')
axs[1].legend(loc='best')
axs[1].grid()

axs[2].plot(z1, label="posição z do Vant1")
axs[2].plot(z2, label="posição z do Vant2")
axs[2].set_title('posição z do robô no tempo')
axs[2].set(ylabel='z[m]')
axs[2].legend(loc='best')
axs[2].grid()

# axs[3].plot(psi1, label="Orientação do Vant1")
# axs[3].plot(psi2, label="Orientação do Vant2")
# axs[3].set_title('Angulo psi do robô no tempo')
# axs[3].set(xlabel='[Ciclos de 100 ms]', ylabel='radianos')
# axs[3].grid()
# axs[3].legend(loc='best')
plt.tight_layout()
plt.savefig('4' + titulo + '.png')

# Erro de trajetoria - erro
titulo = 'Erro de trajetória'
plt.figure(titulo, figsize=(8, 6))
plt.plot(erro, label="Erro de trajetória")
plt.title('Erro de trajetória')
plt.xlabel('[Ciclos de 100 ms]')
plt.ylabel('[m]')
plt.legend(loc='best')
plt.grid(True)
plt.savefig('5' + titulo + '.png')

plt.show()
