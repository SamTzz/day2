if __name__ == '__main__':
    f = open("input.txt","r")
    data = f.read().split("\n")

    instructions = []
    horizontale = 0
    profondeur = 0
    resultat = 0

    for l in data:
        line = l.split(" ")
        tabLine = []
        tabLine.append(line[0])
        tabLine.append(int(line[1]))
        instructions.append(tabLine)

    for l in instructions:
        if l[0] == "forward" :
            horizontale = horizontale + l[1]
        if l[0] == "down" :
            profondeur = profondeur + l[1]
        if l[0] == "up" :
            profondeur = profondeur - l[1]

    resultat = profondeur * horizontale

    print(instructions)
    print(resultat)