n = int(input())
chavesE = 0
chavesD = 0
for i in range (n):
    linha = input()
    chavesE += linha.count("{")
    chavesD += linha.count("}")
if(chavesE == chavesD):
    print("S")
else:
    print("N")
