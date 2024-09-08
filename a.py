import requests

# URL da requisição
url = "http://kobaltkobalxtkobaltkobaltxkobaltkobaltko.duckdns.org/bostil/worker.php"

# Parâmetros da URL
params = {
    'work': 'whattodo',
    'version': 'shuparu-miawara'
}

# Cabeçalhos da requisição
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Host': 'kobaltkobalxtkobaltkobaltxkobaltkobaltko.duckdns.org',
    'User-Agent': 'python-requests/2.28.2'
}

# Fazendo a requisição GET
response = requests.get(url, headers=headers, params=params)

# Imprimindo a resposta
print(response.text)
