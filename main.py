from tabulate import tabulate
import re
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def calcular_lucro():
    for valores in range(4):
        faturamentos = faturamentos_trimestres[valores]
        soma = compras[valores] + despesas[valores] + folhas[valores]
        lucro_real.append(faturamentos - soma)
def input_valor(mensagem):
    while True:
        valor = input(mensagem)
        if re.match(r'^\d+(?:[,.]\d{0,2})?$', valor):
            return float(valor)
        else:
            print("Por favor, insira um valor numérico válido.")

def escolher_tipo_empresa():
    while True:
        print("Escolha o tipo de empresa:")
        print("1 - Venda")
        print("2 - Serviço")
        print("3 - Venda e Serviço")
        print("0 - Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            return 'Venda'
        elif choice == '2':
            return 'Serviço'
        elif choice == '3':
            return 'VendaServiço'
        elif choice == '0':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

class CalculadoraImpostosGerais:
    @staticmethod
    def simples():
        dados_tabela=[]
        cabecalhos=["Trimestre", "Simples a pagar"]

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            simples_serv = faturamento * simples_alq_serv
            simples_serv = round(simples_serv, 2)
            dados_tabela.append([f"Trimestre {trimestre}", simples_serv])
        print("\nSIMPLES NACIONAL: ")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))
    @staticmethod
    def iss():
        dados_tabela=[]
        cabecalhos=["Trimestre", "ISS a pagar"]

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            iss_lp_serv = faturamento * iss_alq_serv
            iss_lp_serv = round(iss_lp_serv, 2)
            dados_tabela.append([f"Trimestre {trimestre}", iss_lp_serv])
        print("\nISS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def icms():
        dados_tabela = []
        cabecalhos = ["Trimestre", "ISS a pagar"]

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            icms_lp_venda = faturamento * icms_alq_venda
            icms_lp_venda = round(icms_lp_venda, 2)
            dados_tabela.append([f"Trimestre {trimestre}", icms_lp_venda])
        print("ICMS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))
    @staticmethod
    def inss():
        dados_tabela=[]
        cabecalhos=["Trimestre", "INSS a pagar"]

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            inss_serv = faturamento * inss_alq_serv
            inss_serv = round(inss_serv, 2)
            dados_tabela.append([f"Trimestre {trimestre}", inss_serv])
        print("\nINSS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

class CalculadoraImpostosServicoLP:
    @staticmethod
    def pis():
        dados_tabela=[]
        cabecalhos=["Trimestre", "PIS a pagar"]
        pis_alq_lp_serv = 0.65

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            pis_lp_serv = faturamento * pis_alq_lp_serv
            dados_tabela.append([f"Trimestre {trimestre}",pis_lp_serv])
        print("PIS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def cofins():
        dados_tabela=[]
        cabecalhos=["Trimestre", "Cofins a pagar"]
        cofins_alq_lp_serv = 0.03

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            cofins_lp_serv = faturamento * cofins_alq_lp_serv
            dados_tabela.append([f"Cofins a pagar no trimestre {trimestre}", cofins_lp_serv])
        print("COFINS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def  csll():
        dados_tabela=[]
        cabecalhos=["Trimestre", "CSLL a pagar"]
        clss_alq = 0.09

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            csll_lp_serv = (faturamento * 0.32) * clss_alq
            dados_tabela.append([f"Trimestre {trimestre}", csll_lp_serv])
        print("CSLL")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def irpj():
        dados_tabela=[]
        cabecalhos=["Trimestre", "IRPJ trimestre", "Adicional", "IRPJ a pagar"]

        for trimestre, lucro_trimestre in enumerate(faturamentos_trimestres, start=1):
            # Calcula o IRPJ
            presuncao = lucro_trimestre * 0.32
            irpj_lr_serv = presuncao * 0.15

            if presuncao > 60000:
                adicional_irpj_lr_serv = (presuncao - 60000) * 0.1
                if adicional_irpj_lr_serv < 0:
                    adicional_irpj_lr_serv = 0
                irpj_a_pagar_serv = irpj_lr_serv + adicional_irpj_lr_serv
                dados_tabela.append([f"Trimestre {trimestre}", irpj_lr_serv, adicional_irpj_lr_serv, irpj_a_pagar_serv])

            elif presuncao <= 60000:
                adicional_irpj_lr_serv = (presuncao - 60000) * 0.1
                if adicional_irpj_lr_serv < 0:
                    adicional_irpj_lr_serv = 0
                irpj_a_pagar_serv = irpj_lr_serv + adicional_irpj_lr_serv
                dados_tabela.append([f"Trimestre {trimestre}", irpj_lr_serv, adicional_irpj_lr_serv, irpj_a_pagar_serv])
        print("IRPJ")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

class CalculadoraImpostosServicoLR:
    @staticmethod
    def pis():
        dados_tabela=[]
        cabecalhos=["Trimestre", "PIS a pagar", "Saldo"]
        pis_alq_lr_serv = 0.0165
        saldo = 0.00

        for trimestre in range(4):
            faturamento = faturamentos_trimestres[trimestre]
            compra = compras[trimestre]
            pis_lr_serv = faturamento * pis_alq_lr_serv
            pis_desconto_lr_serv = compra * pis_alq_lr_serv
            pis_a_pagar_lr_serv = pis_lr_serv - pis_desconto_lr_serv
            pis_a_pagar_lr_serv = round(pis_a_pagar_lr_serv, 2)

            if pis_a_pagar_lr_serv < 0:
                saldo += pis_a_pagar_lr_serv
                dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_serv, saldo])
            elif pis_a_pagar_lr_serv > 0:
                if saldo < 0:
                    pis_compensado_lr_serv = pis_a_pagar_lr_serv + saldo
                    pis_a_pagar_lr_serv = round(pis_a_pagar_lr_serv, 2)
                    dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_serv, pis_compensado_lr_serv])
                    saldo = saldo + pis_a_pagar_lr_serv
                    if saldo < 0:
                        saldo = 0
                else:
                    dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_serv, saldo])
        print("PIS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))


    @staticmethod
    def cofins():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar", "Saldo"]
        cofins_alq_lr_serv = 0.076
        saldo = 0.00

        for trimestre in range(4):
            faturamento = faturamentos_trimestres[trimestre]
            compra = compras[trimestre]
            cofins_lr_serv = faturamento * cofins_alq_lr_serv
            cofins_desconto_lr_serv = compra * cofins_alq_lr_serv
            cofins_a_pagar_lr_serv = cofins_lr_serv - cofins_desconto_lr_serv
            cofins_a_pagar_lr_serv = round(cofins_a_pagar_lr_serv, 2)

            if cofins_a_pagar_lr_serv < 0:
                saldo += cofins_a_pagar_lr_serv
                dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_serv, saldo])
            elif cofins_a_pagar_lr_serv > 0:
                if saldo < 0:
                    cofins_compensado_lr_serv = cofins_a_pagar_lr_serv + saldo
                    cofins_a_pagar_lr_serv = round(cofins_a_pagar_lr_serv, 2)
                    dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_serv, cofins_compensado_lr_serv])
                    saldo = saldo + cofins_a_pagar_lr_serv
                    if saldo < 0:
                        saldo = 0
                else:
                    dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_serv, saldo])
        print("COFINS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def csll():
        dados_tabela=[]
        cabecalhos=["Trimestre", "CSLL a pagar"]
        clss_alq = 0.09

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            csll_lr_serv = faturamento * clss_alq
            dados_tabela.append([f"Trimestre {trimestre}", csll_lr_serv])
        print("CSLL")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def irpj():
        calcular_lucro()


class CalculadoraImpostosVendaLP:
    @staticmethod
    def pis():
        dados_tabela = []
        cabecalhos = ["Trimestre", "PIS a pagar"]
        pis_alq_lp_serv = 0.65

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            pis_lp_serv = faturamento * pis_alq_lp_serv
            dados_tabela.append([f"Trimestre {trimestre}", pis_lp_serv])
        print("PIS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def cofins():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar"]
        cofins_alq_lp_venda = 0.03

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            cofins_lp_venda = faturamento * cofins_alq_lp_venda
            dados_tabela.append([f"Trimestre {trimestre}", cofins_lp_venda])
        print("COFINS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def csll():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar"]
        clss_alq = 0.09

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            csll_lp_venda = (faturamento * 0.12) * clss_alq
            dados_tabela.append([f"Trimestre {trimestre}", csll_lp_venda])
        print("CSLL")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def irpj():
        dados_tabela = []
        cabecalhos = ["Trimestre", "IRPJ trimestre", "Adicional", "IRPJ a pagar"]
        for trimestre, lucro_trimestre in enumerate(faturamentos_trimestres, start=1):

            presuncao = lucro_trimestre * 0.08
            irpj_lp_venda = presuncao * 0.15

            if presuncao > 60000:
                adicional_irpj_lp_venda = (presuncao - 60000) * 0.1
                if adicional_irpj_lp_venda < 0:
                    adicional_irpj_lp_venda = 0
                irpj_a_pagar_venda = irpj_lp_venda + adicional_irpj_lp_venda
                irpj_a_pagar_venda = round(irpj_a_pagar_venda, 2)
                dados_tabela.append([f"Trimestre {trimestre}", irpj_lp_venda, adicional_irpj_lp_venda,
                                     irpj_a_pagar_venda])

            elif presuncao <= 60000:
                adicional_irpj_lp_venda = (presuncao - 60000) * 0.1
                if adicional_irpj_lp_venda < 0:
                    adicional_irpj_lp_venda = 0
                irpj_a_pagar_venda = irpj_lp_venda + adicional_irpj_lp_venda
                irpj_a_pagar_venda = round(irpj_a_pagar_venda, 2)
                dados_tabela.append([f"Trimestre {trimestre}", irpj_lp_venda, adicional_irpj_lp_venda,
                                     irpj_a_pagar_venda])
        print("IRPJ")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

class CalculadoraImpostosVendaLR:
    @staticmethod
    def pis():
        dados_tabela = []
        cabecalhos = ["Trimestre", "PIS a pagar", "Saldo"]
        pis_alq_lr_venda = 0.0165
        saldo = 0.00

        for trimestre in range(4):
            faturamento = faturamentos_trimestres[trimestre]
            compra = compras[trimestre]
            pis_lr_venda = faturamento * pis_alq_lr_venda
            pis_desconto_lr_venda = compra * pis_alq_lr_venda
            pis_a_pagar_lr_venda = pis_lr_venda - pis_desconto_lr_venda
            pis_a_pagar_lr_venda = round(pis_a_pagar_lr_venda, 2)

            if pis_a_pagar_lr_venda < 0:
                saldo += pis_a_pagar_lr_venda
                dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_venda, saldo])
            elif pis_a_pagar_lr_venda > 0:
                if saldo < 0:
                    pis_compensado_lr_venda = pis_a_pagar_lr_venda + saldo
                    pis_a_pagar_lr_venda = round(pis_a_pagar_lr_venda, 2)
                    dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_venda, pis_compensado_lr_venda])
                    saldo = saldo + pis_a_pagar_lr_venda
                    if saldo < 0:
                        saldo = 0
                else:
                    dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_venda, saldo])
        print("PIS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def cofins():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar", "Saldo"]
        cofins_alq_lr_venda = 0.076
        saldo = 0.00

        for trimestre in range(4):
            faturamento = faturamentos_trimestres[trimestre]
            compra = compras[trimestre]
            cofins_lr_venda = faturamento * cofins_alq_lr_venda
            cofins_desconto_lr_venda = compra * cofins_alq_lr_venda
            cofins_a_pagar_lr_venda = cofins_lr_venda - cofins_desconto_lr_venda
            cofins_a_pagar_lr_venda = round(cofins_a_pagar_lr_venda, 2)

            if cofins_a_pagar_lr_venda < 0:
                saldo += cofins_a_pagar_lr_venda
                dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_venda, saldo])
            elif cofins_a_pagar_lr_venda > 0:
                if saldo < 0:
                    cofins_compensado_lr_venda = cofins_a_pagar_lr_venda + saldo
                    cofins_a_pagar_lr_venda = round(cofins_a_pagar_lr_venda, 2)
                    dados_tabela.append(
                        [f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_venda, cofins_compensado_lr_venda])
                    saldo = saldo + cofins_a_pagar_lr_venda
                    if saldo < 0:
                        saldo = 0
                else:
                    dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_venda, saldo])
        print("COFINS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def csll():
        dados_tabela = []
        cabecalhos = ["Trimestre", "CSLL a pagar"]
        clss_alq = 0.09

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            csll_lr_venda = faturamento * clss_alq
            dados_tabela.append([f"Trimestre {trimestre}", csll_lr_venda])
        print("CSLL")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def irpj():
        calcular_lucro()


class CalculadoraImpostosVendaServicoLP:
    @staticmethod
    def pis():
        dados_tabela = []
        cabecalhos = ["Trimestre", "PIS a pagar"]
        pis_alq_lp_vserv = 0.65

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            pis_lp_vserv = faturamento * pis_alq_lp_vserv
            dados_tabela.append([f"Trimestre {trimestre}", pis_lp_vserv])
        print("PIS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def cofins():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar"]
        cofins_alq_lp_vserv = 0.03

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            cofins_lp_vserv = faturamento * cofins_alq_lp_vserv
            dados_tabela.append([f"Trimestre {trimestre}", cofins_lp_vserv])
        print("COFINS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def csll():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar"]
        clss_alq = 0.09

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            csll_lp_vserv = (faturamento * 0.12) * clss_alq
            dados_tabela.append([f"Trimestre {trimestre}", csll_lp_vserv])
        print("CSLL")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def irpj():
        dados_tabela = []
        cabecalhos = ["Trimestre", "IRPJ trimestre", "Adicional", "IRPJ a pagar"]
        for trimestre, lucro_trimestre in enumerate(faturamentos_trimestres, start=1):

            presuncao = lucro_trimestre * 0.08
            irpj_lp_vserv = presuncao * 0.15

            if presuncao > 60000:
                adicional_irpj_lp_vserv = (presuncao - 60000) * 0.1
                if adicional_irpj_lp_vserv < 0:
                    adicional_irpj_lp_vserv = 0
                irpj_a_pagar_vserv = irpj_lp_vserv + adicional_irpj_lp_vserv
                irpj_a_pagar_vserv = round(irpj_a_pagar_vserv, 2)
                dados_tabela.append([f"Trimestre {trimestre}", irpj_lp_vserv, adicional_irpj_lp_vserv,
                                     irpj_a_pagar_vserv])

            elif presuncao <= 60000:
                adicional_irpj_lp_vserv = (presuncao - 60000) * 0.1
                if adicional_irpj_lp_vserv < 0:
                    adicional_irpj_lp_vserv = 0
                irpj_a_pagar_vserv = irpj_lp_vserv + adicional_irpj_lp_vserv
                irpj_a_pagar_vserv = round(irpj_a_pagar_vserv, 2)
                dados_tabela.append([f"Trimestre {trimestre}", irpj_lp_vserv, adicional_irpj_lp_vserv,
                                     irpj_a_pagar_vserv])
        print("IRPJ")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))


class CalculadoraImpostosVendaServicoLR:
    @staticmethod
    def pis():
        dados_tabela = []
        cabecalhos = ["Trimestre", "PIS a pagar", "Saldo"]
        pis_alq_lr_vserv = 0.0165
        saldo = 0.00

        for trimestre in range(4):
            faturamento = faturamentos_trimestres[trimestre]
            compra = compras[trimestre]
            pis_lr_vserv = faturamento * pis_alq_lr_vserv
            pis_desconto_lr_vserv = compra * pis_alq_lr_vserv
            pis_a_pagar_lr_vserv = pis_lr_vserv - pis_desconto_lr_vserv
            pis_a_pagar_lr_vserv = round(pis_a_pagar_lr_vserv, 2)

            if pis_a_pagar_lr_vserv < 0:
                saldo += pis_a_pagar_lr_vserv
                dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_vserv, saldo])
            elif pis_a_pagar_lr_vserv > 0:
                if saldo < 0:
                    pis_compensado_lr_vserv = pis_a_pagar_lr_vserv + saldo
                    pis_a_pagar_lr_vserv = round(pis_a_pagar_lr_vserv, 2)
                    dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_vserv, pis_compensado_lr_vserv])
                    saldo = saldo + pis_a_pagar_lr_vserv
                    if saldo < 0:
                        saldo = 0
                else:
                    dados_tabela.append([f"Trimestre {trimestre + 1}", pis_a_pagar_lr_vserv, saldo])
        print("PIS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def cofins():
        dados_tabela = []
        cabecalhos = ["Trimestre", "COFINS a pagar", "Saldo"]
        cofins_alq_lr_vserv = 0.076
        saldo = 0.00

        for trimestre in range(4):
            faturamento = faturamentos_trimestres[trimestre]
            compra = compras[trimestre]
            cofins_lr_vserv = faturamento * cofins_alq_lr_vserv
            cofins_desconto_lr_vserv = compra * cofins_alq_lr_vserv
            cofins_a_pagar_lr_vserv = cofins_lr_vserv - cofins_desconto_lr_vserv
            cofins_a_pagar_lr_vserv = round(cofins_a_pagar_lr_vserv, 2)

            if cofins_a_pagar_lr_vserv < 0:
                saldo += cofins_a_pagar_lr_vserv
                dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_vserv, saldo])
            elif cofins_a_pagar_lr_vserv > 0:
                if saldo < 0:
                    cofins_compensado_lr_vserv = cofins_a_pagar_lr_vserv + saldo
                    cofins_a_pagar_lr_vserv = round(cofins_a_pagar_lr_vserv, 2)
                    dados_tabela.append(
                        [f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_vserv, cofins_compensado_lr_vserv])
                    saldo = saldo + cofins_a_pagar_lr_vserv
                    if saldo < 0:
                        saldo = 0
                else:
                    dados_tabela.append([f"Trimestre {trimestre + 1}", cofins_a_pagar_lr_vserv, saldo])
        print("COFINS")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def csll():
        dados_tabela = []
        cabecalhos = ["Trimestre", "CSLL a pagar"]
        clss_alq = 0.09

        for trimestre, faturamento in enumerate(faturamentos_trimestres, start=1):
            csll_lr_vserv = faturamento * clss_alq
            dados_tabela.append([f"Trimestre {trimestre}", csll_lr_vserv])
        print("CSLL")
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt='rounded_grid'))

    @staticmethod
    def irpj():
        calcular_lucro()

if __name__ == '__main__':
    while True:
        faturamentos_trimestres = []
        compras = []
        despesas = []
        folhas = []
        lucro_real = []
        for trimestre in range(1, 5):
            faturamento_trimestre = float(
                input_valor(f"Digite o faturamento do trimestre {trimestre}: "))
            faturamentos_trimestres.append(faturamento_trimestre)
            compra = float(input_valor(f"Digite a compra do trimestre {trimestre}: "))
            compras.append(compra)
            despesa = float(input_valor(f"Digite a despesa do trimestre {trimestre}: "))
            despesas.append(despesa)
            folha = float(input_valor(f"Digite a folha do trimestre {trimestre}: "))
            folhas.append(folha)

        tipo_empresa = escolher_tipo_empresa()

        if tipo_empresa == 'Venda':
            print("Impostos Gerais: \n")
            simples_alq_serv = input_valor("Digite a alíquota do Simples Nacional: ")
            inss_alq_serv = input_valor("Digite a alíquota do INSS: ")
            icms_alq_venda = input_valor("Digite a alíquota do ICMS: ")
            CalculadoraImpostosGerais.simples()
            CalculadoraImpostosGerais.inss()
            CalculadoraImpostosGerais.icms()
            print("\nImpostos Lucro Presumido: \n")
            CalculadoraImpostosVendaLP.pis()
            CalculadoraImpostosVendaLP.cofins()
            CalculadoraImpostosVendaLP.csll()
            CalculadoraImpostosVendaLP.irpj()
            print("\nImpostos Lucro Real: \n")
            CalculadoraImpostosVendaLR.pis()
            CalculadoraImpostosVendaLR.cofins()
            CalculadoraImpostosVendaLR.csll()

        elif tipo_empresa == 'Serviço':
            print("Impostos Gerais: \n")
            simples_alq_serv = input_valor("Digite a alíquota do Simples Nacional: ")
            inss_alq_serv = input_valor("Digite a alíquota do INSS: ")
            iss_alq_serv = input_valor("Digite a alíquota do ISS: ")
            CalculadoraImpostosGerais.simples()
            CalculadoraImpostosGerais.inss()
            CalculadoraImpostosGerais.iss()
            print("\nImpostos Lucro Presumido: \n")
            CalculadoraImpostosServicoLP.pis()
            CalculadoraImpostosServicoLP.cofins()
            CalculadoraImpostosServicoLP.csll()
            CalculadoraImpostosServicoLP.irpj()
            print("\nImpostos Lucro Real: \n")
            CalculadoraImpostosServicoLR.pis()
            CalculadoraImpostosServicoLR.cofins()
            CalculadoraImpostosServicoLR.csll()

        elif tipo_empresa == 'VendaServiço':
            simples_alq_serv = input_valor("Digite a alíquota do Simples Nacional: ")
            inss_alq_serv = input_valor("Digite a alíquota do INSS: ")
            icms_alq_venda = input_valor("Digite a alíquota do ICMS: ")
            iss_alq_serv = input_valor("Digite a alíquota do ISS: ")
            print("Impostos Gerais: \n")
            CalculadoraImpostosGerais.simples()
            CalculadoraImpostosGerais.inss()
            CalculadoraImpostosGerais.icms()
            CalculadoraImpostosGerais.iss()
            print("\nImpostos Lucro Presumido: \n")
            CalculadoraImpostosVendaServicoLP.pis()
            CalculadoraImpostosVendaServicoLP.cofins()
            CalculadoraImpostosVendaServicoLP.csll()
            CalculadoraImpostosVendaServicoLP.irpj()
            print("\nImpostos Lucro Real: \n")
            CalculadoraImpostosVendaServicoLR.pis()
            CalculadoraImpostosVendaServicoLR.cofins()
            CalculadoraImpostosVendaServicoLR.csll()
        break



