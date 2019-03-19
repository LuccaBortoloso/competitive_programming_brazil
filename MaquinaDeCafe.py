def main():
    andares = []
    andares.append(int(input()))
    andares.append(int(input()))
    andares.append(int(input()))
    minutos = 0

    if(andares[0] >= andares[1] + andares[2] or andares[2] >= andares[0] + andares[1]):
        index = andares.index(max(andares))
        if(index == 0):
            minutos = andares[1] * 2 + andares[2] * 4
        elif(index == 2):
            minutos = andares[1] * 2 + andares[0] * 4
    else:
        minutos = (andares[0] * 2) + (andares[2] * 2)
    print(minutos)
