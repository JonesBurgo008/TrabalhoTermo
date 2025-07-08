# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
import scipy.interpolate

def TermoTabB(VetPropSubPurEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropSubPurSai, Reg):
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
    #6--------------------------------------------------------------------------
    if ((T != 0 and v != 0) and (P == 0 and u == 0 and h == 0 and s == 0 and x < 0)) or ((T == 0 and v != 0) and (P == 0 and u == 0 and h == 0 and s == 0 and x < 0)):
        i = np.where(TabTlvs[:, 0] >= T)[0][0]
        if i >= 0:
            vlr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
            vvr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 3])(T)
            if vlr <= v <= vvr:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                P = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 1])(T)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 3])(T)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 6])(T)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 9])(T)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 12])(T)
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
                vsa = np.array([scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 1])(T) for j in range(len(Pvsa))])
                k = np.where(vsa <= v)[0][0]
                if v == vsa[k]:
                    P = Pvsa[k]
                    u = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T)
                    h = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T)
                    s = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T)
                else:
                    if (vsa[k + 1] - vsa[k]) < 0.0:
                        k -= 1
                    Pj = [Pvsa[k], Pvsa[k + 1]]
                    vj = [vsa[k], vsa[k + 1]]
                    uj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 2])(T)]
                    hj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 3])(T)]
                    sj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 4])(T)]
                    P = scipy.interpolate.interp1d(vj, Pj)(v)
                    u = scipy.interpolate.interp1d(Pj, uj)(P)
                    h = scipy.interpolate.interp1d(Pj, hj)(P)
                    s = scipy.interpolate.interp1d(Pj, sj)(P)
        elif T < TabTlvs[0, 0] or T > TabTlvs[-1, 0]:
            print('Valor de temperatura informado está fora do intervalo de consulta!!!!!')
    #7--------------------------------------------------------------------------
    if ((T != 0 and u != 0) and (P == 0 and v == 0 and h == 0 and s == 0 and x < 0)) or ((T == 0 and u != 0) and (P == 0 and v == 0 and h == 0 and s == 0 and x < 0)):
        i = np.where(TabTlvs[:, 0] >= T)[0][0]
        if i >= 0:
            ulr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
            uvr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 6])(T)
            if ulr <= u <= uvr:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                P = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 1])(T)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 3])(T)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 6])(T)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 9])(T)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 12])(T)
                x = (u - ul) / (uv - ul)
                v = vl + x * (vv - vl)
                h = hl + x * (hv - hl)
                s = sl + x * (sv - sl)
            elif u < ulr:
                Reg = 'ALC'
                print('Região: Líquido Comprimido')
                print('Esta busca não está implementada!!!!!')
            elif u > uvr:
                Reg = 'VSA'
                print('Região: Vapor Superaquecido')
                usa = np.array([scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 2])(T) for j in range(len(Pvsa))])
                k = np.where(usa <= u)[0][0]
                if u == usa[k]:
                    P = Pvsa[k]
                    v = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T)
                    h = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T)
                    s = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T)
                else:
                    if (usa[k + 1] - usa[k]) < 0.0:
                        k -= 1
                    Pj = [Pvsa[k], Pvsa[k + 1]]
                    uj = [usa[k], usa[k + 1]]
                    vj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 1])(T)]
                    hj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 3])(T)]
                    sj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 4])(T)]
                    P = scipy.interpolate.interp1d(uj, Pj)(u)
                    v = scipy.interpolate.interp1d(Pj, vj)(P)
                    h = scipy.interpolate.interp1d(Pj, hj)(P)
                    s = scipy.interpolate.interp1d(Pj, sj)(P)
        elif T < TabTlvs[0, 0] or T > TabTlvs[-1, 0]:
            print('Valor de temperatura informado está fora do intervalo de consulta!!!!!')
    #8--------------------------------------------------------------------------
    if ((T != 0 and h != 0) and (P == 0 and u == 0 and v == 0 and s == 0 and x < 0)) or ((T == 0 and h != 0) and (P == 0 and u == 0 and v == 0 and s == 0 and x < 0)):
        i = np.where(TabTlvs[:, 0] >= T)[0][0]
        if i >= 0:
            hlr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
            hvr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 9])(T)
            if hlr <= h <= hvr:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                P = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 1])(T)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 3])(T)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 6])(T)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 9])(T)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 12])(T)
                x = (h - hl) / (hv - hl)
                u = ul + x * (uv - ul)
                v = vl + x * (vv - vl)
                s = sl + x * (sv - sl)
            elif h < hlr:
                Reg = 'ALC'
                print('Região: Líquido Comprimido')
                print('Esta busca não está implementada!!!!!')
            elif h > hvr:
                Reg = 'VSA'
                print('Região: Vapor Superaquecido')
                hsa = np.array([scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 3])(T) for j in range(len(Pvsa))])
                k = np.where(hsa <= h)[0][0]
                if h == hsa[k]:
                    P = Pvsa[k]
                    v = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T)
                    u = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T)
                    s = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T)
                else:
                    if (hsa[k + 1] - hsa[k]) < 0.0:
                        k -= 1
                    Pj = [Pvsa[k], Pvsa[k + 1]]
                    hj = [hsa[k], hsa[k + 1]]
                    vj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 1])(T)]
                    uj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 2])(T)]
                    sj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 4])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 4])(T)]
                    P = scipy.interpolate.interp1d(hj, Pj)(h)
                    v = scipy.interpolate.interp1d(Pj, vj)(P)
                    u = scipy.interpolate.interp1d(Pj, uj)(P)
                    s = scipy.interpolate.interp1d(Pj, sj)(P)
        elif T < TabTlvs[0, 0] or T > TabTlvs[-1, 0]:
            print('Valor de temperatura informado está fora do intervalo de consulta!!!!!')
    #9--------------------------------------------------------------------------
    if ((T != 0 and s != 0) and (P == 0 and u == 0 and h == 0 and v == 0 and x < 0)) or ((T == 0 and s != 0) and (P == 0 and u == 0 and h == 0 and v == 0 and x < 0)):
        i = np.where(TabTlvs[:, 0] >= T)[0][0]
        if i >= 0:
            slr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
            svr = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 12])(T)
            if slr <= s <= svr:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                P = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 1])(T)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 3])(T)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 6])(T)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 9])(T)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 12])(T)
                x = (s - sl) / (sv - sl)
                u = ul + x * (uv - ul)
                h = hl + x * (hv - hl)
                v = vl + x * (vv - vl)
            elif s < slr:
                Reg = 'ALC'
                print('Região: Líquido Comprimido')
                print('Esta busca não está implementada!!!!!')
            elif s > svr:
                Reg = 'VSA'
                print('Região: Vapor Superaquecido')
                ssa = np.array([scipy.interpolate.interp1d(TabPvsa[j, :, 0], TabPvsa[j, :, 4])(T) for j in range(len(Pvsa))])
                k = np.where(ssa <= s)[0][0]
                if s == ssa[k]:
                    P = Pvsa[k]
                    v = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T)
                    u = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T)
                    h = scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T)
                else:
                    if (ssa[k + 1] - ssa[k]) < 0.0:
                        k -= 1
                    Pj = [Pvsa[k], Pvsa[k + 1]]
                    sj = [ssa[k], ssa[k + 1]]
                    vj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 1])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 1])(T)]
                    uj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 2])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 2])(T)]
                    hj = [scipy.interpolate.interp1d(TabPvsa[k, :, 0], TabPvsa[k, :, 3])(T),
                          scipy.interpolate.interp1d(TabPvsa[k + 1, :, 0], TabPvsa[k + 1, :, 3])(T)]
                    P = scipy.interpolate.interp1d(sj, Pj)(s)
                    v = scipy.interpolate.interp1d(Pj, vj)(P)
                    u = scipy.interpolate.interp1d(Pj, uj)(P)
                    h = scipy.interpolate.interp1d(Pj, hj)(P)
        elif T < TabTlvs[0, 0] or T > TabTlvs[-1, 0]:
            print('Valor de temperatura informado está fora do intervalo de consulta!!!!!')
    #10--------------------------------------------------------------------------
    if ((T != 0 and (0 <= x <= 1)) and (v == 0 and u == 0 and h == 0 and s == 0)) or ((T == 0 and (0 <= x <= 1)) and (v == 0 and u == 0 and h == 0 and s == 0)):
        i = np.where(TabTlvs[:, 0] >= T)[0][0]
        if i >= 0:
            Reg = 'MLV'
            print('Região: Mistura Líquido e Vapor Saturados')
            P = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 1])(T)
            vl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 2])(T)
            vv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 3])(T)
            ul = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 4])(T)
            uv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 6])(T)
            hl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 7])(T)
            hv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 9])(T)
            sl = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 10])(T)
            sv = scipy.interpolate.interp1d(TabTlvs[:, 0], TabTlvs[:, 12])(T)
            v = vl + x * (vv - vl)
            u = ul + x * (uv - ul)
            h = hl + x * (hv - hl)
            s = sl + x * (sv - sl)
        elif T < TabTlvs[0, 0] or T > TabTlvs[-1, 0]:
            print('Valor de temperatura informado está fora do intervalo de consulta!!!!!')
    #11--------------------------------------------------------------------------
    if (v != 0 and (x == 0 or x == 1)) and (T == 0 and u == 0 and h == 0 and s == 0):
        if x == 0:
            i = np.where(TabTlvs[:, 2] >= v)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 0])(v)
                P = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 1])(v)
                vl = v
                vv = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 3])(v)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 4])(v)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 6])(v)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 7])(v)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 9])(v)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 10])(v)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 2], TabTlvs[:, 12])(v)
                u = ul
                h = hl
                s = sl
            elif v < TabTlvs[0, 2] or v > TabTlvs[-1, 2]:
                print('Valor do volume específico informado está fora do intervalo de consulta!!!!!')
        elif x == 1:
            i = np.where(TabTlvs[:, 3] >= v)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 0])(v)
                P = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 1])(v)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 2])(v)
                vv = v
                ul = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 4])(v)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 6])(v)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 7])(v)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 9])(v)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 10])(v)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 3], TabTlvs[:, 12])(v)
                u = uv
                h = hv
                s = sv
            elif v < TabTlvs[0, 3] or v > TabTlvs[-1, 3]:
                print('Valor do volume específico informado está fora do intervalo de consulta!!!!!')
        else:
            print('O volume específico e o título diferente de 0 ou 1 não definem um estado.')
    #12--------------------------------------------------------------------------
    if (u != 0 and (x == 0 or x == 1)) and (T == 0 and v == 0 and h == 0 and s == 0):
        if x == 0:
            i = np.where(TabTlvs[:, 4] >= u)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 0])(u)
                P = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 1])(u)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 2])(u)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 3])(u)
                ul = u
                uv = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 6])(u)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 7])(u)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 9])(u)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 10])(u)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 4], TabTlvs[:, 12])(u)
                v = vl
                h = hl
                s = sl
            elif u < TabTlvs[0, 4] or u > TabTlvs[-1, 4]:
                print('Valor da energia interna específica informado está fora do intervalo de consulta!!!!!')
        elif x == 1:
            i = np.where(TabTlvs[:, 6] >= u)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 0])(u)
                P = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 1])(u)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 2])(u)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 3])(u)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 4])(u)
                uv = u
                hl = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 7])(u)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 9])(u)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 10])(u)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 6], TabTlvs[:, 12])(u)
                v = vv
                h = hv
                s = sv
            elif u < TabTlvs[0, 6] or u > TabTlvs[-1, 6]:
                print('Valor da energia interna específica informado está fora do intervalo de consulta!!!!!')
        else:
            print('A energia interna específica e o título diferente de 0 ou 1 não definem um estado.')
    #13--------------------------------------------------------------------------
    if (h != 0 and (x == 0 or x == 1)) and (T == 0 and v == 0 and u == 0 and s == 0):
        if x == 0:
            i = np.where(TabTlvs[:, 7] >= h)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 0])(h)
                P = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 1])(h)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 2])(h)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 3])(h)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 4])(h)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 6])(h)
                hl = h
                hv = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 9])(h)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 10])(h)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 7], TabTlvs[:, 12])(h)
                v = vl
                u = ul
                s = sl
            elif h < TabTlvs[0, 7] or h > TabTlvs[-1, 7]:
                print('Valor da entalpia específica informado está fora do intervalo de consulta!!!!!')
        elif x == 1:
            i = np.where(TabTlvs[:, 9] >= h)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 0])(h)
                P = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 1])(h)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 2])(h)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 3])(h)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 4])(h)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 6])(h)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 7])(h)
                hv = h
                sl = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 10])(h)
                sv = scipy.interpolate.interp1d(TabTlvs[:, 9], TabTlvs[:, 12])(h)
                v = vv
                u = uv
                s = sv
            elif h < TabTlvs[0, 9] or h > TabTlvs[-1, 9]:
                print('Valor da entalpia específica informado está fora do intervalo de consulta!!!!!')
        else:
            print('A entalpia específica e o título diferente de 0 ou 1 não definem um estado.')
    #14--------------------------------------------------------------------------
    if (s != 0 and (x == 0 or x == 1)) and (T == 0 and v == 0 and u == 0 and h == 0):
        if x == 0:
            i = np.where(TabTlvs[:, 10] >= s)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 0])(s)
                P = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 1])(s)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 2])(s)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 3])(s)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 4])(s)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 6])(s)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 7])(s)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 9])(s)
                sl = s
                sv = scipy.interpolate.interp1d(TabTlvs[:, 10], TabTlvs[:, 12])(s)
                v = vl
                u = ul
                h = hl
            elif s < TabTlvs[0, 10] or s > TabTlvs[-1, 10]:
                print('Valor da entropia específica informado está fora do intervalo de consulta!!!!!')
        elif x == 1:
            i = np.where(TabTlvs[:, 12] >= s)[0][0]
            if i >= 0:
                Reg = 'MLV'
                print('Região: Mistura Líquido e Vapor Saturados')
                T = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 0])(s)
                P = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 1])(s)
                vl = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 2])(s)
                vv = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 3])(s)
                ul = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 4])(s)
                uv = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 6])(s)
                hl = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 7])(s)
                hv = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 9])(s)
                sl = scipy.interpolate.interp1d(TabTlvs[:, 12], TabTlvs[:, 10])(s)
                sv = s
                v = vv
                u = uv
                h = hv
            elif s < TabTlvs[0, 12] or s > TabTlvs[-1, 12]:
                print('Valor da entropia específica informado está fora do intervalo de consulta!!!!!')
        else:
            print('A entropia específica e o título diferente de 0 ou 1 não definem um estado.')

    VetPropSubPurSai = [T, P, v, u, h, s, x, vl, vv, ul, uv, hl, hv, sl, sv]
    VetPropSai = VetPropSubPurSai

    return VetPropSai, Reg
