import streamlit as st

import func

st.image("images/META_logo.png", width=150)

func.style_setup()

st.markdown("""

# Problemas de Otimização

Os problemas de otimização estão presentes em diversas áreas, como engenharia, economia, logística e ciências da computação. Eles envolvem a busca pela melhor solução possível de acordo com uma função objetivo, que pode ser minimizada ou maximizada, e estão sujeitos a determinadas restrições.

Alguns exemplos de problemas de otimização incluem:

- **Problema do Caixeiro Viajante (TSP)**: Encontrar a rota mais curta que passa por um conjunto de cidades e retorna à cidade de origem, visitando cada cidade apenas uma vez.
- **Problema da Mochila (KP)**: Dado um conjunto de itens com pesos e valores, determinar a combinação de itens que maximiza o valor total sem exceder a capacidade da mochila.
- **Otimização de Portfólio**: Selecionar a combinação de ativos que maximiza o retorno esperado do investimento, sujeito a restrições de risco e liquidez.
- **Escalonamento de Tarefas**: Alocar recursos e programar tarefas de forma a minimizar o tempo total de conclusão, atendendo a restrições de precedência e disponibilidade de recursos.

Os algoritmos de otimização são técnicas e métodos utilizados para encontrar soluções ótimas ou aproximadamente ótimas para esses problemas. Neste site, você aprenderá sobre algoritmos de otimização e como aplicá-los a diversos problemas do mundo real.

""")

st.markdown("""
# Algoritmos de Otimização

Os algoritmos de otimização são técnicas e métodos usados para encontrar soluções ótimas ou aproximadamente ótimas para problemas de otimização. Eles têm ampla aplicação em áreas como engenharia, economia, logística e ciências da computação.

Aqui estão alguns exemplos de algoritmos de otimização populares:

- **Algoritmo Genético (GA)**: Baseado na teoria da evolução natural, os algoritmos genéticos utilizam operadores genéticos, como seleção, cruzamento e mutação, para explorar e explotar o espaço de busca de soluções.
- **Algoritmo de Enxame de Partículas (PSO)**: Inspirado no comportamento de enxames de pássaros e peixes, o PSO ajusta as posições das partículas no espaço de busca com base em suas melhores soluções individuais e coletivas.
- **Otimização de Colônia de Formigas (ACO)**: Baseado no comportamento das formigas na busca por alimentos, o ACO utiliza feromônios artificiais para guiar a busca por soluções ótimas em problemas discretos e contínuos.
- **Simulated Annealing (SA)**: Inspirado no processo de recozimento de metais, o SA é uma técnica de otimização estocástica que explora o espaço de busca por meio de movimentos aleatórios, aceitando soluções piores com uma probabilidade decrescente ao longo do tempo.

Neste site, você encontrará informações e tutoriais sobre como aplicar esses algoritmos de otimização a uma variedade de problemas do mundo real.
    """)


st.title("Sobre o projeto")
st.write("Bem-vindo à página do nosso projeto de pesquisa em Ciências de Dados, onde buscamos discutir e aplicar modelos matemáticos, estatísticos e de inteligência computacional para resolver problemas complexos do mundo real. Este projeto abrange uma ampla gama de abordagens, incluindo algoritmos clássicos de otimização linear e não linear, econométricos, metaheurísticas e machine learning..")
st.write("Nosso projeto é dividido em três frentes principais de pesquisa:")

st.markdown(
    """
    - Estudo do framework dos modelos matemáticos, estatísticos e de inteligência computacional
    - Análise de algoritmos existentes na literatura e proposição de algoritmos híbridos
    - Implementação dos algoritmos propostos em problemas reais
    """
)

st.write("Nossas áreas de aplicação incluem, mas não se limitam a, problemas de predição e otimização em dados do mercado financeiro, produção e produtividade de grãos, clima, educação e pesquisa, e saúde. Acreditamos que o uso de soluções computacionais eficientes e avançadas pode levar a descobertas significativas e melhorias nessas áreas.")

st.write("Além disso, organizamos um desafio em Ciências de Dados nas edições do Congresso de Ciência e Tecnologia da PUC Goiás. Este evento permite que alunos de graduação e pós-graduação apliquem modelos para resolver problemas usando bases de dados reais. A primeira edição foi realizada com sucesso em 2021/2 e continuamos a construir e expandir este evento para envolver mais estudantes e promover a pesquisa em Ciências de Dados.")

st.write("Convidamos você a explorar nosso projeto e descobrir como a aplicação de modelos matemáticos, estatísticos e de inteligência computacional pode levar a soluções inovadoras para os desafios que enfrentamos em diversas áreas. Junte-se a nós nesta jornada de pesquisa e descoberta, enquanto trabalhamos para criar um impacto positivo no mundo através da ciência de dados.")


def upload_file():
    st.markdown("Faça o upload do seu arquivo abaixo:")

    uploaded_file = st.file_uploader("Selecione o arquivo", type=['txt', 'csv', 'json', 'xlsx'])

    if uploaded_file is not None:
        file_details = {
            "Filename": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size
        }
        st.write(file_details)

        # Exibir o conteúdo do arquivo (assumindo que é um arquivo de texto)
        st.text(uploaded_file.getvalue())