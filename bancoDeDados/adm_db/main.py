from database import Database
from adm import ADMs

db = Database(database="fetin", collection="adm")
db.resetDatabase()

adm = ADMs(db)

while True:
    print('1. Adicionar ADM')
    print('2. Aditar ADM')
    print('3. Buscar ADM')
    print('4. Remover ADM')
    print('5. Sair')
    choice = input('Digite um opção: ')
    print('\n'*20)

    if choice == '1':
        print('Adicionar ADM')
        nome = input('Nome: ')
        senha = input('Senha: ')
        adm.createADM(nome,senha)
        print('Aperte enter para continuar...')
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print('\n'*20)
        print('Saindo...')
        break