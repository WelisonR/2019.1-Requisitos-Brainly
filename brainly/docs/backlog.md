# BACKLOG DO PRODUTO

# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 0.1 | 29/04/2019 | Adiciona introdução, metodologia e define estrutura do backlog | Welison Regis |
| 0.2 | 08/04/2019 | Adiciona os épicos na documentação | Lieverton Silva |
| 0.3 | 08/04/2019 | Adiciona as histórias de usuário | André Pinto, Gustavo Marques, Leonardo Medeiros, Lieverton Silva, Paulo Rocha,  Welison Regis |
| 1.0 | 08/04/2019 | Adiciona os critérios de aceitação e gera a primeira versão do _backlog_ | André Pinto, Gustavo Marques, Leonardo Medeiros, Lieverton Silva, Paulo Rocha,  Welison Regis |

# INTRODUÇÃO
O atual documento tem por objetivo apresentar os épicos, as histórias de usuário (US) e o _product backlog_ da plataforma Brainly, tendo como foco a modelagem de requisitos sob os aspectos da metodologia ágil com respaldo dos artefatos coletados nas dinâmicas anteriores. O _backlog_ é composto por US's às quais são resolvidas em um período de tempo (sprint) e que pertencem a um contexto maior, no caso os épicos.

## METODOLOGIA
Para desenvolver as histórias de usuário, tomou-se como base as priorizações dos requisitos elencados ([disponíveis aqui](priorizacao.md)), avaliados pela técnica MoSCoW, além dos outros artefatos dispostos nessa página do projeto. Desenvolveu-se as US's com os devidos critérios de aceitação para a história, além de agregá-las a um épico. Ademais, pontuou-se as histórias de acordo com sua dificuldade com base na sequência de Fibonacci e, por fim, criou-se algumas sprints com as US's mais primordiais.

# ÉPICOS

## EP01 - Documentação

Documentação necessária para o desenvolvimento do projeto, que servirão como base para equipe de desenvolvimento e como guia para para manter a equipe alinhada. Inclui documento de visão, documento de arquitetura, elicitação de requisitos, além de toda documentação necessária para especificar o projeto.

## EP02 - Autenticação

Implementação de mecanismos funcionais que permitem a autenticação do usuário no sistema. Envolve o sistemas de cadastro e login.

## EP03 - Questões

Criar funcionalidades que permita a interação entre os usuário por meio de perguntas e respostas. Inclui os comentários nas questões e divisão das atividades por meio de categorias.

## EP04 - Moderação

Criar mecanismos que possibilitem e facilitem o gerenciamento de condutas impróprias, assim como a possibilidade de usuários denunciá-las.

## EP05 - Perfil

Implementação de mecanismos que possibilitem ao usuário o gerenciamento do próprio perfil. Inclui personalizar conta , visualizar perfil e seguir outros usuário.

## EP06 - Gamificação

Aplicar as técnicas de gamificação citadas no plano de gamificação, assim como implementar funcionalidades próprias de jogos, como sistema de pontuação, ranking e nível.

## EP07 - Multiplataforma

Desenvolver o sistema para plataforma web e para as plataformas mobile android e ios.

# HISTÓRIAS DE USUÁRIO


| **ID**   | **Épico**           | **Nome**                                                   | **Eu, como**         | **desejo**                                                                                            | **para que eu possa**                                                                                                   | **Priorização** | **Pontos** | **Elicitação** |
|:-----|:----------------|:-------------------------------------------------------|:-----------------|:--------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:------------|:-------|:-----------|
| **US01** | Documentação    | Plano de comunicação                                   | membro da equipe | elaborar um plano de comunicação                                                                  | denfinir os canais de comunicação da equipe e formalizar em forma de documento                                      | M           | 5      | -          |
| **US02** | Documentação    | Plano de elicitação                                    | membro da equipe | montar um plano de elicitação                                                                     | definir as técnicas que serão utilizadas para levantar requisitos                                                   | M           | 5      | -          |
| **US03** | Documentação    | Documento de visão                                     | membro da equipe | elaborar o documento de visão                                                                     | disponibilizar a visão do projeto, para que os interessados possam entender o propósito do projeto                  | M           | 5      | -          |
| **US04** | Documentação    | Documento de arquitetura                               | desenvolvedor    | elaborar o documento de arquitetura                                                               | compartilhar com os membros da equipe a arquitetura do projeto                                                      | M           | 8      | -          |
| **US05** | Documentação    | Estrutura analítica de projeto(EAP)                    | membro da equipe | elaborar EAP do projeto                                                                           | identificar elementos terminais (os produtos, serviços e resultados a serem feitos em um projeto).                  | M           | 5      | -          |
| **US06** | Documentação    | Documento de Especificação Suplementar                 | membro da equipe | elaborar Documento de Especificação Suplementar                                                   | é detalhar todos os aspectos não abordados diretamente nos documentos de visão, caso de uso ou arquitetura.         | S           | 5      | -          |
| **US07** | Documentação    | Plano de gamificação                                   | membro da equipe | elaborar o plano de gamificação                                                                   | definir as técnicas de gamificação a serem implantadas no projeto                                                   | M           | 8      | -          |
| **US08** | Documentação    | Protótipo de baixo nível                               | membro da equipe | fazer o protótipo de baixo nível                                                                  | validar com a equipe as idéias propostas                                                                            | M           | 5      | -          |
| **US09** | Documentação    | Protótipo de alta fidelidade                           | membro da equipe | fazer o protótipo de alta fidelidade                                                              | validar o projeto com os usuários ou cliente                                                                        | C           | 13     | -          |
| **US10** | Autenticação    | Login                                                  | usuário          | fazer o login na plataforma usando minha conta                                                    | acessar a plataforma com facilidade                                                                                 | M           | 5      | AP1.2      |
| **US11** | Autenticação    | Cadastro com facebook                                  | usuário          | cadastrar-me na plataforma ultilizando minha conta do facebook                                    | realizar o cadastro de maneira rápida                                                                               | M           | 5      | AP1.1      |
| **US12** | Autenticação    | Termos de uso                                          | proprietário     | que o usuário aceite os termos de uso ao realizar o cadastro na plataforma                        | resguardar-me perante a legislação em vigor                                                                         | M           | 13     | AP1.13     |
| **US13** | Autenticação    | Cadastro com email                                     | usuário          | cadastrar-me na plataforma ultilizando minha conta de email                                       | acessar novas funcionalidades do sistema                                                                            | M           | 5      | AP1.1      |
| **US14** | Autenticação    | Recuperar senha                                        | usuário          | ter a possibilidade de recuperar minha senha caso a esqueça                                       | continuar utilizando o Brainly sem ter a necessidade de criar uma nova conta ao esquecer a senha                    | M           | 5      | BR1.14     |
| **US15** | Autenticação    | Cancelar Conta                                         | usuário          | poder cancelar minha conta                                                                        | retirar todos os meus dados quando desejar                                                                          | S           | 3      | BR1.16     |
| **US16** | Questões        | Responder                                              | usuário          | poder responder uma pergunta                                                                      | ajudar outros usuários da comunidade                                                                                | M           | 3      | AP1.9      |
| **US17** | Questões        | Anexar arquivos                                        | usuário          | anexar arquivos de vários formatos às minhas perguntas                                            | complementar minha pergunta, de modo a facilitar o entendimento dos leitores                                        | C           | 3      | INT 1.1    |
| **US18** | Questões        | Compartilhar questões                                  | usuário          | compartilhar as questões da plataforma nas minhas redes sociais                                   | ter maior visibilidade na minha dúvida e poder solicitar ajuda de amigos                                            | W           | 3      | INT1.3     |
| **US19** | Questões        | Categorizar perguntas por matérias                     | usuário          | categorizar uma pergunta em dada disciplina                                                       | filtrar as questões baseado em uma matéria de interesse                                                             | S           | 5      | API1.5     |
| **US20** | Questões        | Retirar dúvida nos comentários                         | usuário          | interagir na área de comentários de uma pergunta ou resposta                                      | retirar eventuais dúvidas sobre as perguntas e/ou explicações                                                       | S           | 3      | INT1.5     |
| **US21** | Questões        | Recursos de escrita                                    | usuário          | utilizar os diferentes tipos de formatação de texto                                               | possibilitar uma melhor visualização das minhas respostas.                                                          | C           | 8      | INT1.6     |
| **US22** | Questões        | Inserção de fórmulas matemáticas                       | usuário          | inserir fórmulas matemáticas nas respostas.                                                       | possibilitar uma melhor visualização das minhas respostas.                                                          | C           | 8      | INT1.7     |
| **US23** | Questões        | Highlight de texto                                     | usuário          | destacar certas informações do meu texto                                                          | possibilitar uma melhor visualização das minhas respostas.                                                          | C           | 5      | INT1.8     |
| **US24** | Questões        | Limite na quantidade de respostas                      | desenvolvedor    | limitar a quantidade de respostas que podem ser fornecidas em uma questão                         | manter a sustentabilidade da quantidade de dados no banco de dados, além de diminuir redundâncias em respostas      | C           | 1      | EN2.3      |
| **US25** | Questões        | Visualizar perguntas e respondê-las                    | usuário          | ter livre acesso as perguntas, assim como suas respostas                                          | respondê-las ou visualizá-las                                                                                       | M           | 3      | AP1.3      |
| **US26** | Moderação       | Advertências no perfil                                 | moderador        | ver as advertências de um usuário na página de seu perfil                                         | identificar mais facilmente os infratores reincidentes                                                              | C           | 3      | INT2.2     |
| **US27** | Moderação       | Categoria de denúncias                                 | moderador        | visualizar as denúncias separadas por categorias                                                  | filtrar as denúncias e escolhe-las para realizar a moderação.                                                       | C           | 3      | INT2.3     |
| **US28** | Moderação       | Filtragem de denúncias                                 | moderador        | filtrar as denúncias por categorias                                                               | ter mais facilidade ao gerenciar as denúncias recorrentes de infrações na plataforma                                | C           | 5      | INT2.4     |
| **US29** | Moderação       | Denunciar por modalidade                               | usuário          | denunciar as irregularedades que encontrar, de acordo com o tipo da mesma                         | facilitar o trabalho da moderação em verificar esta denúncia                                                        | C           | 3      | INT2.5     |
| **US30** | Moderação       | Denúncias automaticas                                  | administrador    | que a plataforma realize denúncias automáticas                                                    | detectar mais infrações e acelerar o processo de moderação                                                          | W           | 13     | INT 2.6    |
| **US31** | Moderação       | Níveis entre moderadores                               | administrador    | que a plataforma designasse níveis diferentes aos moderadores.                                    | ter uma maior confiabilidade nos moderadores na realização de determinadas tarefas de moderação                     | W           | 5      | INT 2.8    |
| **US32** | Moderação       | Comunicação entre moderadores                          | moderador        | ter um canal de comunicação com outros moderadores e a administração                              | tirar dúvidas  à respeito do sistema ou ações de usuários                                                           | C           | 13     | INT2.11    |
| **US33** | Moderação       | Raking de moderadores                                  | administrador    | que os moderadores possam visualizar um ranking de ações realizadas por moderadores               | para estimular a competição entre eles                                                                              | C           | 5      | INT2.12    |
| **US34** | Moderação       | Painel de denúncias                                    | moderador        | ter um painel central de denuncias                                                                | analizar as denúncias realizadas                                                                                    | S           | 5      | INT2.13    |
| **US35** | Moderação       | Apagar conteúdo                                        | moderador        | apagar conteúdo impróprio ou indevido                                                             | para que questões, comentários ou respostas não possam ser vistas por mais usuários                                 | M           | 2      | INT2.14    |
| **US36** | Moderação       | Exclusão de contas e banimento de usuários             | moderador        | dispor de ferramentas que permitam a exclusão de contas e o banimento de usuários                 | controlar as ações de usuários infratores e puni-los                                                                | M           | 5      | INT2.15    |
| **US37** | Moderação       | Correção de atividades                                 | Moderador        | liberar para edição uma pergunta ou resposta que foi denunciada como incorreta                    | possibilitar ao usuário a edição dos erros cometidos na questão                                                     | S           | 3      | INT2.16    |
| **US38** | Moderação       | Denúncia feita incorretamente                          | Moderador        | aprovar uma tarefa, marcando que suas denúncias foram feitas incorretamente                       | controlar as denuncias indevidas e manter as tarefas coerentes                                                      | S           | 3      | INT2.17    |
| **US39** | Perfil          | Logout em conta                                        | usuário          | poder realizar logout de minha conta                                                              | avisar aos meus amigos que estou offline                                                                            | C           | 1      | AP1.12     |
| **US40** | Perfil          | Seguir usuário                                         | usuário          | seguir outro usuário                                                                              | receber notificações das atividades desse usuário                                                                   | C           | 5      | EN2.2      |
| **US41** | Perfil          | Gerenciar e personalizar conta                         | usuário          | poder visualizar, personalizar, gerenciar minha conta, perfil e informações                       | mostrar ao outros usuários as informações que eu desejar                                                            | S           | 8      | BR1.13     |
| **US42** | Perfil          | Feed de contribuições                                  | usuário          | visualizar meu feed de contribuições feitas para a plataforma                                     | ter o registro de atividades que realizei no site, facilitando um possível acesso futuro.                           | C           | 5      | INT1.4     |
| **US43** | Perfil          | Alterar a região do sistema                            | usuário          | poder alterar a região do meu usuário no Brainly                                                  | ver as perguntas e respostas na minha região e idioma                                                               | W           | 2      | BR1.25     |
| **US44** | Gamificação     | Subir de nível                                         | usuário          | subir de nível                                                                                    | sentir mais interesse em ajudar na plataforma                                                                       | M           | 3      | EN2.5      |
| **US45** | Gamificação     | Ranking de usuário                                     | usuário          | ver um ranking com os melhores usuários                                                           | saber quem são os melhores usuários em termos de respostas                                                          | M           | 8      | EN2.6      |
| **US46** | Gamificação     | Informar o usuário a realização de tarefas e pontuação | usuário          | ser notificado, com os pontos que ganhei, quando realizar uma tarefa                              | saber quando terminei uma tarefa e quantos pontos ganhei, tendo mais controle de minhas ações em relação as tarefas | M           | 2      | AP1.6      |
| **US47** | Gamificação     | Feedback em respostas                                  | usuário          | poder dar um feedback (em formas de curtir, melhor respostas e avaliar a qualidade) nas respostas | demonstrar se fui ou não ajudado, monstrando a quem respondeu e a possíveis leitores                                | M           | 8      | AP3.2      |
| **US48** | Gamificação     | Possibilidade de se tornar moderador                   | usuário          | ter a possibilidade de me tornar moderador                                                        | melhor contribuir com o Brainly                                                                                     | S           | 5      | BR1.17     |
| **US49** | Multiplataforma | Moderação multi Plataforma                             | Moderador        | realizar atividades de moderação em diversas plataformas diferentes                               | ter maior flexibilidade no acesso e realização da moderação.                                                        | S           | 13     | INT2.1     |
| **US50** | Multiplataforma | Multiplataforma                                        | Usuário          | que a plataforma esteja disponivel para diferentes sistemas                                       | acessar à plataforma pelos meus diferentes dispositivos                                                             | S           | 21     | EN2.1      |

# CRITÉRIOS DE ACEITAÇÃO

## US01 - Plano de comunicação

* Conter os canais de comunicação e a especificação como cada um será utilizado.

## US02 - Plano de elicitação

* Conter técnicas a serem aplicadas e justificativas.

## US03 - Documento de visão

* Deve haver uma tabela com as versões do documento;
* Deve apresentar o escopo do projeto;
* Revisão constante do documento por toda equipe do projeto.

## US04 - Documento de arquitetura

* Deve haver uma tabela com as versões do documento;
* Deve conter um diagrama que representa visualmente as camadas da arquitetura;
* Deve haver um texto explicativo sobre todas as camadas da arquitetura;
* Deve conter diagramas de casos de uso para todas as cenas;
* Devem ser apresentadas as plataformas que serão usadas como suporte no desenvolvimento;
* Revisão constante do documento pelo membros da equipe responsáveis pela arquitetura do projeto.


## US05 - EAP

* Todas as entregas do escopo do projeto previstas;
* Divisão do projeto em fases.

## US06 - Especificação suplementar

* Deve conter as restrições do sistema;
* Deve conter os tópicos de usabilidade;
* Os requisitos citados deverão ser justificados;

## US07 - Plano de gamificação

* Deve conter as técnicas a serem utilizadas e a justificativa para implementação de cada uma.

## US08 - Protótipo de baixo nível

* Deve conter as idéias propostas pela equipe;
* Deve conter todas as partes do projeto.

## US09 - Protótipo de alta fidelidade

* Deve conter os fluxos de uso do sistema;
* Deve ser utilizado uma ferramenta própria para criação de protótipos.

## US10 - Login

* Implementar autenticação de usuário e senha no banco de dados;
* Implementar sistema de autenticação com facebook;
* Integração do sistema de login com confirmação por email.

## US11 - Cadastro com facebook

* Implementar a interface de cadastro com facebook de forma dinâmica, de fácil uso - [AP3.3](analise_protocolo.md)
* Implementar sistema de cadastro com facebook.

## US12 - Termos de uso

* Implementar interface de exibição dos termos de uso.
* Garantir que o usuário só poderá prosseguir no cadastro após aceitar os termos de uso.
* Garantir concessão da autorização para o uso de dados do usuário para diversos fins comerciais do Brainly - [BR2.3](brainstorm.md).


## US13 - Cadastro com email

* Sistema deve fazer a validação do email inserido;
* Implementar sistema de confirmação de email;
* Verificar se o usuário atender à idade mínima para registro na plataforma - [BR2.1](brainstorm.md);
* Verificar se o usuário possui menos de 16 anos, para classificar as permissões de acesso a suas informações - [BR2.7](brainstorm.md).

## US14 - Recuperar senha

* Sistema deve enviar uma mensagem para o email cadastrado, com link para redefinição de senha;
* Link enviado por email deve redirecionar para página de redefinição de senha do referido usuário, está página é responsável por fazer a alteração da senha no banco de dados.

## US15 - Cancelar conta

* Deve notificar ao usuário que esta ação é irreversível;
* Deve marcar este usuário como cancelado no banco de dados, mas manter seus dados salvos.

## US16 - Responder

* Respostas devem ser gravadas permanentemente no banco de dados;
* O sistema deve limitar a quantidade de respostas por tarefa em 2.

## US17 - Anexar arquivos

* O usuário deve ser capaz de anexar arquivos nos formatos: docx, odt, txt, png, jpeg, bmp, pdf e html;
* O tamanho do anexo deve ser limitado a 16MB.

## US18 - Compartilhar questões

* Usuário deve ser capaz de compartilhar suas tarefas nas redes sociais: Twitter, Facebook e Instagram.

## US19 - Categorizar perguntas por matérias

* O sistema deverá providenciar as tags necessárias para categorizar as perguntas por área de conhecimento;
* Deve ser possível categorizar uma pergunta em uma das seguintes matérias: Matemática, história, geografia, biologia, português, física, química, filosofia, sociologia, administração, pedagogia, inglês, artes, saúde, educação física, contabilidade, direito, psicologia, informática, lógica, educação moral, espanhol, música, educação técnica ou ENEM.

## US20 - Tirar dúvidas nos comentários

* Para fazer comentário é necessário estar logado no Brainly;
* Deve haver um espaço para comentário tanto na pergunta como nas respostas para que os usuários possam tirar dúvidas sobre a questão;
* O espaço para comentário deve ter um limite de 400 caracteres.

## US21 - Recursos de escrita

* A ferramenta de edição de texto deve possibilitar a escrita em: negrito, itálico, sublinhado;
* Deve ser possível ao usuário inserir diferentes tamanhos para títulos ou textos durante a sua resposta ou pergunta.

## US22 - Inserção de fórmulas matemáticas

* A ferramenta de edição de texto deve possibilitar a inserção de códigos LaTeX para facilitar o desenvolvimento de questões que necessitem de excessivas expressões matemáticas;
* A ferramenta LaTeX deve ser consistente entre as plataformas do sistema Brainly.

## US23 - Highlight de texto

* O sistema deve oferecer recurso para destacar partes do texto, como por exemplo, ocorre em citações em arquivos markdown;
* A implementação do highlight deve observar as restrições de design. ([restrições](https://github.com/brainly/style-guide))

## US24 - Limite na quantidade de respostas

* O sistema deve aceitar apenas duas respostas por questão;
* Apenas duas pessoas podem estar respondendo simultaneamente uma pergunta.

## US25 - Visualizar perguntas e respondê-las

* As perguntas devem ser exibidas no feed principal da plataforma, para que todos os usuários as vejam e possam respondê-las;
* Qualquer usuário deve ter permissão para ler qualquer pergunta.

## US26 - Advertências no perfil

* Os moderadores devem poder ver no perfil do usuário a quantidade de advertências que o mesmo recebeu;
* Usuários comuns não devem ter acesso a este dado no perfil de outros usuários;
* Um usuário pode ver a quantidade de advertências que já recebeu, em seu próprio perfil.

## US27 - Categoria de denúncias

* O sistema deverá providenciar categorização das denúncias por tipo;
* As denúncias devem ser categorizadas nos seguintes tipos: Links, Pergunta não apropriada, Conteúdo ofensivo, Matéria incorreta, Publicidade e Pergunta contém dados pessoais.

## US28 - Filtragem de denúncias

* Ao acessar o Painel de denúncias os moderadores devem ter opção de filtrá-las pelas categorias;
* O filtro ter capacidade para abranger uma ou mais categorias,

## US29 - Denunciar por modalidade

* Ao realizar uma denuncia o usuário deve ser obrigado indicar a qual tipo de infração ela corresponde;
* Esta informação deverá ser enviada aos moderadores.

## US30 - Denúncias automáticas

* O sistema deve detectar automaticamente perguntas suspeitas, com base em palavras ofensivas e excesso de links, e enviá-las para moderação;
* A base de palavras ofensivas deve ser constantemente atualizada, para aumentar a efetividade do sistema.

## US31 - Níveis entre moderadores

* Os moderadores devem ser divididos em níveis baseados em sua pontuação e tempo como moderador;
* Moderadores de níveis mais altos devem possuir poder de moderação sobre moderadores de níveis mais baixos;
* Deve haver uma forma de limitar algumas ações apenas para os níveis mais altos de moderação.

## US32 - Comunicação entre moderadores

* Deve haver um canal de comunicação exclusivo para moderadores;
* Usuários comuns não devem ter acesso a este canal;
* Administradores devem ter acesso a este canal.

## US33 - Raking de moderadores

* O sistema de ranking deve ser baseado apenas nas pontuações de moderação dos moderadores;
* Deve haver um ranking diário;
* Deve haver um ranking semanal;
* Deve haver um ranking mensal;
* Em cada ranking deverá ter uma lista como até 10 usuários;
* Estes rankings não devem ser visíveis para usuários comuns.

## US34 - Painel de denúncias

* Este painel deve ser visível apenas para moderadores e administradores;
* Este painel deve suportar a divisão em categorias e buscas com filtragem;
* Este painel deve estar preparado para suportar grandes quantidades de denúncias.

## US35 - Apagar conteúdo

* Deve haver opção para moderadores e administradores possam apagar conteúdos impróprios ou indevidos;
* Usuário que teve conteúdo apagado deve ser notificado e receber advertência;
* Conteúdo apagado deve permanecer no banco de dados, mas não ser visível para usuários comuns.


## US36 - Exclusão de contas e banimento de usuários

* Deve haver indicadores que auxilie o moderador a tomar uma decisão de banir um usuário
* O moderador deve poder banir um usuário
* Quando um usuário é banido sua conta deve ser excluída 
* Um usuário banido não deve poder criar outra conta

## US37 - Correção de atividades

* Deve ser possível ao moderador enviar uma notificação para um usuário editar uma determinada tarefa
* O usuário que receber uma notificação de editar tarefa deve poder editar a tarefa denunciada

## US38 - Denúncia feita incorretamente

* Deverá ser com computado para o usuário que efetuou a denúncia errada
* Deve ser possível ao moderador aprovar uma tarefa

##US39 - Logout em conta

* Usuário deve ser capaz de sair da sua conta, encerrando sua sessão;
* Amigos devem ser notificados que usuário saiu.

## US40 - Seguir usuário

* Ao seguir um usuário, o mesmo deverá ser notificado que ganhou um seguidor;
* Usuário deve ser notificado quando um usuário que ele segue adiciona uma nova pergunta ou resposta;
* Usuários que foram seguidos deve estar salvo no banco de dados, permanecendo salvo mesmo quando a sessão é encerrada.

## US41 - Gerenciar e personalizar conta

* Usuário deve ser capaz de gerir quais informações deseja exibir em seu perfil.

## US42 - Feed de contribuições

* No perfil de um usuário deve ser exibido o registro das atividades realizadas pelo mesmo;
* Atividades devem ser separadas em Tarefas adicionadas e Tarefas respondidas.

## US43 - Alterar a região do sistema

* Usuário deve ser capaz de alterar a região e língua cadastradas no sistema;
* Alteração deve ser salva no banco de dados e permanecer mesmo que a sessão seja encerrada.

## US44 - Subir de nível

* Para subir de nível usuário deve ter pontos e melhores respostas suficientes;
* Usuário deve ter acesso à informação de quantos pontos são necessários para avançar os níveis;
* Usuário deve ser notificado quando subir de nível.


## US45 - Ranking de usuário

* O sistema de ranking deve ser baseado apenas nas pontuações do usuário
* Deve haver um ranking diário
* Deve haver um ranking semanal
* Deve haver um ranking mensal
* Em cada ranking deverá ter uma lista como até 10 usuários   


## US46 - informar o usuário a realização de tarefas e pontuação

* O usuário deve receber uma notificação ao cumprir uma tarefa
* O usuário deve receber uma notificação contendo a quantidade de pontos ganha

## US47 - Feedback em respostas

* Os usuários não deverão poder favoritar as próprias respostas
* Deve ser possível ao usuário favoritar uma resposta clicando em um ícone em forma de coração
* Deve ser possível ao usuário que fez a pergunta escolher a melhor resposta
* Deve ser possível dar uma nota para uma resposta (de 0 a 5 estrelas)

## US48 - Possibilidade de se tornar moderador

* O sistema deve enviar, para bons usuários, convite para se tornar moderador - [INT2.7](introspeccao.md)
* Os usuários devem poder recusar convite para se tornar moderador

## US49 - Moderação multiplataforma

* Deve estar implementado para ios
* Deve ser implementado para android
* Deve ser implementado para web

## US50 - Multiplataforma

* A ferramenta que possibilita respostas deve ser consistente entre as plataformas - [INT1.2](priorizacao.md#requisitos_nao_funcionais)
* O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados - [INT3.11](priorizacao.md#requisitos_nao_funcionais)
* Deve estar implementado para ios
* Deve ser implementado para android
* Deve ser implementado para web

</br>

# REFERÊNCIAS

**[1]** SERRANO, Maurício; SERRANO, Milene. **Requisitos - Aula 17. 1º/2019**. Material apresentado para a disciplina de Requisitos de Software no curso de Engenharia de Software da UnB, FGA.