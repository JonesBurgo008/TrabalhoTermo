# Importar as bibliotecas necessárias
import numpy as np
from TermoTab import TermoTab

# --- PASSO 1: DEFINIR OS PARÂMETROS DO CICLO ---
# Aqui vamos definir as informações que temos sobre o ciclo
# Por exemplo, a temperatura e pressão na entrada do primeiro compressor.

print("Análise do Ciclo Brayton com Reaquecimento, Regeneração e Intercooler")
print("--------------------------------------------------------------------")

# --- PASSO 2: CALCULAR AS PROPRIEDADES DE CADA ESTADO ---

# Dicionário para armazenar as propriedades de cada estado.
# A chave será o número do estado (1, 2, 3...) e o valor será o vetor de propriedades.
estados = {}


print("Coletando dados iniciais do ciclo:")
T1 = float(input("Temperatura inicial do ar [K]: "))
P1 = float(input("Pressão 1 [kPa]: "))
P2 = float(input("Pressão 2 [kPa]: "))
T6 = float(input("Qual temperatura [K] as turbinas suportam? R: "))
print("-----------------------------------------------------")

# Estado 1 (Entrada do primeiro compressor)
print("\nCalculando Estado 1...")
##T1 = 300  # [K] Exemplo: Temperatura ambiente
##P1 = 100  # [kPa] Exemplo: Pressão atmosférica

# Para o Ar, precisamos de um vetor com 6 posições: [T, u, h, s0, vr, Pr]
# Vamos usar T1 para encontrar o resto.
vetor_entrada_1 = np.array([T1, 0, 0, 0, 0, 0]) 
propriedades_1, _ = TermoTab('AR', vetor_entrada_1)

# Armazenamos o resultado e imprimimos
estados[1] = propriedades_1
T1_calc, u1, h1, s0_1, vr1, Pr1 = propriedades_1
# print(f"Estado 1: T1 = {T1_calc:.2f} K, h1 = {h1:.2f} kJ/kg, Pr1 = {Pr1:.2f}")
print(f"Estado 1: T1 = {T1_calc:.2f} K, h1 = {h1:.2f} kJ/kg, P1 = {P1:.2f} kPa")

# --- PRÓXIMOS PASSOS ---
# Aqui vamos calcular os estados 2, 3, 4, etc.

# Estado 2 (Saída do primeiro compressor)
print("\nCalculando Estado 2...")
# O processo 1-2 é uma compressão isentrópica (s2 = s1).
# Para o ar como gás ideal, isso significa que P2/P1 = Pr2/Pr1.

# Primeiro, definimos a pressão de saída do compressor.
# A razão de pressões (P2/P1) é um parâmetro chave do ciclo. Vamos assumir P2 = 400 kPa.
##P2 = 400 # [kPa]

# Buscamos P1 e Pr1 do estado 1 que já calculamos
#P1 = 100 # Já definido anteriormente
#_, _, _, _, _, Pr1 = estados[1] # Desempacotando o Pr1 do resultado do estado 1

# Agora, calculamos Pr2
Pr2 = Pr1 * (P2 / P1)

# Usamos Pr2 como entrada para encontrar as propriedades do estado 2
# O vetor de entrada agora é [T, u, h, s0, vr, Pr] com Pr sendo o valor conhecido
vetor_entrada_2 = np.array([0, 0, 0, 0, 0, Pr2])
propriedades_2, _ = TermoTab('AR', vetor_entrada_2)

# Armazenamos e imprimimos os resultados do Estado 2
estados[2] = propriedades_2
T2_calc, u2, h2, s0_2, vr2, Pr2_calc = propriedades_2
print(f"Estado 2: T2 = {T2_calc:.2f} K, h2 = {h2:.2f} kJ/kg, P2 = {P2:.2f} kPa")


# Estado 3 (Saída do resfriador intermediário)
print("\nCalculando Estado 3...")
# O processo 2-3 é um resfriamento a pressão constante (ideal).
# A temperatura é resfriada de volta à temperatura de entrada (T3 = T1).

P3 = P2  # Pressão constante no intercooler
T3 = T1  # Resfriado de volta à temperatura inicial

# Com T3 conhecido, podemos usá-lo como entrada para a TermoTab
vetor_entrada_3 = np.array([T3, 0, 0, 0, 0, 0])
propriedades_3, _ = TermoTab('AR', vetor_entrada_3)

# Armazenamos e imprimimos os resultados do Estado 3
estados[3] = propriedades_3
T3_calc, u3, h3, s0_3, vr3, Pr3 = propriedades_3
print(f"Estado 3: T3 = {T3_calc:.2f} K, h3 = {h3:.2f} kJ/kg, P3 = {P3:.2f} kPa")


# Estado 4 (Saída do segundo compressor)
print("\nCalculando Estado 4...")
# O processo 3-4 é a segunda compressão isentrópica (s4 = s3).
# A relação é P4/P3 = Pr4/Pr3.

# Para máxima eficiência, a razão de pressão é a mesma do primeiro estágio.
# Razão de pressão = P2/P1 = 4
P4 = P3 * (P2 / P1)

# Buscamos Pr3 do estado 3 que já calculamos
_, _, _, _, _, Pr3 = estados[3]

# Calculamos Pr4
Pr4 = Pr3 * (P4 / P3)

# Usamos Pr4 como entrada para encontrar as propriedades do estado 4
vetor_entrada_4 = np.array([0, 0, 0, 0, 0, Pr4])
propriedades_4, _ = TermoTab('AR', vetor_entrada_4)

# Armazenamos e imprimimos os resultados do Estado 4
estados[4] = propriedades_4
T4_calc, u4, h4, s0_4, vr4, Pr4_calc = propriedades_4
print(f"Estado 4: T4 = {T4_calc:.2f} K, h4 = {h4:.2f} kJ/kg, P4 = {P4:.2f} kPa")


# --- Parte Quente do Ciclo e Regeneração ---
# Para achar o Estado 5, precisamos da temperatura do Estado 9 (T9).
# Para achar T9, precisamos passar pelas turbinas. Vamos definir os estados 6, 7 e 8.


# Estado 6 (Entrada da primeira turbina, após a câmara de combustão)
print("\nCalculando Estado 6...")
# Esta é a temperatura máxima do ciclo, um parâmetro de projeto.
##T6 = 1400  # [K] Exemplo de temperatura máxima
P6 = P4    # A combustão ocorre a pressão constante (ideal)

vetor_entrada_6 = np.array([T6, 0, 0, 0, 0, 0])
propriedades_6, _ = TermoTab('AR', vetor_entrada_6)
estados[6] = propriedades_6
_, _, h6, _, _, Pr6 = propriedades_6
print(f"Estado 6: T6 = {T6:.2f} K, h6 = {h6:.2f} kJ/kg, P6 = {P6:.2f} kPa")


# Estado 7 (Saída da primeira turbina, entrada do reaquecedor)
print("\nCalculando Estado 7...")
# A expansão na turbina é isentrópica (s7 = s6). P7/P6 = Pr7/Pr6
# A pressão intermediária P7 é escolhida para maximizar o trabalho. A condição ideal é P7/P6 = sqrt(P9/P6).
# Vamos assumir que a razão de pressão na turbina é o inverso da do compressor.
P7 = P6 / (P2 / P1)

Pr7 = Pr6 * (P7 / P6)

vetor_entrada_7 = np.array([0, 0, 0, 0, 0, Pr7])
propriedades_7, _ = TermoTab('AR', vetor_entrada_7)
estados[7] = propriedades_7
T7_calc, _, h7, _, _, _ = propriedades_7
print(f"Estado 7: T7 = {T7_calc:.2f} K, h7 = {h7:.2f} kJ/kg, P7 = {P7:.2f} kPa")


# Estado 8 (Entrada da segunda turbina, após o reaquecimento)
print("\nCalculando Estado 8...")
# O gás é reaquecido até a temperatura máxima do ciclo novamente.
T8 = T6    # Reaquecido até Tmax
P8 = P7    # Reaquecimento a pressão constante

vetor_entrada_8 = np.array([T8, 0, 0, 0, 0, 0])
propriedades_8, _ = TermoTab('AR', vetor_entrada_8)
estados[8] = propriedades_8
_, _, h8, _, _, Pr8 = propriedades_8
print(f"Estado 8: T8 = {T8:.2f} K, h8 = {h8:.2f} kJ/kg, P8 = {P8:.2f} kPa")


# Estado 9 (Saída da segunda turbina)
print("\nCalculando Estado 9...")
# Segunda expansão isentrópica (s9 = s8). P9/P8 = Pr9/Pr8
P9 = P1 # Expande de volta até a pressão inicial (um pouco acima para vencer perdas, mas idealmente P1)

Pr9 = Pr8 * (P9 / P8)

vetor_entrada_9 = np.array([0, 0, 0, 0, 0, Pr9])
propriedades_9, _ = TermoTab('AR', vetor_entrada_9)
estados[9] = propriedades_9
T9_calc, _, h9, _, _, _ = propriedades_9
print(f"Estado 9: T9 = {T9_calc:.2f} K, h9 = {h9:.2f} kJ/kg, P9 = {P9:.2f} kPa")


# Estado 5 (Saída do regenerador, lado frio)
print("\nCalculando Estado 5...")
# Agora que temos T9, podemos calcular o Estado 5.
# O processo 4-5 é aquecimento a pressão constante no regenerador.
P5 = P4

# Em um regenerador ideal, a temperatura de saída do ar frio (T5)
# é igual à temperatura de entrada do gás quente (T9).
T5 = T9_calc

# Usamos T5 como nossa propriedade conhecida.
vetor_entrada_5 = np.array([T5, 0, 0, 0, 0, 0])
propriedades_5, _ = TermoTab('AR', vetor_entrada_5)
estados[5] = propriedades_5
T5_calc, u5, h5, s0_5, vr5, Pr5 = propriedades_5
print(f"Estado 5: T5 = {T5_calc:.2f} K, h5 = {h5:.2f} kJ/kg, P5 = {P5:.2f} kPa")


# Estado 10 (Saída do regenerador, lado quente)
print("\nCalculando Estado 10...")
# O processo 9-10 é o resfriamento do gás de exaustão a pressão constante.
# A energia perdida pelo gás quente é igual à energia ganha pelo ar frio (h9-h10 = h5-h4).
P10 = P9

# Recuperamos as entalpias dos estados que já calculamos
_, _, h4, _, _, _ = estados[4]
_, _, h5, _, _, _ = estados[5]
_, _, h9, _, _, _ = estados[9]

# Calculamos a entalpia do estado 10 pela lei da conservação de energia
h10 = h9 - (h5 - h4)

# Usamos h10 como entrada para encontrar as propriedades do estado 10
vetor_entrada_10 = np.array([0, 0, h10, 0, 0, 0])
propriedades_10, _ = TermoTab('AR', vetor_entrada_10)

# Armazenamos e imprimimos os resultados do Estado 10
estados[10] = propriedades_10
T10_calc, _, h10_calc, _, _, _ = propriedades_10
print(f"Estado 10: T10 = {T10_calc:.2f} K, h10 = {h10_calc:.2f} kJ/kg, P10 = {P10:.2f} kPa")



# --- PASSO 3: CALCULAR O DESEMPENHO DO CICLO ---
# (Calcularemos W_liq e eficiência aqui no final)

print("\n--------------------------------------------------------------------")
print("Cálculo de Desempenho do Ciclo Brayton")

# Extrair todas as entalpias do dicionário de estados
h1 = estados[1][2]
h2 = estados[2][2]
h3 = estados[3][2]
h4 = estados[4][2]
h5 = estados[5][2]
h6 = estados[6][2]
h7 = estados[7][2]
h8 = estados[8][2]
h9 = estados[9][2]
h10 = estados[10][2]

# 1. Calcular o trabalho dos compressores (energia consumida)
W_c1 = h2 - h1
W_c2 = h4 - h3
W_c_total = W_c1 + W_c2
print(f"\nTrabalho total consumido pelos compressores: {W_c_total:.2f} kJ/kg")

# 2. Calcular o trabalho das turbinas (energia produzida)
W_t1 = h6 - h7
W_t2 = h8 - h9
W_t_total = W_t1 + W_t2
print(f"Trabalho total produzido pelas turbinas: {W_t_total:.2f} kJ/kg")

# 3. Calcular o calor adicionado (combustível queimado)
Q_ent1 = h6 - h5  # Câmara de combustão
Q_ent2 = h8 - h7  # Reaquecimento
Q_ent_total = Q_ent1 + Q_ent2
print(f"Calor total adicionado ao ciclo: {Q_ent_total:.2f} kJ/kg")

# 4. Calcular o trabalho líquido do ciclo
W_liq = W_t_total - W_c_total
print(f"\nTrabalho Líquido do Ciclo (W_liq): {W_liq:.2f} kJ/kg")

# 5. Calcular a eficiência térmica do ciclo
eficiencia = (W_liq / Q_ent_total) * 100  # Multiplica por 100 para ver em porcentagem
print(f"Eficiência Térmica do Ciclo: {eficiencia:.2f}%")
print("--------------------------------------------------------------------")
