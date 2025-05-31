import logging
import os
import time

import requests
from dotenv import load_dotenv
from utils.dataset_util import DatasetUtil

logger = logging.getLogger("app-extract-dataset")


def download_dataset(dataset) -> bool:
    maximo_tentativas = os.getenv("MAXIMO_TENTATIVAS", 5)
    if not maximo_tentativas or not isinstance(maximo_tentativas, int):
        maximo_tentativas = 5

    time_sleep_download = os.getenv("TIME_SLEEP_DOWNLOAD", 3)
    if not time_sleep_download or not isinstance(time_sleep_download, int):
        time_sleep_download = 3

    tentativa = 1
    continua = True
    while continua:
        try:
            logger.info(
                f"Tentativa {tentativa} de executar o download do Dataset: '{dataset.get_nome()}'"
            )

            # Executa o time sleep para efetuar o download do dataset como mecanismo de prevenção de sobrecarga do servidor da Embrapa Uva e Vinho
            time.sleep(time_sleep_download)

            # Envia a requisição para a URL informada
            response = requests.get(dataset.get_csv_file_url())

            # Verifica se a requisição foi feita com sucesso (status code 200)
            if response.status_code == 200:
                # Executa a cópia (download) do dataset obtido para o arquivo local
                save_file = "./datasets/" + dataset.get_csv_filename()
                with open(save_file, "wb") as file:
                    file.write(response.content)
                continua = False
                logger.info(
                    f"Download do dataset: '{dataset.get_nome()}' executado com sucesso"
                )
                logger.info(f"Dataset armazenado em: {save_file}")
                return True
            else:
                logger.error(
                    f"Erro ao executar o download do arquivo de dados: {dataset.get_csv_file_url()}, tentativa: {tentativa}"
                )
        except Exception:
            logger.error(
                f"Erro ao executar o donwload do arquivo de dados: {dataset.get_csv_file_url()}, tentativa: {tentativa}"
            )

        if continua and tentativa >= maximo_tentativas:
            continua = False
        elif continua:
            tentativa = tentativa + 1
    return False


def main():
    logging.basicConfig(level=logging.INFO)
    # Carrega as variáveis de ambiente
    load_dotenv()

    # Preenche a lista de datasets que serão obtidos a partir do Banco de Dados de Vitivinicultura (uva, vinho e derivados) da Embrapa Uva e Vinho
    datasets = DatasetUtil.get_datasets()

    results = []
    for dataset in datasets:
        retorno = "OK" if download_dataset(dataset) else "ERRO"
        results.append(f"Download dataset: '{dataset.get_nome()}' ({retorno})")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
