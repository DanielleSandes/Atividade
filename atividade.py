#!/usr/bin/env python
# coding: utf-8

# In[14]:


def menu():
    print('\nOPÇÃO 01 – DIGITAR PALAVRA')
    print('OPÇÃO 02 – CONTAR PALAVRAS')
    print('OPÇÃO 03 – BUSCAR PALAVRA A PARTIR DA LINHA')
    print('OPÇÃO 0 – Sair')
    opcao = input('\nSelecione uma Opção: ')
    return int(opcao)

def digitarPalavra():
    palavra = input('Digite uma palavra: ')
    if len(palavra.split()) > 1:
        print('\nWPalavra inválida!!')
    else:
        with open('arquivo.txt', 'a') as arq:
            arq.write('\n{}'.format(palavra))

def pegarLinhas(): 
    linhas = []
    with open('arquivo.txt', 'r') as arq:
        linhas = arq.readlines()
    return linhas 

def contarPalavras():
    with open('arquivo.txt', 'r') as arq:
        qntd_palavras = len(pegarLinhas())
        print('\nExistem {} palavras no arquivo.'.format(qntd_palavras))

def buscarPalavra():
    numero_linha = int(input('Digite o número da linha que deseja buscar: '))
    linhas = pegarLinhas()
    numero_linha -= 1
    if  0 <= numero_linha < len(linhas):
        print('\nPalavra:', linhas[numero_linha])
    else: 
        print('\nNúmero de linha inválido!')

opcao = None

while opcao != 0:
    opcao = menu()
    if opcao == 1:
        digitarPalavra()
    elif opcao == 2: 
        contarPalavras()
    elif opcao == 3: 
        buscarPalavra()


