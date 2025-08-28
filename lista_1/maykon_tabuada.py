usuario = float(input("entre com o numero que deseja ver a tabuada: "))

print(f"Tabuada do {usuario}:")

for i in range(1, 11):
    resultado = usuario * i
    print(f"{usuario} x {i} = {resultado}")