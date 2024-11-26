import sqlite3


# Conexão com o banco de dados SQLite
conn = sqlite3.connect('CalcularIMC')
cursor = conn.cursor()

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    """Cria as tabelas no banco de dados se não existirem."""
    cursor.execute('''CREATE TABLE IF NOT EXISTS utilizadores (
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    altura REAL NOT NULL,
                    peso REAL NOT NULL)''')

# Função para registar os dados de um utilizador novo
def registo():
    """Regista um novo utilizador no sistema."""
    nome = input("Insira o nome de um utilizador: ")

    # Verifica se o nome de utilizador já existe
    cursor.execute('SELECT * FROM utilizadores WHERE nome = ?', (nome,))
    if cursor.fetchone():
        print("Nome de utilizador já existe. Tente outro.")
        return None

    idade = int(input("Qual é a idade do utilizador? "))  # Convertendo para inteiro

    # Corrigindo o formato da altura e peso
    altura_input = input("Qual é a altura do utilizador? (ex: 1.80 ou 1,80) ")
    altura = float(altura_input.replace(',', '.'))  # Substitui vírgula por ponto

    peso_input = input("Qual é o peso do utilizador? (ex: 70 ou 70,5) ")
    peso = float(peso_input.replace(',', '.'))  # Substitui vírgula por ponto

    # Insere os dados do utilizador na base de dados
    cursor.execute('''INSERT INTO utilizadores (nome, idade, altura, peso) VALUES (?, ?, ?, ?)''',
                   (nome, idade, altura, peso))
    conn.commit()

    print(f'O Utilizador {nome} Foi registado com sucesso')

# Função para calcular o IMC
def calcular_imc(altura, peso):
    """Calcula o IMC de um utilizador."""
    return peso / (altura ** 2)

# Função para determinar a categoria do IMC
def categoria_imc(imc):
    """Retorna a categoria do IMC de acordo com os padrões da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 49.9:
        return "Obesidade"
    elif 50 <= imc:
        return "IMC Impossível, Por favor introduza os dados corretamente."

# Função para pesquisar um utilizador
def pesquisar_utilizador():
    """Permite pesquisar um utilizador pelo nome e exibir seus dados, incluindo o IMC e a categoria."""
    nome_utilizador = input("Digite o nome do utilizador que deseja pesquisar: ")

    # Pesquisar o utilizador no banco de dados
    cursor.execute('SELECT * FROM utilizadores WHERE nome = ?', (nome_utilizador,))
    utilizador = cursor.fetchone()

    if utilizador:
        # Dados do utilizador
        nome = utilizador[0]
        idade = utilizador[1]
        altura = utilizador[2]
        peso = utilizador[3]

        # Calculando o IMC
        imc = calcular_imc(altura, peso)

        # Determinando a categoria do IMC
        categoria = categoria_imc(imc)

        # Exibindo as informações do utilizador, IMC e categoria
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Altura: {altura} metros')
        print(f'Peso: {peso} kg')
        print(f'IMC: {imc:.2f}')  # Exibe o IMC com 2 casas decimais
        print(f'Categoria do IMC: {categoria}')

    else:
        print("Utilizador não encontrado.")

# Função para ver todos os utilizadores registrados
def ver_todos_utilizadores():
    """Exibe todos os utilizadores registrados no banco de dados."""
    cursor.execute('SELECT nome, idade, altura, peso FROM utilizadores')
    utilizadores = cursor.fetchall()

    if utilizadores:
        print("\nUtilizadores Registrados:")
        for utilizador in utilizadores:
            nome, idade, altura, peso = utilizador
            print(f"{nome}")
    else:
        print("Nenhum utilizador registrado.")

# Função para exibir o menu e processar as opções
def exibir_menu():
    """Exibe o menu e executa a opção escolhida pelo utilizador."""
    while True:
        print("\nMenu:")
        print("1. Inserir os dados de um novo utilizador")
        print("2. Pesquisar utilizador")
        print("3. Ver todos os utilizadores")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            registo()  # Chama a função para registrar um novo utilizador
        elif opcao == '2':
            pesquisar_utilizador()  # Chama a função para pesquisar um utilizador
        elif opcao == '3':
            ver_todos_utilizadores()  # Exibe todos os utilizadores registrados
        elif opcao == '4':
            print("Saindo do sistema...")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função para criar as tabelas
criar_tabelas()

# Exibe o menu e processa a escolha do utilizador
exibir_menu()

# Fecha a conexão com o banco de dados
conn.close()
