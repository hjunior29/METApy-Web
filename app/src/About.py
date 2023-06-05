import streamlit as st

import func

st.set_page_config(layout="wide", page_icon="app/src/images/META_logo.png")

func.style_setup()

st.image("app/src/images/META_logo.png", width=150)

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
