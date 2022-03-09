## Executando o projeto

1. Entrar no diretório do node_red

```sh
cd node_red_data
```

Instalar o node_red e as dependências do projeto

```sh
npm install
```

Iniciar o servidor NodeRed

```sh
npm start
```

Concluídas as etapas anteriores é necessário importar o arquivo json com as configurações do projeto. Isto carregará o _flow_ que foi previamente desenvolvido.

## Entendendo o ambiente de simulação

Após a inicialização da simulação os sendores começarão a coletar os dados fisiológicos e os dados exógenos de temperatura e iluminação. Tais dados serão enviados via protocolo COAP para o servidor que é executado no Gateway.
Após o recebimento dos dados, o gateway irá imprimir os mesmos no terminal de DEBUG do NodeRed, para facilitar o acompanhamento.
Além disso, os dados serão transformados em CSV e exportados para posterior análise.
