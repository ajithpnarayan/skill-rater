'''username = "thezillion"
import requests
URL = "http://api.github.com/users/"+username+"/repos"
r = requests.get(url= URL )
data1 = r.json()

#payload = {'token': ' b152d3f067d2e13b6ba14402f557c47b68b3c603'}
#res = requests.post("http://api.github.com/repos/thezillion/Algorithms/collaborators",data=payload)
#print(res.text)

print("Forked Repos:\n")
for x in data1:
    if(x['fork']==True):
        print("Repo: ",x['name'])
        print("\tStars:",x['stargazers_count'],"  Forks:",x['forks'])
        URL1 = "http://api.github.com/repos/"+username+"/"+x['name']+"/commits"
        res = requests.get(url=URL1)
        data2 = res.json()
        for y in data2:
            if(y['committer'] and y['committer']['login']==username):
                print("SUCK CESS")


print("\nOwn Repos:\n")
for x in data1:
    if(x['fork']==False):
        print("Repo: ",x['name'])
        print("\tStars:",x['stargazers_count'],"  Forks:",x['forks'])'''





import requests


class SkillRater:
    def __init__(self):
        self.api_token = "b152d3f067d2e13b6ba14402f557c47b68b3c603"
        self.headers = {'Authorization': 'token %s' %self.api_token}
        self.baseurl = "http://api.github.com"
        

    def _query(self, url, params = None):
        r = requests.get(url, headers = self.headers, params = params)
        return r.json()

    def filter(self, data, key, value):
        filtered_list = []
        for record in data:
            if record[key] == value:
                filtered_list.append(record['repository_url'])

        return filtered_list        

    def get_info(self, username):
        url = self.baseurl+ "/users/" + username
        data = self._query(url)
        return [data['name'], data['location'], data['followers'], data['following']]

    def get_repos(self, username):
        url = self.baseurl + "/users/" + username + "/repos"
        return self._query(url)

    def get_pull_requests(self, username):
        params = {'q': username}
        url = self.baseurl + "/search/issues"
        data = self._query(url, params)
        data = data['items']
        closed = self.filter(data, 'state', 'closed')
        return closed

    def list_languages(self, username, repo ):
        url = self.baseurl + "/repos/" + username + "/" + repo + "/languages"
        lang = self._query(url)
        
        total = 0

        for k,v in lang.items():
            total += v

        for k,v in lang.items():
            lang[k] = v * 100.0 / total

        return lang
    
