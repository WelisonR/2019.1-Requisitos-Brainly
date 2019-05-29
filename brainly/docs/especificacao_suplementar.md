# ESPECIFICAÇÃO SUPLEMENTAR - VERSÃO 1.0

# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 0.1 | 29/04/2019 | Estrutura da especificação e tópicos básicos | Welison Regis e Leonardo Medeiros |
| 0.2 | 29/04/2019 | Adiciona novos tópicos à especificação suplementar | Welison Regis |
| 0.3 | 29/04/2019 | Adicionado requisitos de usabilidade | André Lucas |
| 0.4 | 29/04/2019 | Adiciona tópicos de licenciamento, padrões, interface e suportabilidade | Welison Regis |
| 0.5 | 29/04/2019 | Adiciona requisitos de confiabilidade | Lieverton |
| 1.0 | 29/04/2019 | Conclui primeira versão do documento | Lieverton Silva, Welison Regis |

# INTRODUÇÃO

## FINALIDADE

A especificação suplementar desenvolvida tem por objetivo descrever os requisitos não funcionais relacionados à plataforma Brainly, além dos requisitos não identificados imediatamente nos casos de uso do modelo de casos de uso. A descrição desses requisitos procura atender necessidades que vão sob um aspecto mais subjetivo em relação à qualidade, estrutura e apresentação da plataforma e outras condições de satisfação.

## ESCOPO

Esta especificação suplementar delimita-se no escopo da aplicação Brainly em território nacional brasileiro. Abarca neste documento o escopo relacionado a aplicação web e mobile da plataforma, e procura-se desenvolver como os aspectos da plataforma, especialmente aqueles não-funcionais, interferem no convívio de moderadores, usuários, administradores e demais estudantes que utilizam o Brainly como forma de tirar dúvidas escolares ou acadêmicas.

## DEFINIÇÕES, ACRÔNIMOS E ABREVIATURAS

Vide [léxicos](lexicos10x5f8c4.md)

## REFERÊNCIAS
[1] Funpar. **Template: Especificações Suplementares**. Disponível [aqui](http://www.funpar.ufpr.br:8080/rup/process/artifact/ar_sspec.htm). Acesso em: 23 abr. 2019.

[2] NNGROUP. **Dez heurísticas de usabilidade**. Disponível [aqui](https://www.nngroup.com/articles/ten-usability-heuristics/). Acesso em: 29 abr. 2019.

[3] BRAINLY. **Brainly.com.br - estudamos juntos**. Disponível [aqui](https://brainly.com.br/). Acesso em: 28 abr. 2019.

[4] BRAINLY. **Brainly Front-End Style Guide**. Disponível [aqui](https://styleguide.brainly.com/143.5.3/docs/). Acesso em: 29 abr. 2019.

[5] BRAINLY. **Repositórios do Brainly no GitHub**. Disponível [aqui](https://github.com/brainly/style-guide). Acesso em: 29 abr. 2019.

## VISÃO GERAL

# FUNCIONALIDADE
A documentação das funcionalidades da aplicação Brainly pode ser encontrada [neste endereço](https://welisonr.github.io/2019.1-Requisitos-Brainly/), sendo especialmente recomendado a visualização das funcionalidades com as respectivas priorizações [neste link](./priorizacao.md), além dos casos de uso com as devidas especificações no link de [casos de uso](./casos_uso_perguntas_respostas).

# USABILIDADE
- Consistência ferramental [(INT1.2)](introspeccao.md)
- Curva rápida de aprendizagem [(INT3.9)](introspeccao.md) 
- Versão mobile [(INT3.11)](introspeccao.md) 
- Cadastro fácil [(AP3.3)](introspeccao.md) 
- Tutorial [(AP3.4)](introspeccao.md) 
## REQUISITO DE CONSISTÊNCIA FERRAMENTAL
O sistema deve oferecer uma experiência consistente ao usuário, disponibilizando ferramentas que oferecem um risco pequeno de erro, fazendo com que o usuário tenha uma experiência mais fluida.
## REQUISITO DE CURVA RÁPIDA DE APRENDIZAGEM
A plataforma deve ser feita de tal forma que o usuário aprenda de forma rápida como utilizar as ferramentas essênciais para seguir os possíveis fluxos da aplicação. Um tutorial deve ser feito para usuário novatos, sendo possível repetir caso desejar. O sistema deve seguir as [10 heurísticas de Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/).
## REQUISITO DE VERSÃO MOBILE
O sistema deve possuir, também, uma versão mobile, aumentando o publico alvo e facilitando o uso. Tal versão deve estar disponível para dispositivos Android e iOS e ter um baixo consumo de bateria/dados, para que o usuário não se sinta desmotivado em utilizar a plataforma.
## REQUISITO DE CADASTRO FÁCIL
O cadastro na plataforma deve ocorrer de uma maneira rápida e prática, possuindo apenas os campos mais úteis como e-mail, senha, país e data de nascimento. O sistema deve também disponibilizar cadastro via Facebook por muitos usuários acharem mais prático e conter os dados necessários.
## REQUISITO DE TUTORIAL
O tutorial do sistema deve ocorrer de maneira fluida, rápida, contínua, sem informações não úteis para um usuário novo e deve ser possível repeti-lo caso o usuário sinta necessidade.

# CONFIABILIDADE

- tempo de respostas [(INT3.6)](introspeccao.md)
- Condições de advertência [(INT2.10)](introspeccao.md)
- Sistema gratuito [(EN1.3)](introspeccao.md)
- Utilização de informações de pessoais [(BR2.7)](brainstorm.md)
- Protecão de dados [(BR2.10)](brainstorm.md)
- Atualizar automaticamente o app [(BR2.16)](brainstorm.md)
- Impossibilitar comercialização de informações [(BR2.17)](brainstorm.md)

## REQUISITO DE TEMPO DE RESPOSTA

A plataforma deve possuir membros ativos que ajudem a comunidade a crescer e respondam as perguntas de forma rápida e fácil.

## REQUISITO DE ADVRTÊNCIA

Para aplicação de punições, deve-se levar em conta a conduta (advertências) do usuário na plataforma.

## REQUISITO DE SISTEMA GRATUITO

Manter o sistema gratuito para atrair mais usuários, utilizando apenas de ads para a monetização.

## REQUISITO UTILIZAÇÃO DE INFORMAÇÕES DE PESSOAIS

O sistema não deve utilizar informações de pessoas menores de 16 anos sem autorização. Para isso deve averiguar a idade do usuário antes de utilizar suas informações para marketing.

## REQUISITO DE PROTEÇÃO DE DADOS

O sistema deve possuir um sistema de segurança mais seguro possível dentro dos conhecimentos de segurança atuais.

## REQUISITO DE PROTEÇÃO DE DADOS
	
O sistema deve ser atualizado automaticamente nas plataformas Android e IOS, assim que forem aceitos novos commits na master.

## REQUISITO DE IMPOSSIBILITAR COMERCIALIZAÇÃO DE INFORMAÇÕES

Impedir o vazamento de informações pessoais dos usuários e consequentemente sua venda.

# DESEMPENHO

- Tempo médio de respostas[(INT3.6)](introspeccao.md)
- Versão mobile [(INT3.11)](introspeccao.md)
- Cadastro fácil [(AP3.3)](analise_protocolo.md)
- Apagar perguntas sem reposta [(BR2.15)](brainstorm.md) 

## REQUISITO DE TEMPO MÉDIO DE RESPOSTAS

A plataforma deve possuir membros ativos que ajudem a comunidade a crescer e respondam as perguntas de forma rápida e fácil.

## REQUISITO DE VERSÃO MOBILE

O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados.

## REQUISITO DE CADASTRO FÁCIL

O cadastro na plataforma deve ocorrer de uma maneira rápida e prática.

## REQUISITO DE APAGAR PERGUNTAS SEM RESPOSTA 

O sistema deve excluir perguntas sem respostas após determinado prazo para evitar o acúmulo de informações sem utilidade no banco de dados. 

# SUPORTABILIDADE

- Consistência ferramental [(INT1.2)](introspeccao.md)
- Versão mobile [(INT3.11)](introspeccao.md)
- Atualizar automaticamente as plataformas mobile [(BR2.16)](brainstorm.md)
- Inserção de textos LaTeX e símbolos matemáticos [(INT1.7)](introspeccao.md)

O tráfego de dados no Brainly segue as seguintes proporções:

| Navegador | Versão | Qtde usuários |
| :-------: | :----: | :-----------: |
|Google Chrome|	28+ |	60.77% |
|Safari|7+|12.52%|
|Samsung Internet|1.1+|3.99%|

Logo, nota-se que se deve desenvolver a plataforma pensando na compatibilidade dos navegadores em relação ao `javascript` e demais tecnologias _web_ de forma a possibilitar uma utilização flúida especialmente nos navegadores `chrome`, `safari` e `samsung internet`.

## REQUISITO DE CONSISTÊNCIA  FERRAMENTAL

O sistema deve funcionar de forma concistente, respeitando as limitações de cada plataforma. Deve ser possível acessar todas as funcionalidades em todas plataformas.

## REQUISITO DE VERSÃO MOBILE

O sistema deve ser multiplataforma, incluindo versões para dispositivos com tecnologia android e ios para facilitar o acésso da ferramenta para o usuário.

## ATUALIZAR AUTOMATICAMENTE AS PLATAFORMAS MOBILE

As mudanças realizadas no Brainly _web_ devem refletir diretamente nas aplicações _mobile_ através de um `plano de devops` de modo a manter a suportabilidade das funcionalidades da plataforma de maneira dinâmica.

## INSERÇÃO DE TEXTOS LATEX E SÍMBOLOS MATEMÁTICOS

O sistema deve permitir ao usuário inserir texos latex e símbolos matemáticos quando o mesmo adicionar uma pergunta, respota ou comentário para facilitar a compreensão da informação inserida.

# RESTRIÇÕES DE DESIGN
O sistema deve seguir padrões de _design_ na implementação de suas interfaces de forma a garantir a melhor experiência na utilização da plataforma, seja em um dispositivo móvel ou computadores em geral. Tem-se como referência a documentação de _styleguide_ disposta na página na página do aplicativo no github - [styleguide brainly](https://github.com/brainly/style-guide).

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

# REQUISITOS DE LICENCIAMENTO

- Idade mínima para registro na plataforma [(BR2.1)](./brainstorm)
- Não utilizar informações de menores de 16 anos sem autorização [(BR2.7)](./brainstorm)
- Responsabilidade na propagação de dados é do usuário [(BR2.12)](./brainstorm)
- É autorizado o uso de dados do usuário para diversos fins comerciais do Brainly[(BR2.13)](./brainstorm)

Os serviços Brainly tem por objetivo disseminar o conhecimento e incentivar os estudantes no desenvolvimento acadêmico ou escolar; porém, para a utilização dos serviços o usuário deve concordar com os [termos de uso](https://brainly.com/pages/terms_of_use), [política de privacidade](https://brainly.com/pages/privacy_policy) e a [política de cookies]( https://brainly.com/pages/cookie_policy).

# OBSERVAÇÕES LEGAIS, DE COPYRIGHT E OUTRAS
Os usuários do software são responsáveis pelas respostas que fornecem na plataforma. Assim, o Brainly não tem responsabilidade direta pelo conteúdo prestado na plataforma, servindo apenas como intermediário para a armazenamento e processamento de dados. Reserva-se ao Brainly direitos sobre a marca, nome, logotipo, logomarca utilizados na plataforma.

# PADRÕES APLICÁVEIS
ISO 9241-11:1998, Web Content Accessibility Guidelines (WCAG) 2.0, ISO/IEC 25010:2011.