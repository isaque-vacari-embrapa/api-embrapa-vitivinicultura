# API de Dados de Vitivinicultura

API para exposição de dados referentes à quantidade de uvas processadas, produção e comercialização de vinhos, suco e derivados provenientes do Estado do Rio Grande do Sul, que representa mais de 90% da produção nacional. Apresenta-se também os dados de importações e exportações dos produtos da vitivinicultura.

Vale salientar que os dados de vitinicultura foram extraídos do **Banco de dados de uva, vinho e derivados** organizado pela Embrapa Uva e Vinho, disponível em: http://vitibrasil.cnpuv.embrapa.br/.

De acordo com os organizadores do Portal de Dados da Vitivinicultura, alguns esclarecimentos se fazem necessários, para que os usuários façam o uso correto das informações:

- Os vinhos nacionais são classificados para fins estatísticos em vinho de mesa (elaborados com uvas americanas e/ou híbridas), vinho fino de mesa (elaborados com uvas *Vitis Vinifera* L.) e vinho especial (corte de vinho de mesa e fino de mesa).

- Os vinhos importados, denominados de vinhos de mesa são equivalentes aos vinhos finos de mesa nacionais, pois são elaborados com uvas *Vitis Vinifera* L.

## 🚀 Funcionalidades de Negócio da API

A **API de Dados de Vitivinicultura** é formada pelos seguintes recursos:

- Consulta de dados de produção de vinhos, sucos e derivados do Rio Grande do Sul/RS;
- Consulta da quantidade de uvas processadas (Viníferas, Americanas e híbridas, Uvas de Mesa) no Rio Grande do Sul/RS;
- Consulta da quantidade de comercialização de vinhos e derivados no Rio Grande do Sul/RS;
- Consulta de dados de importação de derivados de uva (Vinhos de mesa, Espumantes, Uvas frescas, Uvas passas e Suco de Uva);
- Consulta de dados de exportação de derivados de uva (Vinhos de mesa, Espumantes, Uvas frescas e Suco de Uva).

## Tecnologias Utilizadas para o Desenvolvimento da API

Do ponto de vista tecnológico, esta API foi desenvolvida com Python/Flask que inclui Web Scraping para consulta de dados em tempo real a partir do Portal de Dados da Vitivinicultura da Embrapa, bem como Web Scraping para extração e carga de dados para consultas "*offline*" em caso de indisponibilidade do Portal de Dados da Vitivinicultura. Vale salientar que o acesso à API requer autenticação do tipo JWT (JSON Web Token). De maneira detalhada, estas são as tecnologias utilizadas:

- **API**: Expõe os dados de dados de vitivinicultura disponibilizados Portal de Dados da Vitivinicultura da Embrapa na forma de API, usando o microframework Python/Flask;
- **Web Scraping**: Consulta de dados de vitivinicultura em tempo real a partir do Portal de Dados da Vitivinicultura da Embrapa, bem como Web Scraping para extração e carga de dados para consultas "*offline*" em caso de indisponibilidade do Portal de Dados da Vitivinicultura, usando BeautifulSoup;
- **Autenticação JWT**: Protege as rotas de consulta aos dados (produção, comercialização, processamento, importação e exportação) de vitivinicultura;
- **Cache e Documentação**: Implementa cache para otimização de consultas e documentação automática com Swagger, usando Flasgger.

## 📁 Estrutura de Diretórios do Projeto

```bash
├── app
│   ├── infrastructure
│   │   ├── cache.py
│   │   ├── config.py
│   ├── models
│   │   ├── base
│   │   │   ├── database.py
│   │   │   ├── dataset.py
│   │   ├── entities
│   │   │   ├── comercializacao.py
│   │   │   ├── exportacao.py
│   │   │   ├── importacao.py
│   │   │   ├── processamento.py
│   │   │   ├── producao.py
│   │   │   └── user.py
│   │   └── forms
│   │       ├── user_form.py
│   │       └── user_login_form.py
│   ├── routes
│   │   ├── comercializacao_api.py
│   │   ├── exportacao_api.py
│   │   ├── importacao_api.py
│   │   ├── processamento_api.py
│   │   ├── producao_api.py
│   │   └── user_api.py
│   ├── run_extract_dataset.py
│   ├── run_load_dataset.py
│   ├── run.py
│   ├── services
│   │   ├── comercializacao_service.py
│   │   ├── exportacao_service.py
│   │   ├── importacao_service.py
│   │   ├── processamento_service.py
│   │   ├── producao_service.py
│   └── utils
│       ├── dataset_util.py
│       ├── general_util.py
├── datasets
│   ├── comercializacao.csv
│   ├── exportacao_espumantes.csv
│   ├── exportacao_suco_de_uva.csv
│   ├── exportacao_uvas_frescas.csv
│   ├── exportacao_vinhos_de_mesa.csv
│   ├── importacao_espumantes.csv
│   ├── importacao_suco_de_uva.csv
│   ├── importacao_uvas_frescas.csv
│   ├── importacao_uvas_passas.csv
│   ├── importacao_vinhos_de_mesa.csv
│   ├── processamento_americanas_e_hibridas.csv
│   ├── processamento_uvas_de_mesa.csv
│   ├── processamento_viniferas.csv
│   └── producao.csv
├── docker-compose.yml
├── Dockerfile
├── instance
│   ├── auth.db
│   └── vitivinicultura.db
├── README.md
└── requirements.txt
```

 - **`app/`**: Diretório principal da API.
    - **`infrastructure/`**: Contém as configurações da aplicação Flask.
    - **`models/`**: Contém as entidades de mapeamento objeto-relacional para o registro e autenticação de usuários, bem como para a consulta de dados de vitivinicultura de maneira *offline*.
    - **`routes/`**: Contém as rotas organizadas por funcionalidades, o registro e autenticação de usuários, bem como a consulta de dados de vitivinicultura.
    - **`services/`**: Serviços para lógica de negócios, como scraping e consulta de dados de maneira *offline*.
    - **`utils/`**: Utilitários, como rotinas de conversão de textos para quantidades em formato numérico.
    - **`run.py`**: Ponto de entrada para iniciar a API.
    - **`run_extract_dataset.py`**: Extrai os arquivos de dados em formato CSV para facilitar a importação em banco de dados.
    - **`run_load_dataset.py`**: Executa a transformação e carga dos arquivos de dados extraídos em formato CSV para o banco de dados de consulta *offline*.
- **`datasets/`**: Armazena os arquivos de dados em formato CSV extraídos do Portal de Dados da Vitivinicultura para carga futura em banco de dados para consulta do tipo *offline*.
- **`instance/`**: Bancos de dados da aplicação.
    - **`auth.db`**: Banco de dados de usuários para autenticação e autorização de acesso à consulta de dados de vitivinicultura.
    - **`vitivinicultura.db`**: Banco de dados de vitivinicultura para consulta de dados *offline* de produção, comercialização, processamento, importação e exportação; executada somente em caso de indisponibilidade do do Portal de Dados da Vitivinicultura da Embrapa Uva e Vinho.
- **`docker-compose.yml`**: Configurações para conteinerização da aplicação em Docker.
- **`Dockerfile`**: Configurações para Docker.
- **`README.md`**: Documentação do projeto.
- **`requirements.txt`**: Lista de dependências do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
https://github.com/isaque-vacari-embrapa/api-embrapa-vitivinicultura.git
cd api-embrapa-vitivinicultura
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

A API estará disponível em `http://localhost:5000`.

## 🐳 Como Usar com Docker

### 1. Construa a Imagem Docker e Execute o Container

```bash
docker compose-up -d
```

Acesse a API em `http://localhost:5000`.

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.