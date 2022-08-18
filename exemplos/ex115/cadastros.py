def linhas():
    print('_'*30)


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
                print('Programa finalizado')
                break
        except ValueError:
            print('digite um valor válido')
        except:
            print('digite um inteiro: ')


def menu():
    linhas()
    print(f'{"MENU PRINCIPAL":^30}')
    linhas()
    print(f"""\033[36m    1 - Ver pessoas cadastradas
    2 - Cadastrar nova pessoa
    3 - Sair do sistema\033[m""")
    linhas()
    escolha = input('\033[35mSua opção: \033[m')
    linhas()
    return escolha


def pessoas_cadastradas(lista):
    linhas()
    print(f'{"PESSOAS CADASTRADAS":^30}')
    linhas()
    for p in lista:
        for i, v in p.items():
            print(f'{i:<10}{v:>20}')


def cadastrar(lista):
    nome = input('nome: ')
    idade = input('idade: ')
    pessoa = {
        'nome': nome,
        'idade': idade
    }
    lista.append(pessoa.copy())
    pessoa.clear()