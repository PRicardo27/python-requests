import requests as req
import base64

class ManagementRepo:

    def __init__(self,owner,token):
        self.owner = owner
        self.token = token
        self.base_url = 'https://api.github.com'
        self.headers = {'Authorization' : 'Bearer '+ self.token,
           'X-GitHub-Api-Version': '2022-11-28'}
        self.headersfork = {'Accept':'application/vnd.github+json',
           'Authorization' : 'Bearer '+ self.token,
           'X-GitHub-Api-Version': '2022-11-28'}
        
    def create_repo(self,name,desc):

        url = f'{self.base_url}/user/repos'

        data = {
            'name':name,
            'description':desc,
            'private':False
        }

        resp = req.post(url,json=data,headers=self.headers)

        if resp.status_code >= 400:
            print(f'\nHouve um erro ao criar o repositório "{name}".\n')
        elif 200 <= resp.status_code < 300: 
            print(f'\nRepositório "{name}" criado com sucesso!\n')

    def delete_repo(self,name):
        
        url = f'{self.base_url}/repos/{self.owner}/{name}'

        resp = req.delete(url,headers=self.headers)


        if resp.status_code >= 400:
            print(f'\nHouve um erro ao deletar o repositório "{name}".\n')
        elif 200 <= resp.status_code < 300: 
            print(f'\nRepositório "{name}" deletado com sucesso!\n')

    def add_file(self,repository,folder,file_name):
        
        url = f'{self.base_url}/repos/{self.owner}/{repository}/contents/{file_name}'

        if folder == '':
            path = file_name
        else:
            path = f'{folder}/{file_name}'

        try:
            with open(path, 'rb') as file:
                file_data = file.read()
        except FileNotFoundError:
            print('Arquivo não encontrado.\n')
        else:

            encoded_data = base64.b64encode(file_data)

            data = { 
                'message':'Adicionando um novo arquivo',
                'content':encoded_data.decode('utf-8')
            }

            resp = req.put(url,json=data,headers=self.headers)

            if resp.status_code >= 400:
                print(f'\nHouve um erro ao tentar inserir o arquivo "{file_name}" no repositório {repository}.\n')
            elif 200 <= resp.status_code < 300: 
                print(f'\nArquivo "{file_name}" inserido no repositório {repository}\n')

    def delete_file(self,file,repository):

        url = f'{self.base_url}/repos/{self.owner}/{repository}/contents/{file}'

        sha = req.get(url,headers=self.headers).json()['sha']

        data = {
            'message':'Arquivo deletado via Python',
            'sha':sha
        }

        resp = req.delete(url,json=data,headers=self.headersfork)

        if resp.status_code >= 400:
            print(f'\nHouve um erro ao deletar o arquivo "{file}".\n')
        elif 200 <= resp.status_code < 300: 
            print(f'\nArquivo "{file}" deletado com sucesso!\n')

    def fork_repo(self,user,repo):

        url = f'{self.base_url}/repos/{user}/{repo}/forks'

        resp = req.post(url,headers=self.headersfork)

        if resp.status_code >= 400:
            print(f'\nHouve um erro ao realizar fork no repositório "{repo}".\n')
        elif 200 <= resp.status_code < 300: 
            print(f'\nFork executado com sucesso no repositório "{repo}"\n')

