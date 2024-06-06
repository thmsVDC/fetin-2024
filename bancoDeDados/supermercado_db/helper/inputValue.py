def input_number():
    value = input("Digite o id, nome, marca ou tipo: ")

    try:
        num = int(value)
        return num
    except ValueError:
        return value