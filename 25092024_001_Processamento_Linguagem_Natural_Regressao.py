'''**Exercício 01: Contexto**

De acordo com o que vimos até o momento, modelo o contexto das seguintes frases:
1.	Maria encontrou a amiga na festa com um vestido azul
2.	Maria estava segurando o livro com a capa vermelha
'''

# Biblioteca SpaCy
# Biblioteca para Processamento de linguagem natural
# pip istall spacy
# doanload do modelo de linguagem PT_BR
# python -m spacy download pt_core_news_sm

import spacy
import spacy.displacy

# carregando o modelo de linguagem
# nlp ou pln
spacyPT = spacy.load('pt_core_news_sm')

# processamento de texto
frase = spacyPT('Maria encontrou a amiga na festa com um vestido azul')
frase1 = spacyPT('Maria estava segurando o livro com a capa vermelha')
print(frase)

# Cada frase é uma sequência de tokens,
# token é cada classe da palavra
# e nós podemos itera sobre cada token
# TOKENIZAR
for token in frase:
    print(token)

# Exibir as categorias morfossintáticas de cada token
# pos_ -> Part of speech
for token in frase:
    print(f'{token.text}:{token.pos_}')

# Visualizar as dependências das categorias morfossintáticas
spacy.displacy.serve([frase,frase1], style='dep')

# Clicar no http://0.0.0.0:5000 com o crtl + botao esquerdo do mouse
# abrir
# Substituir o http://0.0.0.0/ por localhost >>> http://localhost:5000/
