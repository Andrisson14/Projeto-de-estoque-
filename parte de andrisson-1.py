import json
import os

arquivo_estoque = "estoque.json"

if os.path.exists(arquivo_estoque):
    with open(arquivo_estoque, "r", encoding="utf-8") as f:
        estoque = json.load(f)
else:
    estoque = {
}

def salvar_estoque():
    with open(arquivo_estoque, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)


def listar_estoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Itens no estoque:")
        for codigo, item in estoque.items():
            print(f"Código: {codigo} - Produto: {item['nome']} | Quantidade: {item['quantidade']} | Descrição: {item['descrição']} | Unidade: {item['unidade']} | Fornecedor: {item['fornecedor']} | Categoria: {item['categoria']}")


    
def pesquisar_item_estoque():
    while True:
        codigo = input("Digite o código do item que você deseja buscar: ")
        if codigo in estoque:
            item = estoque[codigo]
            print(f"Item encontrado - Produto: {item['nome']} | Quantidade: {item['quantidade']} | Descrição: {item['descrição']} | Unidade: {item['unidade']} | Fornecedor: {item['fornecedor']} | Categoria: {item['categoria']}")
            break
        else:
            print("Item não encontrado no estoque. Tente novamente.")

def adicionar_item_no_estoque():
    while True:
        codigo = input("informe o codigo do item: ")
        if codigo in estoque:
           print("Esse código já está cadastrado! Tente outro.")
        else:
            nome = input("Informe o nome do item: ")
            quantidade = int(input("Informe a quantidade do item: "))
            descrição = input("Informe a descrição do item: ")
            unidade = input("Informe a unidade do item: ")
            fornecedor = input("Informe o fornecedor do item: ")
            categoria = input("Informe a categoria do item: ")
            estoque[codigo] = {"nome": nome, "quantidade": quantidade, "descrição": descrição, "unidade": unidade, "fornecedor": fornecedor, "categoria": categoria}
            print("Item adicionado ao estoque!")
            salvar_estoque()
            break

def editar_item_estoque():
    while True:
        codigo = input("digite o codigo do item: ")
        if codigo in estoque:
            nome = input("digite o novo nome do item: ")
            quantidade = int(input("digite a nova quantidade: "))
            descrição = input("digite a nova descrição: ")
            unidade = input("digite a nova unidade: ")
            fornecedor = input("digite o novo fornecedor: ")
            categoria = input("digite a nova categoria: ")
            estoque[codigo] = {"nome": nome, "quantidade": quantidade, "descrição": descrição, "unidade": unidade, "fornecedor": fornecedor, "categoria": categoria}
            print("Item atualizado com sucesso!")
            salvar_estoque()
            break
        else:
            print("Esse item não está no estoque. Tente novamente.")
            

def excluir_item_estoque():
    while True:
        codigo = input("digite o codigo que voce quer excluir: ")
        if codigo in estoque:
            del estoque[codigo]
            print("Item excluído do estoque!")
            salvar_estoque()
            break
        else:
            codigo = input("Item não encontrado no estoque. Digite um código que esteja dentro do estoque: ")

opcaoEstoque = 0
while(opcaoEstoque != 6):
    print("Escolha qual ação deseja realizar:  \n")
    print("1-Listar Estoque \n")
    print("2-Pesquisar item do estoque \n")
    print("3-Adicionar item do estoque \n")
    print("4-Editar item ao estoque \n")
    print("5-Excluir item do estoque \n")
    opcaoEstoque = int(input("6-Retornar ao Menu inicial   \n"))
    if opcaoEstoque == 1:
        listar_estoque()
    elif opcaoEstoque == 2:
        pesquisar_item_estoque()
    elif opcaoEstoque == 3:
        adicionar_item_no_estoque()
    elif opcaoEstoque == 4:
        editar_item_estoque()
    elif opcaoEstoque == 5:
        excluir_item_estoque()
    elif opcaoEstoque == 6:
        print("Voltando ao menu inicial...")
    else:
        print("Opção inválida. Tente novamente.")
