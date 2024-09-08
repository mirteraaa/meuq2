import requests
import time

# URL e parâmetros para a primeira requisição
url_first = "http://kobaltkobalxtkobaltkobaltxkobaltkobaltko.duckdns.org/bostil/apit.php"
params_first = {
    'username': 'ssnns',
    'resolucao_tela': '1680x1050',
    'memoria_ram_total': '15',
    'num_nucleos_cpu': '10'
}
headers_first = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Host': 'kobaltkobalxtkobaltkobaltxkobaltkobaltko.duckdns.org',
    'User-Agent': 'python-requests/2.28.2'
}

# Fazendo a primeira requisição HTTP GET
response_first = requests.get(url_first, headers=headers_first, params=params_first)
print("Primeira requisição - Resposta:")
print(response_first.text)

# URL e parâmetros para a segunda requisição
url_second = "http://kobaltkobalxtkobaltkobaltxkobaltkobaltko.duckdns.org/bostil/worker.php"
params_second = {
    'work': 'whattodo',
    'version': 'shuparu-miawara'
}
headers_second = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Host': 'kobaltkobalxtkobaltkobaltxkobaltkobaltko.duckdns.org',
    'User-Agent': 'python-requests/2.28.2'
}

# Loop para a segunda requisição HTTP GET
while True:
    response_second = requests.get(url_second, headers=headers_second, params=params_second)
    print("Segunda requisição - Resposta:")
    print(response_second.text)
    
    # Intervalo de tempo antes de repetir (opcional)
    time.sleep(5)  # Espera 5 segundos antes de repetir (ajuste conforme necessário)
