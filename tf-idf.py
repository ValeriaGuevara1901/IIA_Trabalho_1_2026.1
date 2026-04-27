import numpy as np
import re
import random
 
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

#Notas dos livros rating[idDoUser][idDoLivro]
ratings = []

for i in range(0, 100):
     grades = []
     for j in range(0, 50):
          grades.append(random.randint(0,5))
     ratings.append(grades)
 
documents = []

#Sepera só as palavras
def tokenize(text):
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())

#Adiciona a um array, os dados do livro
for book in books:
     phrase = book["autor"] + " " + book["tema"] + " " + book["categoria"]
     tokens = tokenize(phrase)
     documents.append(tokens)

#Impede repetição nesse array
word_set = set()
for doc in documents:
     word_set.update(doc)
word_set = list(word_set)
index_dict = {word: i for i, word in enumerate(word_set)}
total_docs = len(documents)

def compute_idf():
     #Zera os valores 
     word_count = {word: 0 for word in word_set}

     #Conto quantas vezes a palavra apareceu no banco
     for word in word_set:
          for doc in documents:
               if word in doc:
                    word_count[word] += 1

     idf = {}
     #Calcula o idf de cada palavra
     for word in word_set:
          idf[word] = np.log(total_docs / (word_count[word] + 1))

     return idf

idf = compute_idf()

def termfreq(document, word):
     return document.count(word) / len(document) #Calcula tf

def tf_idf(document):
     vec = np.zeros(len(word_set))
     #Coloca o peso tf-idf na posição da palavra no array
     for word in document:
          if word in index_dict:
               tf = termfreq(document, word)
               vec[index_dict[word]] = tf * idf[word]
     return vec

#Cria um vetor para colecionar todos os tf-idf
vectors = [tf_idf(doc) for doc in documents]

#Similaridade de cosseno
def cosine_similarity(a, b):
     if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
          return 0
     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def recomend_by_text(userId,texto_usuario, top_n=5):
     tokens = tokenize(texto_usuario)
     user_vec = tf_idf(tokens)

     similaridades = []

     #Calcula a similaridade da palavra e guarda seu valor
     for i, vec in enumerate(vectors):
          sim = cosine_similarity(user_vec, vec)
          similaridades.append((i, sim))

     similaridades.sort(key=lambda x: x[1], reverse=True)

     print(f"\nPerfil: {users[userId]["nome"]}")
     for i, score in similaridades[:top_n]:
          print(f"{books[i]['nome']} | Score: {score:.4f}")

#Pega os livros mais bem avaliados pelo usuário
def take_top10_rating(idUser):
     return sorted(range(len(ratings[idUser])), key=lambda i: ratings[idUser][i], reverse=True)[:10]

def recomend_books(idUser):
     #Pega as 10 maiores notas do user e faz um texto dos temas que interessa ele
     take_top10_rating_list = take_top10_rating(idUser)
     text = ""
     for i in range(0, len(take_top10_rating_list)):
          author = books[take_top10_rating_list[i]]["autor"]
          category = books[take_top10_rating_list[i]]["categoria"]
          theme = books[take_top10_rating_list[i]]["tema"]
          text += " " + author + " " + category + " " + theme
     recomend_by_text(idUser, text)

#Registra o usuário e sua tabela de notas
def register_user(name):
     users.append({"id": len(users) , "nome": name})
     grades = []
     for i in range(0, 50):
          grades.append(0)
     ratings.append(grades)

#Lista usuários
def list_users():
     print("Usuários: \n")
     for i in users:
          print("ID: ", i["id"], " Nome: ", i["nome"])

     print("----------------------------------------------------\n")

#Lista livros
def list_books():
     print("Livros: \n")
     for i in books:
          print("ID: ", i["id"], " Nome: ", i["nome"], " Autor: ", i["autor"])
     print("----------------------------------------------------\n")

#Avalia livro
def rate_book(userId, bookId, rate):
     if userId > (len(users)-1):
          print("Usuário não existe.")
          return
     if bookId < 0 or bookId > 49:
          print("Livro não existe.")
          return
     if rate < 1 or rate > 5:
          print("Nota inválida, a nota deve ser 1 e 5")
          return
     ratings[userId][bookId] = rate
     
#Lista a opção de usuários     
list_users()

#Lista a opção de livros
list_books()

#Registra um novo usuário
register_user("Bruna Guimarães Gonçalves")

#Lista novamente, mas com o novo usuário
list_users()

#Avalia algus livros
rate_book(100, 0, 1)
rate_book(100, 1, 5)
rate_book(100, 2, 3)
rate_book(100, 3, 2)
rate_book(100, 4, 3)
rate_book(100, 5, 4)
rate_book(100, 6, 4)
rate_book(100, 7, 5)
rate_book(100, 8, 2)
rate_book(100, 9, 4)
rate_book(100, 10, 5)
rate_book(100, 11, 3)

#Recomenda livros para usuários diferentes
recomend_books(100)
recomend_books(0)
