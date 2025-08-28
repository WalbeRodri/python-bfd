numero = int(input("Digite um número para verificar se é primo: "))


primo = True


if numero <= 1:
    primo = False
else:
    
    for i in range(2, int(numero**0.5) + 1):
       
        if numero % i == 0:
            primo = False
            break 

if primo:
    print(f"O número {numero} é um número primo.")
else:
    print(f"O número {numero} não é um número primo.")