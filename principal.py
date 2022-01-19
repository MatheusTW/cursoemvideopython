from uteis.menu import *

from time import sleep

arq = "Registro.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastar nova Pessoa", "Sair do Sistema"])
    if resposta ==  1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até mais!")
        break
    else:
        print("Erro! Digite uma opção válida!")
    sleep(2)





