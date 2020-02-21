import random

arquivo = open('C:/PythonFundamentos/Exercicios Feitos/Python Brasil/6_Strings/Scrambled Word/13_words.txt','r')
conteudo = arquivo.read()

conteudoLista = list(conteudo.split())

word = random.choice(conteudoLista)

shuffled = list(word)
random.shuffle(shuffled)
shuffled = "".join(shuffled)

print("-"*61)
print("-"*20,"SCRAMBLED WORD GAME","-"*20)
print("Guess which word was scrambled below:")
print(shuffled)
print("-"*61)

tent = 0
while (tent < 6):

    letter = input("Type the word you think it is: ").upper()
    print("-"*61)

    if (letter != word):
        tent += 1
        if (tent < 6):
            print("Wrong answer")
            print("Try one more time!")
            print("-" * 61)

    else:
        print("You're right!")
        print("Congratulations!! Won the Game!")
        print("-" * 61)
        break

if (tent >= 6):
    print("You used all your attempts.")
    print("You lost the game.")
    print("-" * 61)

arquivo.close()