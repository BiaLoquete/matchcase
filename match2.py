
cor = str (input("Digite uma cor entre azul, vermelho ou verde: "))


match (cor):
    case ("azul"):
        print('Digitou azul')
    case ("vermelho"):
        print('Digitou vermelho')
    case ("verde"):
        print('Digitou verde')
    case _:
        print('Cor desconhecida')