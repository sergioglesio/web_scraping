#Este código analisa página HTML, e extrai os buttons e o path dos uls.
#pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titulos = soup.find_all('ul', class_='menu-col')

        for titulo in titulos:
            print(titulo.text)
            
            link = titulo.find('a')['href'] if titulo.find('a') else None
            if link:
                print("Link:", link)
            else:
                print("Link não encontrado.")
                
            print()  # Adicionando uma linha em branco entre as notícias
    else:
        print(f"Falha na requisição. Código de status: {response.status_code}")

if __name__ == "__main__":
    #estou usando o site da universidade que fiz minha graduação
    url_do_site = "https://www4.unievangelica.edu.br"

    extract_data(url_do_site)
