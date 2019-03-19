cont = int(input("Quantos números"))

bits,qtd_torneiras,valor_inicial = map(int,input().split())
torneiras = input().split()
torneiras = [int(x) for x in torneiras]

vetor = list(bin(valor_inicial)[2:])
vetor = [int(x) for x in vetor]
vetor_reverso = list(reversed(vetor))

print(vetor)
while(cont> 0):
    xor = 0
    for i in range(qtd_torneiras):
        xor = xor ^ int(vetor_reverso[int(torneiras[i])])
    del vetor[-1]
    vetor.insert(0,xor)
    vetor_reverso = list(reversed(vetor))
    print(vetor)
    cont -= 1
