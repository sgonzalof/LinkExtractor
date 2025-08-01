# WIKIPEDIA

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def scrape_url(url: str):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    print('La petición fue exitosa')

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer todos los enlaces <a>
    enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]
    print(enlaces)

  else:
    print(f'Error al hacer la petición: {response.status_code}')


url  = input("Introduce la URL a scrapear: ")
scrape_url(url)