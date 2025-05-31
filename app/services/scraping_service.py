import logging

import requests
from bs4 import BeautifulSoup
from utils.general_util import transform_scrap_value
from infrastructure.config import Config

logger = logging.getLogger("app-api")


def scraping_producao(site_url, ano) -> None:
    keys = ["ano", "produto", "quantidade"]
    return scraping(site_url, None, ano, keys)


def scraping_processamento(site_url, tipo, ano) -> None:
    keys = ["tipo", "ano", "cultivar", "quantidade"]
    return scraping(site_url, tipo, ano, keys)


def scraping_comercializacao(site_url, ano) -> None:
    keys = ["ano", "produto", "quantidade"]
    return scraping(site_url, None, ano, keys)


def scraping_importacao(site_url, tipo, ano) -> None:
    keys = ["tipo", "ano", "pais", "quantidade", "valor"]
    return scraping(site_url, tipo, ano, keys)


def scraping_exportacao(site_url, tipo, ano) -> None:
    keys = ["tipo", "ano", "pais", "quantidade", "valor"]
    return scraping(site_url, tipo, ano, keys)


def scraping(url, tipo, ano, keys) -> None:
    try:
        url = url + "&ano=" + str(ano)
        response = requests.post(url, timeout=Config.SCRAPING_TIMEOUT_IN_SECONDS)

        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()

        # Parseia o HTML da página usando BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontra a tabela específica pela classe
        table = soup.find("table", {"class": "tb_base tb_dados"})

        # Extrai as linhas da tabela
        rows = table.find_all("tr")

        # Lista para armazenar os dados
        list_values = []

        # Itera sobre as linhas e extrai o texto das células
        header = True
        for row in rows:
            if not header:
                cells = row.find_all(
                    ["th", "td"]
                )  # Inclui cabeçalhos (th) e dados (td)
                cells_text = [cell.get_text(strip=True) for cell in cells]
                values = []
                data = {}
                if tipo:
                    values.append(tipo)
                if ano:
                    values.append(ano)

                tamanho = len(cells_text)
                for i in range(tamanho):
                    values.append(transform_scrap_value(cells_text[i]))
                for i in range(len(keys)):
                    data[keys[i]] = values[i]
                list_values.append(data)
            header = False

        return list_values
    except Exception as e:
        logger.error(e)
        return None
