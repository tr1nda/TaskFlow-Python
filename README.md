# TaskFlow-Python
🔹 O Problema

A empresa TaskFlow, que gerencia projetos de diversas equipes, enfrenta um grande desafio: a falta de organização das tarefas e dos usuários. Atualmente, as tarefas são registradas manualmente, e não há um sistema eficiente para acompanhar o status de cada uma delas.

Diante dessa necessidade, a TaskFlow decidiu criar um Sistema de Gerenciamento de Tarefas. Essa solução permitirá que usuários sejam cadastrados, tarefas sejam atribuídas e que o controle das atividades seja otimizado.

Para isso, a empresa busca um desenvolvedor Python capaz de construir esse sistema utilizando conceitos fundamentais da linguagem, garantindo um código eficiente, modular e escalável.

🔹 O Desafio

Você foi contratado como Desenvolvedor, e seu objetivo é criar um sistema onde:
 1. Usuários podem ser cadastrados, e cada um pode possuir múltiplas tarefas.
 2. As tarefas podem ter diferentes status, sendo:
 • "Pendente"
 • "Em Andamento"
 • "Concluído"

🔹 Personagens do Projeto

🏢 A Empresa - TaskFlow

A TaskFlow é uma empresa inovadora que busca otimizar a gestão de projetos. Seu objetivo é transformar a maneira como as equipes gerenciam suas tarefas e colaboram no dia a dia.

👩‍💻 Você - O Desenvolvedor

Você foi contratado para desenvolver um Sistema de Gerenciamento de Tarefas que atenda às necessidades da empresa.

📌 Os Usuários do Sistema

Para garantir o sucesso do projeto, o sistema deve seguir as seguintes regras:

✅ Cadastro de Usuários
 • Cada usuário deve ter um ID único, um nome e um e-mail.
 • Deve ser possível listar todos os usuários cadastrados.

✅ Cadastro e Gerenciamento de Tarefas
 • Cada tarefa deve ter um ID único, um título, uma descrição, um status e um usuário associado.
 • Deve ser possível listar todas as tarefas cadastradas.
 • Somente usuários existentes podem ser vinculados a uma tarefa.
 • Se tentar criar uma tarefa para um usuário inexistente, o sistema deve retornar um erro.

✅ Exportação de Dados
 • As tarefas devem ser exportadas para um arquivo JSON (tasks.json) e devem conter as informações das tarefas, do usuário responsável e do status.

🔹 Restrições do Cliente

O cliente não deseja que sejam utilizados dicionários (dict) para armazenar e acessar as informações de cada usuário (ID, nome e e-mail) e de cada tarefa (ID, título, descrição, status e usuário associado).

Você deve entregar um código em Python 3.9+ que atenda às necessidades do cliente. 
