# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
from TermoTab import TermoTab

import numpy as np

# Glossário
# T:temperatura; 
# P:pressão; 
# v:volume específico;
# u:energia interna específica; 
# h:entalpia específica; 
# s:entropia específica; 
# l:liquido; 
# v:vapor; 
# 0:referência; 
# r:relativo;

# Definição do tipo de fluido de trabalho (Substância Pura ou Gás Ideal)
TipTab = 'H2O'
# TipTab = 'R134a'
# TipTab = 'AR'

# Entrada das propriedades que caracterizam o estado da Substância Pura
# T[oC]; P[kPa]; v[m3/kg]; u[kJ/kg]; h[kJ/kg]; s[kJ/kgK]; 
# Escolher duas propriedades intensivas e independentes para definir o
# estado (apenas a estas atribuir um valor numérico), ou uma propriedade 
# intensiva e o título, deixando as outras iguais a zero, e no caso do
# título igual a -1.
T = 0
P = 101.325
v = 0
u = 0
h = 0
s = 0
x = 0
VetPropSubPurEnt = np.array([T, P, v, u, h, s, x])
VetPropSubPurSai = np.zeros(15)

# Entrada das propriedades que caracterizam o estado do Gás Ideal
# T[K]; u[kJ/kg]; h[kJ/kg]; s0[kJ/kgK]; 
# Escolher umas das entradas e apenas a esta atribuir um valor numérico, 
# uma vez que estas dependem só da temperatura gás ideal, deixando a outras
# iguais a zero. 
T = 0
u = 0
h = 0
s0 = 0
vr = 0
Pr = 0
VetPropGasIdEnt = np.array([T, u, h, s0, vr, Pr])
VetPropGasIdSai = np.zeros(6)

print('--------------------------------------------------------------------------')

if TipTab in ['H2O', 'R134a']:
    # Chamada da função de cálculo de propriedades
    VetPropSubPurSai, Reg = TermoTab(TipTab, VetPropSubPurEnt)
    
    # Saída das propriedades que caracterizam o estado da Substância Pura
    T, P, v, u, h, s, x, vl, vv, ul, uv, hl, hv, sl, sv = VetPropSubPurSai
    print('Temperatura [oC]')
    print(T)
    print('Pressão [kPa]')
    print(P)
    print('Volume específico [m3/kg]')
    print(v)
    print('Energia interna específica [kJ/kg]')
    print(u)
    print('Entalpia específica [kJ/kg]')
    print(h)
    print('Entropia específica [kJ/kgK]')
    print(s)
    if Reg == 'MLV':
        print('Título')
        print(x)
        print('Volume específico de líquido saturado [m3/kg]')
        print(vl)
        print('Volume específico de vapor saturado [m3/kg]')
        print(vv)
        print('Energia interna específica de líquido saturado [kJ/kg]')
        print(ul)
        print('Energia interna específica de vapor saturado [kJ/kg]')
        print(uv)
        print('Entalpia específica de líquido saturado [kJ/kg]')
        print(hl)
        print('Entalpia específica de vapor saturado [kJ/kg]')
        print(hv)
        print('Entropia específica de líquido saturado [kJ/kgK]')
        print(sl)
        print('Entropia específica de vapor saturado [kJ/kgK]')
        print(sv)
elif TipTab == 'AR':
    # Chamada da função de cálculo de propriedades
    VetPropGasIdSai, Reg = TermoTab(TipTab, VetPropGasIdEnt)
    
    # Saída das propriedades que caracterizam o estado do Gás Ideal
    T, u, h, s0, vr, Pr = VetPropGasIdSai
    print('Temperatura [K]')
    print(T)
    print('Energia interna específica [kJ/kg]')
    print(u)
    print('Entalpia específica [kJ/kg]')
    print(h)
    print('Integral de "cp(T)/T" de T0 a T [kJ/kgK]')
    print(s0)
    print('Volume específico relativo')
    print(vr)
    print('Pressão relativa')
    print(Pr)
