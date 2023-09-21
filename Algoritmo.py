from Classes import *

import os

sair = False
menu_adm = 0
menu_cli = 0
master = Adm("adm", "admin123",0)
loja.inserir_adm(master)
pdtID = 0
contID = 0
admID = 0

while sair == False:
    menu_adm = 0
    loginCorreto = False
    try:
        os.system("cls")
        print(" --- BEM VINDO(A) AO VS STORE --- \n")
        print(" [1] - LOGIN ADM")
        print(" [2] - LOGIN CLIENTE")
        print(" [3] - SAIR")

        menu = int(input("\nDigite a opção desejada:  "))
        os.system("cls")
        

        match menu:
            case 1:
                print("--- ADM LOGIN ---")
                user_login = input("Digite o user: ")
                senha_login = input("Digite a senha: ")

                for vetor, user in loja.adm.items():
                    if user.user == user_login and user.senha == senha_login:
                        loginCorreto = True

                if loginCorreto == True:
                    os.system("cls")
                
                    while menu_adm == 0:
                        print("--- MENU DO ADM --- \n")
                        print("[1] - CADASTRAR CLIENTE")
                        print("[2] - CADASTRAR ADM")
                        print("[3] - CADASTRAR PRODUTO")
                        print("[4] - EXCLUIR PRODUTO")
                        print("[5] - EXCLUIR CLIENTE")                     
                        print("[6] - LISTAR CLIENTE")
                        print("[7] - LISTAR PRODUTO")
                        print("[8] - VOLTAR")
                        op_adm = int(input("\nDigite a opção desejada: "))

                        match op_adm:
                            case 1:
                                os.system("cls")
                                contID += 1
                                idc = contID
                                
                                print("--- CADASTRO DE CLIENTE --- \nPreencha as informações:\n")
                                nome = input("NOME: ")
                                cpf = int(input("CPF: "))
                                idade = int(input("IDADE: "))
                                endereco = input("ENDEREÇO: ")
                                senha = input("SENHA: ")

                                admin.cadastrar_cliente(nome, cpf, idade, endereco, senha, idc)
                                print("\nCliente cadastrado com sucesso!")
                                os.system("pause")
                                os.system("cls")

                            case 2:
                              #  os.system("cls")
                                print("--- CADASTRO ADM--- \nPreencha as informações:\n")
                                admID +=1
                                ida = admID
                                
                                user = input("USER: ")
                                senhaa = input("SENHA: ")

                                adm = Adm(user, senhaa, 0)
                                loja.inserir_adm(adm)
                                print("\nADM cadastrado com sucesso!")


                            case 3:
                                os.system("cls")
                                pdtID += 1
                                idp = pdtID
                                
                                print("--- CADASTRO DE PRODUTO --- \nPreencha as informações:\n")
                                nome_produto = input("NOME DO PRODUTO: ")
                                descricao = input("DESCRIÇÃO DO PRODUTO: ")
                                valor = int(input("VALOR: "))

                                admin.cadastrar_produto(nome_produto, descricao, valor, idp)
                                print("\nProduto cadastrado com sucesso!")
                                os.system("pause")
                                os.system("cls")

                            case 4:
                                pass
                            case 5:
                                pass
                            case 6:
                                pass
                            case 7:
                                pass
                            case 8:
                                os.system("cls")
                                menu_adm = 1

                            case _:
                                print("Opção inválida.")
                        
                else:
                    print("Credenciais inválidas. Tente novamente.")
            case 2:
                os.system("cls")
                print("--- LOGIN CLIENTE ---")
                cpf_cliente = int(input("Digite o CPF: "))
                senha_cliente = input("Digite a senha: ")

            case 3:  
                print("SAINDO...")
                sair = True
            case _:
                print("Opção inválida.")
                
    except Exception as erro:
            print("Opção inválida.")
            print("Erro:", erro.__class__.__name__)
            os.system("pause")
            os.system("cls")
