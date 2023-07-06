#Função para cadastrar os dados no arquivo.txt ↓↓↓↓

def cadastro():
    try:    
        with open('DadosPETSHOP.txt','a') as arquivo:
            nome=str(input("Digite seu nome completo:\n   ")).upper()
            try:
                contato=int(input("Digite seu número de telefone(SEM HÍFEN):\n   "))
            except ValueError:
                print("Certifique-se que você digitou o que é pedido.")
                return
            endereco=input("Digite seu endereço:\n   ")
            bairro=str(input("Digite seu bairro:\n   "))
            try:
                CEP=int(input("Digite seu CEP(SEM HÍFEN):\n   "))
            except ValueError:
                print("Certifique-se que você digitou o que é pedido.")
                return
            ponto_referencia=input("Digite um ponto de referência:\n   ")
            print("-"*5,"INFORMAÇÕES DO SEU PET","-"*5,"\n")
            raca_pet=str(input("Digite o nome da raça do seu pet:\n   "))
            try:
                peso_pet=float(input(f"Digite o peso do seu {raca_pet}:\n   "))
            except ValueError:
                print("Certifique-se que você digitou o que é pedido.")
                return
            cor_pet=str(input(f"Digite a cor do seu {raca_pet}:\n   "))
            observacoes=str(input("Observações:\n   "))

            aluno=(f"{nome},{contato},{endereco},{bairro},{CEP},{ponto_referencia},{raca_pet},{peso_pet},{cor_pet},{observacoes}\n")
            arquivo.write(aluno)

            print("Dados cadastrados.")
            print("--------------------","\n")
    except Exception as e:
        print("Ocorreu um erro ao cadastrar os dados:", str(e))

    

#Função para listar os dados do arquivo.txt ↓↓↓↓

def listar():
    try:
        with open("DadosPETSHOP.txt","r") as arquivo:
            linhas=arquivo.readlines()
            if not linhas:
                print("Nenhum PET foi cadastrado.")
            else:
                print("Dados do(s) PET(s) cadastrado(s):\n")
                for linha in linhas:
                    dados = linha.strip().split(",")
                    print("Nome: ", dados[0],"\n   ")
                    print("Contato: ", dados[1],"\n   ")
                    print("Endereço: ", dados[2],"\n   ")
                    print("Bairro: ", dados[3],"\n   ")
                    print("CEP: ", dados[4],"\n   ")
                    print("Ponto de Referência: ", dados[5],"\n   ")
                    print("Raça do pet: ", dados[6],"\n   ")
                    print("Peso do pet: ", dados[7],"\n   ")
                    print("Cor do pet: ", dados[8],"\n   ")
                    print("Observações: ", dados[9],"\n   ")
                    print("--------------------","\n")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado!")
    except Exception as e:
        print("Ocorreu um erro ao listar os dados!",str(e))



#Função para alterar os dados do arquivo.txt ↓↓↓↓

def alterar():
    try:
        with open("DadosPETSHOP.txt","r") as arquivo:
            linhas=arquivo.readlines()

            if not linhas:
                print("Nenhum dado encontrado para alterar.")
                return
        
        with open("DadosPETSHOP.txt","w") as arquivo:
            codigo_chave=input("Digite o nome que esta relacionado aos dados que deseja mudar:\n   ").upper()
            for linha in linhas:
                dados = linha.strip().split(",")
                if codigo_chave==dados[0]:
                    nome2=input("Novo nome:\n   ").upper()
                    contato2=input("Novo contato:\n   ")
                    endereco2=input("Novo endereço:\n   ")
                    bairro2=input("Novo bairro:\n   ")
                    CEP2=input("Novo CEP:\n   ")
                    ponto_referencia2=input("Novo ponto de referência:\n   ")
                    print("-"*5,"NOVAS INFORMAÇÕES DO SEU PET","-"*5,"\n")
                    raca_pet2=input("Nova raça do pet:\n   ")
                    peso_pet2=input("Novo peso do pet:\n   ")
                    cor_pet2=input("Nova cor do pet:\n   ")
                    observacoes2=input("Novas observações:\n   ")

            novo_cliente=(f"{nome2},{contato2},{endereco2},{bairro2},{CEP2},{ponto_referencia2},{raca_pet2},{peso_pet2},{cor_pet2},{observacoes2}\n")
            arquivo.write(novo_cliente)
        encontrado=True
        print("Dados alterados!")
        print("--------------------","\n")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado!")
    except Exception as e:
        print("Ocorreu um erro ao alterar os dados!",str(e))



#Função para excluir os dados do arquivo.txt ↓↓↓↓

def excluir():
    try:
        with open("DadosPETSHOP.txt","r") as arquivo:
            linhas=arquivo.readlines()

        if not linhas:
            print("Nenhum PET cadastrado!")
            return
            
        nome_codigo=input("Digite o nome do dono do PET que deseja apagar os dados:\n   ").upper()
        encontrado=False

        with open("DadosPETSHOP.txt","w") as arquivo:
            for linha in linhas:
                dados=linha.strip().split(",")
                if dados[0]==nome_codigo:
                    encontrado=True
                    print("Dados do cliente excluídos com sucesso!")
                    print("--------------------","\n")
                else:
                    arquivo.write(linha)            

        if not encontrado:
            print("Nenhum PET encontrado com o nome fornecido!\n")
            return False
        
        return True
    
    except FileNotFoundError:
        print("Arquivo de dados não encontrado!")
        return False
    except Exception as e:
        print("Ocorreu um erro ao excluir os dados:",str(e))
        return False



#Função para realizar backup nos dados do arquivo.txt ↓↓↓↓

def backup():
    try:
        with open("DadosPETSHOP.txt","r") as arquivo_inicial:
            with open("backup_DadosPETSHOP.txt","w") as arquivo_backup:
                dados=arquivo_inicial.read()
                arquivo_backup.write(dados)
        print("Backup concluído!")
        print("--------------------","\n")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao realizar o backup.",str(e))
    
    