"""
Sistema de Recomendação de Livros Brasileiros
Interface Gráfica com Tkinter
Disciplina: Introdução à Inteligência Artificial - UnB 2026/1

Integrantes:
- Leandro Coelho da Silva
- Paulo Henrique Borges Martins  
- Valeria Alexandra Guevara Parra
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
import re
import random

# ==================== DADOS DO SISTEMA ====================

users = [
    {"id": 0, "nome": "Leandro Coelho da Silva"},
    {"id": 1, "nome": "Paulo Henrique Borges Martins"},
    {"id": 2, "nome": "Valeria Alexandra Guevara Parra"},
    {"id": 3, "nome": "Carla Santos"},
    {"id": 4, "nome": "Daniel Oliveira"},
    {"id": 5, "nome": "Eduarda Lima"},
    {"id": 6, "nome": "Felipe Costa"},
    {"id": 7, "nome": "Gabriela Alves"},
    {"id": 8, "nome": "Henrique Pereira"},
    {"id": 9, "nome": "Isabela Rodrigues"},
    {"id": 10, "nome": "João Ferreira"},
    {"id": 11, "nome": "Karina Gomes"},
    {"id": 12, "nome": "Lucas Ribeiro"},
    {"id": 13, "nome": "Mariana Carvalho"},
    {"id": 14, "nome": "Nicolas Martins"},
    {"id": 15, "nome": "Olivia Rocha"},
    {"id": 16, "nome": "Paulo Barros"},
    {"id": 17, "nome": "Renata Dias"},
    {"id": 18, "nome": "Samuel Teixeira"},
    {"id": 19, "nome": "Tatiane Freitas"},
    {"id": 20, "nome": "Victor Araújo"},
    {"id": 21, "nome": "Wesley Batista"},
    {"id": 22, "nome": "Yasmin Duarte"},
    {"id": 23, "nome": "Zeca Moura"},
    {"id": 24, "nome": "Amanda Melo"},
    {"id": 25, "nome": "Brenda Nunes"},
    {"id": 26, "nome": "Caio Farias"},
    {"id": 27, "nome": "Débora Pires"},
    {"id": 28, "nome": "Enzo Castro"},
    {"id": 29, "nome": "Fernanda Lopes"},
    {"id": 30, "nome": "Gustavo Rezende"},
    {"id": 31, "nome": "Helena Moreira"},
    {"id": 32, "nome": "Igor Batista"},
    {"id": 33, "nome": "Juliana Borges"},
    {"id": 34, "nome": "Kevin Andrade"},
    {"id": 35, "nome": "Larissa Moura"},
    {"id": 36, "nome": "Mateus Tavares"},
    {"id": 37, "nome": "Natália Duarte"},
    {"id": 38, "nome": "Otávio Cunha"},
    {"id": 39, "nome": "Priscila Ramos"},
    {"id": 40, "nome": "Rafael Neves"},
    {"id": 41, "nome": "Sabrina Coelho"},
    {"id": 42, "nome": "Thiago Cardoso"},
    {"id": 43, "nome": "Ursula Mendes"},
    {"id": 44, "nome": "Vanessa Teixeira"},
    {"id": 45, "nome": "William Nogueira"},
    {"id": 46, "nome": "Xavier Pinto"},
    {"id": 47, "nome": "Yuri Monteiro"},
    {"id": 48, "nome": "Zilda Campos"},
    {"id": 49, "nome": "Alice Barreto"},
    {"id": 50, "nome": "Beatriz Falcão"},
    {"id": 51, "nome": "César Fonseca"},
    {"id": 52, "nome": "Davi Guimarães"},
    {"id": 53, "nome": "Elisa Monteiro"},
    {"id": 54, "nome": "Fábio Torres"},
    {"id": 55, "nome": "Giovana Peixoto"},
    {"id": 56, "nome": "Hugo Duarte"},
    {"id": 57, "nome": "Irene Pacheco"},
    {"id": 58, "nome": "Jonas Vieira"},
    {"id": 59, "nome": "Kátia Braga"},
    {"id": 60, "nome": "Leonardo Mendes"},
    {"id": 61, "nome": "Mirela Cunha"},
    {"id": 62, "nome": "Noah Batista"},
    {"id": 63, "nome": "Otília Campos"},
    {"id": 64, "nome": "Pedro Lemos"},
    {"id": 65, "nome": "Quésia Rocha"},
    {"id": 66, "nome": "Ricardo Azevedo"},
    {"id": 67, "nome": "Sérgio Freire"},
    {"id": 68, "nome": "Talita Coelho"},
    {"id": 69, "nome": "Ulisses Matos"},
    {"id": 70, "nome": "Vitor Sales"},
    {"id": 71, "nome": "Wellington Cruz"},
    {"id": 72, "nome": "Ximena Luz"},
    {"id": 73, "nome": "Yago Barros"},
    {"id": 74, "nome": "Zuleica Prado"},
    {"id": 75, "nome": "André Nascimento"},
    {"id": 76, "nome": "Bianca Queiroz"},
    {"id": 77, "nome": "Claudio Reis"},
    {"id": 78, "nome": "Denise Albuquerque"},
    {"id": 79, "nome": "Elias Pinheiro"},
    {"id": 80, "nome": "Flávia Antunes"},
    {"id": 81, "nome": "Gilberto Moraes"},
    {"id": 82, "nome": "Heloísa Xavier"},
    {"id": 83, "nome": "Ian Macedo"},
    {"id": 84, "nome": "Jéssica Teles"},
    {"id": 85, "nome": "Kleber Santos"},
    {"id": 86, "nome": "Luan Peçanha"},
    {"id": 87, "nome": "Márcia Vasconcelos"},
    {"id": 88, "nome": "Natan Figueiredo"},
    {"id": 89, "nome": "Orlando Meireles"},
    {"id": 90, "nome": "Patrícia Xavier"},
    {"id": 91, "nome": "Rogério Maciel"},
    {"id": 92, "nome": "Silvia Duarte"},
    {"id": 93, "nome": "Túlio Barbosa"},
    {"id": 94, "nome": "Viviane Soares"},
    {"id": 95, "nome": "Wagner Peixoto"},
    {"id": 96, "nome": "Yasmin Coelho"},
    {"id": 97, "nome": "Zé Carlos"},
    {"id": 98, "nome": "Arthur Nogueira"},
    {"id": 99, "nome": "Bruna Medeiros"}
]

books = [
    {"id": 0, "nome": "Dom Casmurro", "autor": "Machado de Assis", "tema": "ciúme relacionamento psicológico", "categoria": "Romance"},
    {"id": 1, "nome": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "tema": "ironia sociedade morte", "categoria": "Romance"},
    {"id": 2, "nome": "Capitães da Areia", "autor": "Jorge Amado", "tema": "infância pobreza marginalização", "categoria": "Drama"},
    {"id": 3, "nome": "O Cortiço", "autor": "Aluísio Azevedo", "tema": "determinismo ambiente sociedade", "categoria": "Naturalismo"},
    {"id": 4, "nome": "Iracema", "autor": "José de Alencar", "tema": "indígena amor colonização", "categoria": "Romance"},
    {"id": 5, "nome": "Senhora", "autor": "José de Alencar", "tema": "casamento interesse sociedade", "categoria": "Romance"},
    {"id": 6, "nome": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "tema": "romance juventude amor", "categoria": "Romance"},
    {"id": 7, "nome": "Vidas Secas", "autor": "Graciliano Ramos", "tema": "seca miséria sobrevivência", "categoria": "Drama"},
    {"id": 8, "nome": "Grande Sertão: Veredas", "autor": "João Guimarães Rosa", "tema": "sertão existência conflito", "categoria": "Romance"},
    {"id": 9, "nome": "Os Sertões", "autor": "Euclides da Cunha", "tema": "guerra canudos história", "categoria": "Histórico"},
    {"id": 10, "nome": "Quincas Borba", "autor": "Machado de Assis", "tema": "filosofia loucura sociedade", "categoria": "Romance"},
    {"id": 11, "nome": "Helena", "autor": "Machado de Assis", "tema": "família romance segredo", "categoria": "Romance"},
    {"id": 12, "nome": "Esaú e Jacó", "autor": "Machado de Assis", "tema": "política conflito irmãos", "categoria": "Romance"},
    {"id": 13, "nome": "O Alienista", "autor": "Machado de Assis", "tema": "loucura ciência crítica", "categoria": "Conto"},
    {"id": 14, "nome": "Lucíola", "autor": "José de Alencar", "tema": "amor redenção sociedade", "categoria": "Romance"},
    {"id": 15, "nome": "O Guarani", "autor": "José de Alencar", "tema": "aventura indígena heroísmo", "categoria": "Romance"},
    {"id": 16, "nome": "Casa-Grande & Senzala", "autor": "Gilberto Freyre", "tema": "sociedade escravidão cultura", "categoria": "Histórico"},
    {"id": 17, "nome": "Raízes do Brasil", "autor": "Sérgio Buarque de Holanda", "tema": "identidade cultura política", "categoria": "Histórico"},
    {"id": 18, "nome": "Sagarana", "autor": "João Guimarães Rosa", "tema": "sertão contos regionalismo", "categoria": "Conto"},
    {"id": 19, "nome": "Macunaíma", "autor": "Mário de Andrade", "tema": "identidade folclore brasil", "categoria": "Modernismo"},
    {"id": 20, "nome": "A Hora da Estrela", "autor": "Clarice Lispector", "tema": "existência pobreza identidade", "categoria": "Drama"},
    {"id": 21, "nome": "Laços de Família", "autor": "Clarice Lispector", "tema": "relações humanas cotidiano introspecção", "categoria": "Conto"},
    {"id": 22, "nome": "Felicidade Clandestina", "autor": "Clarice Lispector", "tema": "infância desejo leitura", "categoria": "Conto"},
    {"id": 23, "nome": "O Quinze", "autor": "Rachel de Queiroz", "tema": "seca nordeste sobrevivência", "categoria": "Drama"},
    {"id": 24, "nome": "Menino de Engenho", "autor": "José Lins do Rego", "tema": "infância engenho memória", "categoria": "Romance"},
    {"id": 25, "nome": "São Bernardo", "autor": "Graciliano Ramos", "tema": "poder ambição solidão", "categoria": "Drama"},
    {"id": 26, "nome": "Angústia", "autor": "Graciliano Ramos", "tema": "psicológico obsessão ansiedade", "categoria": "Drama"},
    {"id": 27, "nome": "O Tempo e o Vento", "autor": "Erico Verissimo", "tema": "história família brasil", "categoria": "Histórico"},
    {"id": 28, "nome": "Incidente em Antares", "autor": "Erico Verissimo", "tema": "política sátira sociedade", "categoria": "Ficção"},
    {"id": 29, "nome": "Dois Irmãos", "autor": "Milton Hatoum", "tema": "família conflito identidade", "categoria": "Drama"},
    {"id": 30, "nome": "Relato de um Certo Oriente", "autor": "Milton Hatoum", "tema": "memória cultura imigração", "categoria": "Drama"},
    {"id": 31, "nome": "Budapeste", "autor": "Chico Buarque", "tema": "identidade linguagem duplicidade", "categoria": "Ficção"},
    {"id": 32, "nome": "Leite Derramado", "autor": "Chico Buarque", "tema": "memória decadência sociedade", "categoria": "Drama"},
    {"id": 33, "nome": "Estorvo", "autor": "Chico Buarque", "tema": "alienação urbana confusão", "categoria": "Ficção"},
    {"id": 34, "nome": "Nove Noites", "autor": "Bernardo Carvalho", "tema": "mistério antropologia identidade", "categoria": "Ficção"},
    {"id": 35, "nome": "Barba Ensopada de Sangue", "autor": "Daniel Galera", "tema": "isolamento identidade violência", "categoria": "Ficção"},
    {"id": 36, "nome": "O Filho Eterno", "autor": "Cristovão Tezza", "tema": "paternidade deficiência aceitação", "categoria": "Drama"},
    {"id": 37, "nome": "Azul Corvo", "autor": "Adriana Lisboa", "tema": "identidade juventude viagem", "categoria": "Ficção"},
    {"id": 38, "nome": "Torto Arado", "autor": "Itamar Vieira Junior", "tema": "terra escravidão identidade", "categoria": "Drama"},
    {"id": 39, "nome": "Ponciá Vicêncio", "autor": "Conceição Evaristo", "tema": "identidade negra memória resistência", "categoria": "Drama"},
    {"id": 40, "nome": "Olhos d'Água", "autor": "Conceição Evaristo", "tema": "racismo cotidiano violência", "categoria": "Conto"},
    {"id": 41, "nome": "Cidade de Deus", "autor": "Paulo Lins", "tema": "violência favela crime", "categoria": "Drama"},
    {"id": 42, "nome": "Elite da Tropa", "autor": "Luiz Eduardo Soares", "tema": "polícia violência corrupção", "categoria": "Policial"},
    {"id": 43, "nome": "Abusado", "autor": "Caco Barcellos", "tema": "tráfico crime realidade", "categoria": "Policial"},
    {"id": 44, "nome": "Inferno", "autor": "Patrícia Melo", "tema": "crime violência sociedade", "categoria": "Policial"},
    {"id": 45, "nome": "Manual Prático do Ódio", "autor": "Ferréz", "tema": "periferia violência desigualdade", "categoria": "Policial"},
    {"id": 46, "nome": "Dias Perfeitos", "autor": "Raphael Montes", "tema": "obsessão sequestro psicopatia", "categoria": "Suspense"},
    {"id": 47, "nome": "Jantar Secreto", "autor": "Raphael Montes", "tema": "segredo amizade horror", "categoria": "Suspense"},
    {"id": 48, "nome": "Suicidas", "autor": "Raphael Montes", "tema": "mistério morte jogo", "categoria": "Suspense"},
    {"id": 49, "nome": "O Vilarejo", "autor": "Raphael Montes", "tema": "terror contos violência", "categoria": "Terror"}
]

# Matriz de utilidade: ratings[user_id][book_id] = nota (1-5)
random.seed(42)  # Para reprodutibilidade
ratings = []
for i in range(100):
    grades = []
    for j in range(50):
        grades.append(random.randint(0, 5))
    ratings.append(grades)

# ==================== ALGORITMO TF-IDF ====================

documents = []

def tokenize(text):
    """Tokeniza o texto, extraindo apenas palavras."""
    return re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', text.lower())

# Prepara documentos para cada livro
for book in books:
    phrase = book["autor"] + " " + book["tema"] + " " + book["categoria"]
    tokens = tokenize(phrase)
    documents.append(tokens)

# Vocabulário único
word_set = set()
for doc in documents:
    word_set.update(doc)
word_set = list(word_set)
index_dict = {word: i for i, word in enumerate(word_set)}
total_docs = len(documents)

def compute_idf():
    """Calcula o IDF (Inverse Document Frequency) para cada palavra."""
    word_count = {word: 0 for word in word_set}
    for word in word_set:
        for doc in documents:
            if word in doc:
                word_count[word] += 1
    idf = {}
    for word in word_set:
        idf[word] = np.log(total_docs / (word_count[word] + 1))
    return idf

idf = compute_idf()

def termfreq(document, word):
    """Calcula a frequência do termo (TF)."""
    return document.count(word) / len(document)

def tf_idf(document):
    """Calcula o vetor TF-IDF para um documento."""
    vec = np.zeros(len(word_set))
    for word in document:
        if word in index_dict:
            tf = termfreq(document, word)
            vec[index_dict[word]] = tf * idf[word]
    return vec

# Vetores TF-IDF pré-calculados para todos os livros
vectors = [tf_idf(doc) for doc in documents]

def cosine_similarity(a, b):
    """Calcula a similaridade de cosseno entre dois vetores."""
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def take_top10_rating(idUser):
    """Retorna os IDs dos 10 livros com maiores notas do usuário."""
    return sorted(range(len(ratings[idUser])), key=lambda i: ratings[idUser][i], reverse=True)[:10]

def get_recommendations(userId, top_n=5):
    """Gera recomendações baseadas no perfil do usuário."""
    top10_books = take_top10_rating(userId)
    text = ""
    for i in top10_books:
        text += f" {books[i]['autor']} {books[i]['categoria']} {books[i]['tema']}"
    
    tokens = tokenize(text)
    user_vec = tf_idf(tokens)
    
    similaridades = []
    for i, vec in enumerate(vectors):
        sim = cosine_similarity(user_vec, vec)
        similaridades.append((i, sim))
    
    similaridades.sort(key=lambda x: x[1], reverse=True)
    return similaridades[:top_n]

def register_user(name):
    """Registra um novo usuário no sistema."""
    new_id = len(users)
    users.append({"id": new_id, "nome": name})
    ratings.append([0] * 50)
    return new_id

def rate_book(userId, bookId, rate):
    """Avalia um livro."""
    if userId >= len(users):
        return False, "Usuário não existe."
    if bookId < 0 or bookId >= 50:
        return False, "Livro não existe."
    if rate < 1 or rate > 5:
        return False, "Nota inválida (deve ser entre 1 e 5)."
    ratings[userId][bookId] = rate
    return True, "Avaliação registrada com sucesso!"

# ==================== INTERFACE GRÁFICA ====================

class SistemaRecomendacao:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Sistema de Recomendação de Livros Brasileiros")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        self.current_user_id = None
        
        self.create_widgets()
    
    def create_widgets(self):
        """Cria todos os widgets da interface."""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(main_frame, 
                              text="📚 Sistema de Recomendação de Livros Brasileiros",
                              font=('Helvetica', 18, 'bold'),
                              bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)
        
        subtitle = tk.Label(main_frame,
                           text="Baseado em Filtragem por Conteúdo com TF-IDF",
                           font=('Helvetica', 12),
                           bg='#f0f0f0', fg='#7f8c8d')
        subtitle.pack()
        
        # Notebook para abas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Aba 1: Cadastro/Login
        self.tab_login = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_login, text="👤 Cadastro/Login")
        self.create_login_tab()
        
        # Aba 2: Catálogo de Livros
        self.tab_books = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_books, text="📖 Catálogo")
        self.create_books_tab()
        
        # Aba 3: Avaliações
        self.tab_rate = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_rate, text="⭐ Avaliar")
        self.create_rate_tab()
        
        # Aba 4: Recomendações
        self.tab_recommend = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_recommend, text="🎯 Recomendações")
        self.create_recommend_tab()
        
        # Aba 5: Sobre o Projeto
        self.tab_about = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_about, text="ℹ️ Sobre")
        self.create_about_tab()
        
        # Barra de status
        self.status_var = tk.StringVar()
        self.status_var.set("Bem-vindo! Faça login ou cadastre-se para começar.")
        status_bar = tk.Label(main_frame, textvariable=self.status_var,
                             bd=1, relief=tk.SUNKEN, anchor=tk.W,
                             font=('Helvetica', 10))
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_login_tab(self):
        """Cria a aba de login/cadastro."""
        frame = ttk.LabelFrame(self.tab_login, text="Entrar ou Cadastrar", padding="20")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Seção de Login
        login_frame = ttk.LabelFrame(frame, text="Selecionar Usuário Existente", padding="10")
        login_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(login_frame, text="Usuário:").pack(anchor=tk.W)
        self.user_combo = ttk.Combobox(login_frame, width=50, state="readonly")
        self.user_combo['values'] = [f"{u['id']} - {u['nome']}" for u in users]
        self.user_combo.pack(fill=tk.X, pady=5)
        
        ttk.Button(login_frame, text="Entrar", command=self.login).pack(pady=5)
        
        # Seção de Cadastro
        register_frame = ttk.LabelFrame(frame, text="Cadastrar Novo Usuário", padding="10")
        register_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(register_frame, text="Nome completo:").pack(anchor=tk.W)
        self.name_entry = ttk.Entry(register_frame, width=50)
        self.name_entry.pack(fill=tk.X, pady=5)
        
        ttk.Button(register_frame, text="Cadastrar", command=self.register).pack(pady=5)
        
        # Info do usuário atual
        self.user_info_frame = ttk.LabelFrame(frame, text="Usuário Atual", padding="10")
        self.user_info_frame.pack(fill=tk.X, pady=10)
        
        self.user_info_label = ttk.Label(self.user_info_frame, 
                                         text="Nenhum usuário logado",
                                         font=('Helvetica', 12))
        self.user_info_label.pack()
    
    def create_books_tab(self):
        """Cria a aba do catálogo de livros."""
        frame = ttk.Frame(self.tab_books, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Filtro
        filter_frame = ttk.Frame(frame)
        filter_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(filter_frame, text="Filtrar por categoria:").pack(side=tk.LEFT)
        self.category_filter = ttk.Combobox(filter_frame, width=20, state="readonly")
        categories = list(set(b['categoria'] for b in books))
        self.category_filter['values'] = ['Todas'] + sorted(categories)
        self.category_filter.set('Todas')
        self.category_filter.pack(side=tk.LEFT, padx=5)
        self.category_filter.bind('<<ComboboxSelected>>', self.filter_books)
        
        # Treeview para livros
        columns = ('ID', 'Nome', 'Autor', 'Categoria', 'Temas')
        self.books_tree = ttk.Treeview(frame, columns=columns, show='headings', height=20)
        
        for col in columns:
            self.books_tree.heading(col, text=col)
            if col == 'ID':
                self.books_tree.column(col, width=40)
            elif col == 'Temas':
                self.books_tree.column(col, width=200)
            else:
                self.books_tree.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.books_tree.yview)
        self.books_tree.configure(yscrollcommand=scrollbar.set)
        
        self.books_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.load_books()
    
    def create_rate_tab(self):
        """Cria a aba de avaliação."""
        frame = ttk.LabelFrame(self.tab_rate, text="Avaliar Livros", padding="20")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Seleção de livro
        ttk.Label(frame, text="Selecione o livro:").pack(anchor=tk.W)
        self.book_combo = ttk.Combobox(frame, width=60, state="readonly")
        self.book_combo['values'] = [f"{b['id']} - {b['nome']} ({b['autor']})" for b in books]
        self.book_combo.pack(fill=tk.X, pady=5)
        
        # Nota
        ttk.Label(frame, text="Sua nota (1-5 estrelas):").pack(anchor=tk.W, pady=(10, 0))
        
        stars_frame = ttk.Frame(frame)
        stars_frame.pack(pady=10)
        
        self.rating_var = tk.IntVar(value=3)
        for i in range(1, 6):
            rb = ttk.Radiobutton(stars_frame, text=f"{'⭐' * i}", 
                                variable=self.rating_var, value=i)
            rb.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame, text="Enviar Avaliação", command=self.submit_rating).pack(pady=20)
        
        # Histórico de avaliações do usuário
        self.ratings_frame = ttk.LabelFrame(frame, text="Suas Avaliações", padding="10")
        self.ratings_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.ratings_text = scrolledtext.ScrolledText(self.ratings_frame, height=10, width=60)
        self.ratings_text.pack(fill=tk.BOTH, expand=True)
    
    def create_recommend_tab(self):
        """Cria a aba de recomendações."""
        frame = ttk.Frame(self.tab_recommend, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Quantidade de recomendações:").pack(anchor=tk.W)
        self.num_recommendations = ttk.Spinbox(frame, from_=1, to=20, width=10)
        self.num_recommendations.set(5)
        self.num_recommendations.pack(anchor=tk.W, pady=5)
        
        ttk.Button(frame, text="🎯 Gerar Recomendações", 
                   command=self.show_recommendations).pack(pady=10)
        
        # Área de resultados
        results_frame = ttk.LabelFrame(frame, text="Livros Recomendados para Você", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.recommendations_text = scrolledtext.ScrolledText(results_frame, height=15, width=70)
        self.recommendations_text.pack(fill=tk.BOTH, expand=True)
    
    def create_about_tab(self):
        """Cria a aba sobre o projeto."""
        frame = ttk.Frame(self.tab_about, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        about_text = """
╔══════════════════════════════════════════════════════════════════════╗
║     SISTEMA DE RECOMENDAÇÃO DE LIVROS BRASILEIROS                    ║
║     Projeto 1 - Introdução à Inteligência Artificial                 ║
║     Universidade de Brasília - 2026/1                                ║
╚══════════════════════════════════════════════════════════════════════╝

📖 SOBRE O PROJETO
Este sistema implementa um modelo de recomendação por conteúdo utilizando
o algoritmo TF-IDF (Term Frequency - Inverse Document Frequency) para
recomendar livros da literatura brasileira.

🔬 COMO FUNCIONA
1. Cada livro possui 3 características: autor, tema e categoria
2. O algoritmo TF-IDF calcula a relevância das palavras em cada perfil
3. A similaridade de cosseno mede a semelhança entre preferências
4. Recomendações são baseadas nos livros melhor avaliados pelo usuário

📊 DADOS DO SISTEMA
• 50 livros da literatura brasileira
• 100 usuários de treinamento
• Matriz de utilidade com 5.000 avaliações
• Escala de avaliação: 1 a 5 estrelas

👥 INTEGRANTES
• Leandro Coelho da Silva
• Paulo Henrique Borges Martins
• Valeria Alexandra Guevara Parra

📚 REFERÊNCIAS
• Sistemas de Recomendação - Loren Terveen & Will Hill
• Introduction to Information Retrieval - Manning, Raghavan & Schütze
• Mining of Massive Datasets - Leskovec, Rajaraman & Ullman
        """
        
        text_widget = scrolledtext.ScrolledText(frame, height=25, width=80,
                                                font=('Courier', 10))
        text_widget.insert(tk.END, about_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(fill=tk.BOTH, expand=True)
    
    # ==================== MÉTODOS DE AÇÃO ====================
    
    def login(self):
        """Realiza o login do usuário selecionado."""
        selection = self.user_combo.get()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione um usuário!")
            return
        
        user_id = int(selection.split(' - ')[0])
        self.current_user_id = user_id
        user_name = users[user_id]['nome']
        
        self.user_info_label.config(text=f"👤 {user_name} (ID: {user_id})")
        self.status_var.set(f"Logado como: {user_name}")
        self.update_user_ratings()
        
        messagebox.showinfo("Sucesso", f"Bem-vindo(a), {user_name}!")
    
    def register(self):
        """Registra um novo usuário."""
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Aviso", "Digite seu nome!")
            return
        
        if len(name) < 3:
            messagebox.showwarning("Aviso", "Nome muito curto!")
            return
        
        new_id = register_user(name)
        self.current_user_id = new_id
        
        # Atualiza o combobox
        self.user_combo['values'] = [f"{u['id']} - {u['nome']}" for u in users]
        
        self.user_info_label.config(text=f"👤 {name} (ID: {new_id})")
        self.status_var.set(f"Cadastrado e logado como: {name}")
        self.name_entry.delete(0, tk.END)
        
        messagebox.showinfo("Sucesso", 
                           f"Usuário cadastrado com sucesso!\nSeu ID: {new_id}\n\n"
                           "Agora avalie alguns livros para receber recomendações personalizadas!")
    
    def load_books(self, category=None):
        """Carrega os livros na treeview."""
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        
        for book in books:
            if category and category != 'Todas' and book['categoria'] != category:
                continue
            self.books_tree.insert('', tk.END, values=(
                book['id'],
                book['nome'],
                book['autor'],
                book['categoria'],
                book['tema']
            ))
    
    def filter_books(self, event=None):
        """Filtra livros por categoria."""
        category = self.category_filter.get()
        self.load_books(category if category != 'Todas' else None)
    
    def submit_rating(self):
        """Submete uma avaliação."""
        if self.current_user_id is None:
            messagebox.showwarning("Aviso", "Faça login primeiro!")
            return
        
        selection = self.book_combo.get()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione um livro!")
            return
        
        book_id = int(selection.split(' - ')[0])
        rating = self.rating_var.get()
        
        success, message = rate_book(self.current_user_id, book_id, rating)
        
        if success:
            messagebox.showinfo("Sucesso", message)
            self.update_user_ratings()
        else:
            messagebox.showerror("Erro", message)
    
    def update_user_ratings(self):
        """Atualiza a lista de avaliações do usuário."""
        if self.current_user_id is None:
            return
        
        self.ratings_text.delete(1.0, tk.END)
        
        user_ratings = ratings[self.current_user_id]
        rated_books = [(i, r) for i, r in enumerate(user_ratings) if r > 0]
        rated_books.sort(key=lambda x: x[1], reverse=True)
        
        if not rated_books:
            self.ratings_text.insert(tk.END, "Você ainda não avaliou nenhum livro.\n")
            return
        
        self.ratings_text.insert(tk.END, f"Total de avaliações: {len(rated_books)}\n")
        self.ratings_text.insert(tk.END, "=" * 60 + "\n\n")
        
        for book_id, rating in rated_books:
            book = books[book_id]
            stars = "⭐" * rating
            self.ratings_text.insert(tk.END, 
                f"{book['nome']}\n"
                f"   Autor: {book['autor']}\n"
                f"   Nota: {stars} ({rating}/5)\n\n")
    
    def show_recommendations(self):
        """Mostra as recomendações para o usuário."""
        if self.current_user_id is None:
            messagebox.showwarning("Aviso", "Faça login primeiro!")
            return
        
        try:
            n = int(self.num_recommendations.get())
        except:
            n = 5
        
        recommendations = get_recommendations(self.current_user_id, n)
        
        self.recommendations_text.delete(1.0, tk.END)
        
        user_name = users[self.current_user_id]['nome']
        self.recommendations_text.insert(tk.END, 
            f"🎯 Recomendações para {user_name}\n")
        self.recommendations_text.insert(tk.END, "=" * 60 + "\n\n")
        
        for rank, (book_id, score) in enumerate(recommendations, 1):
            book = books[book_id]
            self.recommendations_text.insert(tk.END,
                f"#{rank} - {book['nome']}\n"
                f"    📝 Autor: {book['autor']}\n"
                f"    📂 Categoria: {book['categoria']}\n"
                f"    🏷️ Temas: {book['tema']}\n"
                f"    📊 Score de Similaridade: {score:.4f}\n\n")
        
        self.recommendations_text.insert(tk.END, "\n" + "=" * 60 + "\n")
        self.recommendations_text.insert(tk.END, 
            "💡 Dica: Avalie mais livros para recomendações mais precisas!")

# ==================== EXECUÇÃO PRINCIPAL ====================

def main():
    root = tk.Tk()
    app = SistemaRecomendacao(root)
    root.mainloop()

if __name__ == "__main__":
    main()
