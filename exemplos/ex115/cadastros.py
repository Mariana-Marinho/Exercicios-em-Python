# importando a função leia_int()
from exemplos.ex113 import *


def linhas():
    print('_'*30)


def bloco(frase):
    linhas()
    print(f'{frase:^30}')
    linhas()


def cadastro():
    cadastrados = []
    while True:
        escolha = menu()
        try:
            escolha = int(escolha)
            if escolha == 1:
                pessoas_cadastradas(cadastrados)
            elif escolha == 2:
                cadastrar(cadastrados)
            elif escolha == 3:
                print(f'\n\033[31mPrograma finalizado\033[m')
                break
        except ValueError:
            print('digite um valor válido')
        except:
            print('digite um inteiro: ')


def menu():
    print()
    bloco('MENU PRINCIPAL')
    print(f"""\033[36m    1 - Ver pessoas cadastradas
    2 - Cadastrar nova pessoa
    3 - Sair do sistema\033[m""")
    linhas()
    escolha = leia_int('\033[35mSua opção: \033[m')
    linhas()
    return escolha


def pessoas_cadastradas(lista):
    bloco('PESSOAS CADASTRADAS')
    for p in lista:
        print(f'{p[0]:<10}{p[1]:>20}')


def cadastrar(lista):
    pessoa = []
    nome = input('nome: ')
    idade = input('idade: ')
    pessoa.append(nome)
    pessoa.append(idade)
    lista.append(pessoa.copy())
    pessoa.clear()
