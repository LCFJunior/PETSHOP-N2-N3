#Turma: ADS12
#Alunos: Luiz Carlos Francisco Junior



#Chamada de função:

from Funcoes import *

#Base do código (ESTRUTURA):



while True:
    try:
        opcao=int(input("Digite a opção desejada:\n   0 = Sair\n   1 = Cadastrar os dados\n   2 = Listar os dados\n   3 = Alterar os dados\n   4 = Excluir os dados\n   5 = Fazer backup dos dados\n"))
        if opcao==1:
            cadastro()
        elif opcao==2:
            listar()
        elif opcao==3:
            alterar()
        elif opcao==4:
            excluir()
        elif opcao==5:
            backup()
        elif opcao==0:
            print("Programa finalizado!")
            break
        else:
            print("(ERRO) Essa opção não existe, tente novamente!")
    except ValueError:
        print("Certifique-se que você digitou oq foi pedido!")
    except Exception as e:
        print("Ocorreu um erro no programa!",str(e))

    
