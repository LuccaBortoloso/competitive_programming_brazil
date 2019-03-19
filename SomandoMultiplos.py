a= int(input())
b= int(input())
soma = 0
if(a < b):
    for i in range(a+1, b):
        if(i % 4 == 0 and 1000 % i == 0):
            soma += i
else:
    for i in range(b+1, a):
        if(i%4==0 and 1000 % i == 0):
            soma += i
print(soma)
