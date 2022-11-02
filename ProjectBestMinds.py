def sistema_principal():
    print("Bem vindo à empresa Oliveira Trade. Escolha a opção desejada para continuar: ")
    escolha = int(input("(1) para Cadastramento de usuário ou (2) para Login no Sistema: "))

    opcoes = [1, 2]
    opcao_valida = escolha in opcoes

    if opcao_valida:
        if escolha == 1:
            criar_usuario()
        elif escolha == 2:
            realizar_login()
        else:
            while not opcao_valida:
                print("Opção inválida. Escolha entra as opções citadas abaixo: ")
                nova_escolha = int(input("(1) para Cadastramento de usuário ou (2) para Login no Sistema: "))
                opcao_valida = nova_escolha in opcoes

                if opcao_valida:
                    if opcoes == 1:
                        criar_usuario()
                    elif opcoes == 2:
                        realizar_login()

    refazer_processo()


def criar_usuario():

    arquivo_logins = open("listaDeUsuarios.txt", "a")

    cadastro_login = input("Insira o usuário que será cadastrado: ").capitalize()

    arquivo_logins.write(f"{cadastro_login}\n")

    print("Cadastro Realizado com sucesso")

    arquivo_logins.close()


def realizar_login():

    arquivo_logins = open("listaDeUsuarios.txt", "r")

    usuario = input("Para efetuar o login em sua conta, por favor insira seu nome de usuário: \n").capitalize()

    usuarios_cadastrados = arquivo_logins.readlines()

    usuario_valido = (usuario + "\n" in usuarios_cadastrados)

    if usuario_valido:
        print(f"Login realizado com sucesso. Bem vindo(a) {usuario}")
    else:
        while not usuario_valido:
            novo_usuario = input("Usuário Inválido. Digite seu usuário para realizar o login no Sistema: \n")
            usuario_valido = novo_usuario + "\n" in usuarios_cadastrados

            if usuario_valido:
                print(f"Login realizado com sucesso. Bem vindo(a) {novo_usuario}")

    arquivo_logins.close()


def refazer_processo():
    processo = input("Deseja realizar uma nova operação no Sistema? (S/N)\n").upper()

    confirmacao = ["SIM", "S"]
    negacao = ["N", "NAO"]

    while processo not in confirmacao and processo not in negacao:
        print("Comando inválido")
        processo = input("Deseja realizar uma nova operação no Sistema? (S/N) ").upper()

    if processo in confirmacao:
        print("\n")
        sistema_principal()
    if processo in negacao:
        print("Encerrando Sistema")


if __name__ == "__main__":
    sistema_principal()


# arq = open('listaDeUsuarios.txt', 'a')
# print('Olá, aqui você pode adicionar uma nova conta!')
# nome_usuario = input('Digite o nome de usuário: ')
#
# arq.write('{}\n'.format(nome_usuario))
# '''
# Adição da constante \n new line
# Uma vez que write não o adiciona automaticamente
# '''
#
# print('Cadastro realizado com sucesso!\n')
# arq.close() #O arquivo é fechado do modo de adição para ser aberto
#             #posteriormente no modo de leitura
#
# arq = open('listaDeUsuarios.txt') #abrindo no modo de leitura
# print('Efetue o seu login')
# nome_login = input('Digite o seu nome de usuario: ')
#
# registrados = arq.readlines()
# if nome_login + '\n' in registrados:
#     print('Bem vindo(a), {}!'.format(nome_login))
# else:
#     print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
# arq.close()
