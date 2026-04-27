"""
Sistema de Recomendação de Livros Brasileiros
Backend Flask - API REST
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import re
import random

app = Flask(__name__)

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

# Matriz de utilidade
random.seed(42)
ratings = []
for i in range(100):
    grades = []
    for j in range(50):
        grades.append(random.randint(0, 5))
    ratings.append(grades)

# ==================== ALGORITMO TF-IDF ====================

documents = []

def tokenize(text):
    return re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', text.lower())

for book in books:
    phrase = book["autor"] + " " + book["tema"] + " " + book["categoria"]
    tokens = tokenize(phrase)
    documents.append(tokens)

word_set = set()
for doc in documents:
    word_set.update(doc)
word_set = list(word_set)
index_dict = {word: i for i, word in enumerate(word_set)}
total_docs = len(documents)

def compute_idf():
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
    return document.count(word) / len(document)

def tf_idf(document):
    vec = np.zeros(len(word_set))
    for word in document:
        if word in index_dict:
            tf = termfreq(document, word)
            vec[index_dict[word]] = tf * idf[word]
    return vec

vectors = [tf_idf(doc) for doc in documents]

def cosine_similarity(a, b):
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def take_top10_rating(idUser):
    return sorted(range(len(ratings[idUser])), key=lambda i: ratings[idUser][i], reverse=True)[:10]

def get_recommendations(userId, top_n=5):
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

# ==================== ROTAS FLASK ====================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users')
def get_users():
    return jsonify(users)

@app.route('/api/books')
def get_books():
    return jsonify(books)

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('nome', '').strip()
    if not name or len(name) < 3:
        return jsonify({'error': 'Nome inválido'}), 400
    
    new_id = len(users)
    users.append({"id": new_id, "nome": name})
    ratings.append([0] * 50)
    return jsonify({"id": new_id, "nome": name})

@app.route('/api/rate', methods=['POST'])
def rate_book():
    data = request.json
    user_id = data.get('userId')
    book_id = data.get('bookId')
    rate = data.get('rate')
    
    if user_id >= len(users):
        return jsonify({'error': 'Usuário não existe'}), 400
    if book_id < 0 or book_id >= 50:
        return jsonify({'error': 'Livro não existe'}), 400
    if rate < 1 or rate > 5:
        return jsonify({'error': 'Nota inválida'}), 400
    
    ratings[user_id][book_id] = rate
    return jsonify({'success': True})

@app.route('/api/ratings/<int:user_id>')
def get_user_ratings(user_id):
    if user_id >= len(users):
        return jsonify({'error': 'Usuário não existe'}), 400
    
    user_ratings = []
    for i, rate in enumerate(ratings[user_id]):
        if rate > 0:
            user_ratings.append({
                'book': books[i],
                'rate': rate
            })
    return jsonify(user_ratings)

@app.route('/api/recommend/<int:user_id>')
def recommend(user_id):
    top_n = request.args.get('n', 5, type=int)
    
    if user_id >= len(users):
        return jsonify({'error': 'Usuário não existe'}), 400
    
    recommendations = get_recommendations(user_id, top_n)
    result = []
    for book_id, score in recommendations:
        result.append({
            'book': books[book_id],
            'score': round(score, 4)
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
