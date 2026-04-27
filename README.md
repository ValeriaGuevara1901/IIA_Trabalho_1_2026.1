# 📚 Sistema de Recomendação de Livros Brasileiros

Sistema inteligente de recomendação por conteúdo utilizando TF-IDF para literatura brasileira.

**Disciplina:** Introdução à Inteligência Artificial — UnB 2026/1  
**Professor:** Díbio  
**Repositório:** https://github.com/ValeriaGuevara1901/IIA_Trabalho_1_2026.1

## 👥 Integrantes

- Leandro Coelho da Silva
- Paulo Henrique Borges Martins
- Valeria Alexandra Guevara Parra

---

## 📋 Descrição do Projeto

Este projeto implementa um sistema de recomendação baseado em conteúdo para uma livraria virtual de literatura brasileira. O sistema utiliza o algoritmo **TF-IDF (Term Frequency - Inverse Document Frequency)** para analisar as características dos livros e gerar recomendações personalizadas.

### Características:
- ✅ 50 livros da literatura brasileira
- ✅ 3 características por livro (autor, tema, categoria)
- ✅ 100 usuários de treinamento
- ✅ Matriz de utilidade com 5.000 avaliações
- ✅ Escala de avaliação: 1-5 estrelas

---

## 📁 Estrutura do Projeto

```
IIA_Trabalho_1_2026.1/
│
├── tf-idf.py                              # Código original do algoritmo TF-IDF
├── app.py                                 # Backend Flask — servidor web
├── templates/
│   └── index.html                         # Interface visual (HTML/CSS/JS)
├── Recomendacao_Livros_COLAB.ipynb        # Notebook pronto para Google Colab
├── Sistema_Recomendacao_Livros.ipynb      # Jupyter Notebook documentado
├── Relatorio_Projeto.md                   # Mini-relatório do projeto
└── README.md                              # Este arquivo
```

---

## 🔧 Pré-requisitos

**Python 3.7 ou superior** — verifique com:
```bash
python --version
```

Instale as dependências de uma vez:
```bash
pip install --user flask numpy
```

> **Windows:** se `pip install` der erro de permissão, use sempre `pip install --user`.

---

## 🚀 Como Executar

### ✅ Opção 1 — Interface Web com Flask (Recomendado)

> A interface visual fica no arquivo `templates/index.html`, mas **não abra esse arquivo diretamente**.  
> Ele só funciona quando o servidor Flask estiver rodando.

**Passo a passo:**

1. Instale as dependências (apenas uma vez):
   ```bash
   pip install --user flask numpy
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd "caminho/para/IIA_Trabalho_1_2026.1"
   ```

3. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
   Você verá no terminal:
   ```
   * Running on http://127.0.0.1:5000
   ```

4. **Abra o navegador** e acesse:
   ```
   http://localhost:5000
   ```
   ⚠️ **NÃO abra o `index.html` diretamente** — abra sempre pelo navegador via `http://localhost:5000`.

5. Para parar o servidor: `Ctrl + C` no terminal.

---

### ✅ Opção 2 — Google Colab (sem instalar nada)

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. Clique em **Arquivo → Fazer upload de notebook**
3. Selecione o arquivo `Recomendacao_Livros_COLAB.ipynb`
4. Execute as células em ordem com `Shift + Enter`

---

### Opção 3 — Código Base (Terminal)

```bash
python tf-idf.py
```

### Opção 4 — Jupyter Notebook local

```bash
pip install --user jupyter
jupyter notebook
```
Abra `Sistema_Recomendacao_Livros.ipynb` e execute as células em ordem.

---

## 📖 Guia de Uso da Interface

### 1. Cadastro/Login

![Aba Login](docs/login.png)

- **Usuário existente**: Selecione na lista e clique em "Entrar"
- **Novo usuário**: Digite seu nome e clique em "Cadastrar"

### 2. Catálogo de Livros

![Aba Catálogo](docs/catalogo.png)

- Visualize todos os 50 livros disponíveis
- Use o filtro de categoria para encontrar gêneros específicos
- Clique em um livro para ver detalhes

### 3. Avaliar Livros

![Aba Avaliar](docs/avaliar.png)

1. Selecione um livro na lista
2. Escolha uma nota de 1 a 5 estrelas
3. Clique em "Enviar Avaliação"

> **Dica**: Avalie pelo menos 5-10 livros para recomendações mais precisas!

### 4. Receber Recomendações

![Aba Recomendações](docs/recomendacoes.png)

1. Defina quantas recomendações deseja (1-20)
2. Clique em "Gerar Recomendações"
3. Veja os livros recomendados com seus scores de similaridade

---

## 🧮 Como Funciona o Algoritmo

### TF-IDF (Term Frequency - Inverse Document Frequency)

1. **Tokenização**: Extrai palavras das características dos livros
2. **TF (Term Frequency)**: Calcula frequência de cada termo no documento
3. **IDF (Inverse Document Frequency)**: Calcula importância global do termo
4. **TF-IDF**: Multiplica TF × IDF para obter peso do termo

### Processo de Recomendação

```
Usuário avalia livros
        ↓
Sistema identifica os 10 livros mais bem avaliados
        ↓
Combina características em um vetor TF-IDF
        ↓
Calcula similaridade de cosseno com todos os livros
        ↓
Ordena por similaridade e retorna top N
```

---

## 📊 Convertendo o Relatório para PDF

### Opção 1: Usando Pandoc (Recomendado)

1. Instale o Pandoc: https://pandoc.org/installing.html
2. Execute:
   ```bash
   pandoc Relatorio_Projeto.md -o Relatorio_Projeto.pdf
   ```

### Opção 2: VS Code com extensão

1. Instale a extensão "Markdown PDF" no VS Code
2. Abra `Relatorio_Projeto.md`
3. Pressione `Ctrl+Shift+P` → "Markdown PDF: Export (pdf)"

### Opção 3: Online

1. Acesse https://www.markdowntopdf.com/
2. Cole o conteúdo do arquivo .md
3. Baixe o PDF gerado

### Opção 4: Jupyter Notebook

1. Abra o notebook `Sistema_Recomendacao_Livros.ipynb`
2. File → Download as → PDF via LaTeX

---

## 🧪 Testando o Sistema

### Teste Rápido

```python
# Após executar interface.py ou tf-idf.py

# 1. Cadastre um novo usuário
register_user("Seu Nome")

# 2. Avalie alguns livros
rate_book(100, 0, 5)   # Dom Casmurro - 5 estrelas
rate_book(100, 1, 4)   # Memórias Póstumas - 4 estrelas
rate_book(100, 10, 5)  # Quincas Borba - 5 estrelas

# 3. Obtenha recomendações
recomend_books(100)
```

### Resultado Esperado

Se você avaliou bem obras de Machado de Assis, deve receber recomendações de outros livros do mesmo autor ou com temas similares.

---

## 📝 Requisitos do Projeto Atendidos

| Requisito | Status |
|-----------|--------|
| 50+ produtos | ✅ 50 livros |
| 3 características/produto | ✅ Autor, tema, categoria |
| Produtos nacionais | ✅ 100% brasileiro |
| 100+ linhas na matriz | ✅ 100 usuários |
| Modelo TF-IDF documentado | ✅ |
| Interface para cadastro | ✅ Tkinter |
| Jupyter Notebook | ✅ |
| Mini-relatório | ✅ |

---

## 🐛 Solução de Problemas

### Erro: "No module named 'numpy'"
```bash
pip install numpy
```

### Erro: "No module named 'tkinter'"
No Windows, reinstale Python marcando "tcl/tk and IDLE" durante a instalação.

No Linux:
```bash
sudo apt-get install python3-tk
```

### Interface não abre
Verifique se está usando Python 3.x:
```bash
python3 interface.py
```

---

## 📚 Referências

1. Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval*
2. Leskovec, J., Rajaraman, A., & Ullman, J. D. (2014). *Mining of Massive Datasets*
3. Ricci, F., Rokach, L., & Shapira, B. (2015). *Recommender Systems Handbook*

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte da disciplina de Introdução à Inteligência Artificial da Universidade de Brasília.

---

**Universidade de Brasília - 2026**
