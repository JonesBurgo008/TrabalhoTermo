# app.py (versão de página única, sem gráfico)
from flask import Flask, render_template, request
import numpy as np
from TermoTab import TermoTab

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora_brayton():
    contexto = {}

    if request.method == 'POST':
        T1 = float(request.form['T1'])
        P1 = float(request.form['P1'])
        P2 = float(request.form['P2'])
        T6 = float(request.form['T6'])

        contexto['T1_input'] = T1
        contexto['P1_input'] = P1
        contexto['P2_input'] = P2
        contexto['T6_input'] = T6

        estados = {}
        pressoes = {}
        
        # Estado 1
        pressoes[1] = P1
        vetor_entrada_1 = np.array([T1, 0, 0, 0, 0, 0]) 
        propriedades_1, _ = TermoTab('AR', vetor_entrada_1)
        estados[1] = propriedades_1
        _, _, _, _, _, Pr1 = propriedades_1

        # Estado 2
        pressoes[2] = P2
        Pr2 = Pr1 * (P2 / P1)
        vetor_entrada_2 = np.array([0, 0, 0, 0, 0, Pr2])
        propriedades_2, _ = TermoTab('AR', vetor_entrada_2)
        estados[2] = propriedades_2

        # Estado 3
        P3 = P2
        T3 = T1
        pressoes[3] = P3
        vetor_entrada_3 = np.array([T3, 0, 0, 0, 0, 0])
        propriedades_3, _ = TermoTab('AR', vetor_entrada_3)
        estados[3] = propriedades_3
        _, _, _, _, _, Pr3 = propriedades_3

        # Estado 4
        P4 = P3 * (P2 / P1)
        pressoes[4] = P4
        Pr4 = Pr3 * (P4 / P3)
        vetor_entrada_4 = np.array([0, 0, 0, 0, 0, Pr4])
        propriedades_4, _ = TermoTab('AR', vetor_entrada_4)
        estados[4] = propriedades_4

        # Estado 6
        P6 = P4
        pressoes[6] = P6
        vetor_entrada_6 = np.array([T6, 0, 0, 0, 0, 0])
        propriedades_6, _ = TermoTab('AR', vetor_entrada_6)
        estados[6] = propriedades_6
        _, _, _, _, _, Pr6 = propriedades_6

        # Estado 7
        P7 = P6 / (P2 / P1)
        pressoes[7] = P7
        Pr7 = Pr6 * (P7 / P6)
        vetor_entrada_7 = np.array([0, 0, 0, 0, 0, Pr7])
        propriedades_7, _ = TermoTab('AR', vetor_entrada_7)
        estados[7] = propriedades_7

        # Estado 8
        T8 = T6
        P8 = P7
        pressoes[8] = P8
        vetor_entrada_8 = np.array([T8, 0, 0, 0, 0, 0])
        propriedades_8, _ = TermoTab('AR', vetor_entrada_8)
        estados[8] = propriedades_8
        _, _, _, _, _, Pr8 = propriedades_8

        # Estado 9
        P9 = P1
        pressoes[9] = P9
        Pr9 = Pr8 * (P9 / P8)
        vetor_entrada_9 = np.array([0, 0, 0, 0, 0, Pr9])
        propriedades_9, _ = TermoTab('AR', vetor_entrada_9)
        estados[9] = propriedades_9
        T9_calc, _, _, _, _, _ = propriedades_9

        # Estado 5
        P5 = P4
        pressoes[5] = P5
        T5 = T9_calc
        vetor_entrada_5 = np.array([T5, 0, 0, 0, 0, 0])
        propriedades_5, _ = TermoTab('AR', vetor_entrada_5)
        estados[5] = propriedades_5

        # Estado 10
        P10 = P9
        pressoes[10] = P10
        h4 = float(estados[4][2])
        h5 = float(estados[5][2])
        h9 = float(estados[9][2])
        h10 = h9 - (h5 - h4)
        vetor_entrada_10 = np.array([0, 0, h10, 0, 0, 0])
        propriedades_10, _ = TermoTab('AR', vetor_entrada_10)
        estados[10] = propriedades_10

        # Cálculos de Desempenho
        h1, h2, h3, h6, h7, h8 = float(estados[1][2]), float(estados[2][2]), float(estados[3][2]), float(estados[6][2]), float(estados[7][2]), float(estados[8][2])
        W_c_total = (h2 - h1) + (h4 - h3)
        W_t_total = (h6 - h7) + (h8 - h9)
        Q_ent_total = (h6 - h5) + (h8 - h7)
        W_liq = W_t_total - W_c_total
        eficiencia = (W_liq / Q_ent_total) * 100

        # Limpeza dos dados
        contexto['estados'] = {i: [float(p) for p in props] for i, props in estados.items()}
        contexto['pressoes'] = {i: float(p) for i, p in pressoes.items()}
        contexto['w_liq'] = float(W_liq)
        contexto['eficiencia'] = float(eficiencia)
        contexto['w_c'] = float(W_c_total)
        contexto['w_t'] = float(W_t_total)
        contexto['q_ent'] = float(Q_ent_total)
    
    return render_template('calculadora_brayton.html', **contexto)

if __name__ == '__main__':
    app.run(debug=True)