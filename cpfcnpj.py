from validate_docbr import CPF,CNPJ

class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError ("CPF Inválido")

    def __str__(self):
        return self.formataCPF()

    def valida(self, documento):
        if len(str(documento)) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def formataCPF(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError ("CNPJ Inválido")

    def __str__(self):
        return self.formataCNPJ()

    def valida(self, documento):
        if len(str(documento)) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def formataCNPJ(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


class documento:

    @staticmethod
    def cria_documento(documento, tipoDocumento):
        if tipoDocumento == 'cpf':
            return DocCPF(documento)
        elif tipoDocumento == 'cnpj':
            return DocCNPJ(documento)
        else:
            raise ValueError ("Tipo de documento não encontrado!!")
