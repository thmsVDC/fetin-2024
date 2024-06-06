from database import Database
from supermercado import Produtos
from helper.convertion import dict_to_doc
from helper.inputValue import input_number

db = Database(database="fetin", collection="supermercado")
dbCounters = Database(database="fetin", collection="counters")
#db.resetDatabase()

product = Produtos(db)
while True:
    print('1. Adicionar produto')
    print('2. Buscar produto')
    print('3. Editar produto')
    print('4. Remover produto')
    print('5. Sair')
    choice = input('Digite uma opção: ')
    print('----------')

    if choice == '1':
        nome = str(input('Nome: '))
        quantidadePorUnidade = str(input('quantidadePorUnidade: '))
        marca = str(input('Marca: '))
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        tipo = str(input('Tipo: '))
        localizacao = str(input('Localização: '))

        product.createProduct(nome, quantidadePorUnidade, marca, quantidade, preco, tipo, localizacao)


    if choice == '2':
        search = str(input('Digite o que deseja procurar: '))

        results = product.searchProduct(search)
        documents = [dict_to_doc(d) for d in results]
        for doc in documents:
            print(
                f'{doc.id} | {doc.nome} | {doc.quantidadePorUnidade} | {doc.marca} | {doc.quantidade} | R${doc.preco} | {doc.tipo} | {doc.localizacao} |')

        input('Aperte enter para continuar...')
        print('\n' * 100)

    elif choice == '3':
        control = True
        while control:
            search = input_number()
            type(search)
            results = product.showAllProducts(search)
            documents = [dict_to_doc(d) for d in results]
            for doc in documents:
                print(
                    f'{doc.id} | {doc.nome} | {doc.quantidadePorUnidade} | {doc.marca} | {doc.quantidade} | R${doc.preco} | {doc.tipo} | {doc.localizacao} |')

            product_found = str(input('Produto encontrado? [S/N]'))
            if product_found == 'S' or product_found == 's':
                control = False
            print('----------')
            id_search = int(input('Digite o ID do produto: '))

            print('\n' * 100)
            result = product.showAllProducts(id_search)
            document = dict_to_doc(result[0])
            print(
                f'{document.id} | {document.nome} | {document.quantidadePorUnidade} | {document.marca} | {document.quantidade} | R${document.preco} | {document.tipo} | {document.localizacao} |')

            print(f'Editando produto com ID: {id_search}')

            id = id_search
            nome = str(input('Nome: '))
            quantidadePorUnidade = str(input('quantidadePorUnidade: '))
            marca = str(input('Marca: '))
            quantidade = int(input('Quantidade: '))
            preco = float(input('Preço: '))
            tipo = str(input('Tipo: '))
            localizacao = str(input('Localização: '))

            product.editProcuct(id, nome, quantidadePorUnidade, marca, quantidade, preco, tipo, localizacao)

    elif choice == '4':
        pass

    elif choice == '5':
        print('\n' * 100)
        print('Volte sempre!')
        break

    else:
        input('Opção inválida. Aperte enter para tentar novamente...')
        print('\n' * 100)
