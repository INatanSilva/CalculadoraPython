n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))

op = input('Escolha a sua operação (+, -, *, /):')

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)

else:
    op != '+, -, *, /'
    print('Operação Invalida.')
