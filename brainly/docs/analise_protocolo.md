#ANÁLISE DE PROTOCOLO

##Versionamento
|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 0.1 | 09/04/2019 | Introdução | Lieverton Santos |
| 0.2 | 09/04/2019 | Análises de protocolo 1 e 2 | Lieverton Santos |
| 0.3 | 09/04/2019 | Análise de protocolo 3 | André Pinto |
| 0.4 | 10/04/ 2019 | Aplicação do MoSCoW nas análises de protocolo 1 e 2 | Lieverton Santos |
| 1.0 | 16/04/2019 | Análise de protocolo 4 | Welison Regis |

##Análise de Protocolo

Consiste em um método que solicita ao usuário a realização de uma tarefa e concorrentemente, em voz alta, a explicação do processo que realiza. A equipe realizou o procedimento com usuários que conheciam a plataforma Brainly e com novos usuários para identificar diferentes pontos de vista.

## AP01
##Análise de Protocolo 1

**Relator**: Pedro Henrique  
**Analisador**: Lieverton Santos

O método foi realizado com um usuário novato, que permitiu que fosse gravado em áudio a experiência com a plataforma. Inicialmente, apenas foi especificado o objetivo do site para não influnciar o usuário.

[link](https://drive.google.com/file/d/1IckFQJgQgHs38VM_-6csSMJ-4uf5fbMT/view) para o áudio.

###Resumo da Narração

O usuário para acessar os serviços do Brainly fez um cadastro a partir do facebook e aceitou os termos de uso. Logo notou que havia perguntas na página inicial e que havia scroll na página. Ele escolheu uma pergunta e viu que era de matemática mas não havia o anexo necessário para responde-la, então ele notou que poderia filtrar as perguntas por matéria. Ao responder uma pergunta ele recebeu um feedback do sistema que continha o ganho de pontos e uma mensagem motivadora. O usuário voltou à página inicial e notou mais algumas opções: rankings, desafios e faça sua pergunta. Ao fazer uma pergunta viu que era necessário escolher uma matéria e o número pontos que ele oferecia pela resposta. Por fim, clicou no perfil e fez o logout.

#### Requisitos Elicitados

| Código | Requisito | Descrição | Prioridade |
| :----: | :-------: | :-------: | :-------: |
| AP1.1 | Cadastro | Registro do usuário no sistema | M |
| AP1.2 | Entrar com facebook | O usuário pode se cadastrar com o facebook | S |
| AP1.3 | Campo com perguntas | O usuário poderá ver perguntas e respondê-las | M |
| AP1.4 | Scroll | A página tem um sistema de rolagem | S |
| AP1.5 | Categorias de perguntas | As perguntas podem ser categorizadas por matéria | S |
| AP1.6 | Feedback do sistema | O sistema deve informar ao usuário realização de tarefas e pontuação | C |
| AP1.7 | Sistema de Rankings | O sistema deve mostrar os usuários com maior pontuação | C |
| AP1.8 | Sistema de Desafios | Deve haver desafios para o usuário com recompensas | W |
| AP1.9 | Tirar dúvidas | O usuário poderá fazer perguntas | M |
| AP1.10 | Pagamento por pergunta | O usuário poderá oferecer uma certa quantidade de pontos para alguém sanar sua dúvida | C |
| AP1.11 | Pefil | O usuário deverá ter um perfil com suas informações | C |
| AP1.12 | Logout | O usuário poderá sair da sua conta | M |
| AP1.13 | Termos de uso | Ao se cadastrar o usuário terá acesso aos termos de uso e para concluir o registro deverá aceitá-lo | M |

Legenda - técnica de priorização:

*   M: **Must have**; S: **Should have**; C: **Could have**; W: **Would have**.

## AP02
##Análise de Protocolo 2

**Relator**: Leonardo Sampaio  
**Analisador**: Lieverton Santos

O método foi realizado com um usuário que já conhecia o aplicativo Brainly, que permitiu que fosse gravado o procedimento em áudio.

[link](https://drive.google.com/file/d/1jOXGGO6JYpKyRU_QSIITH4rBCV2LHqgL/view) para o áudio.

###Resumo da Narração

Inicialmente o usuário pesquisou sobre uma questão de cálculo 1 e logo depois fez uma pergunta. Depois o usuário respondeu uma pergunta e por fim fez outra pesquisa e saiu do aplicativo.

#### Requisitos Elicitados

| Código | Requisito | Descrição | Prioridade |
| :----: | :-------: | :-------: | :-------: |
| AP2.1 | Campo de pesquisa | O usuário pode pesquisar conteúdos para ver se alguma pergunta já respondida pode tirar suas dúvidas | C |
| AP2.2 | Filtro por matéria | O usuário pode escolher matérias específicas para responder questões | S |

Legenda - técnica de priorização:

*   M: **Must have**; S: **Should have**; C: **Could have**; W: **Would have**.

## AP03
##Análise de Protocolo 3

**Relator**: Lais Priscila  
**Analisador**: André Pinto

##Metodologia

Para a execução dessa análise de protocolo foi preciso a ajuda de um usuário que nunca tinha tido contato com o Brainly, porém tivesse algum contato com outras plataformas como Stack Overflow e Yahoo respostas. O analisador não interferiu durante o processo, deixando o usuário livre para explorar as funções da forma que mais lhe agradava. O áudio do processo foi gravado com o consentimento da pessoa.

###Analise do Usuário
[link](https://drive.google.com/drive/folders/1nXl8VUbnya1pisaA3z5I8ODgyufCNtba) para o áudio.
Abaixo, segue as notas da gravação de Lais Priscila

| Atividade | Comentário |
| :--: | ---- |
| Criação de pergunta | O usuário confundiu a pesquisa por pergunta com criação de perguntas na tela inicial |
| Visualização das respostas | O usuário não encontrou nenhuma resposta que solucionava sua dúvida |
| Avaliar resposta | O usuário gostou do sistema de avaliar respostas, podendo dar nota baixa para respostas sem sentido |
| Página principal | O usuário achou coerente a localidade do botão para voltar para a página inicial |
| Cadastro | O usuário preferiu utilizar o email para realizar o cadastro |
| Cadastro | O usuário gostou de ter feito o cadastro de modo pratico |
| Tutorial | O usuário preferiu não ler completamente o tutorial inicial e achou um ruim ter mais do que dois popups de tutorial |

####Requisitos Elicitados

| Código | Requisito | Descrição | Prioridade |
| :----: | :-------: | :-------: | :----: |
| AP3.1 | Funções de pesquisa e criação de perguntas intuitivas | O sistema deve fornecer funções de fácil entendimento, com uma curva de aprendizado baixo e com maior diferenciação em funções parecidas | S |
| AP3.2 | Avaliar respostas | O sistema deve oferecer ao usuário uma forma de ele dar feedback as respostas | M |
| AP3.3 | Cadastro fácil | O cadastro na plataforma deve ocorrer de uma maneira rápida e prática | S |
| AP3.4 | Tutorial | O sistema poderia ter um sistema de tutorial mais rápido com menos passos | W |

Legenda - técnica de priorização:

*   M: **Must have**; S: **Should have**; C: **Could have**; W: **Would have**.

## AP04
##Análise de Protocolo 4

**Relator**: Edinalva Almeida

**Analisador**: Welison Regis

##Metodologia

A análise de protocolo abaixo proposta foi desenvolvida com um usuário que possui razoável conhecimento sobre o uso da _internet_ voltada para _sites_ de auxílio acadêmico e escolar. Na situação, o analisador liberou as ferramentas de moderação e solicitou a pessoa que as utilizasse para realizar algumas tarefas enquanto estava sendo supervisionada. Elencou-se como afazeres na plataforma:
*   Moderar uma atividade irregular na área de matemática.
*   Solicitar correção em uma atividade denunciada.
*   Explorar outros itens no menu de moderador.
O analisador não interveio, apenas observou as ações, deixando a cargo do usuário realizá-las.

O usuário autorizou a divulgação do áudio. [LINK](https://drive.google.com/open?id=1dpkgJa2i8CQVrACUzIMNFwDDLuj0De5g) para o áudio.

###Análise do Usuário
Abaixo, segue as notas da gravação

| Atividade | Comentário |
| :--: | ---- |
| Acesso ao moderar tudo | No primeiro contato o usuário demorou um pouco para encontrar o ícone de moderar tudo (onde fica as denúncias) na tela principal |
| Filtro de denúncias | O usuário considerou importante a capacidade de filtrar (priorizar) os tipos de denúncias |
| Painel de moderação | O usuário ao entrar no painel de moderação ficou pensativo e confuso sobre a quantidade de itens que a tela possui para apresentar |
| Exclusão de itens | O usuário não encontrou problema para justificar e excluir conteúdos |
| Pedido de correção | O usuário não encontrou problema para solicitar pedido de correção |
| Visualizar férias dos moderadores | O usuário acessou tranquilamente o menu de férias |
| Visualizar moderadores | O usuário não encontrou problemas para visualizar outros moderadores |
| Painel de moderação | O usuário ficou confuso com o fato do ícone de moderar mudar de posição na tela do painel de moderação |
| Painel de moderação | A relatora sentiu falta de algum falta de algum campo que tivesse um tutorial de moderação ou que fornecesse dicas |
| Acesso ao fórum | Ao clicar em "fórum" o usuário foi redirecionado ao facebook, o que o desagradou, pois uma página foi aberta encima da outra |

####Requisitos Elicitados

| Código | Requisito | Descrição | Prioridade |
| :----: | :-------: | :-------: | :----: |
| AP4.1 | Filtros de denúncias | O sistema deve implementar filtros de denúncias | M |
| AP4.2 | Tutorial de moderação | O sistema deve disponibilizar tutoriais aos moderadores | S |
| AP4.3 | Suporte a moderação | O sistema deve ter uma área de FAQ para moderadores | C |
| AP4.4 | Design minimalista | A interface de moderação deve ser minimalista | C |
| AP4.5 | Consistência do painel de moderação | A apresentação do painel de moderação deve ser consistente entre telas, não alterando a localização de sua aparição | C |
| AP4.6 | Liberdade de navegação | O moderador deve ter liberdade em sua navegação, não sendo redirecionado a outros sites sem o seu consentimento | C |

Legenda - técnica de priorização:

*   M: **Must have**; S: **Should have**; C: **Could have**; W: **Would have**.

