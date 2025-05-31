import csv
import logging

from models.base.database import Base
from models.entities.comercializacao import Comercializacao
from models.entities.exportacao import Exportacao
from models.entities.importacao import Importacao
from models.entities.processamento import Processamento
from models.entities.producao import Producao
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists
from utils.dataset_util import DatasetUtil
from utils.general_util import transform_value

logger = logging.getLogger("app-load-dataset")


def load_dataset_producao(engine) -> None:
    logger.info("Carregando dados de Produção")
    datasets = DatasetUtil.get_producao_datasets()
    with Session(engine) as session:
        for dataset in datasets:
            logger.info(f"Dataset: {dataset.get_nome()}")
            save_file = "./datasets/" + dataset.get_csv_filename()
            with open(save_file, newline="") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=dataset.get_csv_delimiter())
                headers = next(csv_reader, None)
                ano_posicao_inicial = 3
                ano_posicao_final = len(headers) - 1
                for row in csv_reader:
                    dataset_id = int(row[0].strip())
                    dataset_nome = dataset.get_nome().strip()
                    control = row[1].strip()
                    produto = row[2].strip()
                    anos = range(ano_posicao_inicial, ano_posicao_final + 1)
                    for index in anos:
                        ano = int(headers[index].strip())
                        value = row[index].strip()
                        quantidade = transform_value(value)
                        producao = Producao(
                            dataset_id=dataset_id,
                            dataset_nome=dataset_nome,
                            control=control,
                            produto=produto,
                            ano=ano,
                            quantidade=quantidade,
                        )
                        session.add(producao)
                        session.commit()
    logger.info("Finalizado a carga de dados de Produção")


def load_dataset_processamento(engine) -> None:
    logger.info("Carregando dados de Processamento")
    datasets = DatasetUtil.get_processamento_datasets()
    with Session(engine) as session:
        for dataset in datasets:
            if not dataset.get_csv_filename():
                continue

            logger.info(f"Dataset: {dataset.get_nome()}")
            save_file = "./datasets/" + dataset.get_csv_filename()
            with open(save_file, newline="") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=dataset.get_csv_delimiter())
                headers = next(csv_reader, None)
                ano_posicao_inicial = 3
                ano_posicao_final = len(headers) - 1
                for row in csv_reader:
                    dataset_id = int(row[0].strip())
                    dataset_nome = dataset.get_nome().strip()
                    tipo = dataset.get_sub_categoria().strip()
                    control = row[1].strip()
                    cultivar = row[2].strip()
                    anos = range(ano_posicao_inicial, ano_posicao_final + 1)
                    for index in anos:
                        ano = int(headers[index].strip())
                        value = row[index].strip()
                        quantidade = transform_value(value)
                        processamento = Processamento(
                            dataset_id=dataset_id,
                            dataset_nome=dataset_nome,
                            tipo=tipo,
                            control=control,
                            cultivar=cultivar,
                            ano=ano,
                            quantidade=quantidade,
                        )
                        session.add(processamento)
                        session.commit()
    logger.info("Finalizado a carga de dados de Processamento")


def load_dataset_comercializacao(engine) -> None:
    logger.info("Carregando dados de Comercialização")
    datasets = DatasetUtil.get_comercializacao_datasets()
    with Session(engine) as session:
        for dataset in datasets:
            logger.info(f"Dataset: {dataset.get_nome()}")
            save_file = "./datasets/" + dataset.get_csv_filename()
            with open(save_file, newline="") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=dataset.get_csv_delimiter())
                headers = next(csv_reader, None)
                ano_posicao_inicial = 3
                ano_posicao_final = len(headers) - 1
                for row in csv_reader:
                    dataset_id = int(row[0].strip())
                    dataset_nome = dataset.get_nome().strip()
                    control = row[1].strip()
                    produto = row[2].strip()
                    anos = range(ano_posicao_inicial, ano_posicao_final + 1)
                    for index in anos:
                        ano = int(headers[index].strip())
                        value = row[index].strip()
                        quantidade = transform_value(value)
                        comercializacao = Comercializacao(
                            dataset_id=dataset_id,
                            dataset_nome=dataset_nome,
                            control=control,
                            produto=produto,
                            ano=ano,
                            quantidade=quantidade,
                        )
                        session.add(comercializacao)
                        session.commit()
    logger.info("Finalizado a carga de dados de Comercialização")


def load_dataset_importacao(engine) -> None:
    logger.info("Carregando dados de Importação")
    datasets = DatasetUtil.get_importacao_datasets()
    with Session(engine) as session:
        for dataset in datasets:
            logger.info(f"Dataset: {dataset.get_nome()}")
            save_file = "./datasets/" + dataset.get_csv_filename()
            with open(save_file, newline="") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=dataset.get_csv_delimiter())
                headers = next(csv_reader, None)
                ano_posicao_inicial = 2
                ano_posicao_final = len(headers) - 1
                for row in csv_reader:
                    dataset_id = int(row[0].strip())
                    dataset_nome = dataset.get_nome().strip()
                    tipo = dataset.get_sub_categoria().strip()
                    pais = row[1].strip()
                    anos = range(ano_posicao_inicial, ano_posicao_final + 1)
                    quantidade = 0
                    valor = 0
                    for index in anos:
                        ano = int(headers[index].strip())
                        value = row[index].strip()

                        salva_dados = index % 2 != 0
                        if not salva_dados:
                            quantidade = transform_value(value)
                        else:
                            valor = transform_value(value)

                        if salva_dados:
                            importacao = Importacao(
                                dataset_id=dataset_id,
                                dataset_nome=dataset_nome,
                                tipo=tipo,
                                pais=pais,
                                ano=ano,
                                quantidade=quantidade,
                                valor=valor,
                            )
                            session.add(importacao)
                            session.commit()
    logger.info("Finalizado a carga de dados de Importação")


def load_dataset_exportacao(engine) -> None:
    logger.info("Carregando dados de Exportação")
    datasets = DatasetUtil.get_exportacao_datasets()
    with Session(engine) as session:
        for dataset in datasets:
            logger.info(f"Dataset: {dataset.get_nome()}")
            save_file = "./datasets/" + dataset.get_csv_filename()
            with open(save_file, newline="") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=dataset.get_csv_delimiter())
                headers = next(csv_reader, None)
                ano_posicao_inicial = 2
                ano_posicao_final = len(headers) - 1
                for row in csv_reader:
                    dataset_id = int(row[0].strip())
                    dataset_nome = dataset.get_nome().strip()
                    tipo = dataset.get_sub_categoria().strip()
                    pais = row[1].strip()
                    anos = range(ano_posicao_inicial, ano_posicao_final + 1)
                    quantidade = 0
                    valor = 0
                    for index in anos:
                        ano = int(headers[index].strip())
                        value = row[index].strip()

                        salva_dados = index % 2 != 0
                        if not salva_dados:
                            quantidade = transform_value(value)
                        else:
                            valor = transform_value(value)

                        if salva_dados:
                            exportacao = Exportacao(
                                dataset_id=dataset_id,
                                dataset_nome=dataset_nome,
                                tipo=tipo,
                                pais=pais,
                                ano=ano,
                                quantidade=quantidade,
                                valor=valor,
                            )
                            session.add(exportacao)
                            session.commit()
    logger.info("Finalizado a carga de dados de Exportação")


def create_database_vitivinicultura() -> Engine:
    engine = create_engine("sqlite:///instance/vitivinicultura.db")
    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    if database_exists(engine.url):
        logger.info("Banco de Dados de Vitivinicultura carregado com sucesso")
    return engine


def main():
    logging.basicConfig(level=logging.INFO)
    engine = create_database_vitivinicultura()
    load_dataset_producao(engine)
    load_dataset_processamento(engine)
    load_dataset_comercializacao(engine)
    load_dataset_importacao(engine)
    load_dataset_exportacao(engine)


if __name__ == "__main__":
    main()
