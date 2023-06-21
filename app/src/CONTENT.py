import streamlit as st

def ABOUT():
    st.markdown("""
    # Problemas de Otimização
    
    Os problemas de otimização estão presentes em diversas áreas, como engenharia, economia, logística e ciências da computação. Eles envolvem a busca pela melhor solução possível de acordo com uma função objetivo, que pode ser minimizada ou maximizada, e estão sujeitos a determinadas restrições.
    
    Alguns exemplos de problemas de otimização incluem:
    
    - **Knapsack Problem**: Dado um conjunto de itens com pesos e valores, determinar a combinação de itens que maximiza o valor total sem exceder a capacidade da mochila.
    - **Portfolio Problem**: Selecionar a combinação de ativos que maximiza o retorno esperado do investimento, sujeito a restrições de risco e liquidez.
    
    # Algoritmos de Otimização
    
    Os algoritmos de otimização são técnicas e métodos usados para encontrar soluções ótimas ou aproximadamente ótimas para problemas de otimização. Eles têm ampla aplicação em áreas como engenharia, economia, logística e ciências da computação.
    
    Aqui estão alguns exemplos de algoritmos de otimização populares:
    
    - **Firefly**: Baseado nas interações sociais dos vaga-lumes, o algoritmo Firefly ajusta a atração dos vaga-lumes (ou seja, partículas) no espaço de busca com base em seu brilho, que é determinado pelo valor da função objetivo de um dado problema. Vaga-lumes movem-se em direção aos mais atraentes e brilhantes, e se nenhum for encontrado, movem-se aleatoriamente.
    
    Neste site, você encontrará informações e tutoriais sobre como aplicar esses algoritmos de otimização a uma variedade de problemas do mundo real.
    
    # Sobre o projeto
    
    Bem-vindo à página do nosso projeto de pesquisa em Ciências de Dados, onde buscamos discutir e aplicar modelos matemáticos, estatísticos e de inteligência computacional para resolver problemas complexos do mundo real. Este projeto abrange uma ampla gama de abordagens, incluindo algoritmos clássicos de otimização linear e não linear, econométricos, metaheurísticas e machine learning.
    
    Nosso projeto é dividido em três frentes principais de pesquisa:
    
    - Estudo do framework dos modelos matemáticos, estatísticos e de inteligência computacional
    - Análise de algoritmos existentes na literatura e proposição de algoritmos híbridos
    - Implementação dos algoritmos propostos em problemas reais
    
    Nossas áreas de aplicação incluem, mas não se limitam a, problemas de predição e otimização em dados do mercado financeiro, produção e produtividade de grãos, clima, educação e pesquisa, e saúde. Acreditamos que o uso de soluções computacionais eficientes e avançadas pode levar a descobertas significativas e melhorias nessas áreas.
    
    Além disso, organizamos um desafio em Ciências de Dados nas edições do Congresso de Ciência e Tecnologia da PUC Goiás. Este evento permite que alunos de graduação e pós-graduação apliquem modelos para resolver problemas usando bases de dados reais. A primeira edição foi realizada com sucesso em 2021/2 e continuamos a construir e expandir este evento para envolver mais estudantes e promover a pesquisa em Ciências de Dados.
    
    Convidamos você a explorar nosso projeto e descobrir como a aplicação de modelos matemáticos, estatísticos e de inteligência computacional pode levar a soluções inovadoras para os desafios que enfrentamos em diversas áreas. Junte-se a nós nesta jornada de pesquisa e descoberta, enquanto trabalhamos para criar um impacto positivo no mundo através da ciência de dados.
    
    """)

def KP_THEORY():
    st.markdown("""
    # Knapsack Problem
    O Problema da Mochila é um desafio em otimização combinatória que busca encontrar a melhor combinação de objetos a serem alocados em uma mochila, considerando que cada objeto possui um valor monetário e um peso, e que a mochila possui uma capacidade máxima de armazenamento representada por $c_{max}$.
    
    Para entender melhor este problema, vamos considerar um conjunto de $N$ objetos, onde cada objeto i tem um valor monetário $V_i$ e um peso $P_i$ . A solução ótima do Problema da Mochila consiste em selecionar um subconjunto desses objetos de tal forma que o valor total dos itens na mochila seja maximizado, sem exceder a capacidade máxima de armazenamento. O problema é descrito por meio da equação $(1)$ .
    Função objetivo:
    """)
    st.latex("""
    FO(x_i) = \sum_{i=1}^{N} x_i V_i \\tag{1}
    """)
    st.markdown("""
    A função objetivo $(1)$ busca maximizar o valor total dos itens selecionados para a mochila. A variável binária $x_i$ indica se o objeto $i$ foi selecionado (1) ou não (0).
    Restrições:
    """)
    st.latex("""
    \sum_{i=1}^{N} x_i P_i \leq c_{max} \\tag{2}
    """)
    st.markdown("""
    A restrição $(2)$ garante que a capacidade máxima da mochila não seja excedida. O peso total dos objetos selecionados não pode ser maior que a capacidade máxima de armazenamento $c_{max}$.
    """)
    st.latex("""
    x_i \in \{0, 1\} \quad \\forall i \in \{1, 2, ..., N\} \\tag{3}
    """)
    st.markdown("""
    Devido à sua natureza combinatória e à quantidade de variações possíveis, o Problema da Mochila é classificado como um problema NP-difícil, ou seja, um problema cuja solução exata pode ser difícil de ser encontrada em tempo hábil, especialmente para grandes conjuntos de dados. Como resultado, várias abordagens heurísticas e metaheurísticas foram desenvolvidas para encontrar soluções aproximadas e eficientes para este problema, como algoritmos genéticos, busca tabu e otimização por colônia de formigas.
    
    Além disso, o Problema da Mochila possui diversas variações, como o problema da mochila fracionária, no qual é permitido dividir os objetos e incluir apenas uma fração deles na mochila, e o problema da mochila multidimensional, que considera múltiplas restrições além do peso, como volume e quantidade disponível de cada item. Estas variações ampliam ainda mais a aplicabilidade do Problema da Mochila e o tornam uma importante área de estudo na pesquisa de otimização combinatória.
    
    As instâncias do Problema da Mochila são conjuntos de dados específicos que representam casos particulares desse problema. Cada instância é composta por um conjunto de objetos, com seus respectivos pesos e valores monetários, e uma capacidade máxima da mochila. Ao utilizar diferentes instâncias, é possível analisar o desempenho e a eficácia de diversos algoritmos de solução, incluindo heurísticas e metaheurísticas, em diferentes cenários e tamanhos de problema. Para facilitar o acesso a essas instâncias, disponibilizamos uma tabela geral com o [links de download](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/instances_01_KP.zip). A tabela apresenta detalhes sobre cada instância, como o número de objetos, a capacidade máxima $c_{max}$ da mochila e outras informações relevante como pode ser visto abaixo:
    
    **Tabela 1**: Low-dimensional 0/1 knapsack problems.
    | Nome da Instância | Número de Objetos | Capacidade $c_{max}$ | Ótimo    |
    |-------------------|-------------------|----------------------|----------|
    | F1-LOWKP-10D      | 10                | 269                  | 29.5     |
    | F2-LOWKP-20D      | 20                | 878                  | 1024     |
    | F3-LOWKP-4D       | 4                 | 20                   | 35       |
    | F4-LOWKP-4D       | 4                 | 11                   | 23       |
    | F5-LOWKP-15D      | 15                | 375                  | 481.0694 |
    | F6-LOWKP-10D      | 10                | 60                   | 52       |
    | F7-LOWKP-7D       | 7                 | 50                   | 107      |
    | F8-LOWKP-23D      | 23                | 10000                | 9767     |
    | F9-LOWKP-5D       | 5                 | 80                   | 130      |
    | F10-LOWKP-20D     | 20                | 879                  | 1025     |

    # Example
    No exemplo dado, temos a instância **F1-LOWKP-10D**, que consiste em um conjunto de 10 objetos com seus respectivos valores e pesos. A variável de decisão x indica se cada objeto é selecionado (x = 1) ou não (x = 0).
    **Tabela 2**: F1-LOWKP-10D
    | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
    |------------|------------|-------------|
    | 1          | 55         | 95          |
    | 2          | 10         | 4           |
    | 3          | 47         | 60          |
    | 4          | 5          | 32          |
    | 5          | 4          | 23          |
    | 6          | 50         | 72          |
    | 7          | 8          | 80          |
    | 8          | 61         | 62          |
    | 9          | 85         | 65          |
    | 10         | 87         | 46          |
    
    Dado a instância **F1-LOWKP-10D** descrita na Tabela 2 com 10 objetos conforme descrito na Tabela 1 e considerando que o vetor de variáveis de decisão é dado por $x={1,0,1,1,0,0,0,1,1,0}$.
    
    A função objetivo $(1)$ que soma apenas os itens escolhidos com base na variável binária $x_i$.Substituindo os valores de $x_i$ e $V_i$:
    """)
    st.latex("""
    f(x) = (1 \\times 95) + (0 \\times 4) + (1 \\times 60) + (1 \\times 32) + (0 \\times 23) + (0 \\times 72) + (0 \\times 80) + (1 \\times 62) + (1 \\times 65) + (0 \\times 46)
    """)
    st.markdown("""
    A restrição $(2)$ deve ser menor ou igual à capacidade máxima da mochila $c_{max}$. Substituindo os valores de $x_i$ e $P_i$:
    """)
    st.latex("""
    r(x) = (1 \\times 55) + (0 \\times 10) + (1 \\times 47) + (1 \\times 5) + (0 \\times 4) + (0 \\times 50) + (0 \\times 8) + (1 \\times 61) + (1 \\times 85) + (0 \\times 87)
    """)
    st.markdown("""
    Assim, a função objetivo e a restrição são:
    """)
    st.latex("""
    f(x) = - (95 + 0 + 60 + 32 + 0 + 0 + 0 + 62 + 65 + 0) = - 314
    """)
    st.latex("""
    r(x) = - (55 + 0 + 47 + 5 + 0 + 0 + 0 + 61 + 85 + 0) = - 253
    """)
    st.markdown("""
    Ao aplicar a equação (1), que calcula o valor da FO, utilizando o vetor de variáveis de decisão dado x = {1, 0, 1, 1, 0, 0, 0, 1, 1, 0}, obtemos o valor de -110, ou seja, a função objetivo é de minimização. É importante ressaltar que, na plataforma Meta, que é utilizada para a resolução deste problema, a FO é sempre de minimização, portanto, quando se faz otimização para maximização, a função objetivo fica negativa.
    """)
    st.latex("""
    value = -\left(55x_1 + 10x_2 + 47x_3 + 5x_4 + 4x_5 + 50x_6 + 8x_7 + 61x_8 + 85x_9 + 87x_{10}\\right) \\tag{1}
    """)
    st.markdown("""
    Além disso, é necessário verificar as restrições do problema, que neste caso são a restrição de capacidade da mochila. Na instância **F1-LOWKP-10D**, a capacidade da mochila é de 269, e a soma dos pesos dos objetos selecionados (55 + 10 + 47 + 8 + 61 + 85 + 87) é igual a 353, portanto, a restrição de capacidade não é atendida e a solução não é viável.
    """)
    st.latex("""
    w = 55x_1 + 10x_2 + 47x_3 + 5x_4 + 4x_5 + 50x_6 + 8x_7 + 61x_8 + 85x_9 + 87x_{10} \leq w_{max} \\tag{2}
    """)

def PORTFOLIO_THEORY():
    st.markdown("""
    # Portifolio Problem    
    O Problema do Portfólio consiste em selecionar diferentes ativos financeiros para compor uma carteira de investimentos, com o intuito de maximizar o retorno esperado e reduzir os riscos associados à flutuações do mercado. O modelo de Markowitz é aplicado para determinar os pesos ideais de cada ativo na carteira, por meio da diversificação e da otimização, a fim de alcançar uma combinação ótima que satisfaça os objetivos financeiros do investidor.
    
    A implementação da uma otimização de portfólio é feita utilizando o algoritmo Firefly. O objetivo é encontrar a alocação ótima de um portfólio, que maximize o índice de Sharpe, que relaciona o retorno do portfólio com o seu risco, com a introdução de restrições de limites de investimento em cada ativo do portfólio.
    A implementação está estruturada da seguinte forma:
    - A função **STOCKS_DATASET** carrega as informações de retorno e covariância diários de cada ativo do portfólio em um intervalo de tempo definido pelo usuário. Para fazer o calculo do retorno e covariância é usado as seguintes equações:
    """)
    st.latex("""
    \\text{{Return}} = \\frac{{\\text{{['Close']}}[J + 1]}}{{\\text{{['Close']}}[J]}} - 1 \\tag{1}
    """)
    st.markdown("""
    Onde:
    
    $['Close'][J + 1]$: é o preço de fechamento do dia atual.
    
    $['Close'][J] - 1$: é o preço de fechamento do dia anterior.
    """)
    st.latex("""
    \\text{{COVARIANCE}} = \\text{{RETURN}}.\\text{{cov}}() \\tag{2}
    """)
    st.markdown("""
    - A função **PORTIFOLIO_RETURN_RISK** calcula o retorno e risco anualizados do portfólio, dado um determinado vetor de pesos $X$, utilizando a matriz de covariância e o vetor de retornos, definidos no dicionário NULL_DIC. O cálculo do retorno e risco anualizado do portfolio é feito usando as seguintes equações: 
    """)
    st.latex("""
    \\text{{Retorno}}_{\\text{{carteira}}} = \sum X[I] \cdot \\text{{RETURN}}[I] \cdot T_Y \\tag{3}
    """)
    st.markdown("""
    Onde:
    
    $X[I]$: é a lista de pesos para os ativos.
    
    $RETURN$: é a lista de retorno dos ativos.
    
    $T_Y$: é o número de dias que a bolsa  opera em 1 ano.
    """)
    st.latex("""
    \\text{{VAR}} = \sum X[I] \cdot X[J] \cdot \\text{{COVARIANCE}}[I, J] \cdot T_Y \\tag{4}
    """)
    st.markdown("""
    Onde: 
    
    $X[I]$: é a lista de pesos para os ativos.
    
    $COVARIANCE[I,J]$: é a matriz de covariância.
    
    $T_Y$: é o número de dias que a bolsa  opera em 1 ano.
    """)
    st.latex("""
    \\text{{Risco}}_{\\text{{carteira}}} = \sqrt{{\\text{{Var}}}} \\tag{5}
    """)
    st.markdown("""
    - A função objetiva do problema de otimização, definida como o índice de Sharpe negativo do portfólio (de forma a transformar o problema de maximização em minimização), acrescido de uma penalização às violações da restrição de investimento em cada ativo do portfólio.
    
    Por fim, o código define os limites de investimento $(X_L e X_U)$, o dicionário **NULL_DIC**, contendo as informações necessárias para a resolução do problema de otimização, e os parâmetros do algoritmo **Firefly (PARAMETERS)**. A função **OF_FUNCTION** é utilizada como a função objetivo do algoritmo, e a função **PORTIFOLIO_RETURN_RISK** é utilizada para calcular o retorno e risco do portfólio em cada iteração do algoritmo.
    
    """)