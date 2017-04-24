import requests
from .models import Repos

class Githubapi:
    """githubapi

        Get information for github.

    """

    def getMostPopularReposByCountry(self, country, limit=10):
        repos = Repos.objects.filter(country=country).order_by('-stars')[:limit]
        if repos.count() == 0:
            repos_tmp = self.getReposByCountry(country)
            repos_tmp.sort(key=lambda x: x['stars'], reverse=True)
            repos = repos_tmp[:limit]

        return repos

    def getMostCollaboratorsReposByCountry(self, country, limit=10):
        repos = Repos.objects.filter(country=country).order_by('-colabs')[:limit]
        if repos.count() == 0:
            repos_tmp = self.getReposByCountry(country)
            repos_tmp.sort(key=lambda x: x['colabs'], reverse=True)
            repos = repos_tmp[:limit]
        
        return repos
        

    def getReposByCountry(self, country):
        url = 'https://api.github.com/search/users?q=location:{0}&per_page=1000'.format(country)
        url1 = 'https://api.github.com/users/{0}/repos?type:owner&per_page=1000'
        url2 = 'https://api.github.com/orgs/{0}/repos?type:all&per_page=1000'
        url3 = 'https://api.github.com/repos/{0}/{1}/contributors?per_page=1000'
        message = ""
        colabs = 0
        info = []
        item = {}

        while url:
            r = requests.get(url)
            if r.ok:
                users = r.json()['items']
                for u in users:
                    if u['type'] == 'User':
                        url_repos = url1.format(u['login'])
                    else:
                        url_repos = url2.format(u['login'])

                    while url_repos:
                        r1 = requests.get(url_repos)
                        if r1.ok:
                            if r1.text:
                                repos = r1.json()
                            else:
                                repos = []
                            for repo in repos:
                                url_colabs = url3.format(u['login'], repo['name'])
                                colabs = 0
                                while url_colabs:
                                    r2 = requests.get(url_colabs)
                                    if r2.ok:
                                        if r2.text:                                        
                                            colabs = colabs + len(r2.json())
                                        item['username'] = u['login']
                                        item['repo'] = repo['name']
                                        item['stars'] = repo['stargazers_count']
                                        item['colabs'] = colabs
                                        item['country'] = country
                                        info.append(item.copy())
                                    else:
                                        message = "Fallo obteniendo los colaboradores"

                                    if r2.links.get('next'):
                                        url_colabs = r2.links.get('next').get('url')
                                    else:
                                        url_colabs = False                        
                        else:
                           message = "Fallo obteniendo los repositorios"

                        if r1.links.get('next'):
                            url_repos = r1.links.get('next').get('url')
                        else:
                            url_repos = False
            else:
                message = "Fallo obteniendo los usuarios"

            if r.links.get('next'):
                url = r.links.get('next').get('url')
            else:
                url = False
        
        if len(info) > 0:
            for re in info:
                Repos.objects.create(username=re['username'], repo=re['repo'], stars=re['stars'], colabs=re['colabs'], country=re['country'])

        return info
