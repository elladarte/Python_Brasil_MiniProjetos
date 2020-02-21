print("-"*25,"NUMBER PRIME","-"*25)

number = int(input("Type a number: "))
seq_number,prime, not_prime = [],[],[]
dict = {}

for i in range(0,number + 1):
    seq_number.append(i)
print(f"Sequence: {seq_number}")

for i in seq_number:
    val_prime = True
    for j in range(2,int(i/2 + 1)):
        if (i % j == 0):
            val_prime = False

    if (val_prime):
        prime.append(i)
    else:
        not_prime.append(i)

for i in not_prime:
    div = []
    for j in range(1,i+1):
        if (i % j == 0):
            div.append(j)

        dict[i] = div

print(f"Number prime: {prime}")
print(f"Numbers not prime: {not_prime}")

print("-"*65)
print("Divisor of numbers not prime: ")

for num,divi in dict.items():
    print(num,divi)

print("-"*65)