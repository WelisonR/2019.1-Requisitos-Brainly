# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 1.0 | 21/04/2019 | Gera primeira versão dos artefatos | Grupo |

# administrador

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    administrador   |
|      Noção    |    Funcionário que trabalha no Brainly;</br>Responsável pela gerência de [contas](lexicos10x58ed251.md#perfil) e necessidades da plataforma;</br>Responsável pela orientação do [time de respostas](lexicos10x58ed251.md#time-de-respostas) e dos [universitários](lexicos10x58ed251.md#universitário).</br>Pessoa responsável pela coordenação das atividades de moderação;   |
| Classificação |    sujeito   |
|    Impacto    |    O administrador exclui [contas](lexicos10x58ed251.md#perfil) de [infratores](lexicos10x58ed251.md#infrator);</br>O administrador realiza a comunicação de avisos através de [notificações](lexicos10x58ed251.md#notificações);</br>Recruta [moderador](lexicos10x58ed251.md#moderador);</br>O administrador fornece instrução de moderação ao [moderador](lexicos10x58ed251.md#moderador);</br>O administrador realiza promoção de [moderador](lexicos10x58ed251.md#moderador);</br>O administrador relata falhas técnicas ao time de desenvolvimento;</br>O administrador assiste o usuário que pede auxílio.   |
|    Sinônimos  |    gerente, administradores, gerentes, administração.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [moderar denúncia](cenarios10x58ed251.md#id=3030) |   |



# amigo

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    amigo   |
|      Noção    |    Pessoa que segue ou é seguido.   |
| Classificação |    sujeito   |
|    Impacto    |    Ao adicionar uma amigo, o mesmo aparece na aba de amigos.</br>[perguntas](lexicos10x58ed251.md#pergunta) ou [respostas](lexicos10x58ed251.md#respondidas) geram [notificação](lexicos10x58ed251.md#notificações) para os amigos.   |
|    Sinônimos  |    seguidor.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# banido

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    banido   |
|      Noção    |    Usuário impossibilitado de acessar sua [conta](lexicos10x58ed251.md#perfil).</br>Apos infringir certos tipos de regras ou ser reincidente em advertencias.   |
| Classificação |    estado   |
|    Impacto    |    Usuário após ser temporariamente banido deve ser mais cauteloso em seu comportamento: ESTADO - [conta](lexicos10x58ed251.md#perfil) sob supervisão.</br></br>Após banimento total, usuário não pode mais utilizar sua [conta](lexicos10x58ed251.md#perfil): ESTADO - [conta](lexicos10x58ed251.md#perfil) excluída.   |
|    Sinônimos  |    punido, retirado, excluido.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [moderar denúncia](cenarios10x58ed251.md#id=3030) | [denunciar](lexicos10x58ed251.md#denunciar) |



# bloquear usuário

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    bloquear usuário   |
|      Noção    |    Usuário sofre bloqueio temporário no Brainly devido a prática de infrações.</br>Usuário impossibilitado de acessar sua [conta](lexicos10x58ed251.md#perfil) temporariamente.   |
| Classificação |    verbo   |
|    Impacto    |    O [moderador](lexicos10x58ed251.md#moderador) ou a [administração](lexicos10x58ed251.md#administrador) do Brainly bloqueia o usuário.</br>O usuário tem sua [conta](lexicos10x58ed251.md#perfil) suspensa por alguns dias.   |
|    Sinônimos  |    bloqueiam usuário, bloquear usuários, reter usuários, travar usuário, reter usuário, bloqueia usuário.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [moderar denúncia](cenarios10x58ed251.md#id=3030) |   |



# comentário

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    comentário   |
|      Noção    |    ponderação, crítica ou esclarecimento.   |
| Classificação |    objeto   |
|    Impacto    |    alguém pode escrever um comentário em uma [pergunta](lexicos10x58ed251.md#pergunta) ou em uma [resposta](lexicos10x58ed251.md#respondidas).</br>A [comunidade](lexicos10x58ed251.md#comunidade) pode usar os comentários para comunicação.   |
|    Sinônimos  |    explicação, avaliação.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [moderar denúncia](cenarios10x58ed251.md#id=3030) | [notificações](lexicos10x58ed251.md#notificações) |
|   | [moderador](lexicos10x58ed251.md#moderador) |



# comunidade

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    comunidade   |
|      Noção    |    conjunto de pessoas em prol de se ajudarem.   |
| Classificação |    sujeito   |
|    Impacto    |    a comunidade pode ajuda a [responder](lexicos10x58ed251.md#responder);</br>a comunidade faz [perguntas](lexicos10x58ed251.md#pergunta);</br>a comunidade pode [denunciar](lexicos10x58ed251.md#denunciar) atitudes impróprias.   |
|    Sinônimos  |    usuários.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [faça sua pergunta](cenarios10x58ed251.md#id=2996) | [comentário](lexicos10x58ed251.md#comentário) |
| [responder tarefa](cenarios10x58ed251.md#id=2997) | [mensagens](lexicos10x58ed251.md#mensagens) |
| [pesquisar](cenarios10x58ed251.md#id=3000) | [tarefas resolvidas](lexicos10x58ed251.md#tarefas-resolvidas) |
|   | [moderador](lexicos10x58ed251.md#moderador) |
|   | [pergunta respondida](lexicos10x58ed251.md#id=12644) |



# denunciar

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    denunciar   |
|      Noção    |    Realizada pelo usuário quando encontra uma [resposta](lexicos10x58ed251.md#respondidas) ou [pergunta](lexicos10x58ed251.md#pergunta) inadequada.</br>Ao clicar no botão de denunciar, o [moderador](lexicos10x58ed251.md#moderador) é acionado.   |
| Classificação |    verbo   |
|    Impacto    |    [pergunta](lexicos10x58ed251.md#pergunta) ou [resposta](lexicos10x58ed251.md#respondidas) apagada.</br>Usuário denunciado é advertido ou [banido](lexicos10x58ed251.md#banido).   |
|    Sinônimos  |    sinalizar, reportar.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [comunidade](lexicos10x58ed251.md#comunidade) |



# desafios

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    desafios   |
|      Noção    |    [tarefas](lexicos10x58ed251.md#pergunta) em um período de tempo.   |
| Classificação |    objeto   |
|    Impacto    |    Desafios completos geram [pontos](lexicos10x58ed251.md#pontos);</br>Um usuário pode aceitar um unico desafio por vez;</br>Servem para impulsionar um usuário a uma [tarefa](lexicos10x58ed251.md#pergunta).   |
|    Sinônimos  |    desafio.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [iniciar desafios](cenarios10x58ed251.md#id=2998) | [pontos](lexicos10x58ed251.md#pontos) |



# emblemas

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    emblemas   |
|      Noção    |    Símbolos ou imagens que representam uma atividade.   |
| Classificação |    objeto   |
|    Impacto    |    Uma atividade completa gera um emblema.</br>Os usuário podem ver o próprio progresso para conquistar um emblema.   |
|    Sinônimos  |    conquistas, emblema, conquista.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [emblemas mais próximos](lexicos10x58ed251.md#emblemas-mais-próximos) |
|   | [emblemas recentes](lexicos10x58ed251.md#emblemas-recentes) |
|   | [emblemas conquistados.](lexicos10x58ed251.md#emblemas-conquistados) |



# emblemas conquistados.

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    emblemas conquistados.   |
|      Noção    |    Atividade cumprida.   |
| Classificação |    estado   |
|    Impacto    |    Os [emblemas](lexicos10x58ed251.md#emblemas) conquistados ficam salvos em [emblemas](lexicos10x58ed251.md#emblemas) obtidos.</br>Os [emblemas](lexicos10x58ed251.md#emblemas) servem evidenciar o progresso do usuário no brainly.   |
|    Sinônimos  |    emblemas adquiridos .   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# emblemas mais próximos

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    emblemas mais próximos   |
|      Noção    |    Atividades perto de serem cumpridas.   |
| Classificação |    estado   |
|    Impacto    |    [emblemas](lexicos10x58ed251.md#emblemas) que estão mais perto de serem cumpridos são mostrados em [emblemas](lexicos10x58ed251.md#emblemas) mais próximos.</br>Os [emblemas](lexicos10x58ed251.md#emblemas) mais próximos podem impulsionar um usuário a se empenhar em uma atividade.   |
|    Sinônimos  |    próxima conquista.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# emblemas recentes

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    emblemas recentes   |
|      Noção    |    Últimas atividades cumpridas;</br>Últimos [emblemas](lexicos10x58ed251.md#emblemas) adquiridos.   |
| Classificação |    estado   |
|    Impacto    |    Os últimos [emblemas](lexicos10x58ed251.md#emblemas) ficam salvos em [emblemas](lexicos10x58ed251.md#emblemas) mais recentes.   |
|    Sinônimos  |    conquista recente.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# infrator

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    infrator   |
|      Noção    |    Pessoa que não cumpre com as políticas do regulamento do Brainly.</br>Responsável pela perda de tempo de [moderadores](lexicos10x58ed251.md#moderador) e estudantes devido ao cometimento de irregularidades.   |
| Classificação |    sujeito   |
|    Impacto    |    O infrator prática irregularidades na plataforma;</br>O infrator prejudica aos [moderadores](lexicos10x58ed251.md#moderador), aos estudantes e à plataforma devido ao tempo e recurso gasto.</br>O infrator participa em [perguntas](lexicos10x58ed251.md#pergunta), [respostas](lexicos10x58ed251.md#respondidas), comentários e no chat de maneira inadequada.</br>O infrator prática spam, brincadeiras e pedidos de informações pessoais.   |
|    Sinônimos  |    infratores.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [moderar denúncia](cenarios10x58ed251.md#id=3030) |   |



# matéria

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    matéria   |
|      Noção    |    Área de conhecimento.   |
| Classificação |    objeto   |
|    Impacto    |    As [perguntas](lexicos10x58ed251.md#pergunta) são divididas por matéria;</br>Um usuário pode filtrar os resultados por matéria.   |
|    Sinônimos  |    tema.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# melhor resposta

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    melhor resposta   |
|      Noção    |    Solução mais adequada, ou que melhor tirou a [dúvida](lexicos10x58ed251.md#pergunta).   |
| Classificação |    estado   |
|    Impacto    |    Um usuário ao ter sua [dúvida](lexicos10x58ed251.md#pergunta) respondida pode escolher a melhor [resposta](lexicos10x58ed251.md#respondidas).</br>Ao [responder](lexicos10x58ed251.md#responder) um usuário pode ganhar melhor [resposta](lexicos10x58ed251.md#respondidas).</br>Uma certa quantidade de melhores [respostas](lexicos10x58ed251.md#respondidas) é necessária para subir de [nível](lexicos10x58ed251.md#nível).   |
|    Sinônimos  |    melhores respostas.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [nível](lexicos10x58ed251.md#nível) |
|   | [pergunta](lexicos10x58ed251.md#pergunta) |
|   | [notificações](lexicos10x58ed251.md#notificações) |
|   | [pergunta respondida](lexicos10x58ed251.md#id=12644) |



# mensagens

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    mensagens   |
|      Noção    |    Informações trocadas em forma de texto.   |
| Classificação |    objeto   |
|    Impacto    |    Um [moderador](lexicos10x58ed251.md#moderador) poder chamar atenção de alguém ou fazer um esclarecimento.</br>Um usuário pode mandar mensagem para o [moderador](lexicos10x58ed251.md#moderador).</br>A [comunidade](lexicos10x58ed251.md#comunidade) não pode trocar mensagem privada.   |
|    Sinônimos  |    mensagem, mensagem privada.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# moderador

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    moderador   |
|      Noção    |    Pessoa que modera os conteúdos do Brainly.</br>Responsável por esclarecer as políticas da plataforma à [comunidade](lexicos10x58ed251.md#comunidade);</br>Responsável por manter o [nível](lexicos10x58ed251.md#nível) de qualidade da plataforma em [pergunta](lexicos10x58ed251.md#pergunta), [resposta](lexicos10x58ed251.md#respondidas) e [comentário](lexicos10x58ed251.md#comentário).   |
| Classificação |    sujeito   |
|    Impacto    |    O moderador exclui [pergunta](lexicos10x58ed251.md#pergunta), [resposta](lexicos10x58ed251.md#respondidas) ou [comentário](lexicos10x58ed251.md#comentário) indevido;</br>O moderador comunica [infratores](lexicos10x58ed251.md#infrator) as políticas do regulamento;</br>O moderador retira [dúvida](lexicos10x58ed251.md#pergunta) de estudantes sobre o regulamento da plataforma;</br>O moderador pode [bloquear usuários](lexicos10x58ed251.md#bloquear-usuário) irregulares.</br>O moderador define [respostas verificadas](lexicos10x58ed251.md#respostas-verificadas), corretas.   |
|    Sinônimos  |    moderadores.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [moderar denúncia](cenarios10x58ed251.md#id=3030) | [mensagens](lexicos10x58ed251.md#mensagens) |
|   | [administrador](lexicos10x58ed251.md#administrador) |
|   | [denunciar](lexicos10x58ed251.md#denunciar) |
|   | [bloquear usuário](lexicos10x58ed251.md#bloquear-usuário) |



# nível

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    nível   |
|      Noção    |    Classificação do desempenho do usuário.   |
| Classificação |    objeto   |
|    Impacto    |    Para subir de nível é necessário alcançar uma meta de [pontos](lexicos10x58ed251.md#pontos) e de [melhor resposta](lexicos10x58ed251.md#melhor-resposta).</br>Níveis podem servir como meta para [usuários](lexicos10x58ed251.md#comunidade).   |
|    Sinônimos  |    níveis.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [melhor resposta](lexicos10x58ed251.md#melhor-resposta) |
|   | [pontos](lexicos10x58ed251.md#pontos) |
|   | [notificações](lexicos10x58ed251.md#notificações) |
|   | [moderador](lexicos10x58ed251.md#moderador) |



# notificações

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    notificações   |
|      Noção    |    Feedback do sistema.   |
| Classificação |    objeto   |
|    Impacto    |    Uma pessoa recebe uma notificação ao receber um [obrigado](lexicos10x58ed251.md#obrigados), ter uma [pergunta expirada](lexicos10x58ed251.md#pergunta-expirada) ou respondida, cumprir um [desafio](lexicos10x58ed251.md#desafios), ganhar um [emblema](lexicos10x58ed251.md#emblemas), ganhar [melhor resposta](lexicos10x58ed251.md#melhor-resposta), subir de [nível](lexicos10x58ed251.md#nível) ou quando outra pessoa adiciona [comentário](lexicos10x58ed251.md#comentário) em sua [pergunta](lexicos10x58ed251.md#pergunta) ou [resposta](lexicos10x58ed251.md#respondidas).   |
|    Sinônimos  |    notificação, aviso.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [administrador](lexicos10x58ed251.md#administrador) |



# obrigados

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    obrigados   |
|      Noção    |    Agradecimento.   |
| Classificação |    objeto   |
|    Impacto    |    Obrigados são representados por corações.</br>Pode-se agradecer a uma [resposta](lexicos10x58ed251.md#respondidas) com um obrigado.   |
|    Sinônimos  |    botão de agradecimento, obrigado.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# perfil

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    perfil   |
|      Noção    |    Ambiente que possui as informações do usuário.   |
| Classificação |    objeto   |
|    Impacto    |    Apresenta as informações do usuário.</br>Permite o usuário alterar algumas de sua informações.   |
|    Sinônimos  |    perfis, conta, contas.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [faça sua pergunta](cenarios10x58ed251.md#id=2996) |   |
| [alterar perfil](cenarios10x58ed251.md#id=3032) |   |
| [adicionar anexo para pergunta](cenarios10x58ed251.md#id=3033) |   |
| [adicionar símbolo para pergunta](cenarios10x58ed251.md#id=3034) |   |
| [adicionar equação para pergunta](cenarios10x58ed251.md#id=3035) |   |



# pergunta

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    pergunta   |
|      Noção    |    Questão proposta para que alguém tire uma dúvida.   |
| Classificação |    objeto   |
|    Impacto    |    Para fazer um pergunta o usuário deve oferecer [pontos](lexicos10x58ed251.md#pontos).</br>Quando alguém tem sua [pergunta respondida](lexicos10x58ed251.md#id=12644), pode escolher a [melhor resposta](lexicos10x58ed251.md#melhor-resposta).   |
|    Sinônimos  |    tarefa, dúvida, tarefas, perguntas.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [faça sua pergunta](cenarios10x58ed251.md#id=2996) | [pontos](lexicos10x58ed251.md#pontos) |
| [responder tarefa](cenarios10x58ed251.md#id=2997) | [comentário](lexicos10x58ed251.md#comentário) |
| [dar obrigado](cenarios10x58ed251.md#id=2999) | [notificações](lexicos10x58ed251.md#notificações) |
| [moderar denúncia](cenarios10x58ed251.md#id=3030) | [pergunta expirada](lexicos10x58ed251.md#pergunta-expirada) |
| [adicionar anexo para pergunta](cenarios10x58ed251.md#id=3033) | [tarefas resolvidas](lexicos10x58ed251.md#tarefas-resolvidas) |
| [adicionar símbolo para pergunta](cenarios10x58ed251.md#id=3034) | [tarefas adicionadas](lexicos10x58ed251.md#tarefas-adicionadas) |
| [adicionar equação para pergunta](cenarios10x58ed251.md#id=3035) | [recebendo resposta](lexicos10x58ed251.md#recebendo-resposta) |
|   | [moderador](lexicos10x58ed251.md#moderador) |
|   | [denunciar](lexicos10x58ed251.md#denunciar) |
|   | [pergunta popular](lexicos10x58ed251.md#pergunta-popular) |



# pergunta expirada

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    pergunta expirada   |
|      Noção    |    [pergunta](lexicos10x58ed251.md#pergunta) com prazo de [resposta](lexicos10x58ed251.md#respondidas) vencido.   |
| Classificação |    estado   |
|    Impacto    |    Ao ter o prazo de [resposta](lexicos10x58ed251.md#respondidas) vencido os [pontos](lexicos10x58ed251.md#pontos) oferecidos são devolvidos.</br>Uma [pergunta](lexicos10x58ed251.md#pergunta) expirada é eliminada do brainly.   |
|    Sinônimos  |    pergunta deletada, tarefa expirada.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [notificações](lexicos10x58ed251.md#notificações) |



# pergunta popular

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    pergunta popular   |
|      Noção    |    [pergunta](lexicos10x58ed251.md#pergunta) muito acessada por estudantes.   |
| Classificação |    objeto   |
|    Impacto    |    A [pergunta](lexicos10x58ed251.md#pergunta) popular recebe maior destaque no Brainly.</br>A [pergunta](lexicos10x58ed251.md#pergunta) popular é responsável por atrair maior acesso à plataforma.</br>O [time de respostas](lexicos10x58ed251.md#time-de-respostas), os [moderadores](lexicos10x58ed251.md#moderador), os [universitários](lexicos10x58ed251.md#universitário), a [administração](lexicos10x58ed251.md#administrador) e os [usuários](lexicos10x58ed251.md#comunidade) empenham-se mais em [responder](lexicos10x58ed251.md#responder) essas [perguntas](lexicos10x58ed251.md#pergunta).   |
|    Sinônimos  |    perguntas populares, populares, questões populares, questão popular.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# pontos

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    pontos   |
|      Noção    |    Método de premiação.   |
| Classificação |    objeto   |
|    Impacto    |    Um usuário ganha pontos ao [responder](lexicos10x58ed251.md#responder) uma [pergunta](lexicos10x58ed251.md#pergunta).</br>Para fazer uma [pergunta](lexicos10x58ed251.md#pergunta) é necessário oferecer pontos.</br>É necessário alcançar uma meta de pontos para subir de [nível](lexicos10x58ed251.md#nível).</br>Ao cumprir [desafios](lexicos10x58ed251.md#desafios) o usuário ganha pontos.   |
|    Sinônimos  |    pontuação, ponto.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [iniciar desafios](cenarios10x58ed251.md#id=2998) | [responder](lexicos10x58ed251.md#responder) |
| [adicionar anexo para pergunta](cenarios10x58ed251.md#id=3033) | [nível](lexicos10x58ed251.md#nível) |
| [adicionar símbolo para pergunta](cenarios10x58ed251.md#id=3034) | [pergunta](lexicos10x58ed251.md#pergunta) |
| [adicionar equação para pergunta](cenarios10x58ed251.md#id=3035) | [desafios](lexicos10x58ed251.md#desafios) |
|   | [rankings](lexicos10x58ed251.md#rankings) |
|   | [pergunta expirada](lexicos10x58ed251.md#pergunta-expirada) |
|   | [cadastrar](lexicos10x58ed251.md#id=12647) |
|   | [log in](lexicos10x58ed251.md#id=12648) |
|   | [logado](lexicos10x58ed251.md#id=12651) |



# rankings

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    rankings   |
|      Noção    |    Listagem dos melhores.   |
| Classificação |    objeto   |
|    Impacto    |    As pessoas com mais [pontos](lexicos10x58ed251.md#pontos) aparecem no ranking.</br>o ranking é dividido em diário, semanal e mensal.   |
|    Sinônimos  |    ranking.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# recebendo resposta

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    recebendo resposta   |
|      Noção    |    [perguntas](lexicos10x58ed251.md#pergunta) que estão sendo [respondidas](lexicos10x58ed251.md#respondidas).   |
| Classificação |    estado   |
|    Impacto    |    Quando uma [pergunta](lexicos10x58ed251.md#pergunta) já está sendo respondida por duas pessoas, outras pessoas podem apenas fazer comentários;</br>O usuário que fez a [pergunta](lexicos10x58ed251.md#pergunta) recebe uma [notificação](lexicos10x58ed251.md#notificações) que sua [pergunta](lexicos10x58ed251.md#pergunta) está sendo respondida.   |
|    Sinônimos  |    tarefa sendo respondida.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# responder

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    responder   |
|      Noção    |    Tirar [dúvida](lexicos10x58ed251.md#pergunta) de outro usuário.   |
| Classificação |    verbo   |
|    Impacto    |    Responder gera [pontos](lexicos10x58ed251.md#pontos).</br>A [resposta](lexicos10x58ed251.md#respondidas) deve ser detalhada para que o usuário com [dúvida](lexicos10x58ed251.md#pergunta) entenda.   |
|    Sinônimos  |    responde.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [iniciar desafios](cenarios10x58ed251.md#id=2998) | [melhor resposta](lexicos10x58ed251.md#melhor-resposta) |
|   | [pontos](lexicos10x58ed251.md#pontos) |
|   | [tarefas resolvidas](lexicos10x58ed251.md#tarefas-resolvidas) |
|   | [comunidade](lexicos10x58ed251.md#comunidade) |
|   | [pergunta popular](lexicos10x58ed251.md#pergunta-popular) |
|   | [cadastrar](lexicos10x58ed251.md#id=12647) |
|   | [log in](lexicos10x58ed251.md#id=12648) |
|   | [logado](lexicos10x58ed251.md#id=12651) |



# respondidas

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    respondidas   |
|      Noção    |    Dúvidas Tiradas ou respondidas.   |
| Classificação |    estado   |
|    Impacto    |    [perguntas](lexicos10x58ed251.md#pergunta) com duas respostas,  apenas podem receber comentários.</br>Pode-se agradecer ou qualificar respostas.   |
|    Sinônimos  |    resposta, respostas.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [tarefas resolvidas](lexicos10x58ed251.md#tarefas-resolvidas) |
|   | [sem resposta](lexicos10x58ed251.md#sem-resposta) |
|   | [recebendo resposta](lexicos10x58ed251.md#recebendo-resposta) |
|   | [time de respostas](lexicos10x58ed251.md#time-de-respostas) |
|   | [universitário](lexicos10x58ed251.md#universitário) |
|   | [pergunta respondida](lexicos10x58ed251.md#id=12644) |



# respostas verificadas

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    respostas verificadas   |
|      Noção    |    [respostas](lexicos10x58ed251.md#respondidas) revisadas, que foram destacadas devido seu detalhamento e precisão.   |
| Classificação |    estado   |
|    Impacto    |    As [melhores respostas](lexicos10x58ed251.md#melhor-resposta) analisadas pelo time tornam-se verificadas.</br>Ao fazer uma pesquisa são mostradas as [respostas](lexicos10x58ed251.md#respondidas) verificadas.   |
|    Sinônimos  |    tarefas verificadas, respostas revisadas, resposta revisada.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [pesquisar](cenarios10x58ed251.md#id=3000) | [moderador](lexicos10x58ed251.md#moderador) |



# sem resposta

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    sem resposta   |
|      Noção    |    não respondida.   |
| Classificação |    estado   |
|    Impacto    |    [perguntas](lexicos10x58ed251.md#pergunta) que podem ser [respondidas](lexicos10x58ed251.md#respondidas).</br>[tarefas](lexicos10x58ed251.md#pergunta) que ficam muito tempo sem [resposta](lexicos10x58ed251.md#respondidas) são deletadas.   |
|    Sinônimos  |    tarefa sem resposta.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| [responder tarefa](cenarios10x58ed251.md#id=2997) |   |



# tarefas adicionadas

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    tarefas adicionadas   |
|      Noção    |    [pergunta](lexicos10x58ed251.md#pergunta) feita.   |
| Classificação |    estado   |
|    Impacto    |    As dúvidas tiradas são salvas em [tarefas](lexicos10x58ed251.md#pergunta) adicionadas.</br>As [tarefas](lexicos10x58ed251.md#pergunta) adicionadas servem para usuário rever uma [pergunta](lexicos10x58ed251.md#pergunta).   |
|    Sinônimos  |    pergunta adicionada.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# tarefas resolvidas

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    tarefas resolvidas   |
|      Noção    |    [perguntas](lexicos10x58ed251.md#pergunta) [respondidas](lexicos10x58ed251.md#respondidas).   |
| Classificação |    estado   |
|    Impacto    |    Ao [responder](lexicos10x58ed251.md#responder) uma [pergunta](lexicos10x58ed251.md#pergunta) a [tarefa](lexicos10x58ed251.md#pergunta) fica salva em [tarefas](lexicos10x58ed251.md#pergunta) [respondidas](lexicos10x58ed251.md#respondidas).</br>As [perguntas](lexicos10x58ed251.md#pergunta) resolvidas servem para o [comunidade](lexicos10x58ed251.md#comunidade) ver as [respostas](lexicos10x58ed251.md#respondidas) de um usuário.   |
|    Sinônimos  |    perguntas resolvidas.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



# time de respostas

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    time de respostas   |
|      Noção    |    [usuários](lexicos10x58ed251.md#comunidade) mais experientes em dar [respostas](lexicos10x58ed251.md#respondidas) na plataforma.</br>Time coordenado e selecionado pela [administração](lexicos10x58ed251.md#administrador) do Brainly devido ao bom desempenho.   |
| Classificação |    sujeito   |
|    Impacto    |    O time de [respostas](lexicos10x58ed251.md#respondidas) aumenta a qualidade das [perguntas](lexicos10x58ed251.md#pergunta) [respondidas](lexicos10x58ed251.md#respondidas).</br>As [perguntas populares](lexicos10x58ed251.md#pergunta-popular) são focalizadas pelo time de [respostas](lexicos10x58ed251.md#respondidas).</br>O time de [respostas](lexicos10x58ed251.md#respondidas) recebe orientações de participação na plataforma por parte dos [administradores](lexicos10x58ed251.md#administrador).   |
|    Sinônimos  |    equipe de resposta, equipes de respostas, time de resposta.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
|   | [administrador](lexicos10x58ed251.md#administrador) |
|   | [pergunta popular](lexicos10x58ed251.md#pergunta-popular) |



# universitário

|  Informações  | Símbolo |
|:-------------:|:-------:|
|      Nome     |    universitário   |
|      Noção    |    É o usuário da plataforma que cursa ensino superior.</br>Estudante selecionado pela [administração](lexicos10x58ed251.md#administrador) a partir de processo seletivo em universidade.</br>Possui amparo e resguardo de ações por parte da [administração](lexicos10x58ed251.md#administrador).   |
| Classificação |    sujeito   |
|    Impacto    |    O universitário [responde](lexicos10x58ed251.md#responder) questões específicas, especialmente as [perguntas populares](lexicos10x58ed251.md#pergunta-popular).</br>O universitário recebe orientação por parte da [administração](lexicos10x58ed251.md#administrador) sobre as [perguntas](lexicos10x58ed251.md#pergunta) a serem [respondidas](lexicos10x58ed251.md#respondidas).</br>O universitário gera [respostas](lexicos10x58ed251.md#respondidas) com alta qualidade no Brainly.   |
|    Sinônimos  |    acadêmico, universitários, acadêmicos.   |


|    Cenários   | Léxicos |
|:-------------:|:-------:|
| - | - |



