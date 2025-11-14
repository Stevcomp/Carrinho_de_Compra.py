# Calculadora de ingestão diária de água
# Fórmula: peso corporal (kg) x 35 ml

def calcular_agua(peso):
    # Multiplica o peso por 35 ml e converte para litros
    litros = (peso * 35) / 1000
    return litros

# Entrada do usuário
peso = float(input("Digite seu peso exato em kg (Ex: 60.77): "))

# Cálculo
quantidade = calcular_agua(peso)

# Saída
print(f"Você deve tomar aproximadamente {quantidade:.2f} litros de água por dia!")