from dados_repo import RepositoryData
from manage_repo import ManagementRepo
import os


os.system('clear')

print('=== Manipulando dados dos repostiórios Github ===\n')

owner = input('\nDigite o login do Github:\n')
token = input('Informe o token de autenticação:\n')

option = ''

#Validação para manter o programa em loop
while option.upper() != '0':

    #Título com opções de acesso
    print(f'Escolha uma das opções:\n\t(1) Extrair linguagens de repositórios de um usuário\n',
          '\t(2) Manipular repositórios Github (necessário conta e token do Github)\n\t(0) Sair\n')
    option = input('Opção: ')

    if option == '1':
        os.system('clear')

        while option == '1':   

            print(f'== Extrair linguagens de repositórios ==\n')
            print('Digite o nome de usuário ao qual pertence os repositórios.\nDigite "-0" para encerrar o programa, ou "-1" para voltar ao menu anterior\n')
            user = input('Opção: ')

            if user.upper() == '-0':
                option = '0'
                break

            if user.upper() == '-1':
                user = '-0' 
                break

            dataframe = RepositoryData(user,token).create_df_languages()

    elif option == '2':
        
        manager = ManagementRepo(owner,token)
        os.system('clear')
          
        print(f'== Manipulando repositórios Github ==\n')

        while option == '2':

            Manage_options = ['1','2','3','4','5','6','7']

            print(f'Escolha uma opção:\n\t(1) Criar repositório\n\t(2) Deletar um repositório\n\t(3) Adicionar arquivo\n',
                                '\t(4) Deletar um arquivo\n\t(5) Fork Repositório\n\n\t(6) Voltar ao menu anterior\n\t(7) Sair do programa')
            Manage_option = input('Opção: ')
            
            if Manage_option == '1':
                os.system('clear')
                print(f'== Manipulando repositórios Github ==\n= Criando repositório =\n')

                repo_name = input(f'Digite o nome do novo repositório:\n')
                repo_desc = input(f'\nDigite a descrição do "{repo_name}":\n')

                manager.create_repo(repo_name,repo_desc)

            elif Manage_option == '2':
                os.system('clear')
                print(f'== Manipulando repositórios Github ==\n= Deletando repositório =\n')

                repo_name = input(f'Digite o nome do repositório para exclusão:\n')

                manager.delete_repo(repo_name)

            elif Manage_option == '3':
                os.system('clear')
                print(f'== Manipulando repositórios Github ==\n= Inserindo arquivo =\n')

                repo_name = input('Digite o nome do repositório para inserir o arquivo:\n')

                repo_folder = input('Pasta dentro do repositório (opcional):\n')
                file = input('Arquivo (caminho completo do arquivo):\n')

                manager.add_file(repo_name,repo_folder,file)

            elif Manage_option == '4':
                os.system('clear')
                print(f'== Manipulando repositórios Github ==\n= Deletando arquivo =\n')

                repo_name = input('Digite o nome do repositório onde está o arquivo:\n')

                file = input('\nDigite o nome do arquivo: ')

                manager.delete_file(file,repo_name)

            elif Manage_option == '5':
                os.system('clear')
                print(f'== Manipulando repositórios Github ==\n= Fork Repositório =\n')

                user = input('Digite o nome do usuário dono do repositório:\n')

                repo_name = input('\nDigite o nome do repositório:\n')

                manager.fork_repo(user,repo_name)

            elif Manage_option == '6':
                option = ''
                os.system('clear')
            elif Manage_option == '7':
                option = '0'
        
            
          

print('\nPrograma encerrado!')

