class Adm:
    def __init__(self, user, senha, id_adm):
        self.user = user
        self.senha = senha
        self.id_adm = id_adm

    def getUser(self):
        return self.user

    def getSenha(self):
        return self.senha

    def getIDadm(self):
        return self.id_adm

    def cadastrar_adm(self, user, senha):
        adm = Adm(user, senha)
        loja.inserir_adm(adm)


class Cliente:
    def __init__(self, nome, cpf, idade, endereco, senha, idc):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.senhacli = senha
        self.id = idc
        self.carrinho = []
        self.compras = []

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCpf(self):
        return self.cpf

    def getEndereco(self):
        return self.endereco

    def get_Senha(self):
        return self.senhacli

    def getId(self):
        return self.id

    def adicionar_ao_carrinho(self, id_produto, qtd):
        if id_produto in loja.produtos:
            produto = loja.produtos[id_produto]
            for _ in range(qtd):
                self.carrinho.append(produto)
            print(f"{qtd} unidades de {produto.get_nome_produto()} foram adicionadas ao carrinho.")
        else:
            print("Produto não encontrado.")

    def adicionar_ao_carrinho(self, id_produto, qtd):
        if id_produto in loja.produtos:
            produto = loja.produtos[id_produto]
            if produto.getQTd() >= qtd:  # Verifica se a quantidade em estoque é suficiente
                for _ in range(qtd):
                    self.carrinho.append(produto)
                produto.setQtd(produto.getQTd() - qtd)  # Diminui a quantidade em estoque
                print(f"{qtd} unidades de {produto.get_nome_produto()} foram adicionadas ao carrinho.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

    def delProduto(self, vetor):
        self.vetor_lista = vetor - 1
        if 0 <= self.vetor_lista < len(self.carrinho):
            removed_item = self.carrinho.pop(self.vetor_lista)
            print(f"{removed_item.get_nome_produto()} foi removido do carrinho.")
        else:
            print("ID do produto no carrinho inválido.")

    def finalizar_compra(self):
        if len(self.carrinho) == 0:
            print("Seu carrinho está vazio. Não é possível finalizar a compra.")
        else:
            compra = list(self.carrinho)
            self.compras.append(compra)  
            self.carrinho.clear()         
            print("Compra finalizada com sucesso!")

            menu_cli = 0

    def listar_compras(self):
        print("Suas compras:")
        for i, compra in enumerate(self.compras, 1):
            print(f"Compra {i}:")
            for produto in compra:
                print(f"Nome: {produto.get_nome_produto()} | Valor: R${produto.get_valor()}")


class Produto:
    def __init__(self, nome_produto, descricao, valor, idp, qtd):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor
        self.idp = idp
        self.qtd = qtd

    def get_nome_produto(self):
        return self.nome_produto

    def get_descricao(self):
        return self.descricao

    def get_valor(self):
        return self.valor

    def get_idp(self):
        return self.idp

    def getQTd(self):
        return self.qtd

    def setQtd(self, new_qtd):
        self.qtd = new_qtd


class Loja:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.adm = {}
        self.produtos = {}
        self.clientes = {}

    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco

    def get_cnpj(self):
        return self.cnpj

    def inserir_cliente(self, valor, vetor):
        self.clientes[vetor] = valor

    def inserir_produto(self, valor, vetor):
        self.produtos[vetor] = valor

    def inserir_adm(self, valor):
        vetor = len(self.adm) + 1
        self.adm[vetor] = valor

    def listarClientes(self):
        for chave, cliente in self.clientes.items():
            print(f"ID:{chave} - Nome: {cliente.getNome()} - CPF: {cliente.getCpf()} - Idade: {cliente.getIdade()} - Endereço: {cliente.getEndereco()}")

    def listarProdutos(self):
        for chave, produto in self.produtos.items():
            print(f"ID:{chave} - Nome: {produto.get_nome_produto()} - Descrição: {produto.get_descricao()} - Valor: R${produto.get_valor()} - Quantidade: {produto.getQTd()}")

    def excluir_produto(self, vetor):
        self.vetor = vetor - 1
        return self.produtos.pop(vetor)

    def excluir_cliente(self, vetorc):
        self.vetorc = vetorc - 1
        return self.clientes.pop(vetorc)
    
    def total_vendas(self):
        total = 0
        for cliente in self.clientes.values():
            for compra in cliente.compras:
                for produto in compra:
                    total += produto.get_valor()
        return total


loja = Loja("VS STORE", "Av. das Codificações, Nº1011", 123456789)
master = Adm("adm", "admin123", 0)
loja.inserir_adm(master)