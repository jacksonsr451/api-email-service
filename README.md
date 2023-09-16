# Email Service

Este é um serviço de e-mail construído em Python com o framework Flask, seguindo uma arquitetura modular com as seguintes camadas: Core, Application, Infrastructure, Adapters e Controllers. Ele fornece uma rota POST para enviar e-mails.

## Instalação

Antes de começar, certifique-se de ter o Python e o Poetry instalados. Se você ainda não tem o Poetry, você pode instalá-lo seguindo as [instruções oficiais](https://python-poetry.org/docs/#installation).

Após instalar o Poetry, você pode criar um ambiente virtual para o projeto executando o seguinte comando na raiz do projeto:

```bash
poetry install
```

## Configuração

Antes de executar o serviço, você precisa configurar as variáveis de ambiente para autenticar-se com um serviço de e-mail, como o AWS SES. Crie um arquivo .env na raiz do projeto e configure as seguintes variáveis:

env

AWS_ACCESS_KEY_ID=seu-id-de-chave-de-acesso
AWS_SECRET_ACCESS_KEY=sua-chave-secreta-de-acesso
AWS_REGION=sua-região-da-aws

## Uso

Para iniciar o serviço, execute o seguinte comando:

```bash
poetry run flask run
```

**O serviço estará disponível em** `http://localhost:5000`.

## Enviar um e-mail

Você pode enviar um e-mail fazendo uma solicitação POST para a rota `/api/v1/email/`.
**Aqui está um exemplo de solicitação usando cURL:**

```bash

curl -X POST http://localhost:5000/api/v1/email/ -H "Content-Type: application/json" -d '{
  "to": "destinatario@example.com",
  "subject": "Assunto do E-mail",
  "body": "Conteúdo do e-mail"
}'
```

### Resposta

- O serviço responderá com um JSON indicando se o e-mail foi enviado com sucesso ou não.

## Estrutura do Projeto

- A estrutura do projeto segue uma arquitetura modular com as seguintes camadas:

  - core/: Camada central com entidades e lógica de negócios.

  - application/: Camada de aplicação que contém casos de uso.

  - infrastructure/: Camada de infraestrutura com adaptadores, como o adaptador para serviços de e-mail.

  - adapters/: Camada de adaptadores para integrações externas.

  - email_service/: Pacote que atua como a camada de aplicação (app) e contém os blueprints.

  - controllers/: Camada de controladores para manipulação das solicitações HTTP.

  - app.py: Configuração principal do Flask e definição de rotas.

## Contribuindo

Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode abrir problemas (issues) e enviar solicitações de pull (pull requests) para colaborar.
Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter detalhes.
