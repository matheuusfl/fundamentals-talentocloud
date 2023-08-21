def soma (number1, number2, operador):
    return(number1+number2)
def subtrair (number1, number2):
    return(number1-number2)
def multitiplicar (number1, number2):
    return (number1*number2)
def divisao (number1, number2):
    return(number1/number2)
def calculadora(number1, number2, operador):
    if operador == 1:  
        resultado = number1 + number2
    elif operador == 2:  
        resultado = number1 - number2
    elif operador == 3:  
        resultado = number1 * number2
    elif operador == 4:  
        if number2 != 0:
            resultado = number1 / number2
        else:
            print("Erro!")
            return None
        return 0
    
    return resultado

number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))
operador = int(input("Digite o número da operação (1. soma, 2. Subtrair, 3. multiplicar, 4. divisao): "))

resultado = calculadora(number1, number2, operador)
if resultado is not None:
    print("resultado da operaçao:", resultado)