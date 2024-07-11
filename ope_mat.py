num1 = int (input("digite o primeiro numero: "))
num2 = int (input("digite o segundo numero"))

operacao = input ("digite a operação que deseja realizar (+,-,*,/): ")

if operacao == '+':
    print(num1+num2)
elif operacao == '-':
    print(num1-num2)
elif operacao == '*':
    print(num1*num2)
elif operacao == '/':
    print(num1/num2)
else: 
    print ("operação invalida")