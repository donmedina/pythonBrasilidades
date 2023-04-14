import re
import requests

class buscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if (self.validaCEP(cep)):
            self.cep = cep
        else:
            raise ValueError ("CEP inválido")

    def __str__(self):
        return self.formataCEP()

    def viaCEP(self):
        if (self.cep.find("-") == -1):
            cepRequisitado = self.cep
        else:
            cepRequisitado = self.cep.replace("-","")
        r = requests.get("https://viacep.com.br/ws/{}/json/".format(cepRequisitado))
        dados = r.json()
        return (dados['logradouro'],
                dados['complemento'],
                dados['bairro'],
                dados['localidade'],
                dados['uf']
                )

    def validaCEP(self, cep):
        padraoValidador = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
        return (re.match(padraoValidador, cep))

    def formataCEP(self):
        if (self.cep.find("-") == -1):
            return "{}-{}".format(self.cep[:5],self.cep[5:])
        else:
            return "{}-{}".format(self.cep[:5],self.cep[6:])


