class Dataset:
    def __init__(
        self,
        nome,
        categoria,
        sub_categoria,
        csv_file_url,
        csv_filename,
        csv_delimiter,
        site_url,
    ) -> None:
        self.__nome = nome
        self.__categoria = categoria
        self.__sub_categoria = sub_categoria
        self.__csv_file_url = csv_file_url
        self.__csv_filename = csv_filename
        self.__csv_delimiter = csv_delimiter
        self.__site_url = site_url

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria

    def get_sub_categoria(self):
        return self.__sub_categoria

    def get_csv_file_url(self):
        return self.__csv_file_url

    def get_csv_filename(self):
        return self.__csv_filename

    def get_csv_delimiter(self):
        return self.__csv_delimiter

    def get_site_url(self):
        return self.__site_url
