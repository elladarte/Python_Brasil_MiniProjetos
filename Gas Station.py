print("----------------------- GAS STATION ------------------------")

def calculate():

    pa, pg = 1.9, 2.5
    l = float(input("Type how many litter you want to put:"))

    if (c == "A"):
        p = l * pa
        if (l <= 20):
            p *= 0.97
        else:
            p *= 0.95

    if (c == "G"):
        p = l * pg
        if (l <= 20):
            p *= 0.96
        else:
            p *= 0.94

    print("-" * 60)
    print("Value to pay: ", round(p))

# MAIN PROGRAM
print("Type which fuel you want to fill"
                "\n A - Alcool"
                "\n G - Gasoline ")
c = str(input("===> ").upper())
print("-" * 60)

if (c == "A") or (c == "G"):
    calculate()
else:
    print("Invalid Operation")
print("-" * 60)
