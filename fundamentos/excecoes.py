while True:
    try:
        valor = int(input("Digite um numero: "))
    except ValueError:
        print("valor inválido!")
    except KeyBoardInterrupt:
        print("usuário interrompeu o programa")
        break
    else:
        print("o valor é {0}".format(valor))
        break
