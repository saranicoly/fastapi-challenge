# Desafio Backend

## Decisões Iniciais

- Havia a possibilidade de usar Python, Java ou Node.js para o desafio. Eu escolhi Python por já ter familiaridade com a linguagem.
- Feito isso, eu ponderei o que iria usar para o webservice. Dentre as opções principais estavam: Django, Flask e FastAPI.
- Eu não tinha familiaridade com nenhum dos frameworks citados, então esse não foi um fator decisivo. Acabei decidindo por FastAPI por se tratar de um framework de mais fácil aprendizado e pelo fato de o desafio em si ser bastante simples. Caso existisse um cenário de complexidade maior, muito provavelmente eu usaria Django (por ser mais "robusto").

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
