rule = ['/', '*', '+', '-']

inp = "5+5*5/5"
inp += "z"

char = ""
x = []

for d in inp:
    if d in rule or d == "z":
        if d != "z":
            x.append(d)
        x.append(char)
        char = ""
        continue
    if d != "z":
        char += d

inp = x.copy()
print(inp)


def calculator(y, z, sym):
    y, z = float(y), float(z)

    if sym == "+":
        return str(z + y)
    elif sym == "-":
        return str(y - z)
    elif sym == "*":
        return str(y * z)
    else:
        return str(y / z)


while len(inp) != 1:
    for i in range(len(rule)):
        while True:
            if "temp" in inp:
                inp.remove("temp")
            else:
                break
        print(inp)
        for j in range(len(inp)):
            try:
                if inp[j] == rule[i]:
                    temp = calculator(inp[j - 1], inp[j + 1], inp[j])
                    print(inp)
                    inp[j - 1] = temp
                    print(inp)
                    inp[j] = "temp"
                    print(inp)
                    inp[j + 1] = "temp"
                    print(inp)
            except IndexError:
                pass
