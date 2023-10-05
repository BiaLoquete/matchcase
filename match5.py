
login = str (input("Digite seu Login: "))
senha = str (input("Digite sua senha: "))

match (login,senha):
    case ("admin", "admin_pass"):
        print('Logado com sucesso')
    case ("user", "user_pass"):
        print('Logado com sucesso')
    case ("guest", _):
        print('Logado com sucesso')
    case _:
        print('Login ou senha incorreto')
