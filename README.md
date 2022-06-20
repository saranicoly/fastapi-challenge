# Desafio Backend

## Decisões Tomadas

### Decisões Iniciais

- Havia a possibilidade de usar Python, Java ou Node.js para o desafio. Eu escolhi Python por já ter familiaridade com a linguagem.
- Feito isso, eu ponderei o que iria usar para o webservice. Dentre as opções principais estavam: Django, Flask e FastAPI.
- Eu não tinha familiaridade com nenhum dos frameworks citados, então esse não foi um fator decisivo. Acabei decidindo por FastAPI por se tratar de um framework de mais fácil aprendizado e pelo fato de o desafio em si ser bastante simples. Caso existisse um cenário de complexidade maior, muito provavelmente eu usaria Django (por ser mais "robusto") e visto que seria mais fácil utilizar o padrão MVC com o Django para criar um possível front-end.

### Decisões no decorrer do desenvolvimento

- Inicialmente, decidi utilizar uma matriz de adjacência (em vez de lista de adjacência) porque é necessário realizar muitas consultas e, em Python, eu poderia assim acessar diretamente o dado que quero saber. Por exemplo: `matriz_Adj[x][y]`.
- Eu tentei utilizar os conceitos de orientação a objetos no decorrer do projeto, de forma que ficasse mais fácil de entender o código.
- Dividi os diretórios da seguinte forma: 
  - `src`: contém o README.md, requirements.txt e o Dockerfile
  - `/app`: contém o arquivo principal do projeto, `main.py` e os arquivos das classes.
- Decidi dessa forma para facilitar o desenvolvimento e o entendimento do projeto, considerando que se trata de um código simples.

### Possíveis melhorias

- O principal ponto que eu não implementei, mas gostaria de ter, é a utilização de testes. Acabei não implementando por questão de tempo.
- Ter um frontend conectado com esse backend deixaria muito mais intuitivo.
- Também seria interessante fazer deploy do projeto na nuvem.
- Desacoplar algumas coisas de http de dentro do grafo e colocá-las no main.py, que é onde estão sendo definidas as rotas.

## Rodando o projeto

### Nativo

Para executar o projeto, basta seguir o seguinte passo a passo:

- Instalar as dependências com um `pip install -r requirements.txt`
- Executar o comando `uvicorn main:app --reload` dentro da pasta `app`
- Se dirigir ao endereço `127.0.0.1:8000/docs`

### Docker

Caso deseje, também é possível executar a aplicação através do Docker. Para isso, basta seguir os seguintes passos:

- Ter o docker instalado na sua máquina
- Criar a imagem com o seguinte comando, a partir da raiz do projeto: `docker build -t testeluizalabs .`
- Executar o container com `docker run -p 8080:80 -it testeluizalabs`
- Abrir o navegador no endereço `0.0.0.0:8080/docs`
- Explorar a API a partir desse endereço.

**Dica:**  Em `0.0.0.0:8080/docs`, você pode clicar em "Try it out" e testar a API.

### OBS

- O arquivo `main.py` é o arquivo principal da aplicação e contém as rotas que estão sendo usadas.
- `grafo.py` e `person.py` são os arquivos referentes às classes utilizadas (Grafo e Person).
- Observe que o programa é case sensitive. Isso significa que se cadastrar um usuário como "user" e depois procurar por "User", o programa não o encontrará.
