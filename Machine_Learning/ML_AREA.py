# Entrada dos valores e conversão para float
lados = [float(x) for x in input().split()]

# Atribuição dos valores
a = lados[0]
b = lados[1]
c = lados[2]

# Verificação da condição de existência de um triângulo
if a + b > c and a + c > b and b + c > a:
    print(f"Perimetro = {a + b + c:.1f}")
else:
    # Cálculo da área do trapézio usando a fórmula ( (base maior + base menor) * altura ) / 2
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
