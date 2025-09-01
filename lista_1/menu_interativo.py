def menu_interativo():
    while True:
        print("\n=== MENU INTERATIVO ===")
        print("1 - Olá mundo")
        print("2 - Eu programo em Python")
        print("3 - Laços de repetição")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print("Olá mundo")
        elif escolha == "2":
            print("Eu programo em Python")
        elif escolha == "3":
            print("Laços de repetição")
        elif escolha == "0":
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Chamar a função principal
menu_interativo()
