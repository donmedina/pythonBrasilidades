from cpfcnpj import documento


class mainCPFCNPJ:

    def __init__(self):
        opc = "0"
        while opc != "3":
            opc = input("### MENU ###\n(1) CPF\n(2) CNPJ\n(3) SAIR\nEscolha a validação:")
            if opc == "1":
                cpf_usuario = input("Digite o CPF a ser verificado sem pontos e traço: ")
                obj_cpf = documento.cria_documento(str(cpf_usuario),"cpf")
                print("O CPF {} é válido.". format(obj_cpf))
            elif opc == "2":
                cnpj_usuario = input("Digite o CNPJ a ser verificado sem pontos e traço: ")
                obj_cnpj = documento.cria_documento(str(cnpj_usuario), "cnpj")
                print("O CNPJ {} é válido.".format(obj_cnpj))
            elif opc == "3":
                print("Fechando aplicação")
            else:
                raise ValueError("Opção escolhida é inválida!!")
