def cpafVadid(cpf):

    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    cpfNew = cpf[0:9]
    cv = cpf[9:11]

    if (len(cpf) != 11) \
            or (cpf == "00000000000") or (cpf == "11111111111" ) \
            or (cpf == "22222222222") or (cpf == "33333333333") \
            or (cpf == "44444444444") or (cpf == "55555555555") \
            or (cpf == "66666666666") or (cpf == "77777777777") \
            or (cpf == "88888888888") or (cpf == "99999999999"):
        print("CPF informado invalido")
        return False

    fator = 10
    soma = 0
    for i in range(0, 9):
        soma += (int(cpfNew[i]) * fator)
        fator -= 1

    restoDivi = soma % 11
    res = 11 - restoDivi

    if (res > 9):
        res = 0

    cvGer = str(res)

    cpfGerTemp = cpfNew + cvGer

    fator2 = 11
    soma2 = 0
    for i in range(0, 10):
        soma2 += (int(cpfGerTemp[i]) * fator2)
        fator2 -= 1

    restoDiv2 = soma2 % 11
    res2 = 11 - restoDiv2

    if (res2 > 9):
        res2 = 0

    cvGer += str(res2)
    cpfGer = cpfNew + cvGer

    if (cpf == cpfGer):
        print("CPF informado Valido")
    else:
        print("CPF informado Invalido")
        return False

    return True
