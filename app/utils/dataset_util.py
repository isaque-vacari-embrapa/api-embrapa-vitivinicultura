from models.base.dataset import Dataset

datasets = [
    # Datasets de produção de vinhos, sucos e derivados do Rio Grande do Sul
    Dataset(
        "producao",
        "Produção",
        None,
        "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "producao.csv",
        ";",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02",
    ),
    # Datasets de processamento de quantidade de uvas processadas no Rio Grande do Sul
    Dataset(
        "processamento-viniferas",
        "Processamento",
        "Viníferas",
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "processamento_viniferas.csv",
        ";",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03",
    ),
    Dataset(
        "processamento-americanas-e-hibridas",
        "Processamento",
        "Americanas e híbridas",
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "processamento_americanas_e_hibridas.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03",
    ),
    Dataset(
        "processamento-uvas-de-mesa",
        "Processamento",
        "Uvas de mesa",
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "processamento_uvas_de_mesa.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03",
    ),
    Dataset(
        "processamento-sem-classificacao",
        "Processamento",
        "Sem classificação",
        None,
        None,
        None,
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03",
    ),
    # Datasets de comercialização de vinhos e derivados no Rio Grande do Sul
    Dataset(
        "comercializacao",
        "Comercialização",
        None,
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "comercializacao.csv",
        ";",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04",
    ),
    # Datasets de importação de derivados de uva
    Dataset(
        "importacao-vinhos-de-mesa",
        "Importação",
        "Vinhos de mesa",
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "importacao_vinhos_de_mesa.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05",
    ),
    Dataset(
        "importacao-espumantes",
        "Importação",
        "Espumantes",
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "importacao_espumantes.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05",
    ),
    Dataset(
        "importacao-uvas-frescas",
        "Importação",
        "Uvas frescas",
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "importacao_uvas_frescas.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05",
    ),
    Dataset(
        "importacao-uvas-passas",
        "Importação",
        "Uvas passas",
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "importacao_uvas_passas.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05",
    ),
    Dataset(
        "importacao-suco-de-uva",
        "Importação",
        "Suco de uva",
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "importacao_suco_de_uva.csv",
        ";",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05",
    ),
    # Datasets de exportação de derivados de uva
    Dataset(
        "exportacao-vinhos-de-mesa",
        "Exportação",
        "Vinhos de mesa",
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "exportacao_vinhos_de_mesa.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06",
    ),
    Dataset(
        "exportacao-espumantes",
        "Exportação",
        "Espumantes",
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "exportacao_espumantes.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06",
    ),
    Dataset(
        "exportacao-uvas-frescas",
        "Exportação",
        "Uvas frescas",
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "exportacao_uvas_frescas.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06",
    ),
    Dataset(
        "exportacao-suco-de-uva",
        "Exportação",
        "Suco de uva",
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "exportacao_suco_de_uva.csv",
        "	",
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06",
    ),
]


class DatasetUtil:
    @staticmethod
    def get_datasets():
        return datasets

    @staticmethod
    def get_producao_datasets():
        return [
            dataset for dataset in datasets if dataset.get_categoria() == "Produção"
        ]

    @staticmethod
    def get_comercializacao_datasets():
        return [
            dataset
            for dataset in datasets
            if dataset.get_categoria() == "Comercialização"
        ]

    @staticmethod
    def get_processamento_datasets():
        return [
            dataset
            for dataset in datasets
            if dataset.get_categoria() == "Processamento"
        ]

    @staticmethod
    def get_importacao_datasets():
        return [
            dataset for dataset in datasets if dataset.get_categoria() == "Importação"
        ]

    @staticmethod
    def get_exportacao_datasets():
        return [
            dataset for dataset in datasets if dataset.get_categoria() == "Exportação"
        ]

    @staticmethod
    def get_producao_dataset():
        return [dataset for dataset in datasets if dataset.get_nome() == "producao"][0]

    @staticmethod
    def get_processamento_viniferas_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "processamento-viniferas"
        ][0]

    @staticmethod
    def get_processamento_americanas_e_hibridas_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "processamento-americanas-e-hibridas"
        ][0]

    @staticmethod
    def get_processamento_uvas_de_mesa_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "processamento-uvas-de-mesa"
        ][0]

    @staticmethod
    def get_processamento_sem_classificacao_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "processamento-sem-classificacao"
        ][0]

    @staticmethod
    def get_comercializacao_dataset():
        return [
            dataset for dataset in datasets if dataset.get_nome() == "comercializacao"
        ][0]

    @staticmethod
    def get_importacao_vinhos_de_mesa_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "importacao-vinhos-de-mesa"
        ][0]

    @staticmethod
    def get_importacao_espumantes_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "importacao-espumantes"
        ][0]

    @staticmethod
    def get_importacao_uvas_frescas_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "importacao-uvas-frescas"
        ][0]

    @staticmethod
    def get_importacao_uvas_passas_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "importacao-uvas-passas"
        ][0]

    @staticmethod
    def get_importacao_suco_de_uva_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "importacao-suco-de-uva"
        ][0]

    @staticmethod
    def get_exportacao_vinhos_de_mesa_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "exportacao-vinhos-de-mesa"
        ][0]

    @staticmethod
    def get_exportacao_espumantes_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "exportacao-espumantes"
        ][0]

    @staticmethod
    def get_exportacao_uvas_frescas_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "exportacao-uvas-frescas"
        ][0]

    @staticmethod
    def get_exportacao_suco_de_uva_dataset():
        return [
            dataset
            for dataset in datasets
            if dataset.get_nome() == "exportacao-suco-de-uva"
        ][0]
