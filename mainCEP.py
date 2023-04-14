from buscaCEP import buscaEndereco
import requests

class buscadorEndereco:

    def __init__(self):
        opc = "0"
        while opc != "2":
            opc = input("### MENU ###\n(1) Verificar CEP\n(2) SAIR\nEscolha a opção:")
            if opc == "1":
                cep = input("Digite o CEP a ser verificado: ")
                objCEP = buscaEndereco(cep)
                print(objCEP)
                endereco = objCEP.viaCEP()
                print("{} {}, {}, {}, {}".format(endereco[0],endereco[1],endereco[2],endereco[3],endereco[4]))
            elif opc == "2":
                print("Fechando aplicação")
            else:
                raise ValueError("Opção escolhida é inválida!!")

