

# Análise Computacional de Ciclo Brayton Ideal

**Universidade de Brasília (UnB)**
**Disciplina:** Termodinâmica 1
**Autor:** João Pedro Avelino Lemos Fernandes

---

## 1. Introdução

Este projeto consiste em uma ferramenta computacional desenvolvida em Python para a análise de um Ciclo Brayton ideal. O objetivo é aplicar os conceitos da Termodinâmica na criação de um programa capaz de consultar as propriedades termodinâmicas do Ar (tratado como gás ideal) e, a partir disso, resolver numericamente um Ciclo Brayton complexo, com regeneração, reaquecimento e intercooler.

Para facilitar a utilização, foi desenvolvida uma interface gráfica web utilizando o micro-framework Flask. Esta interface proporciona uma experiência de usuário interativa, permitindo a inserção de dados de entrada do ciclo e a visualização clara dos resultados de desempenho, como trabalho líquido e eficiência térmica.

## 2. Funcionalidades

* Cálculo das propriedades termodinâmicas (Temperatura, Pressão, Entalpia, etc.) para todos os 10 estados do ciclo.
* Cálculo do desempenho do ciclo, incluindo Trabalho dos Compressores, Trabalho das Turbinas, Calor Adicionado, Trabalho Líquido e Eficiência Térmica.
* Interface web interativa para inserção de dados e visualização dos resultados.

## 3. Requisitos do Sistema

Para executar este projeto, é necessário ter instalado:

* Python (versão 3.6 ou superior)
* Gerenciador de pacotes `pip` (geralmente instalado junto com o Python)

## 4. Guia de Instalação

Siga os passos abaixo para configurar o ambiente e rodar a aplicação.

**Passo 1: Obtenha o Código**
Faça o download dos arquivos do projeto e extraia-os em uma pasta de sua preferência no computador.

**Passo 2: Crie o Arquivo de Dependências (Se não existir)**
Para facilitar a instalação das bibliotecas necessárias, um arquivo `requirements.txt` é utilizado. Para gerá-lo, abra um termina na pasta do projeto e execute:

```bash
pip freeze > requirements.txt
````

**Passo 3: Instale as Bibliotecas**
Com o arquivo `requirements.txt` na pasta, execute o seguinte comando no terminal para instalar todas as dependências de uma só vez:

```bash
pip install -r requirements.txt
```

Este comando instalará o `Flask`, `numpy`, `scipy` e outras bibliotecas necessárias.

## 5\. Como Usar a Aplicação

**Passo 1: Inicie o Servidor:**

Com o terminal aberto na pasta do projeto, execute o seguinte comando:

```bash
python app.py
```

O terminal exibirá uma mensagem indicando que o servidor está rodando, algo como `* Running on http://127.0.0.1:5000`. Não feche esta janela do terminal.

**Passo 2: Acesse a Interface no Navegador:**

Abra seu navegador de internet (Chrome, Firefox, etc.) e acesse o seguinte endereço:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

**Passo 3: Insira os Dados e Calcule:**
A página exibirá o formulário "Dados de Entrada":

  * **Temperatura T1 [K]:** Temperatura do ar na entrada do primeiro compressor.
  * **Pressão P1 [kPa]:** Pressão do ar na entrada do primeiro compressor.
  * **Pressão P2 [kPa]:** Pressão do ar na saída do primeiro compressor.
  * **Temperatura Máxima T6 [K]:** Temperatura máxima do ciclo, na entrada da primeira turbina.

Preencha os campos com os valores desejados e clique no botão **"Calcular"**.

**Passo 4: Analise os Resultados**
A mesma página será recarregada, agora exibindo as seções "Resultados da Análise" e "Propriedades nos Estados" com todos os valores calculados para o ciclo.

## 6\. Considerações e Limitações

A análise realizada por esta ferramenta baseia-se em um modelo de **ciclo ideal**. As seguintes suposições são aplicadas:

  * Os processos de compressão (1-2 e 3-4) e expansão (6-7 e 8-9) são **isentrópicos**.
  * Não há perdas de pressão nos trocadores de calor (intercooler, regenerador, câmara de combustão, reaquecedor).
  * O regenerador possui efetividade de 100% (ideal), ou seja, a temperatura do ar na saída do lado frio é igual à temperatura dos gases na entrada do lado quente ($T\_5 = T\_9$).
  * O ar é tratado como um **gás ideal** com calores específicos variáveis, com base nas tabelas fornecidas.
