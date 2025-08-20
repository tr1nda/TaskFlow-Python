import shortuuid #Gera IDs unicos e exclusivos para cada usuario/tarefa
import json #Persistência de dados em arquivo JSON
import os #Verifica a existência do arquivo "tasks.json"


FILE_NAME = "tasks.json"

class Usuario():
    #Cria a classe Usuário
    def __init__(self, nome, email):
        self.id = str(shortuuid.uuid()[:5])
        self.nome = nome
        self.email = email
        self.tarefas = []

    def infosUser(self):
       #Percorre todas as tarefas atribuidas aquele usuário, e retorna uma string com as informações do usuário e os IDs das suas tarefas
        tarefas_ids = [tarefa.titulo for tarefa in self.tarefas]
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Tarefas IDs: {tarefas_ids}"
    
    def adicionarTarefa(self, titulo, descricao):
        #cria um objeto Tarefa e adiciona a lista de tarefas do usuario
        tarefa = Tarefa(titulo, descricao)  # Criando a tarefa antes
        self.tarefas.append(tarefa)  # Adicionando à lista de tarefas
        print(f"Tarefa '{tarefa.titulo}' adicionada para {self.nome}!\nID: {tarefa.id}")

    def listarTarefas(self):
        #Busca e retorna informações sobre as tarefas atribuidas ao usuario
        if not self.tarefas:
            return "Nenhuma tarefa cadastrada!"
        return "\n".join([f"ID: {tarefa.id}- Titulo: {tarefa.titulo} - Descrição: {tarefa.descricao} - Status: {tarefa.status}" for tarefa in self.tarefas])
    
    def buscarTarefa(self, taskId):
        #Faz uma pesquisa por ID da alguma tarefa
        for task in self.tarefas:
            if task.id == taskId:
                return task
        return None
    
    def to_list(self):
        #Transforma os atributos do objeto Usuario em uma Lista(para ser utilizado pelo Json)
        return [self.id, self.nome, self.email, [tarefa.to_list() for tarefa in self.tarefas]]
    
    @classmethod
    def from_list(cls, data):
        #recria um Objeto Usuário a partir de uma lista, sem a necessidade de recriação manual
        usuario = cls(data[1], data[2])  # Cria o objeto com nome e email
        usuario.id = data[0]  # Atribui o ID do usuário
        usuario.tarefas = [Tarefa.from_list(tarefa) for tarefa in data[3]]  # Recria as tarefas associadas
        return usuario


    
class Tarefa():
    #Cria o objeto do tipo Tarefa
    def __init__(self, titulo, descricao):
        self.id = str(shortuuid.uuid()[:7])
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Pendente"

    def to_list(self):
        #transforma o objeto tarefa em uma lista para ser salvo em .json
        return [self.id, self.titulo, self.descricao, self.status]
    
    @classmethod
    def from_list(cls, data):
        #Recria o objeto tarefa a partir de uma lista
        tarefa = cls(data[1], data[2])  # Cria o objeto com título e descrição
        tarefa.id = data[0]  # Atribui o ID da tarefa
        tarefa.status = data[3]  # Atribui o status
        return tarefa



def buscarUsuario(user_id):
    #Faz uma procura por ID de um objeto do tipo Usuario na "usersList"
    for usuario in usersList:
        if usuario.id == user_id:
            return usuario
    return None

def addUsuario(nome, email):
    #Cria e adiciona na lista um objeto do tipo usuario
    newUser = Usuario(nome, email)
    print(f"Usuário {newUser.nome} adicionado\nId: {newUser.id}")
    usersList.append(newUser)

def salvar_dados(lista_usuarios):
    #Salva a lista de ususários em um arquivo Json
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump([usuario.to_list() for usuario in lista_usuarios], file, indent=4)

def carregar_dados():
    """Carrega os dados do arquivo JSON e recria os objetos Usuario e Tarefa."""
    if os.path.exists(FILE_NAME) and os.stat(FILE_NAME).st_size > 0:  # Verifica se o arquivo existe e não está vazio
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)  # Lê os dados do JSON
            return [Usuario.from_list(user) for user in data]  # Converte as listas para objetos Usuario e Tarefa
    return []  # Se o arquivo não existir ou estiver vazio, retorna uma lista vazia

usersList = carregar_dados()

menu = 1
while (menu == 1):
    option = int(input("[1] - Cadastrar Usuário\n[2] - Cadastrar Tarefa\n[3] - listar Usuarios\n[4] - Listar Tarefas\n[5] - Buscar Usuário\n[6] - Alterar Tarefa\n[7] - Sair\n:"))
    if option == 1:
        nome = str(input("Nome do novo usuário:\n"))
        email = str(input("E-mail do novo usuário:\n"))
        addUsuario(nome, email)

    elif option == 2:
        if not usersList:
            print("Nenhum Usuário Cadastrado!")
        else:
            userSearch = str(input("ID do usuário:\n"))
            user = buscarUsuario(userSearch)
            if user:
                title = str(input("Título da nova tarefa: "))
                description = str(input("Descrição da tarefa: "))
                user.adicionarTarefa(title, description)
            else:
                print("Usuário não encontrado")
        
    elif option == 3:
        if not usersList:
            print("Nenhum Usuário Cadastrado!")
        else:
            for usuario in usersList:
                print(f"ID:{usuario.id} - Usuario:{usuario.nome}")

    elif option == 4:
        if not usersList:
            print("Nenhum Usuário Cadastrado!")
        else:
            userSearch = str(input("ID do usuário:\n"))
            user = buscarUsuario(userSearch)
            if user:
                print(user.listarTarefas())
            else:
                print("Usuário não encontrado")
        
    elif option == 5:
        if not usersList:
            print("Nenhum Usuário Cadastrado!")
        else:
            userSearch = str(input("ID do usuário:\n"))
            user = buscarUsuario(userSearch)
            if user:
                print(user.infosUser())
            else: 
                print("Usuário não encontrado")

    elif option == 6:
        if not usersList:
            print("Nenhum Usuário Cadastrado!")
        else:
            userSearch = str(input("ID do usuário:\n"))
            user = buscarUsuario(userSearch)
            if user:
                taskSearch = str(input("ID da Tarefa:\n"))
                task = user.buscarTarefa(taskSearch)
                if task:
                    newStatus = str(input('Qual o novo status da tarefa:'))
                    task.status = newStatus
                    print(f"Status de {task.id} - {task.titulo} alterado para {task.status} ")
                else:
                    print('Tarefa não encontrada')
            else: 
                print('Usuário não encontrado')
             
    else:
        salvar_dados(usersList)
        menu = 0