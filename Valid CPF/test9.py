import sys

cpf = input("Digite o numero do seu cpf no formato xxx.xxx.xxx-xx: ")

cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

cpfNew = cpf[0:9]
cv = cpf[9:11]

print(cpfNew)
print(cv)

if (len(cpf) != 11):
    print("CPF informado invalido")
    sys.exit()

fator1 = 10
soma1 = 0
for i in range(0, 9):
    soma1 += (int(cpfNew[i]) * fator1)
    fator1 -= 1

restoDiv = soma1 % 11
print("resto Divisao 1:",restoDiv)
res = 11 - restoDiv
print("resultado 1:",res)

if (res > 9):
    res = 0
else:
    res = res

cvGer = str(res)

print("codigo gerado 1:",cvGer)

cpfGerTemp = cpfNew + cvGer
print("cpf gerado temporario:",cpfGerTemp)

fator2 = 11
soma2 = 0
for i in range(2,10):
    soma2 += (int(cpfGerTemp[i]) * fator2)
    fator2 -= 1

print("soma 2 antes de soma o 1:",soma2)
#soma2 += int(cpfNew[0])
print("soma 2 depois de soma o 1:",soma2)
restoDiv2 = soma2 % 11
print("resto Divisao 2:",restoDiv2)
res2 = 11 - restoDiv2
print("resultado 2:",res2)

if (res2 > 9):
    res2 = 0
else:
    res2 = res2

cvGer += str(res2)
print("codigo gerado: ",cvGer)
cpfGer = cpfNew + cvGer
print("cpf gerado 2: ",cpfGer)

if (cpf == cpfGer):
    print("CPF informado Valido")
else:
    print("CPF informado Invalido")