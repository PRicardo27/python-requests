import requests as req
import pandas as pd

class RepositoryData:

    def __init__(self,owner,token):
        self.owner = owner
        self.base_url = 'https://api.github.com'
        self.token = token
        self.headers = {'Authorization' : 'Bearer '+ self.token,
           'X-GitHub-Api-Version': '2022-11-28'}
        
    def __repository_list(self):
        repos_list = []
        url = f'{self.base_url}/users/{self.owner}'
        pg = 1

        response = req.get(url)

        if response.status_code > 400:
            raise ValueError(f'O usuário {self.owner} não foi encontrado\n')
        
        response = response.json()

        if response['public_repos'] == 0:
            raise ValueError(f'O usuário {self.owner} não possui repositórios\n')

        print(f'Paginando repositórios de {self.owner}')

        while True:

            repo = req.get(f'{url}/repos?per_page=100&page={pg}',headers=self.headers)

            if len(repo.json())== 0:
                break
            
            print('',end='.')
            repos_list.append(repo.json())
            pg += 1

        print('\n')
        return repos_list

    def __repos_name(self,repos_list):

        repo_names = []

        for pg in repos_list:
            repo_names += (repo['name'] for repo in pg)

        return repo_names
    
    def __repos_language(self,repos_list):

        repo_languages = []

        for pg in repos_list:
            repo_languages += (repo['language'] for repo in pg)

        return repo_languages
    
    def __save_df(self,dataframe):
        
        dataframe.to_csv(f'data/linguagens_{self.owner}.csv')
    
    def create_df_languages(self):

        try:
            repo = self.__repository_list()
            
        except Exception as e: 
            print(f'\tERROR: {e}')
            return 
        else:
            names = self.__repos_name(repo)
            languages = self.__repos_language(repo)

            dataframe = pd.DataFrame()

            dataframe['Nomes'] = names
            dataframe['Linguagens'] = languages

            self.__save_df(dataframe)

            print(f'Criado arquivo "linguagens_{self.owner}.csv" com as linguagens dos repositórios do {self.owner} na pasta "data".\n\n')
            return dataframe
