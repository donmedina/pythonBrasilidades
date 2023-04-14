from mainCPF_CNPJ import mainCPFCNPJ
from mainCEP import buscadorEndereco

opc = "0"
while opc != "3":
    opc = input("### MENU PRINCIPAL ###\n(1) Validação de CPF/CNPJ\n(2) Busca de Endereços\n(3) SAIR\nEscolha a validação:")
    if opc == "1":
        mainCPFCNPJ()
    elif opc == "2":
        buscadorEndereco()
    elif opc == "3":
        print("Fechando aplicação")
    else:
        raise ValueError("Opção escolhida é inválida!!")