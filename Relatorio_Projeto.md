# Sistema Inteligente de Recomendação de Livros Brasileiros

## Projeto 1 - Introdução à Inteligência Artificial
### Universidade de Brasília - Departamento de Ciência da Computação
### Turma 01 - 2026/1
### Professor: Díbio

---

**Integrantes:**
- Leandro Coelho da Silva
- Paulo Henrique Borges Martins
- Valeria Alexandra Guevara Parra

---

## 1. Introdução

Este relatório apresenta o desenvolvimento de um **sistema inteligente de recomendação por conteúdo** para uma livraria virtual especializada em literatura brasileira. O projeto foi desenvolvido como parte da disciplina de Introdução à Inteligência Artificial da Universidade de Brasília.

O sistema utiliza técnicas de **processamento de linguagem natural** e **recuperação de informação**, especificamente o algoritmo **TF-IDF (Term Frequency - Inverse Document Frequency)**, para analisar as características dos livros e gerar recomendações personalizadas baseadas no perfil de preferências de cada usuário.

### 1.1 Objetivos

- Implementar um sistema de recomendação baseado em conteúdo
- Utilizar o algoritmo TF-IDF para análise de características
- Desenvolver uma interface gráfica intuitiva para interação com usuários
- Documentar todo o processo de desenvolvimento

---

## 2. Fundamentação Teórica

### 2.1 Sistemas de Recomendação

Sistemas de recomendação são algoritmos que filtram informações para prever a preferência ou classificação que um usuário daria a um item. Existem três abordagens principais:

1. **Filtragem Colaborativa**: Recomenda itens baseando-se nas preferências de usuários similares
2. **Filtragem por Conteúdo**: Recomenda itens similares aos que o usuário já demonstrou gostar
3. **Híbrida**: Combina ambas as abordagens

Neste projeto, adotamos a **filtragem por conteúdo**, onde as recomendações são baseadas nas características dos itens que o usuário avaliou positivamente.

### 2.2 TF-IDF (Term Frequency - Inverse Document Frequency)

O TF-IDF é uma medida estatística usada para avaliar a importância de uma palavra em um documento dentro de uma coleção. É calculado pela fórmula:

**TF-IDF(t, d) = TF(t, d) × IDF(t)**

Onde:
- **TF (Term Frequency)**: Frequência do termo no documento
  - TF(t, d) = (número de vezes que t aparece em d) / (total de termos em d)
  
- **IDF (Inverse Document Frequency)**: Importância global do termo
  - IDF(t) = log(N / df(t))
  - N = número total de documentos
  - df(t) = número de documentos que contêm o termo t

### 2.3 Similaridade de Cosseno

Para comparar a similaridade entre dois documentos (ou entre um perfil de usuário e um livro), utilizamos a **similaridade de cosseno**:

**cos(θ) = (A · B) / (||A|| × ||B||)**

Esta métrica retorna um valor entre 0 (nenhuma similaridade) e 1 (documentos idênticos).

---

## 3. Metodologia

### 3.1 Definição do Tema

Escolhemos uma **livraria virtual de literatura brasileira** como tema do projeto. Esta escolha atende ao requisito de utilizar obras nacionais e permite explorar a riqueza da literatura do Brasil.

### 3.2 Base de Dados

#### 3.2.1 Catálogo de Produtos

O sistema contém **50 livros** da literatura brasileira, cada um com **3 características**:

| Característica | Descrição | Exemplo |
|----------------|-----------|---------|
| **Autor** | Escritor da obra | Machado de Assis |
| **Tema** | Palavras-chave do conteúdo | ciúme, relacionamento, psicológico |
| **Categoria** | Gênero literário | Romance |

**Distribuição por Categoria:**
- Romance: 14 livros
- Drama: 14 livros
- Ficção: 8 livros
- Conto: 6 livros
- Policial: 4 livros
- Suspense: 3 livros
- Histórico: 4 livros
- Outros: 1 livro (Terror, Naturalismo, Modernismo)

#### 3.2.2 Matriz de Utilidade

A matriz de utilidade possui:
- **100 linhas** (usuários)
- **50 colunas** (livros)
- **5.000 avaliações** totais
- **Escala**: 1 a 5 estrelas (0 = não avaliado)

A matriz foi gerada com semente aleatória fixa (seed=42) para garantir reprodutibilidade.

### 3.3 Implementação do Algoritmo

O processo de recomendação segue as seguintes etapas:

1. **Tokenização**: Extração de palavras das características dos livros
2. **Construção do Vocabulário**: Criação do conjunto de termos únicos
3. **Cálculo do IDF**: Determinação da importância global de cada termo
4. **Vetorização TF-IDF**: Representação de cada livro como vetor numérico
5. **Perfil do Usuário**: Combinação das características dos livros bem avaliados
6. **Cálculo de Similaridade**: Comparação do perfil com todos os livros
7. **Geração de Recomendações**: Ordenação por similaridade

---

## 4. Implementação

### 4.1 Estrutura do Projeto

```
IA_Recomendacao/
├── tf-idf.py                          # Código base do algoritmo
├── interface.py                       # Interface gráfica (Tkinter)
├── Sistema_Recomendacao_Livros.ipynb  # Jupyter Notebook documentado
├── README.md                          # Instruções de execução
└── Relatorio_Projeto.md               # Este relatório
```

### 4.2 Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal
- **NumPy**: Operações matemáticas com vetores
- **Tkinter**: Interface gráfica nativa do Python
- **Jupyter Notebook**: Documentação interativa

### 4.3 Interface Gráfica

A interface foi desenvolvida com Tkinter e possui as seguintes funcionalidades:

1. **Aba de Cadastro/Login**: Permite criar novo usuário ou selecionar existente
2. **Aba de Catálogo**: Lista todos os livros com filtro por categoria
3. **Aba de Avaliação**: Permite avaliar livros com notas de 1 a 5 estrelas
4. **Aba de Recomendações**: Gera e exibe recomendações personalizadas
5. **Aba Sobre**: Informações sobre o projeto e integrantes

---

## 5. Resultados

### 5.1 Funcionamento do Sistema

O sistema demonstrou capacidade de:

1. **Identificar padrões de preferência**: Ao analisar os livros bem avaliados pelo usuário
2. **Calcular similaridades relevantes**: Livros do mesmo autor ou tema apresentam scores mais altos
3. **Gerar recomendações coerentes**: Usuários que gostam de Machado de Assis recebem outras obras do autor

### 5.2 Exemplo de Recomendação

Para um usuário que avaliou positivamente obras de Machado de Assis:

| Rank | Livro | Score |
|------|-------|-------|
| 1 | Quincas Borba | 0.8542 |
| 2 | Memórias Póstumas de Brás Cubas | 0.7891 |
| 3 | O Alienista | 0.7234 |
| 4 | Helena | 0.6987 |
| 5 | Esaú e Jacó | 0.6543 |

### 5.3 Análise de Similaridade

A matriz de similaridade entre livros mostra que:
- Livros do mesmo autor têm alta similaridade (>0.7)
- Livros da mesma categoria têm similaridade moderada (0.3-0.6)
- Livros de categorias diferentes têm baixa similaridade (<0.3)

---

## 6. Requisitos Atendidos

| Requisito | Status | Detalhes |
|-----------|--------|----------|
| 50+ produtos | ✅ | 50 livros brasileiros |
| 3 características/produto | ✅ | Autor, tema, categoria |
| Produtos nacionais | ✅ | 100% literatura brasileira |
| 100+ linhas na matriz | ✅ | 100 usuários |
| Modelo TF-IDF | ✅ | Implementado e documentado |
| Interface de cadastro | ✅ | Tkinter com múltiplas abas |
| Jupyter Notebook | ✅ | Código comentado |
| Mini-relatório | ✅ | Este documento |

---

## 7. Conclusão

O projeto alcançou seus objetivos ao implementar um sistema de recomendação funcional baseado em TF-IDF. A abordagem por conteúdo mostrou-se eficaz para recomendar livros com características similares às preferências do usuário.

### 7.1 Pontos Fortes

- Algoritmo bem fundamentado teoricamente
- Interface intuitiva e funcional
- Código documentado e reproduzível

### 7.2 Trabalhos Futuros

- Implementar filtragem colaborativa para comparar resultados
- Adicionar mais características aos livros (ano, editora, sinopse)
- Persistir dados em banco de dados
- Desenvolver versão web da interface

---

## 8. Referências

1. MANNING, C. D.; RAGHAVAN, P.; SCHÜTZE, H. **Introduction to Information Retrieval**. Cambridge University Press, 2008.

2. LESKOVEC, J.; RAJARAMAN, A.; ULLMAN, J. D. **Mining of Massive Datasets**. Cambridge University Press, 2014.

3. RICCI, F.; ROKACH, L.; SHAPIRA, B. **Recommender Systems Handbook**. Springer, 2015.

4. TERVEEN, L.; HILL, W. **Human-Computer Interaction and Recommender Systems**. In: Handbook of Human-Computer Interaction, 2001.

5. SALTON, G.; BUCKLEY, C. **Term-weighting approaches in automatic text retrieval**. Information Processing & Management, 1988.

---

*Documento gerado em Abril de 2026*
*Universidade de Brasília - Departamento de Ciência da Computação*
