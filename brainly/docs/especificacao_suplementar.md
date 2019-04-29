# ESPECIFICAÇÃO SUPLEMENTAR - VERSÃO 1.0

# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 0.1 | 29/04/2019 | Estrutura da especificação e tópicos básicos | Welison Regis e Leonardo Medeiros |
| 0.5 | 29/04/2019 | Adiciona novos tópicos à especificação suplementar | Welison Regis |

# INTRODUÇÃO

## FINALIDADE

A especificação suplementar desenvolvida tem por objetivo descrever os requisitos não funcionais relacionados à plataforma Brainly. A descrição desses requisitos procura atender necessidades que vão sob um aspecto mais subjetivo em relação à qualidade, estrutura e apresentação da plataforma e outras condições de satisfação.

## ESCOPO

Esta especificação suplementar delimita-se no escopo da aplicação Brainly em território nacional brasileiro. Abarca nesse documento o escopo relacionado a aplicação web e mobile da plataforma, e procura-se desenvolver como os aspectos da plataforma, especialmente aqueles não-funcionais, interferem no convívio de moderadores, usuários, administradores e demais estudantes que utilizam o Brainly como forma de tirar dúvidas escolares ou acadêmicas.

## DEFINIÇÕES, ACRÔNIMOS E ABREVIATURAS

## REFERÊNCIAS


## VISÃO GERAL

# FUNCIONALIDADE
A documentação das funcionalidades da aplicação Brainly pode ser encontrada neste [endereço](https://welisonr.github.io/2019.1-Requisitos-Brainly/), sendo especialmente recomendado a visualização das funcionalidades com as respectivas priorizações no link ([priorizações](./priorizacao.md)), além dos casos de uso com as devidas especificações no link de [casos de uso](./casos_uso_perguntas_respostas).

# USABILIDADE

# CONFIABILIDADE

# DESEMPENHO

# SUPORTABILIDADE

# RESTRIÇÕES DE DESIGN
O sistema deve seguir padrões de _deisgn_ na implementação de suas interfaces de forma a garantir a melhor experiência na utilização da plataforma, seja em um dispositivo móvel ou computadores em geral. Tem-se como referência a documentação de _styleguide_ disposta na página na página do aplicativo no github - [styleguide brainly](https://github.com/brainly/style-guide).

# REQUISITOS DE SISTEMA DE AJUDA E DE DOCUMENTAÇÃO DE USUÁRIO ON-LINE
O sistema de ajuda e a sua respectiva documentação deve ser de fácil acesso pelo usuário através do próprio aplicativo ou da plataforma web e, deve cobrir prioritariamente os seguintes tópicos:

*	Fluxo para realizar uma pergunta;
*	Fluxo para responder a uma pergunta;
*	Adicionar comentários às questões ou as respostas;
*	Denunciar uma pergunta, resposta ou comentário;
*	Modificar dados da conta ou deletá-la.

O suporte online pode ser dividido em duas categorias, sendo:

*   Seção de dúvidas frequentes, o que proporciona acesso rápido a problemas e questionamentos comuns relacionados ao uso do aplicativo - disponível no seguinte formato de [ajuda](https://brainly.com.br/pages/questoes_frequentes);
*   Canal para envio de correspondências ou mensagens de forma a tirar dúvidas ou questões individuais.

# COMPONENTES ADQUIRIDOS
Os _softwares_ utilizados para a elaboração do projeto são gratuitos e cada um consta individualmente com sua licença, dentre as principais licenças, tem-se: `NodeJS` com licença própria, `react`, `react native`, `KaTeX` (latex) sob a licença `MIT`.

# INTERFACES

## Interfaces do usuário
O sistema deve ter uma interfaces gráficas que possibilitem que o usuário interaja com a plataforma.
O sistema utilizará componentes em `react` ou `react native` para modularizar a interface da aplicação.

## Interfaces de hardware
O sistema deve manter suporte para dispositivos móveis e computadores, possibilitando que as requisições sejam feitas utilizando protocolos seguros como `https`. Deve haver suporte aos sistemas `ios`, `android`.

## Interfaces de software

O sistema deve utilizar tecnologias de linguagens e frameworks pertencentes a um paradigma que favoreça a solução do problema de forma eficiente no desenvolvimento e fácil manutenção. Estão entre as opções utilizadas: `NodeJS 8+`, `React`, `React Native`, `yarn`, etc.

## Interfaces de comunicação

O sistema deve ter uma interface de comunicação que torne possível múltiplas requisições simultâneas entre os aplicativos que compõem o sistema mantendo a integridade dos dados.
A comunicação será realizada com múltiplos _backends_ em `NodeJS` com a interface feita majoritariamente em `react`.

## Requisitos de licenciamento
Para a utilização dos serviços Brainly requere-se que o usuário concorde com a [política de privacidade](https://brainly.com/pages/privacy_policy) da plataforma, [política de cookies](https://brainly.com/pages/cookie_policy) e os [termos de uso](https://brainly.com/pages/terms_of_use).

# REQUISITOS DE LICENCIAMENTO

# OBSERVAÇÕES LEGAIS, DE COPYRIGHT E OUTRAS

# PADRÕES APLICÁVEIS
