# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np
import os
from TermoTab import TermoTab


# Definição do tipo de fluido de trabalho (Substância Pura ou Gás Ideal)
print("Definição do fluido de trabalho:")
print("1 para H2O")
print("2 para R134a")
print("3 para Ar")
FldTrab = int(input("Entre o número: "))

# Limpar a tela
#os.system('cls' if os.name == 'nt' else 'clear')

if FldTrab == 1:
    TipTab = 'H2O'
elif FldTrab == 2:
    TipTab = 'R134a'
elif FldTrab == 3:
    TipTab = 'AR'

print('--------------------------------------------------------------------------')

if TipTab in ['H2O', 'R134a']:
    # Entrada das propriedades que caracterizam o estado da Substância Pura
    T, P, v, u, h, s, x = 0, 0, 0, 0, 0, 0, -1
    
    propriedades = """
    Números identificadores das propriedades:
    1 para Temperatura, T, em [oC]
    2 para Pressão, P, em [kPa]
    3 para Volume específico, v, em [m3/kg]
    4 para Energia interna específica, u, em [kJ/kg]
    5 para Entalpia específica, h, em [kJ/kg]
    6 para Entropia específica, s, em [kJ/kgK]
    7 para Título, x, em [m3/kg]
    """
    print(propriedades)
    PropId1 = int(input('Primeira propriedade - Entre o número identificador:'))
    Prop1 = float(input('Primeira propriedade - Entre o valor da propriedade:'))
    PropId2 = int(input('Segunda propriedade - Entre o número identificador:'))
    Prop2 = float(input('Segunda propriedade - Entre o valor da propriedade:'))

    props = {1: 'T', 2: 'P', 3: 'v', 4: 'u', 5: 'h', 6: 's', 7: 'x'}
    if PropId1 in props:
        exec(f"{props[PropId1]} = Prop1")
    else:
        print('Escolha errada da propriedade 1!')
        TipTab = ''
        
    if PropId2 in props:
        exec(f"{props[PropId2]} = Prop2")
    else:
        print('Escolha errada da propriedade 2!')
        TipTab = ''
        
    VetPropSubPurEnt = [T, P, v, u, h, s, x]
    VetPropSubPurSai = np.zeros(15)
    
elif TipTab == 'AR':
    # Entrada das propriedades que caracterizam o estado do Gás Ideal
    T, u, h, s0, vr, Pr = 0, 0, 0, 0, 0, 0
    
    entradas = """
    Números identificadores das entradas:
    1 para Temperatura, T, em [K]
    2 para Energia interna específica, u, em [kJ/kg]
    3 para Entalpia específica, h, em [kJ/kg]
    4 para Entropia específica, s0, em [kJ/kgK]
    5 para Volume relativo, vr
    6 para Pressão relativa, Pr
    """
    print(entradas)
    PropId1 = int(input('Entre o número identificador:'))
    Prop1 = float(input('Entre o valor da entrada:'))

    props = {1: 'T', 2: 'u', 3: 'h', 4: 's0', 5: 'vr', 6: 'Pr'}
    if PropId1 in props:
        exec(f"{props[PropId1]} = Prop1")
    else:
        print('Escolha errada da entrada!')
        TipTab = ''

    VetPropGasIdEnt = [T, u, h, s0, vr, Pr]
    VetPropGasIdSai = np.zeros(6)

if TipTab in ['H2O', 'R134a']:
    # Chamada da função de cálculo de propriedades
    VetPropSubPurSai, Reg = TermoTab(TipTab, VetPropSubPurEnt)
    
    # Saída das propriedades que caracterizam o estado da Substância Pura
    (T, P, v, u, h, s, x, vl, vv, ul, uv, hl, hv, sl, sv) = VetPropSubPurSai
    
    print('Temperatura [oC]', T)
    print('Pressão [kPa]', P)
    print('Volume específico [m3/kg]', v)
    print('Energia interna específica [kJ/kg]', u)
    print('Entalpia específica [kJ/kg]', h)
    print('Entropia específica [kJ/kgK]', s)
    
    if Reg == 'MLV':
        print('Título', x)
        print('Volume específico de líquido saturado [m3/kg]', vl)
        print('Volume específico de vapor saturado [m3/kg]', vv)
        print('Energia interna específica de líquido saturado [kJ/kg]', ul)
        print('Energia interna específica de vapor saturado [kJ/kg]', uv)
        print('Entalpia específica de líquido saturado [kJ/kg]', hl)
        print('Entalpia específica de vapor saturado [kJ/kg]', hv)
        print('Entropia específica de líquido saturado [kJ/kgK]', sl)
        print('Entropia específica de vapor saturado [kJ/kgK]', sv)
        
elif TipTab == 'AR':
    VetPropGasIdSai, Reg = TermoTab(TipTab, VetPropGasIdEnt)
    
    # Saída das propriedades que caracterizam o estado do Gás Ideal
    (T, u, h, s0, vr, Pr) = VetPropGasIdSai
    
    print('Temperatura [K]', T)
    print('Energia interna específica [kJ/kg]', u)
    print('Entalpia específica [kJ/kg]', h)
    print('Integral de "cp(T)/T" de T0 a T [kJ/kgK]', s0)
    print('Volume específico relativo', vr)
    print('Pressão relativa', Pr)
