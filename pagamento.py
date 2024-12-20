import json

class Pagamento:


    def processar_pagamento(self):
        pass


class CartaoCredito(Pagamento):

    def __init__(self,numero_cartao,nome_titular, validade, ccv):
        self.numero_cartao = numero_cartao
        self.nome_titular = nome_titular
        self.validade = validade
        self.ccv = ccv
    
    def processar_pagamento(self, amount):
        print(f"€{amount} com Cartão de Crédito ({self.numero_cartao})")
    

class TransferenciaBancaria(Pagamento):

    def __init__(self,banco,agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta


    def processar_pagamento(self, amount):
        print(f"€{amount} com Transferência Bancária (banco: {self.banco}, conta: {self.conta})")


class PayPal(Pagamento):

    def __init__(self,email):
        self.email = email

    def processar_pagamento(self, amount):
        print(f"€{amount} com Paypal (e-mail: {self.email})")


def realizar_pagamento(pagamento, amount):
    pagamento.processar_pagamento(amount)

cartao_credito = CartaoCredito(numero_cartao="1234 5678 9012 3456", nome_titular="João Silva",
validade="12/25", ccv="123")
paypal = PayPal(email="joao.silva@email.com")
transferencia = TransferenciaBancaria(banco="Banco Central", agencia="1234", conta="12345678")

realizar_pagamento(cartao_credito, 150.00)
realizar_pagamento(paypal, 200.00)
realizar_pagamento(transferencia, 300.00)
