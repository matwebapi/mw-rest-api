# Executando a aplicação

## Dependências

**Python 3**

É necessário utilizar o `Python3` para executar a aplicação. Recomendamos o Python na versão `3.6.4`.

**Bibliotecas**

Todas as bibliotecas utilizadas estão especificadas no arquivo `requirements.txt`, na pasta raiz do projeto.

### Instalando as dependências

Recomendamos utilizar o `pip3` como gerenciador de pacotes para instalar as bibliotecas necessárias:

```shell
pip3 install -r requirements.txt
```

## Executando a aplicação localmente

1. Clone o projeto
```
git clone https://github.com/matwebapi/mwapi.git
```
2. Entre na pasta que contem o arquivo `manage.py`:
```
cd mwapi/mw_api/
```
3. Execute os seguintes comandos:
```shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
<br>ou, de forma alternativa, execute o script `run.sh`:
```shell
sh run.sh
```

4. Acesse a url da aplicação:
`http://0.0.0.0:8000/`

## Populando a API com os dados do MatriculaWeb

Após a aplicação ter sido executada (passo anterior) é possível popular o banco de dados com os dados disponíveis do MatriculaWeb, para que possam ser acessíves através da API. O comando `populate_prod` do `manage.py` faz toda esta operação. Para executar o comando:

1.
```shell
python3 manage.py populate_prod
```
