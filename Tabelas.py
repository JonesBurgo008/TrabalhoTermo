# Código: Consulta a Tabelas Propriedades Termodinâmicas 
# Responsável: Manuel Nascimento Dias Barcelos Júnior (professor)
# e-mail: manuelbarcelos@aerospace.unb.br
#         manuelbarcelos@unb.br
# Código: TermoTab0.1
# Data: 16/07/2024

import numpy as np

def Tabelas(TipTab):
    Pvsa = 0
    TabPvsa = 0
    n1 = 0
    TabPlvs = 0
    TabTlvs = 0
    TabArGI = 0

    if TipTab == 'H2O':
        from TabelasH2OA import TabelasH2OA
        TabPlvs, TabTlvs = TabelasH2OA()
        from TabelasH2OB import TabelasH2OB
        Pvsa, n1, TabPvsa = TabelasH2OB()
        from TabelasH2OC import TabelasH2OC
        Plc, TabPlc, TabPsvs = TabelasH2OC()

    elif TipTab == 'R134a':
        from TabelasR134a import TabelasR134a
        TabTlvs, TabPlvs, Pvsa, n1, TabPvsa = TabelasR134a()

    elif TipTab == 'AR':
        from TabelasAR import TabelasAR
        TabArGI = TabelasAR()

    return Pvsa, TabPvsa, n1, TabPlvs, TabTlvs, TabArGI

