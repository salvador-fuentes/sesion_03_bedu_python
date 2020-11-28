## Hagamos un bot para descargar fotos de los usuarios de github.

import requests

# Constants
BASE_URL = 'https://api.github.com/'

#Functions#
##Getting user info:
def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Para descargar la foto del usuario de github
def download_github_user_avatar(avatar_url, username):
    response = requests.get(avatar_url)
    if response.status_code == 200:
        #download a file from internet
        response_content = response.content
        filename = f'tmp/{username}.png' 
        with open (filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None

username = input('Give me a Github username: \t')
user = get_github_user(username)
filename = download_github_user_avatar(user['avatar_url'], username)
print(filename)

#Nota: se creó una carpeta tmp donde se descargarán las imágenes. 

