# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
from Tabelas import Tabelas

def TermoTab(TipTab, VetPropEnt):
    VetPropSubPurSai = np.zeros(15)
    VetPropGasIdSai = np.zeros(6)
    Reg = '   '
    ErrCarrTab = 0
    
    if TipTab in ['H2O', 'R134a']:
        VetPropSubPurEnt = VetPropEnt
        VetPropGasIdEnt = np.zeros(6)
    elif TipTab == 'AR':
        VetPropGasIdEnt = VetPropEnt
        VetPropSubPurEnt = np.array([0, 0, 0, 0, 0, 0, -1])
    
    contPropSP = 0
    if TipTab in ['H2O', 'R134a']:
        contPropSP = sum(1 for i in range(6) if VetPropSubPurEnt[i] != 0)
        if VetPropSubPurEnt[6] != -1:
            contPropSP += 1
    
    contPropGI = 0
    if TipTab == 'AR':
        contPropGI = sum(1 for i in range(6) if VetPropGasIdEnt[i] != 0)
    
    # Carregar tabelas do fluido de trabalho
    if TipTab == 'H2O':
        print('As tabelas das propriedades da água foram carregadas!')
        Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI = Tabelas(TipTab)
        Pvsa *= 1000
        n = nPvsa
        N = len(Pvsa)
    elif TipTab == 'R134a':
        print('As tabelas das propriedades do R134a foram carregadas!')
        Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI = Tabelas(TipTab)
        Pvsa *= 1000
        n = nPvsa
        N = len(Pvsa)
    elif TipTab == 'AR':
        print('As tabelas das propriedades do ar foram carregadas!')
        Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI = Tabelas(TipTab)
    else:
        print('Não foram carregadas tabelas de propriedades do fluido de trabalho!!!!!')
        ErrCarrTab = 1
    
    if ErrCarrTab == 0:
        if (TipTab in ['H2O', 'R134a']) and (contPropSP <= 2):
            from TermoTabA import TermoTabA
            VetPropSubPurSai, Reg = TermoTabA(VetPropSubPurEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropSubPurSai, Reg)
            from TermoTabB import TermoTabB
            VetPropSubPurSai, Reg = TermoTabB(VetPropSubPurEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropSubPurSai, Reg)
            from TermoTabC import TermoTabC
            VetPropSubPurSai, Reg = TermoTabC(VetPropSubPurEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropSubPurSai, Reg)
            VetPropSai = VetPropSubPurSai
        elif (TipTab == 'AR') and (contPropGI == 1):
            from TermoTabD import TermoTabD
            VetPropSai, Reg = TermoTabD(VetPropGasIdEnt, Pvsa, TabPvsa, nPvsa, TabPlvs, TabTlvs, TabArGI, VetPropGasIdSai, Reg)
        else:
            print('Não foi feita a opção correta do fluido de trabalho!!!!!')
            print('Ou não foi escolhida a quantidade correta de propriedades para caracterizar o estado!!!!!')
    
    return VetPropSai, Reg


