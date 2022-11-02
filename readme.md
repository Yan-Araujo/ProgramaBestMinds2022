# Project Best Minds 2022:

## Sobre o projeto:

Esse Projeto foi realizado com o objetivo de criar um sistema de Login
para a empresa Oliveira Trade. Nele, utilizo 4 funções onde cada uma
é responsável por um comportamento de forma individual. 

1. A função "sistema_principal()" é responsável pela inicialização
código. Ela chama as funções de criação de usuário, login no 
sistema e repetição do código.

2. A segunda Função: "criar_usuario()" é responsável pela criação de um novo usuário no arquivo
no arquivo "listaDeUsuarios.txt". Primeiramente ela acessa esse arquivo e adiciona a entrada do 
usuário ao mesmo.

3. A terceira função: "realizar_login()" realiza a verificação da entrada do usuário, conferindo
se a mesma está presente no arquivo "listaDeUsuarios.txt". Se o usuário informar uma entrada não
válida, o programa entra em loop pedindo por um usuário válido. Quando isso acontece, a função
imprime "Bem Vindo" + O nome do usuário

4. A quarta função: "repetir_processo()" é é responsável por averiguar se o usuário deseja
realizar uma nova operação no sistema. Ela recebe a entrada do usuário confirmando ou não essa
informação e entra em loop caso as repostas não sejam válidas

