# BACKLOG DO PRODUTO

# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 0.1 | 29/04/2019 | Adiciona introdução, metodologia e define estrutura do backlog | Welison Regis |
| 0.2 | 08/04/2019 | Adiciona os épicos na documentação | Lieverton Silva |
| 0.3 | 08/04/2019 | Adiciona as histórias de usuário | André Pinto, Gustavo Marques, Leonardo Medeiros, Lieverton Silva, Paulo Rocha,  Welison Regis |
| [1.0](modelagem_v1/backlog.md) | 08/04/2019 | Adiciona os critérios de aceitação e gera a primeira versão do _backlog_ | André Pinto, Gustavo Marques, Leonardo Medeiros, Lieverton Silva, Paulo Rocha,  Welison Regis |
| 2.0 | 21/06/2019 | Corrige hyperlinks, erros na documentação, refatora apresentação das USs | Lieverton Silva, Welison Regis |

# INTRODUÇÃO
O atual documento tem por objetivo apresentar os épicos, as histórias de usuário (US) e o _product backlog_ da plataforma Brainly, tendo como foco a modelagem de requisitos sob os aspectos da metodologia ágil com respaldo dos artefatos coletados nas dinâmicas anteriores. O _backlog_ é composto por US's às quais são resolvidas em um período de tempo (sprint) e que pertencem a um contexto maior, no caso os épicos.

## METODOLOGIA
Para desenvolver as histórias de usuário, tomou-se como base as priorizações dos requisitos elencados ([disponíveis aqui](priorizacao.md)), avaliados pela técnica MoSCoW, além dos outros artefatos dispostos nessa página do projeto. Desenvolveu-se as US's com os devidos critérios de aceitação para a história, além de agregá-las a um épico. Ademais, pontuou-se as histórias de acordo com sua dificuldade com base na sequência de Fibonacci e, por fim, criou-se algumas sprints com as US's mais primordiais.

# ÉPICOS

## EP02
### Autenticação

Implementação de mecanismos funcionais que permitem a autenticação do usuário no sistema. Envolve o sistemas de cadastro e login.

## EP03
### Questões

Criar funcionalidades que permita a interação entre os usuário por meio de perguntas e respostas. Inclui os comentários nas questões e divisão das atividades por meio de categorias.

## EP04
### Moderação

Criar mecanismos que possibilitem e facilitem o gerenciamento de condutas impróprias, assim como a possibilidade de usuários denunciá-las.

## EP05
### Perfil

Implementação de mecanismos que possibilitem ao usuário o gerenciamento do próprio perfil. Inclui personalizar conta , visualizar perfil e seguir outros usuário.

## EP06
### Gamificação

Aplicar as técnicas de gamificação citadas no plano de gamificação, assim como implementar funcionalidades próprias de jogos, como sistema de pontuação, ranking e nível.

## EP07
### Multiplataforma

Desenvolver o sistema para plataforma web e para as plataformas mobile android e ios.

# HISTÓRIAS DE USUÁRIO

## US10

| US10 | Login |
|--------:|:-|
| **Épico** | [Autenticação](#ep02) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>fazer o login na plataforma usando minha conta<br/>acessar a plataforma com facilidade. |
| **Priorização:** | M |
| **Pontos:** | 5 |
| **Elicitação:** | [AP1.2](analise_protocolo.md#ap01) |
| **Critérios de aceitação:** | - Implementar autenticação de usuário e senha no banco de dados; <br/>- Implementar sistema de autenticação com facebook;<br/>- Integração do sistema de login com confirmação por email. |


## US11

| US11 | Cadastro com facebook |
|--------:|:-|
| **Épico** | [Autenticação](#ep02) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>fazer o login na plataforma usando minha conta<br/>acessar a plataforma com facilidade. |
| **Priorização:** | M |
| **Pontos:** | 5 |
| **Elicitação:** | [AP1.1](analise_protocolo.md#ap01)  |
| **Critérios de aceitação:** | - Implementar a interface de cadastro com facebook de forma dinâmica, de fácil uso;<br/>- Implementar sistema de cadastro com facebook([AP3.3](analise_protocolo.md#ap03)). |


## US12

| US12 | Termos de uso |
|--------:|:-|
| **Épico** | [Autenticação](#ep02) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Proprietário<br/>que o usuário aceite os termos de uso ao realizar o cadastro na plataforma<br/>resguardar-me perante a legislação em vigor. |
| **Priorização:** | M |
| **Pontos:** | 13 |
| **Elicitação:** | [AP1.13](analise_protocolo.md#ap01)  |
| **Critérios de aceitação:** | - Implementar interface de exibição dos termos de uso;<br/>- Garantir que o usuário só poderá prosseguir no cadastro após aceitar os termos de uso;<br/>- Garantir concessão da autorização para o uso de dados do usuário para diversos fins comerciais do Brainly - [BR2.3](brainstorm.md#tabela-de-requisitos-nao-funcionais). |



## US13

| US13 | Cadastro com email |
|--------:|:-|
| **Épico** | [Autenticação](#ep02) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>cadastrar-me na plataforma ultilizando minha conta de email<br/>acessar novas funcionalidades do sistema. |
| **Priorização:** | M |
| **Pontos:** | 5 |
| **Elicitação:** | [AP1.1](analise_protocolo.md#ap01)  |
| **Critérios de aceitação:** | - Sistema deve fazer a validação do email inserido;<br/>- Implementar sistema de confirmação de email;<br/>-Verificar se o usuário atender à idade mínima para registro na plataforma - [BR2.1](brainstorm.md#tabela-de-requisitos-nao-funcionais);<br/>- Verificar se o usuário possui menos de 16 anos, para classificar as permissões de acesso a suas informações - [BR2.7](brainstorm.md#tabela-de-requisitos-nao-funcionais).|

## US14

| US14 | Recuperar senha |
|--------:|:-|
| **Épico** | [Autenticação](#ep02) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>ter a possibilidade de recuperar minha senha caso a esqueça<br/>continuar utilizando o Brainly sem ter a necessidade de criar uma nova conta ao esquecer a senha. |
| **Priorização:** | M |
| **Pontos:** | 5 |
| **Elicitação:** | [BR1.14](brainstorm.md#tabela-de-requisitos-funcionais)  |
| **Critérios de aceitação:** | - Sistema deve enviar uma mensagem para o email cadastrado, com link para redefinição de senha;<br/>- Link enviado por email deve redirecionar para página de redefinição de senha do referido usuário, está página é responsável por fazer a alteração da senha no banco de dados. |

## US15

| US15 | Cancelar conta |
|--------:|:-|
| **Épico** | [Autenticação](#ep02) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>poder cancelar minha conta<br/>retirar todos os meus dados quando desejar. |
| **Priorização:** | S |
| **Pontos:** | 3 |
| **Elicitação:** | [BR1.16](brainstorm.md#tabela-de-requisitos-funcionais)  |
| **Critérios de aceitação:** | - Deve notificar ao usuário que esta ação é irreversível;<br/>- Deve marcar este usuário como cancelado no banco de dados, mas manter seus dados salvos.|


## US16

| US16 | Responder |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>poder responder uma pergunta<br/>ajudar outros usuários da comunidade. |
| **Priorização:** | M |
| **Pontos:** | 3 |
| **Elicitação:** | [AP1.9](analise_protocolo.md#ap01)  |
| **Critérios de aceitação:** | - Respostas devem ser gravadas permanentemente no banco de dados;<br/>- O sistema deve limitar a quantidade de respostas por tarefa em 2.|

## US17

| US17 | Anexar arquivos |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>anexar arquivos de vários formatos às minhas perguntas<br/>complementar minha pergunta, de modo a facilitar o entendimento dos leitores. |
| **Priorização:** | C |
| **Pontos:** | 3 |
| **Elicitação:** | [INT 1.1](introspeccao.md#int01)  |
| **Critérios de aceitação:** | - O usuário deve ser capaz de anexar arquivos nos formatos: docx, odt, txt, png, jpeg, bmp, pdf e html;<br/>- O tamanho do anexo deve ser limitado a 16MB.|


## US18

| US18 | Compartilhar questões |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>compartilhar as questões da plataforma nas minhas redes sociais<br/>ter maior visibilidade na minha dúvida e poder solicitar ajuda de amigos. |
| **Priorização:** | W |
| **Pontos:** | 3 |
| **Elicitação:** | [INT1.3](introspeccao.md#int01)  |
| **Critérios de aceitação:** | - Usuário deve ser capaz de compartilhar suas tarefas nas redes sociais: Twitter, Facebook e Instagram.|


## US19

| US19 | Categorizar perguntas por matérias |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>categorizar uma pergunta em dada disciplina<br/>filtrar as questões baseado em uma matéria de interesse. |
| **Priorização:** | S |
| **Pontos:** | 5 |
| **Elicitação:** | [API1.5](analise_protocolo.md#ap01)  |
| **Critérios de aceitação:** | - O sistema deverá providenciar as tags necessárias para categorizar as perguntas por área de conhecimento;<br/>- Deve ser possível categorizar uma pergunta em uma das seguintes matérias: Matemática, história, geografia, biologia, português, física, química, filosofia, sociologia, administração, pedagogia, inglês, artes, saúde, educação física, contabilidade, direito, psicologia, informática, lógica, educação moral, espanhol, música, educação técnica ou ENEM.|


## US20

| US20 | Retirar dúvida nos comentários |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>interagir na área de comentários de uma pergunta ou resposta<br/>retirar eventuais dúvidas sobre as perguntas e/ou explicações. |
| **Priorização:** | S |
| **Pontos:** | 3 |
| **Elicitação:** | [INT1.5](introspeccao.md#int01)  |
| **Critérios de aceitação:** | - Para fazer comentário é necessário estar logado no Brainly; - Deve haver um espaço para comentário tanto na pergunta como nas respostas para que os usuários possam tirar dúvidas sobre a questão; - O espaço para comentário deve ter um limite de 400 caracteres.|

## US21

| US21 | Recursos de escrita |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>utilizar os diferentes tipos de formatação de texto<br/>possibilitar uma melhor visualização das minhas respostas. |
| **Priorização:** | C |
| **Pontos:** | 8 |
| **Elicitação:** | [INT1.6](introspeccao.md#int01)  |
| **Critérios de aceitação:** | - A ferramenta de edição de texto deve possibilitar a escrita em: negrito, itálico, sublinhado;<br/>- Deve ser possível ao usuário inserir diferentes tamanhos para títulos ou textos durante a sua resposta ou pergunta.|

## US22

| US22 | Inserção de fórmulas matemáticas |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>inserir fórmulas matemáticas nas respostas<br/>possibilitar uma melhor visualização das minhas respostas. |
| **Priorização:** | C |
| **Pontos:** | 8 |
| **Elicitação:** | [INT1.7](introspeccao.md#int01)  |
| **Critérios de aceitação:** | - A ferramenta de edição de texto deve possibilitar a inserção de códigos LaTeX para facilitar o desenvolvimento de questões que necessitem de excessivas expressões matemáticas;<br/>- A ferramenta LaTeX deve ser consistente entre as plataformas do sistema Brainly.|

## US23

| US23 | Highlight de texto |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>destacar certas informações do meu texto<br/>possibilitar uma melhor visualização das minhas respostas. |
| **Priorização:** | C |
| **Pontos:** | 5 |
| **Elicitação:** | [INT1.8](introspeccao.md#int01) |
| **Critérios de aceitação:** | - O sistema deve oferecer recurso para destacar partes do texto, como por exemplo, ocorre em citações em arquivos markdown;<br/>- A implementação do highlight deve observar as restrições de design. ([restrições](https://github.com/brainly/style-guide))|

## US24

| US24 | Limite na quantidade de respostas |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Desenvolvedor<br/>limitar a quantidade de respostas que podem ser fornecidas em uma questão<br/>manter a sustentabilidade da quantidade de dados no banco de dados, além de diminuir redundâncias em respostas. |
| **Priorização:** | C |
| **Pontos:** | 1 |
| **Elicitação:** | [EN2.3](entrevista.md#en02) |
| **Critérios de aceitação:** | - O sistema deve aceitar apenas duas respostas por questão;<br/>- Apenas duas pessoas podem estar respondendo simultaneamente uma pergunta.|

## US25

| US25 | Visualizar perguntas e respondê-las |
|--------:|:-|
| **Épico** | [Questões](#ep03) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>ter livre acesso as perguntas, assim como suas respostas<br/>respondê-las ou visualizá-las. |
| **Priorização:** | M |
| **Pontos:** | 3 |
| **Elicitação:** | [AP1.3](analise_protocolo.md#ap01) |
| **Critérios de aceitação:** | - As perguntas devem ser exibidas no feed principal da plataforma, para que todos os usuários as vejam e possam respondê-las;<br/>- Qualquer usuário deve ter permissão para ler qualquer pergunta.|

## US26

| US26 | Advertências no perfil |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>ver as advertências de um usuário na página de seu perfil<br/>identificar mais facilmente os infratores reincidentes. |
| **Priorização:** | C |
| **Pontos:** | 3 |
| **Elicitação:** | [INT2.2](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Os moderadores devem poder ver no perfil do usuário a quantidade de advertências que o mesmo recebeu;<br/>- Usuários comuns não devem ter acesso a este dado no perfil de outros usuários;<br/>- Um usuário pode ver a quantidade de advertências que já recebeu, em seu próprio perfil.|

## US27

| US27 | Categoria de denúncias |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>visualizar as denúncias separadas por categorias<br/>filtrar as denúncias e escolhe-las para realizar a moderação. |
| **Priorização:** | C |
| **Pontos:** | 3 |
| **Elicitação:** | [INT2.3](introspeccao.md#int02) |
| **Critérios de aceitação:** | - O sistema deverá providenciar categorização das denúncias por tipo;<br/>- As denúncias devem ser categorizadas nos seguintes tipos: Links, Pergunta não apropriada, Conteúdo ofensivo, Matéria incorreta, Publicidade e Pergunta contém dados pessoais.|


## US28

| US28 | Filtragem de denúncias |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>filtrar as denúncias por categorias<br/>ter mais facilidade ao gerenciar as denúncias recorrentes de infrações na plataforma. |
| **Priorização:** | C |
| **Pontos:** | 5 |
| **Elicitação:** | [INT2.4](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Ao acessar o Painel de denúncias os moderadores devem ter opção de filtrá-las pelas categorias;<br/>- O filtro ter capacidade para abranger uma ou mais categorias.|

## US29

| US29 | Denunciar por modalidade |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>denunciar as irregularedades que encontrar, de acordo com o tipo da mesma<br/>facilitar o trabalho da moderação em verificar esta denúncia. |
| **Priorização:** | C |
| **Pontos:** | 3 |
| **Elicitação:** | [INT2.5](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Ao realizar uma denuncia o usuário deve ser obrigado indicar a qual tipo de infração ela corresponde;<br/>- Esta informação deverá ser enviada aos moderadores.|

## US30

| US30 | Denúncias automáticas |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Administrador<br/>que a plataforma realize denúncias automáticas<br/>detectar mais infrações e acelerar o processo de moderação. |
| **Priorização:** | W |
| **Pontos:** | 13 |
| **Elicitação:** | [INT 2.6](introspeccao.md#int02) |
| **Critérios de aceitação:** | - O sistema deve detectar automaticamente perguntas suspeitas, com base em palavras ofensivas e excesso de links, e enviá-las para moderação;<br/>- A base de palavras ofensivas deve ser constantemente atualizada, para aumentar a efetividade do sistema.|

## US31

| US31 | Níveis entre moderadores |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Administrador<br/>que a plataforma designasse níveis diferentes aos moderadores<br/>ter uma maior confiabilidade nos moderadores na realização de determinadas tarefas de moderação. |
| **Priorização:** | W |
| **Pontos:** | 5 |
| **Elicitação:** | [INT 2.8](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Os moderadores devem ser divididos em níveis baseados em sua pontuação e tempo como moderador;<br/>- Moderadores de níveis mais altos devem possuir poder de moderação sobre moderadores de níveis mais baixos;<br/>- Deve haver uma forma de limitar algumas ações apenas para os níveis mais altos de moderação.|

## US32

| US32 | Comunicação entre moderadores |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>ter um canal de comunicação com outros moderadores e a administração<br/>tirar dúvidas  à respeito do sistema ou ações de usuários. |
| **Priorização:** | C |
| **Pontos:** | 13 |
| **Elicitação:** | [INT2.11](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Deve haver um canal de comunicação exclusivo para moderadores;<br/>- Usuários comuns não devem ter acesso a este canal;<br/>- Administradores devem ter acesso a este canal.|

## US33

| US33 | Raking de moderadores |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Administrador<br/>que os moderadores possam visualizar um ranking de ações realizadas por moderadores<br/>para estimular a competição entre eles. |
| **Priorização:** | C |
| **Pontos:** | 5 |
| **Elicitação:** | [INT2.12](introspeccao.md#int02) |
| **Critérios de aceitação:** | - O sistema de ranking deve ser baseado apenas nas pontuações de moderação dos moderadores;<br/>- Deve haver um ranking diário;<br/>- Deve haver um ranking semanal;<br/>- Deve haver um ranking mensal;<br/>- Em cada ranking deverá ter uma lista como até 10 usuários;<br/>Estes rankings não devem ser visíveis para usuários comuns.|

## US34

| US34 | Painel de denúncias |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>ter um painel central de denúncias<br/>analizar as denúncias realizadas. |
| **Priorização:** | S |
| **Pontos:** | 5 |
| **Elicitação:** | [INT2.13](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Este painel deve ser visível apenas para moderadores e administradores;<br/>- Este painel deve suportar a divisão em categorias e buscas com filtragem;<br/>- Este painel deve estar preparado para suportar grandes quantidades de denúncias.|

## US35

| US37 | Apagar conteúdo |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>apagar conteúdo impróprio ou indevido<br/>para que questões, comentários ou respostas não possam ser vistas por mais usuários. |
| **Priorização:** | M |
| **Pontos:** | 2 |
| **Elicitação:** | [INT2.14](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Deve haver opção para moderadores e administradores possam apagar conteúdos impróprios ou indevidos;<br/> - Usuário que teve conteúdo apagado deve ser notificado e receber advertência;<br/> - Conteúdo apagado deve permanecer no banco de dados, mas não ser visível para usuários comuns. |

## US36

| US36 | Exclusão de contas e banimento de usuários |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>dispor de ferramentas que permitam a exclusão de contas e o banimento de usuários<br/>controlar as ações de usuários infratores e puni-los. |
| **Priorização:** | M |
| **Pontos:** | 5 |
| **Elicitação:** | [INT2.15](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Deve haver indicadores que auxilie o moderador a tomar uma decisão de banir um usuário;<br/> - O moderador deve poder banir um usuário;<br/> - Quando um usuário é banido sua conta deve ser excluída;<br/>Um usuário banido não deve poder criar outra conta. |

## US37

| US37 | Correção de atividades |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>liberar para edição uma pergunta ou resposta que foi denunciada como incorreta<br/>possibilitar ao usuário a edição dos erros cometidos na questão. |
| **Priorização:** | S |
| **Pontos:** | 3 |
| **Elicitação:** | [INT2.16](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Deve ser possível ao moderador enviar uma notificação para um usuário editar uma determinada tarefa;<br/> - O usuário que receber uma notificação de editar tarefa deve poder editar a tarefa denunciada. | 

## US38

| US38 | Denúncia feita incorretamente |
|--------:|:-|
| **Épico** | [Moderação](#ep04) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>aprovar uma tarefa, marcando que suas denúncias foram feitas incorretamente<br/>controlar as denúncias indevidas e manter as tarefas coerentes. |
| **Priorização:** | S |
| **Pontos:** | 3 |
| **Elicitação:** | [INT2.17](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Deverá ser com computado para o usuário que efetuou a denúncia errada;<br/> - Deve ser possível ao moderador aprovar uma tarefa. |

## US39

| US39 | Logout em conta |
|--------:|:-|
| **Épico** | [Perfil](#ep05) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>poder realizar logout de minha conta<br/>avisar aos meus amigos que estou offline. |
| **Priorização:** | C |
| **Pontos:** | 1 |
| **Elicitação:** | [AP1.12](analise_protocolo.md#ap01) |
| **Critérios de aceitação:** | - Usuário deve ser capaz de sair da sua conta, encerrando sua sessão;<br/> - Amigos devem ser notificados que usuário saiu. |

## US40

| US40 | Seguir usuário |
|--------:|:-|
| **Épico** | [Perfil](#ep05) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>seguir outro usuário<br/>receber notificações das atividades desse usuário. |
| **Priorização:** | C |
| **Pontos:** | 5 |
| **Elicitação:** | [EN2.2](entrevista.md#en02) |
| **Critérios de aceitação:** | - Ao seguir um usuário, o mesmo deverá ser notificado que ganhou um seguidor;<br/> - Usuário deve ser notificado quando um usuário que ele segue adiciona uma nova pergunta ou resposta;<br/> - Usuários que foram seguidos deve estar salvo no banco de dados, permanecendo salvo mesmo quando a sessão é encerrada. |

## US41

| US41 | Gerenciar e personalizar conta |
|--------:|:-|
| **Épico** | [Perfil](#ep05) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>poder visualizar, personalizar, gerenciar minha conta, perfil e informações<br/>mostrar ao outros usuários as informações que eu desejar. |
| **Priorização:** | S |
| **Pontos:** | 8 |
| **Elicitação:** | [BR1.13](brainstorm.md#tabela-de-requisitos-funcionais) |
| **Critérios de aceitação:** | - Usuário deve ser capaz de gerir quais informações deseja exibir em seu perfil. |

## US42

| US42 | Feed de contribuições |
|--------:|:-|
| **Épico** | [Perfil](#ep05) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>visualizar meu feed de contribuições feitas para a plataforma<br/>ver as perguntas e respostas na minha região e idioma. |
| **Priorização:** | C |
| **Pontos:** | 5 |
| **Elicitação:** | [INT1.4](introspeccao.md#int01) |
| **Critérios de aceitação:** | - No perfil de um usuário deve ser exibido o registro das atividades realizadas pelo mesmo;<br/>ter o registro de atividades que realizei no site, facilitando um possível acesso futuro. |

## US43

| US43 | Alterar a região do sistema |
|--------:|:-|
| **Épico** | [Perfil](#ep05) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>poder alterar a região do meu usuário no Brainly<br/>ver as perguntas e respostas na minha região e idioma. |
| **Priorização:** | W |
| **Pontos:** | 2 |
| **Elicitação:** | [BR1.25](brainstorm.md#tabela-de-requisitos-funcionais) |
| **Critérios de aceitação:** | - Usuário deve ser capaz de alterar a região e língua cadastradas no sistema;<br/>Alteração deve ser salva no banco de dados e permanecer mesmo que a sessão seja encerrada. |

## US44

| US44 | Subir de nível |
|--------:|:-|
| **Épico** | [Gamificação](#ep06) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>subir de nível<br/>sentir mais interesse em ajudar na plataforma. |
| **Priorização:** | M |
| **Pontos:** | 3 |
| **Elicitação:** | [EN2.5](entrevista.md#en02) |
| **Critérios de aceitação:** | - Para subir de nível usuário deve ter pontos e melhores respostas suficientes;<br/>- Usuário deve ter acesso à informação de quantos pontos são necessários para avançar os níveis;<br/>Usuário deve ser notificado quando subir de nível. |

## US45

| US45 | Ranking de usuárioinformar o usuário a realização de tarefas e pontuação |
|--------:|:-|
| **Épico** | [Gamificação](#ep06) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>ver um ranking com os melhores usuários<br/>saber quem são os melhores usuários em termos de respostas. |
| **Priorização:** | M |
| **Pontos:** | 8 |
| **Elicitação:** | [EN2.6](entrevista.md#en02) |
| **Critérios de aceitação:** | - O sistema de ranking deve ser baseado apenas nas pontuações do usuário;<br/>- Deve haver um ranking diário;<br/>Deve haver um ranking semanal;<br/>Deve haver um ranking mensal;<br/>Em cada ranking deverá ter uma lista como até 10 usuários. |

## US46

| US46 | informar o usuário a realização de tarefas e pontuação |
|--------:|:-|
| **Épico** | [Gamificação](#ep06) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>ser notificado, com os pontos que ganhei, quando realizar uma tarefa<br/>saber quando terminei uma tarefa e quantos pontos ganhei, tendo mais controle de minhas ações em relação as tarefas. |
| **Priorização:** | M |
| **Pontos:** | 2 |
| **Elicitação:** | [AP1.6](analise_protocolo.md#ap01) |
| **Critérios de aceitação:** | - O usuário deve receber uma notificação ao cumprir uma tarefa;<br/>- O usuário deve receber uma notificação contendo a quantidade de pontos ganha. |

## US47

| US47 | Feedback em respostas |
|--------:|:-|
| **Épico** | [Gamificação](#ep06) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>poder dar um feedback (em formas de curtir, melhor respostas e avaliar a qualidade) nas respostas<br/>demonstrar se fui ou não ajudado, monstrando a quem respondeu e a possíveis leitores. |
| **Priorização:** | M |
| **Pontos:** | 8 |
| **Elicitação:** | [AP3.2](analise_protocolo.md#ap03) |
| **Critérios de aceitação:** | - Os usuários não deverão poder favoritar as próprias respostas;<br/>- Deve ser possível ao usuário favoritar uma resposta clicando em um ícone em forma de coração;<br/>Deve ser possível ao usuário que fez a pergunta escolher a melhor resposta;<br/>Deve ser possível dar uma nota para uma resposta (de 0 a 5 estrelas). |

## US48

| US48 | Possibilidade de se tornar moderador |
|--------:|:-|
| **Épico** | [Gamificação](#ep06) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário<br/>ter a possibilidade de me tornar moderador<br/>melhor contribuir com o Brainly. |
| **Priorização:** | S |
| **Pontos:** | 5 |
| **Elicitação:** | [BR1.17](brainstorm.md#tabela-de-requisitos-funcionais) |
| **Critérios de aceitação:** | - O sistema deve enviar, para bons usuários, convite para se tornar moderador - [INT2.7](introspeccao.md#int02);<br/>- Os usuários devem poder recusar convite para se tornar moderador. |

## US49

| US49 | Moderação multi Plataforma |
|--------:|:-|
| **Épico** | [Multiplataforma](#ep07) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Moderador<br/>realizar atividades de moderação em diversas plataformas diferentes<br/>ter maior flexibilidade no acesso e realização da moderação. |
| **Priorização:** | S |
| **Pontos:** | 13 |
| **Elicitação:** | [INT2.1](introspeccao.md#int02) |
| **Critérios de aceitação:** | - Deve estar implementado para ios;<br/>- Deve ser implementado para android;<br/>- Deve estar implementado para ios;<br/>- Deve ser implementado para web. |

## US50

| US50 | Multiplataforma |
|--------:|:-|
| **Épico** | [Multiplataforma](#ep07) |
|  **Eu, como:**<br/>**Desejo:**<br/>**Para que eu possa:** | Usuário <br/>que a plataforma esteja disponivel para diferentes sistemas<br/>acessar à plataforma pelos meus diferentes dispositivos. |
| **Priorização:** | S |
| **Pontos:** | 21 |
| **Elicitação:** | [EN2.1](entrevista.md#en02) |
| **Critérios de aceitação:** | - A ferramenta que possibilita respostas deve ser consistente entre as plataformas - [INT1.2](introspeccao.md#int01);<br/>- O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados - [INT3.11](introspeccao.md#int03);<br/>- Deve estar implementado para ios;<br/>- Deve ser implementado para android;<br/>- Deve ser implementado para web. |

</br>

# REFERÊNCIAS

**[1]** SERRANO, Maurício; SERRANO, Milene. **Requisitos - Aula 17. 1º/2019**. Material apresentado para a disciplina de Requisitos de Software no curso de Engenharia de Software da UnB, FGA.