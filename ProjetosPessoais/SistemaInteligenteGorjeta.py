# Criar um Sistema de Inteligente de Gorjetas

# Crie as funções necessárias para o sistema de gorjetas

historico = []

def calcular_gorjeta(valor_conta, percentual_gorjeta):
    return valor_conta * percentual_gorjeta
def calcular_total(valor_conta, gorjeta):
    return valor_conta + gorjeta
def exibir_resultados(valor_conta, percentual_gorjeta, gorjeta, total):
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Percentual de gorjeta: {percentual_gorjeta * 100:.0f}%")
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

def registrar_historico(valor_conta, percentual_gorjeta, gorjeta, total):
    historico.append({
        'valor_conta': valor_conta,
        'percentual_gorjeta': percentual_gorjeta,
        'gorjeta': gorjeta,
        'total': total
    })
def exibir_historico():
    if not historico:
        print("Nenhum registro de gorjeta encontrado.")
        return
    print("\nHistórico de Gorjetas:")
    for i, registro in enumerate(historico, start=1):
        print(f"{i}. Valor da conta: R$ {registro['valor_conta']:.2f}, "
              f"Percentual de gorjeta: {registro['percentual_gorjeta'] * 100:.0f}%, "
              f"Gorjeta: R$ {registro['gorjeta']:.2f}, "
              f"Total: R$ {registro['total']:.2f}")
