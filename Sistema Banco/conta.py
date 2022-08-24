import datetime
from extrato import Extrato

class Conta:
    def __init__(self, titular, numero, saldo, limite):
        print("Iniciliazando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def deposita(self, valor):
        self.saldo += valor
        return self.saldo

    def saca(self, valor):
        if self.saldo < valor:
            return ("Você não possui saldo suficiente.")
        else:
            self.saldo -= valor
            return True
    
    def transfere(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Você não possui saldo suficiente.")

        else:
            self.saldo -= valor
            contaDestino += valor
            return ("Transação realizada com sucesso!")
    
    def saldo(self):
        return self.saldo