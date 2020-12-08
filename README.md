# desafioItau

Esta é uma API destinada ao uso do Itau.

## Configurações
Esta API foi criada pensando em custo/beneficio, usando o framework flask, muito utilizado para API's com baixo tempo investido. Este framework é amplamente utilizado pela comunidade. A linguagem utilizada foi o Python, em sua versão 3 ou superior. Os motivos considerados para escolher a linguagem foram:
- Popularidade
* Python hoje e uma das linguagens mais utilizadas do mundo e com mais colaboradores em bibliotecas, com isto, teríamos resultados mais rápidos e performáticos ao utilizar o Python.
- Conhecimento
* E a linguagem que detenho mais conhecimento, onde utilizo principalmente para scripts de automações. Não tendo tempo hábil para aprender Kotlin, escolhi a linguagem onde me sairia melhor.
 
## Pre-requisitos
Como pre-requisito basta instalar o python em sua versão 3 ou superior e o pip.
  Python
  > apt-get install python3
  Pip
  > apt-get install pip3
 
## Execução
Existem 2 maneiras de executar essa aplicação localmente, via linha de comando e via Docker. Segue abaixo passo-a-passo para a execução de ambos
 
### Linha de comando
``` 
cd app
python3 api.py
```

### Docker
#### Docker Hub
 ``` 
 docker pull julioback/desafioitau:5
 ```
#### Docker local
 ``` 
 cd app
 docker build -t desafioitau:1 .
 docker run -d -p 80:80 desafioitau:1
 ```
 
## Acessando a aplicação
Para acessar a aplicação basta digitar no navegador http://127.0.0.1
 
## Documentação
Para documentação foi utilizado o protocolo Swagger
> https://app.swaggerhub.com/apis/julioback/DesafioItau/1.0.0
 
## Testes
Como e uma API simples, não foi identificado a necessidade de testes, porem em casos de aplicações em produção, iria utilizar o pytest para escrever os testes e o pytest-cov utilizando o SonarQube para mostrar os resultados.
