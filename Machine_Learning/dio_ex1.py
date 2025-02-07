# SOBRE ENTRADA E SAÍDA DE DADOS EM PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# geralmente informando que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;

# Abaixo segue um exemplo de código que você pode ou não utilizar

# TODO: Com base nos pesos informados das notas A e B calcule a média.
# DICA: Utilize seus conhecimentos em lógica de programação, Precedência de Operadores Lógicos;

def calc (number1, number2):
    media = (3.5*number1+7.5*number2)/11
    return media

a = float(input(''))
b = float(input(''))
env = calc(a,b)

print(f"MEDIA = {env:.5f}")