# Tabuada
print("Tabuada: ")
numero = int(input("Digite seu número: "))

for tabuada in range(0, 11):

    print(f"{numero} X {tabuada} = {numero*tabuada}")
print("\n")

# Contador em duas forma, no for e while.
# Números impares e pares, crescente e
# decrescente, em duas forma, no for e while
# Soma até 100
# Soma os pares até 50
# Fibonacci com for e while


print("Contador no for: ")
for numeros in range(1, 11):
    print(numeros)
print("\n")


print("Contador no for decrescente: ")
for numero in range(10, 0, -1):
    print(numero)
print("\n")


print("Número pares no for: ")
for pares in range(2, 21, 2):
    print(pares)
print("\n")


print("Número pares decrescente no for: ")
for pares in range(20, 1, -2):
    print(pares)
print("\n")


print("Número impares no for: ")
for impares in range(1, 16, 2):
    print(impares)
print("\n")


print("Número impares decrescente no for: ")
for impa_decresente in range(15, 0, -2):
    print(impa_decresente)
print("\n")


print("Contador no while: ")
numero = 1
limite = 10

while numero <= limite:
    print(numero)
    numero += 1
print("\n")


print("Contador no while decrescente: ")
numero = 10
limite = 1

while numero >= limite:
    print(numero)
    numero -= 1
print("\n")


print("Número pares no while: ")
numero = 1
limite = 10

while numero <= limite:
    if numero % 2 == 0:
        print(numero)
    numero += 1
print("\n")


print("Números pares no while decrescente: ")
numero = 10
limite = 1

while numero >= limite:
    if numero % 2 == 0:
        print(numero)
    numero -= 1
print("\n")


print("Número impares no while: ")
numero = 1
limite = 10

while numero <= limite:
    if numero % 2 != 0:
        print(numero)
    numero += 1
print("\n")


print("Número impares no while decrescente: ")
numero = 10
limite = 1

while numero >= limite:
    if numero % 2 != 0:
        print(numero)
    numero -= 1
print("\n")

print("Soma dos números de 1 até 100: ")
soma = 0
for numero in range(1, 101):
    soma += numero
    print(soma)
print("\n")


print("Soma dos números pares até 50 no while: ")
numero = 0
limite = 50
soma = 0

while numero <= limite:
    if numero % 2 == 0:
        soma += numero
        print(soma)
    numero += 1
print("\n")


print("Sequência fibonacci até o 10° termo no for: ")
n = 10
a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b
print("\n")


print("Sequência fibonacci até o 10° termo no while: ")
n = 10
a, b = 0, 1
i = 0

while i < n:
    print(a)
    a, b = b, a + b
    i += 1
print("\n")


print("Sequência fibonacci até o 10° termo no while: ")
n = 10
a, b = 0, 1
i = 0

while i < n:
    print(a, end = " ")
    a, b = b, a + b
    i += 1
print("\n")