# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
import scipy.interpolate

def TermoTabC(VetPropSubPurEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropSubPurSai, Reg):
    if (Reg=='   '):
        T = VetPropSubPurEnt[0]
        P = VetPropSubPurEnt[1]
        v = VetPropSubPurEnt[2]
        u = VetPropSubPurEnt[3]
        h = VetPropSubPurEnt[4]
        s = VetPropSubPurEnt[5]
        x = VetPropSubPurEnt[6]
        vl = 0
        vv = 0
        ul = 0
        uv = 0
        hl = 0
        hv = 0
        sl = 0
        sv = 0
    else:
        T = VetPropSubPurSai[0]
        P = VetPropSubPurSai[1]
        v = VetPropSubPurSai[2]
        u = VetPropSubPurSai[3]
        h = VetPropSubPurSai[4]
        s = VetPropSubPurSai[5]
        x = VetPropSubPurSai[6]
        vl = VetPropSubPurSai[7]
        vv = VetPropSubPurSai[8]
        ul = VetPropSubPurSai[9]
        uv = VetPropSubPurSai[10]
        hl = VetPropSubPurSai[11]
        hv = VetPropSubPurSai[12]
        sl = VetPropSubPurSai[13]
        sv = VetPropSubPurSai[14]
        

    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    #15--------------------------------------------------------------------------
    if (T != 0 and P != 0) and (v == 0 and u == 0 and h == 0 and s == 0) or (T == 0 and P != 0) and (v == 0 and u == 0 and h == 0 and s == 0):
        i = np.where(TabTlvs[:, 0] >= T)[0][0]
        if i >= 0:
            Psat = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 1])(T)
            if P == Psat:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                print('O par temperatura e pressão são os de saturação!!!!!')
                print('Para definir o estado é necessário uma terceira propriedade intensiva ou o título.')
            elif P > Psat:
                Reg = 'ALC'
                print('Região: Líquido Comprimido')
                v = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
                u = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
                h = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
                s = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
            else:
                Reg = 'VSA'
                print('Região: Vapor Superaquecido')
                j = np.where(Pvsa == P)[0][0]
                if j >= 0:
                    v = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 1])(T)
                    u = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 2])(T)
                    h = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 3])(T)
                    s = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 4])(T)
                else:
                    k = np.where(Pvsa > P)[0][0]
                    if k >= 0:
                        vk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 1])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T)]
                        uk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 2])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T)]
                        hk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 3])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T)]
                        sk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 4])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T)]
                        Pk = [Pvsa[k - 1], Pvsa[k]]
                        v = scipy.interpolate.interp1d(Pk, vk)(P)
                        u = scipy.interpolate.interp1d(Pk, uk)(P)
                        h = scipy.interpolate.interp1d(Pk, hk)(P)
                        s = scipy.interpolate.interp1d(Pk, sk)(P)
        elif T < TabTlvs[0, 0] or T > TabTlvs[-1, 0]:
            Reg = 'VSA'
            print('Região: Vapor Superaquecido')
            j = np.where(Pvsa == P)[0][0]
            if j >= 0:
                v = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 1])(T)
                u = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 2])(T)
                h = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 3])(T)
                s = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 4])(T)
            else:
                k = np.where(Pvsa > P)[0][0]
                if k >= 0:
                    vk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 1])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T)]
                    uk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 2])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T)]
                    hk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 3])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T)]
                    sk = [scipy.interpolate.interp1d(TabPvsa[k - 1, :, 0], TabPvsa[k - 1, :, 4])(T), scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T)]
                    Pk = [Pvsa[k - 1], Pvsa[k]]
                    v = scipy.interpolate.interp1d(Pk, vk)(P)
                    u = scipy.interpolate.interp1d(Pk, uk)(P)
                    h = scipy.interpolate.interp1d(Pk, hk)(P)
                    s = scipy.interpolate.interp1d(Pk, sk)(P)

    VetPropSubPurSai = [T, P, v, u, h, s, x, vl, vv, ul, uv, hl, hv, sl, sv]
    VetPropSai = VetPropSubPurSai
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    return VetPropSai, Reg
