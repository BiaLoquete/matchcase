
semana = str (input("Digite um dia da semana (segunda-feira, terça-feira...): "))


match (semana):
    case ("segunda-feira"):
        print('Dia útil: segunda')
    case ("terça-feira"):
        print('Dia útil: terça')
    case ("quarta-feira"):
        print('Dia útil: quarta')
    case ("quinta-feira"):
        print('Dia útil: quinta')
    case ("sexta-feira"):
        print('Dia útil: sexta')
    case ("sábado"):
        print('Fim de semana: sábado')
    case ("domingo"):
        print('Fim de semana: domingo')