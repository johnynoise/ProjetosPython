class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.limite_saque = 500.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque:
            print(f"Valor acima do limite de saque de R$ {self.limite_saque:.2f}.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\n========== Extrato ==========")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("==============================")


def menu():
    banco = Banco()

    while True:
        print("\n========== Sistema Bancário ==========")
        print("[1] Depósito")
        print("[2] Saque")
        print("[3] Extrato")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor para depósito: R$ "))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Informe o valor para saque: R$ "))
            banco.sacar(valor)
        elif opcao == '3':
            banco.exibir_extrato()
        elif opcao == '4':
            print("Obrigado por utilizar o sistema bancário. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
