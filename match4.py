
animal = str (input("Digite um animal: "))


match (animal):
    case ("vaca"):
        print('O animal é a vaca')
    case ("galinha"):
        print('O animal é a galinha')
    case ("ovelha"):
        print('O animal é a ovelha')
    case _:
        print('Animal desconhecido')