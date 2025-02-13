class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    def depositar(self, sumar):
        self.sumar = sumar
        self.saldo += self.sumar
    def ver_saldo(self):
        return f"El saldo es de {self.saldo}"
    def retirar(self, restar):
        self.restar = restar
        self.saldo -= self.restar
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.ver_saldo())