import requests

# Constants
base_url = 'https://api.github.com/'

response = requests.get(base_url)
print(response)


#username = input('Give me a github username: ')
