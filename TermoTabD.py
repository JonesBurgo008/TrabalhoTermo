# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
import scipy.interpolate

def TermoTabD(VetPropGasIdEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropGasIdSai, Reg):
    T = VetPropGasIdEnt[0]
    u = VetPropGasIdEnt[1]
    h = VetPropGasIdEnt[2]
    s0 = VetPropGasIdEnt[3]
    vr = VetPropGasIdEnt[4]
    Pr = VetPropGasIdEnt[5]

    #16--------------------------------------------------------------------------
    if T != 0 and (h == 0 and u == 0 and s0 == 0 and vr == 0 and Pr == 0):
        i = np.where(TabArGI[:, 0] >= T)[0][0]
        if i >= 0:
            h = scipy.interpolate.interp1d(TabArGI[:, 0], TabArGI[:, 1])(T)
            Pr = scipy.interpolate.interp1d(TabArGI[:, 0], TabArGI[:, 2])(T)
            u = scipy.interpolate.interp1d(TabArGI[:, 0], TabArGI[:, 3])(T)
            vr = scipy.interpolate.interp1d(TabArGI[:, 0], TabArGI[:, 4])(T)
            s0 = scipy.interpolate.interp1d(TabArGI[:, 0], TabArGI[:, 5])(T)
        elif T < TabArGI[0, 0] or T > TabArGI[-1, 0]:
            print('Valor de temperatura informado está fora do intervalo de consulta!!!!!')
    #17--------------------------------------------------------------------------
    if h != 0 and (T == 0 and u == 0 and s0 == 0 and vr == 0 and Pr == 0):
        i = np.where(TabArGI[:, 1] >= h)[0][0]
        if i >= 0:
            T = scipy.interpolate.interp1d(TabArGI[:, 1], TabArGI[:, 0])(h)
            Pr = scipy.interpolate.interp1d(TabArGI[:, 1], TabArGI[:, 2])(h)
            u = scipy.interpolate.interp1d(TabArGI[:, 1], TabArGI[:, 3])(h)
            vr = scipy.interpolate.interp1d(TabArGI[:, 1], TabArGI[:, 4])(h)
            s0 = scipy.interpolate.interp1d(TabArGI[:, 1], TabArGI[:, 5])(h)
        elif h < TabArGI[0, 1] or h > TabArGI[-1, 1]:
            print('Valor de entalpia informado está fora do intervalo de consulta!!!!!')
    #18--------------------------------------------------------------------------
    if u != 0 and (T == 0 and h == 0 and s0 == 0 and vr == 0 and Pr == 0):
        i = np.where(TabArGI[:, 3] >= u)[0][0]
        if i >= 0:
            T = scipy.interpolate.interp1d(TabArGI[:, 3], TabArGI[:, 0])(u)
            Pr = scipy.interpolate.interp1d(TabArGI[:, 3], TabArGI[:, 2])(u)
            h = scipy.interpolate.interp1d(TabArGI[:, 3], TabArGI[:, 1])(u)
            vr = scipy.interpolate.interp1d(TabArGI[:, 3], TabArGI[:, 4])(u)
            s0 = scipy.interpolate.interp1d(TabArGI[:, 3], TabArGI[:, 5])(u)
        elif u < TabArGI[0, 3] or u > TabArGI[-1, 3]:
            print('Valor de energia interna específica informado está fora do intervalo de consulta!!!!!')
    #19--------------------------------------------------------------------------
    if s0 != 0 and (T == 0 and h == 0 and u == 0 and vr == 0 and Pr == 0):
        i = np.where(TabArGI[:, 5] >= s0)[0][0]
        if i >= 0:
            T = scipy.interpolate.interp1d(TabArGI[:, 5], TabArGI[:, 0])(s0)
            Pr = scipy.interpolate.interp1d(TabArGI[:, 5], TabArGI[:, 2])(s0)
            h = scipy.interpolate.interp1d(TabArGI[:, 5], TabArGI[:, 1])(s0)
            vr = scipy.interpolate.interp1d(TabArGI[:, 5], TabArGI[:, 4])(s0)
            u = scipy.interpolate.interp1d(TabArGI[:, 5], TabArGI[:, 3])(s0)
        elif s0 < TabArGI[0, 5] or s0 > TabArGI[-1, 5]:
            print('Valor da Integral de "cp(T)/T" de T0 a T informado está fora do intervalo de consulta!!!!!')
    #20--------------------------------------------------------------------------
    if vr != 0 and (T == 0 and h == 0 and u == 0 and s0 == 0 and Pr == 0):
        i = np.where(TabArGI[:, 4] >= vr)[0][0]
        if i >= 0:
            T = scipy.interpolate.interp1d(TabArGI[:, 4], TabArGI[:, 0])(vr)
            Pr = scipy.interpolate.interp1d(TabArGI[:, 4], TabArGI[:, 2])(vr)
            h = scipy.interpolate.interp1d(TabArGI[:, 4], TabArGI[:, 1])(vr)
            s0 = scipy.interpolate.interp1d(TabArGI[:, 4], TabArGI[:, 5])(vr)
            u = scipy.interpolate.interp1d(TabArGI[:, 4], TabArGI[:, 3])(vr)
        elif vr < TabArGI[0, 4] or vr > TabArGI[-1, 4]:
            print('Valor do volume específico relativo informado está fora do intervalo de consulta!!!!!')
    #21--------------------------------------------------------------------------
    if Pr != 0 and (T == 0 and h == 0 and u == 0 and s0 == 0 and vr == 0):
        i = np.where(TabArGI[:, 2] >= Pr)[0][0]
        if i >= 0:
            T = scipy.interpolate.interp1d(TabArGI[:, 2], TabArGI[:, 0])(Pr)
            vr = scipy.interpolate.interp1d(TabArGI[:, 2], TabArGI[:, 4])(Pr)
            h = scipy.interpolate.interp1d(TabArGI[:, 2], TabArGI[:, 1])(Pr)
            s0 = scipy.interpolate.interp1d(TabArGI[:, 2], TabArGI[:, 5])(Pr)
            u = scipy.interpolate.interp1d(TabArGI[:, 2], TabArGI[:, 3])(Pr)
        elif Pr < TabArGI[0, 2] or Pr > TabArGI[-1, 2]:
            print('Valor da pressão relativa informado está fora do intervalo de consulta!!!!!')
    #--------------------------------------------------------------------------
    VetPropGasIdSai = [T, u, h, s0, vr, Pr]
    VetPropSai = VetPropGasIdSai
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    return VetPropSai, Reg
