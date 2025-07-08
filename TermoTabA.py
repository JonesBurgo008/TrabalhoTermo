# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
import scipy.interpolate

def TermoTabA(VetPropSubPurEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropSubPurSai, Reg):
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

    # 1---------------------------------------------------------------------
    if (P != 0 and v != 0) and (T == 0 and u == 0 and h == 0 and s == 0):
        i = np.where(TabPlvs[:, 0] >= P)[0][0]
        if i > 0:
            vlr = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 2])(P)
            vvr = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 3])(P)
            if v >= vlr and v <= vvr:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 1])(P)
                vl = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 2])(P)
                vv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 3])(P)
                ul = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 4])(P)
                uv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 6])(P)
                hl = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 7])(P)
                hv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 9])(P)
                sl = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 10])(P)
                sv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 12])(P)
                x = (v - vl) / (vv - vl)
                u = ul + x * (uv - ul)
                h = hl + x * (hv - hl)
                s = sl + x * (sv - sl)
            elif v < vlr:
                Reg = 'ALC'
                print('Região: Líquido Comprimido')
                print('Esta busca não está implementada!!!!!')
            elif v > vvr:
                Reg = 'VSA'
                print('Região: Vapor Superaquecido')
                j = np.where(Pvsa == P)[0][0]
                if j > 0:
                    T = scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 1])(v)
                    k = np.where(TabPvsa[j, :, 1] >= T)[0][0]
                    if k > 0:
                        ul = scipy.interpolate.interp1d(TabPvsa[j, :, 1], TabPvsa[j, :, 4])(T)
                        uv = scipy.interpolate.interp1d(TabPvsa[j, :, 1], TabPvsa[j, :, 6])(T)
                        hl = scipy.interpolate.interp1d(TabPvsa[j, :, 1], TabPvsa[j, :, 7])(T)
                        hv = scipy.interpolate.interp1d(TabPvsa[j, :, 1], TabPvsa[j, :, 9])(T)
                        sl = scipy.interpolate.interp1d(TabPvsa[j, :, 1], TabPvsa[j, :, 10])(T)
                        sv = scipy.interpolate.interp1d(TabPvsa[j, :, 1], TabPvsa[j, :, 12])(T)
                        u = ul + x * (uv - ul)
                        h = hl + x * (hv - hl)
                        s = sl + x * (sv - sl)
        elif P < TabPlvs[0, 0] or P > TabPlvs[-1, 0]:
            print('Valor de pressão informado está fora do intervalo de consulta!!!!!')

    # 5---------------------------------------------------------------------
    if (P != 0 and (0 <= x <= 1)) and (T == 0 and v == 0 and u == 0 and h == 0 and s == 0):
        i = np.where(TabPlvs[:, 0] >= P)[0][0]
        if i >= 0:
            Reg = 'MLV'
            print('Região: Mistura Líquido e Vapor Saturados')
            T = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 1])(P)
            vl = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 2])(P)
            vv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 3])(P)
            ul = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 4])(P)
            uv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 6])(P)
            hl = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 7])(P)
            hv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 9])(P)
            sl = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 10])(P)
            sv = scipy.interpolate.interp1d(TabPlvs[:, 0], TabPlvs[:, 12])(P)
            v = vl + x * (vv - vl)
            u = ul + x * (uv - ul)
            h = hl + x * (hv - hl)
            s = sl + x * (sv - sl)
        elif P < TabPlvs[0, 0] or P > TabPlvs[-1, 0]:
            print('Valor de pressão informado está fora do intervalo de consulta!!!!!')

    VetPropSubPurSai = [T, P, v, u, h, s, x, vl, vv, ul, uv, hl, hv, sl, sv]
    VetPropSai = VetPropSubPurSai

    return VetPropSai, Reg
