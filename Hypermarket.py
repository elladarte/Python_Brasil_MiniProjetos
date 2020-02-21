print("-"*25,"HYPERMARKET TABAJARA","-"*25)

def calculate(tipoCarne):

    quantidade = float(input("Informe a quantidade comprada: "))

    if (tipoCarne == 1):
        carne = "File Duplo"
        if (quantidade <= 5):
            valorBruto = quantidade * 4.9
        else:
            valorBruto = quantidade * 5.8

    if (tipoCarne == 2):
        carne = "Alcatra"
        if (quantidade <= 5):
            valorBruto = quantidade * 5.9
        else:
            valorBruto = quantidade * 6.8

    if (tipoCarne == 3):
        carne = "Picanha"
        if (quantidade <= 5):
            valorBruto = quantidade * 6.9
        else:
            valorBruto = quantidade * 7.8

    cartaoTabajara = input("Usara cartao Tabajara (S/N): ").upper()

    print("-" * 72)
    print("                              CUPOM FISCAL")

    desconto = 0.0

    print(f"Carne Escolhida: {carne}")
    print("Valor Bruto: ", valorBruto)

    if (cartaoTabajara == 'S'):
        print("Pagamento com cartao Tabajara")
        desconto = valorBruto * 0.05
    else:
        print("Pagamento nao sera com o cartao Tabajara")

    print("Desconto: ", desconto)
    print("Valor a Pagar: ", (valorBruto - desconto))

# MAIN PROGRAM
print("Açougue: Informe o tipo da carne escolhida: ")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")
tipoCarne = int(input("===> "))

if (tipoCarne == 1) or (tipoCarne == 2) or (tipoCarne == 3) :
    calculate(tipoCarne)
else:
    print("Invalid Operation")

print("-"*72)