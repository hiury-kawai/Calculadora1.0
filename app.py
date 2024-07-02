# Calculadora básica em Python
import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def raiz_quadrada(a):
    return math.sqrt(a)

def potencia(a, b):
    return a ** b

def logaritmo(a):
    return math.log(a)

def seno(a):
    return math.sin(a)

def cosseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

def opcao_to_str(opcao):
    if opcao == 1:
        return "+"
    elif opcao == 2:
        return "-"
    elif opcao == 3:
        return "*"
    elif opcao == 4:
        return "/"
    elif opcao == 5:
        return "√"
    elif opcao == 6:
        return "^"
    elif opcao == 7:
        return " log "
    elif opcao == 8:
        return " sen "
    elif opcao == 9:
        return " cos "
    elif opcao == 10:
        return " tan "



historico = []

print("Calculadora básica")
print("------------------")

while True:
    print("Opções:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz quadrada")
    print("6. Potência")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Cosseno")
    print("10. Tangente")
    print("11. Histórico")
    print("12. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 5:
            num1 = float(input("Digite o primeiro número: "))
            resultado = raiz_quadrada(num1)
            historico.append(f"{num1} {opcao_to_str(opcao)} = {resultado}")
            print(f"A raiz quadrada de {num1} é: {resultado}")
            print()
            print()
            continue
        elif opcao == 7:
            num1 = float(input("Digite o número: "))
            resultado = logaritmo(num1)
            historico.append(f"{num1} {opcao_to_str(opcao)} = {resultado}")
            print(f"O logaritmo de {num1} é: {resultado}")
            print()
            print()
            continue
        elif opcao == 8:
            num1 = float(input("Digite o número: "))
            resultado = seno(num1)
            historico.append(f"{num1} {opcao_to_str(opcao)} = {resultado}")
            print(f"O seno de {num1} é: {resultado}")
            print()
            print()
            continue
        elif opcao == 9:
            num1 = float(input("Digite o número: "))
            resultado = cosseno(num1)
            historico.append(f"{num1} {opcao_to_str(opcao)} = {resultado}")
            print(f"O cosseno de {num1} é: {resultado}")
            print()
            print()
            continue
        elif opcao == 10:
            num1 = float(input("Digite o número: "))
            resultado = tangente(num1)
            historico.append(f"{num1} {opcao_to_str(opcao)} = {resultado}")
            print(f"A tangente de {num1} é: {resultado}")
            print()
            print()
            continue
        elif opcao == 12:
            break

        elif opcao == 11:
            print()
            print("Histórico de operações:")
            for i, opera in enumerate(historico):
                print(f"{i+1}. {opera}")
                print()
            continue

        elif opcao > 12:
            print("Opção inválida")
            print("#########################################")
            print()
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: entrada inválida!")
        print()
        print()
        continue

    if opcao == 1:
        resultado = soma(num1, num2)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = divisao(num1, num2)
    elif opcao == 6:
        resultado = potencia(num1, num2)
    elif opcao == 7:
        continue
       
    historico.append(f"{num1} {opcao_to_str(opcao)} {num2} = {resultado}")
    print(f"Resultado: {resultado}")
    print()
    print()