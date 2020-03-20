print("CONTROLE DE COTAS DE DISCO")

# CRIANDO O ARQUIVO USUARIOS
arq = open("usuarios.txt","w")
arq.write("alexandre 456123789"
    "\nanderson 1245698456"
    "\nantonio 123456456"
    "\ncarlos 91257581"
    "\ncesar 987458"
    "\nrosemary 789456125")
arq.close()

# LENDO O ARQUIVO USUARIOS LINHA POR LINHA
arq_read = open("usuarios.txt","r")
linhas = arq_read.readlines()
arq_read.close()

# VARIAVEIS
usuarios = []
espacosUtilizados = []
espacoTotal = 0.0

# LOOP FOR PARA ADICIONAR CADA UMA DAS LINHAS DO ARQUIVO NAS VARIAVEIS
for linha in linhas:
    campos = linha.split()
    usuario = campos[0]
    espacoUtilizado = int(campos[1])
    usuarios.append(usuario)
    espacosUtilizados.append(espacoUtilizado)
    espacoTotal += espacoUtilizado

# CRIANDO O ARQUIVO PARA O RELATORIO
arq1 = open('relatorio.txt', 'w')
arq1.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
arq1.write(
    '------------------------------------------------------------------------')
arq1.write('\nNr.  Usuario        Espaco utilizado     %% do uso')

# LOOP FOR PARA REALIZAR OS CALCULOS DE CADA ITENS DAS LISTAS/VARIAVEIS
for i in range(0, len(usuarios)):
    espacoMB = espacosUtilizados[i] / (1024.0 * 1024.0)
    percentualUso = espacosUtilizados[i] / espacoTotal
    arq1.write('\n%d - %s - %.2f MB - %.2f%%' %
                       (i + 1, usuarios[i], espacoMB, percentualUso * 100.0))

#  RESULTADO FINAL DOS CALCULOS
arq1.write('\nEspaco total ocupado: %.2f MB' %
                   (espacoTotal / (1024.0 * 1024.0)))
arq1.write('\nEspaco medio ocupado: %.2f MB' %
                   (espacoTotal / len(usuarios) / (1024.0 * 1024.0)))
arq1.close()
