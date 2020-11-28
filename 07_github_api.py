import requests

# Constants
BASE_URL = 'https://api.github.com/'

#Function
##Getting user info
def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

username = input('Give me a Github username: \t')
user = get_github_user(username)
print(user)


