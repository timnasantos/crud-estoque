from random import randint 

end = 0
codigo = []
nome = []
descricao = []
marca = [] 
valor_de_custo = []
valor_de_venda = [] 

while end != 1: 
    sistema = int(input("O que gostaria de fazer? \n [0] Cadastrar um produto \n [1] Listar todos os produtos \n [2] Atualizar o valor de um produto \n [3] Deletar um produto \n [4] Finalizar "))
    print("\n") 
    if sistema == 0: 
        codigo.append(randint(000000, 999999)) 
        nome.append(input("Digite o nome do produto: "))
        descricao.append(input("Digite a descrição do produto: "))
        marca.append(input("Digite a marca do produto: "))
        valor_de_custo.append(float(input("Digite o valor de custo do produto: ")))
        valor_de_venda.append(float(input("Digite o valor de venda do produto: ")))
        print("Produto adicionado com sucesso!")

    if sistema == 1: 
        print("Os produtos já cadastrados no sistema são: ")
        print(nome, codigo)

    if sistema == 2: 
        int(input("Digite o código do produto que você quer atualizar: "))
        novo_valor = float(input("Digite o novo valor de venda deste produto: "))
        valor_de_venda = novo_valor 
        print("Valor de venda do produto alterado com sucesso!")

    if sistema == 3: 
        int(input("Digite o código do produto que você deseja deletar: "))
        print("Pronto! O produto ", nome,  " foi deletado com sucesso!")

    if sistema == 4: 
        end = 1
        print("Finalizado com sucesso!")
