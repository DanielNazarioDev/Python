# Calcule o IMC e classifique o resultado

peso = float(input("Digite seu peso com decimais:(ex: 78.0) - "))
altura = float(input("Digite sua altura em metros:(ex: 1.68) - "))

formulaIMC = peso / (altura ** 2)

# Classificações:

if formulaIMC <= 18.5:
    print("Abaixo do peso")
elif formulaIMC <= 24.9:
    print("Peso normal")
elif formulaIMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

# Sistema de Notas

nota = float(input("Digite sua nota: "))
# Critérios:
# 9.0 a 10.0: A (Excelente)
# 7.0 a 8.9: B (Bom)
# 5.0 a 6.9: C (Regular)
# 3.0 a 4.9: D (Insuficiente)
# 0.0 a 2.9: F (Reprovado)

if nota >= 9.0:
    print("A (Excelente)")
elif nota >= 7.0:
    print("B (Bom)")
elif nota >= 5.0:
    print("C (Regular)")
elif nota >= 3.0:
    print("D (Insuficiente)")
else:
    print("Reprovado")

# Classificador de Temperatura
# Classifique a temperatura

temperatura = float(input("Digite a temperatua atual: "))
if temperatura < 0:
    print("Congelante")
elif temperatura <= 15:
    print("Frio")
elif temperatura <= 25:
    print("Agradável")
elif temperatura <= 35:
    print("Quente")
else:
    print("Escaldante")

# Sistema de Login

# Simule um sistema de autenticação
usuario = "admin", "user", "guest"
senha = "Exemplo123", "SenhaUser", "Guest123"
tentativas = 3

# Regras:
"""
- Usários e senhas corretos: "Login realizado com sucesso!"
- Usuário correto, senha incorreta: "Senha incorreta. Tente novamente."
- Usuário incorreto: "Usuário não encontrado."
- Mais de 3 tentativas: "Número máximo de tentativas excedido. Acesso bloqueado."

# Usuários válidos: admin, user, guest
# Senhas: admin= "Exemplo123", user="SenhaUser", guest="Guest123"
"""
# Codigos aqui:
while tentativas > 0:
    usuario_input = input("Digite seu usuário: ")
    senha_input = input("Digite sua senha: ")

    if usuario_input == usuario and senha_input == senha:
        print("Login realizado com sucesso!")
        break
    elif usuario_input == usuario and senha_input != senha:
        tentativas -= 1
        print(f"Senha incorreta. Tente novamente. Tentativas restantes: {tentativas}")
    elif usuario_input != usuario:
        print("Usuário não encontrado.")
        break
    if tentativas == 0:
        print("Número máximo de tentativas excedido. Acesso bloqueado.")
        break

# Calculadora de Desconto
# Sistema de desconto por categoria de cliente

# Regras de desconto:
"""
- Nprmal: 5% se primeira compra, senão 0%
- Premium: 10% sempre, +5% se primeira compra
- VIP: 15% sempre, +10% se primeira compra
- COMPRAS ACIMA DE R$ 1000,00 TEM +5% adicional para TODOS
"""
valor_compra = float(input("Digite o valor da compra: R$"))
categoria = input("Digite sua categoria (Normal, Premium, VIP): ").strip().lower()
primeira_compra = input("É sua primeira compra? (sim/não): ").strip().lower() == "sim"
desconto = 0
if categoria == "normal":
    desconto = 0.05 if primeira_compra else 0
elif categoria == "premium":
    desconto = 0.10 + (0.05 if primeira_compra else 0)
elif categoria == "vip":
    desconto = 0.15 + (0.10 if primeira_compra else 0)
if valor_compra > 1000:
    desconto += 0.05
valor_final = valor_compra * (1 - desconto)
print(f"Valor final com desconto: R${valor_final:.2f} (Desconto de {desconto * 100:.2f}%)")

# Validador de Idade para conteúdo
# Regras:
# Infantil: qualquer idade
# Ação: 12 anos ou mais
# Terror: 16 anos ou 14+ com autorização dos pais
# Adulto: 18+ anos
# Retorne "Acesso permitido" ou "Acesso negado"

idade = int(input("Digite sua idade: "))
genero = input("Digite o gênero do conteúdo (Infantil, Ação, Terror, Adulto): ").strip().lower()
if genero == "infantil":
    print("Acesso permitido")
elif genero == "ação":
    if idade >= 12:
        print("Acesso permitido")
    else:
        print("Acesso negado")
elif genero == "terror":
    if idade >= 16 or (idade >= 14 and input("Você tem autorização dos pais? (sim/não): ").strip().lower() == "sim"):
        print("Acesso permitido")
    else:
        print("Acesso negado")
elif genero == "adulto":
    if idade >= 18:
        print("Acesso permitido")
    else:
        print("Acesso negado")
# Sistema de Comissão de Vendas
# Calcule comissão baseada em múltiplos critérios
"""
REGRAS DE COMISSÃO:
Base: 3% das vendas se bateu a meta, 1% se não bateu
Bônus tempo de empresa:
 - 6 a 12 meses: +0.5%
 - 12 a 24 meses: +1%
 - 24 meses ou mais: +2% se vendas trimestrais > 3000
 Limite maximo: 8% das vendas
"""
# Codigos aqui:
vendas = float(input("Digite o valor total das vendas: R$"))
meta = float(input("Digite o valor da meta: R$"))
tempo_empresa = int(input("Digite o tempo de empresa em meses: "))
if vendas >= meta:
    comissao = 0.03 * vendas
else:
    comissao = 0.01 * vendas
if 6 <= tempo_empresa < 12:
    comissao += 0.005 * vendas
elif 12 <= tempo_empresa < 24:
    comissao += 0.01 * vendas
elif tempo_empresa >= 24:
    if vendas > 3000:
        comissao += 0.02 * vendas
if comissao > 0.08 * vendas:
    comissao = 0.08 * vendas
print(f"Comissão total: R${comissao:.2f} (Limite máximo de 8% das vendas aplicado)")

# Sistema de Aprovação de Empréstimo
# Critérios de aprovação:
# 1. Idade entre 18 e 70 anos
# 2. Renda mensal >= R$ 2000
# 3. Valor empréstimo <= 5x a renda mensal
# 4. Score >= 600
# 5. Sem restrições no CPF
# 6. Tempo de emprego >= 12 meses

# Bônus: Score >= 750 permite empréstimo até 8x a renda

# Seu código aqui:
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: R$"))
valor_emprestimo = float(input("Digite o valor do empréstimo: R$"))
score = int(input("Digite seu score de crédito: "))
restricoes_cpf = input("Você tem restrições no CPF? (sim/não): ").strip().lower() == "sim"
tempo_emprego = int(input("Digite o tempo de emprego em meses: "))
if 18 <= idade <= 70 and renda_mensal >= 2000 and not restricoes_cpf and tempo_emprego >= 12:
    limite_emprestimo = 5 * renda_mensal
    if score >= 750:
        limite_emprestimo = 8 * renda_mensal
    if valor_emprestimo <= limite_emprestimo:
        print("Empréstimo aprovado!")
    else:
        print(f"Empréstimo negado! Valor máximo permitido: R${limite_emprestimo:.2f}")
else:
    print("Empréstimo negado! Verifique os critérios de idade, renda, restrições no CPF e tempo de emprego.")

# Sistema de Entrega Dinâmico
# Regras:
# Prazo base por região (primeiros 2 dígitos do CEP):
# 01-05 (SP capital): 1 dia
# 06-19 (SP interior): 2 dias
# 20-28 (RJ): 3 dias
# Outros: 5 dias

# Modificadores:
# - Cliente premium: -1 dia
# - Peso > 5kg: +1 dia
# - Valor > R$ 500: frete grátis, senão R$ 15 + R$ 3 por kg
# - Pedido sexta/sábado/domingo: +1 dia

# Seu código aqui:
cep = input("Digite o CEP (somente números): ")
peso = float(input("Digite o peso do pacote em kg: "))
valor_pedido = float(input("Digite o valor do pedido: R$"))
cliente_premium = input("Você é um cliente premium? (sim/não): ").strip().lower() == "sim"
dia_entrega = 0

if cep.startswith(("01", "02", "03", "04", "05")):
    dia_entrega = 1
elif cep.startswith(("06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19")):
    dia_entrega = 2
elif cep.startswith(("20", "21", "22", "23", "24", "25", "26", "27", "28")):
    dia_entrega = 3
else:
    dia_entrega = 5
if cliente_premium:
    dia_entrega -= 1
if peso > 5:
    dia_entrega += 1
if valor_pedido > 500:
    frete = 0
else:
    frete = 15 + (3 * peso)
if dia_entrega < 0:
    dia_entrega = 0
if cep.endswith(("6", "7", "8", "9", "0")):  # Verifica se é sexta, sábado ou domingo
    dia_entrega += 1
print(f"Prazo de entrega: {dia_entrega} dias")