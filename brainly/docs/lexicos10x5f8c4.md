# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| [1.0](./modelagem_v1/lexicos10x58ed251.md) | 21/04/2019 | Gera primeira versão dos artefatos | Grupo |
| 2.0 | 22/04/2019 | Gera segunda versão dos artefatos, crawler otimizado | Grupo |
| 2.1 | 22/04/2019 | Adiciona introdução e descrição sobre o crawler utilizado | Welison Regis |
| 2.2 | 22/04/2019 | Adicionado requisitos relacionados | Andre Pinto, Leonardo Medeiros |

# Introdução

A modelagem por léxicos baseia-se na descrição de símbolos tendo como base a noção que transmitem (sentido denotativo) e o impacto que ocasionam (sentido conotativo). Os léxicos abaixo dividem-se em: nome, noção, classificação (sujeito, objeto, verbo, estado) e impacto.

O arquivo _markdown_ aqui disposto é gerado automaticamente por uma ferramenta desenvolvida em python disponível em nosso _github_ que, baseado nas _urls_, puxa todas as informações dos léxicos do site [C&L](http://pes.inf.puc-rio.br/cel/aplicacao/) referente ao projeto Brainly e gera esse _markdown_ com âncoras nas palavras chaves (inclusive sinônimos). O _notebook_ com o código e as orientações está disponível em [C&L Crawler](https://github.com/WelisonR/2019.1-Requisitos-Brainly/blob/master/CeL_crawler_pucrio.ipynb).
>>>>>>> ddbd32728e6cd9c6bea26882e4c24c4550e0d9da

# administrador
### L12529

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    administrador   |
|  **Noção**      |    Funcionário que trabalha no Brainly;</br>Responsável pela gerência de [contas](lexicos10x5f8c4.md#l12532) e necessidades da plataforma;</br>Responsável pela orientação do [time de respostas](lexicos10x5f8c4.md#l12576) e dos [universitários](lexicos10x5f8c4.md#l12577).</br>[pessoa](lexicos10x5f8c4.md#l12660) responsável pela coordenação das atividades de moderação;   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    O administrador exclui [contas](lexicos10x5f8c4.md#l12532) de [infratores](lexicos10x5f8c4.md#l12531);</br>O administrador realiza a comunicação de avisos através de [notificações](lexicos10x5f8c4.md#l12509);</br>Recruta [moderador](lexicos10x5f8c4.md#l12528);</br>O administrador fornece instrução de moderação ao [moderador](lexicos10x5f8c4.md#l12528);</br>O administrador realiza promoção de [moderador](lexicos10x5f8c4.md#l12528);</br>O administrador relata falhas técnicas ao time de desenvolvimento;</br>O administrador assiste o [usuário](lexicos10x5f8c4.md#l12660) que pede auxílio.   |
|  **Sinônimos**  |    gerente, administradores, gerentes, administração.   |
| **Requisitos** | [INT2.11](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.8](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.7](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [editar](lexicos10x5f8c4.md#l12659) |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) | [usuário](lexicos10x5f8c4.md#l12660) |



# amigo
### L12502

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    amigo   |
|  **Noção**      |    [pessoa](lexicos10x5f8c4.md#l12660) que segue ou é seguido.   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    Ao adicionar uma amigo, o mesmo aparece na aba de amigos.</br>[perguntas](lexicos10x5f8c4.md#l12494) ou [respostas](lexicos10x5f8c4.md#l12521) geram [notificação](lexicos10x5f8c4.md#l12509) para os amigos.   |
|  **Sinônimos**  |    seguidor, amigos.   |
| **Requisitos** | [EN2.2](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# banido
### L12534

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    banido   |
|  **Noção**      |    Usuário impossibilitado de acessar sua [conta](lexicos10x5f8c4.md#l12532).</br>Apos infringir certos tipos de regras ou ser reincidente em advertencias.   |
|**Classificação**|    estado   |
|  **Impacto**    |    [usuário](lexicos10x5f8c4.md#l12660) após ser temporariamente banido faz sua [conta](lexicos10x5f8c4.md#l12532) [entrar](lexicos10x5f8c4.md#l12648) em um período de observação: ESTADO - [conta](lexicos10x5f8c4.md#l12532) sob supervisão.</br></br>Após banimento total, [usuário](lexicos10x5f8c4.md#l12660) não pode mais utilizar sua [conta](lexicos10x5f8c4.md#l12532): ESTADO - [conta excluída](lexicos10x5f8c4.md#l12658).   |
|  **Sinônimos**  |    excluido, retirado, punido.   |
| **Requisitos** | [INT2.15](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.10](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [denunciar](lexicos10x5f8c4.md#l12533) |



# bloquear usuário
### L12574

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    bloquear usuário   |
|  **Noção**      |    [usuário](lexicos10x5f8c4.md#l12660) sofre bloqueio temporário no Brainly devido a prática de infrações.</br>[usuário](lexicos10x5f8c4.md#l12660) impossibilitado de acessar sua [conta](lexicos10x5f8c4.md#l12532) temporariamente.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    O [moderador](lexicos10x5f8c4.md#l12528) ou a [administração](lexicos10x5f8c4.md#l12529) do Brainly bloqueia o [usuário](lexicos10x5f8c4.md#l12660).</br>O [usuário](lexicos10x5f8c4.md#l12660) tem sua [conta](lexicos10x5f8c4.md#l12532) suspensa por alguns dias.   |
|  **Sinônimos**  |    bloqueiam usuário, bloquear usuários, reter usuários, travar usuário, reter usuário, bloqueia usuário.   |
| **Requisitos** | [INT2.15](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.10](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) |   |



# cadastrar
### L12647

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    cadastrar   |
|  **Noção**      |    O [usuário](lexicos10x5f8c4.md#l12660) se cadastra.</br>O [usuário](lexicos10x5f8c4.md#l12660) se cadastra quando deseja ter uma [conta](lexicos10x5f8c4.md#l12532) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) cadastra o nome de [usuário](lexicos10x5f8c4.md#l12660); a data de nascimento; o email dos pais ou responsáveis, se menor de 13 anos; e aceita os [termos de uso](lexicos10x5f8c4.md#l12646) e [política de privacidade](lexicos10x5f8c4.md#l12645).   |
|**Classificação**|    verbo   |
|  **Impacto**    |    O [usuário](lexicos10x5f8c4.md#l12660) está em sua [conta](lexicos10x5f8c4.md#l12532) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) define uma senha e um endereço de email para sua [conta](lexicos10x5f8c4.md#l12532).</br>Quando cadastrado via email, é necessário confirmá-lo.</br>Ao realizar o primeiro [log in](lexicos10x5f8c4.md#l12648), o [usuário](lexicos10x5f8c4.md#l12660) receberá um tutorial básico.</br>O [usuário](lexicos10x5f8c4.md#l12660) ganha [pontos](lexicos10x5f8c4.md#l12492) por criar uma [conta](lexicos10x5f8c4.md#l12532).</br>O [usuário](lexicos10x5f8c4.md#l12660) pode fazer [perguntas](lexicos10x5f8c4.md#l12494).</br>O [usuário](lexicos10x5f8c4.md#l12660) pode [responder](lexicos10x5f8c4.md#l12489) [perguntas](lexicos10x5f8c4.md#l12494) e ganhar [pontos](lexicos10x5f8c4.md#l12492) pelas [respostas](lexicos10x5f8c4.md#l12521).   |
|  **Sinônimos**  |    registrar.   |
| **Requisitos** | [AP3.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.13](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/)  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [entre agora!](lexicos10x5f8c4.md#l12649) |
|   | [entrar com facebook](lexicos10x5f8c4.md#l12650) |



# comentário
### L12506

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    comentário   |
|  **Noção**      |    ponderação, crítica ou esclarecimento.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    alguém pode escrever um comentário em uma [pergunta](lexicos10x5f8c4.md#l12494) ou em uma [resposta](lexicos10x5f8c4.md#l12521).</br>A [comunidade](lexicos10x5f8c4.md#l12525) pode usar os comentários para comunicação.   |
|  **Sinônimos**  |    avaliação, explicação, comentários.   |
| **Requisitos** | [INT1.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.14](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [notificações](lexicos10x5f8c4.md#l12509) |
| [adicionar comentário](cenarios10x5f8c4.md#c3042) | [moderador](lexicos10x5f8c4.md#l12528) |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) |   |



# comunidade
### L12525

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    comunidade   |
|  **Noção**      |    conjunto de [pessoas](lexicos10x5f8c4.md#l12660) em prol de se ajudarem.   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    a comunidade pode ajudar a [responder](lexicos10x5f8c4.md#l12489);</br>a comunidade faz [perguntas](lexicos10x5f8c4.md#l12494);</br>a comunidade pode [denunciar](lexicos10x5f8c4.md#l12533) atitudes impróprias.   |
|  **Sinônimos**  |    usuários.   |
| **Requisitos** | [INT3.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [AP1.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [responder tarefa](cenarios10x5f8c4.md#c2997) | [comentário](lexicos10x5f8c4.md#l12506) |
| [pesquisar](cenarios10x5f8c4.md#c3000) | [mensagens](lexicos10x5f8c4.md#l12508) |
| [adicionar comentário](cenarios10x5f8c4.md#c3042) | [tarefas resolvidas](lexicos10x5f8c4.md#l12512) |
|   | [moderador](lexicos10x5f8c4.md#l12528) |
|   | [pergunta respondida](lexicos10x5f8c4.md#l12644) |



# confirmar email
### L12657

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    confirmar email   |
|  **Noção**      |    [usuário](lexicos10x5f8c4.md#l12660) verifica que o email utilizado na criação da [conta](lexicos10x5f8c4.md#l12532) é o dele próprio ou um email que tem acesso.</br>Ocorre quando o [usuário](lexicos10x5f8c4.md#l12660) acaba de criar uma [conta](lexicos10x5f8c4.md#l12532) e está [logado](lexicos10x5f8c4.md#l12651).</br>[usuário](lexicos10x5f8c4.md#l12660) recebe uma [mensagem](lexicos10x5f8c4.md#l12508) dizendo para confirmar o email, [usuário](lexicos10x5f8c4.md#l12660) deve então acessar seu email e confirmar a [conta](lexicos10x5f8c4.md#l12532) do brainly.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    Email foi confirmado.</br>Uma vez que o email foi confirmado não pode se confirmar de novo.</br>[usuário](lexicos10x5f8c4.md#l12660) ganha 10 [pontos](lexicos10x5f8c4.md#l12492) por confirmar o email.   |
|  **Sinônimos**  |    confirmação de email, aprovação de email, aprovar email.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# conta deletada
### L12658

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    conta deletada   |
|  **Noção**      |    [conta](lexicos10x5f8c4.md#l12532) não existe mais.</br>Ocorre quando um [usuário](lexicos10x5f8c4.md#l12660) consegue deletar a [conta](lexicos10x5f8c4.md#l12532).   |
|**Classificação**|    estado   |
|  **Impacto**    |    Quando algum [usuário](lexicos10x5f8c4.md#l12660) tenta abrir um [conta](lexicos10x5f8c4.md#l12532) com o mesmo email e nome de antes ele consegue: Estado - [conta](lexicos10x5f8c4.md#l12532) criada   |
|  **Sinônimos**  |    conta apagada, conta retirada, conta excluída.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [deletar conta](cenarios10x5f8c4.md#id=3039) |   |



# denunciar
### L12533

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    denunciar   |
|  **Noção**      |    Realizada pelo [usuário](lexicos10x5f8c4.md#l12660) quando encontra uma [resposta](lexicos10x5f8c4.md#l12521) ou [pergunta](lexicos10x5f8c4.md#l12494) inadequada.</br>Ao clicar no botão de denunciar, o [moderador](lexicos10x5f8c4.md#l12528) é acionado.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    [pergunta](lexicos10x5f8c4.md#l12494) ou [resposta](lexicos10x5f8c4.md#l12521) apagada.</br>[usuário](lexicos10x5f8c4.md#l12660) denunciado é advertido ou [banido](lexicos10x5f8c4.md#l12534).   |
|  **Sinônimos**  |    sinalizar, reportar.   |
| **Requisitos** | [INT2.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.13](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.16](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [INT2.17](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [comunidade](lexicos10x5f8c4.md#l12525) |



# desafios
### L12496

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    desafios   |
|  **Noção**      |    [tarefas](lexicos10x5f8c4.md#l12494) em um período de tempo.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Desafios completos geram [pontos](lexicos10x5f8c4.md#l12492);</br>Um [usuário](lexicos10x5f8c4.md#l12660) pode aceitar um unico desafio por vez;</br>Servem para impulsionar um [usuário](lexicos10x5f8c4.md#l12660) a uma [tarefa](lexicos10x5f8c4.md#l12494).   |
|  **Sinônimos**  |    desafio.   |
| **Requisitos** | [AP1.8](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [iniciar desafios](cenarios10x5f8c4.md#c2998) | [pontos](lexicos10x5f8c4.md#l12492) |



# deslogado
### L12653

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    deslogado   |
|  **Noção**      |    [usuário](lexicos10x5f8c4.md#l12660) ainda não está [logado](lexicos10x5f8c4.md#l12651) ao sistema</br></br>Isso ocorre quando o [usuário](lexicos10x5f8c4.md#l12660) não [logou](lexicos10x5f8c4.md#l12651) no sistema ou quando acabou de se desconectar.   |
|**Classificação**|    estado   |
|  **Impacto**    |    Quando o [usuário](lexicos10x5f8c4.md#l12660) se conecta:Estado – [usuário](lexicos10x5f8c4.md#l12660) [logado](lexicos10x5f8c4.md#l12651)   |
|  **Sinônimos**  |    desconectado, deslogou, desloga, saiu.   |
| **Requisitos** | [AP1.12](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [logado](lexicos10x5f8c4.md#l12651) |



# editar
### L12659

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    editar   |
|  **Noção**      |    Edição do conteúdo de [perguntas](lexicos10x5f8c4.md#l12494) ou [respostas](lexicos10x5f8c4.md#l12521) na plataforma.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    Corrigir erros em [perguntas](lexicos10x5f8c4.md#l12494) e [respostas](lexicos10x5f8c4.md#l12521).</br>[moderador](lexicos10x5f8c4.md#l12528), [administrador](lexicos10x5f8c4.md#l12529) pedir correção para incluir mais detalhes na [pergunta](lexicos10x5f8c4.md#l12494) ou [resposta](lexicos10x5f8c4.md#l12521).   |
|  **Sinônimos**  |    edição, modificar, mudar.   |
| **Requisitos** | [INT1.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) |   |
| [alterar perfil](cenarios10x5f8c4.md#c3032) |   |
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) |   |
| [deletar conta](cenarios10x5f8c4.md#id=3039) |   |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) |   |



# emblemas
### L12495

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    emblemas   |
|  **Noção**      |    Símbolos ou imagens que representam uma atividade.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Uma atividade completa gera um emblema.</br>Os [usuário](lexicos10x5f8c4.md#l12660) podem ver o próprio progresso para conquistar um emblema.   |
|  **Sinônimos**  |    conquistas, emblema, conquista.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [emblemas mais próximos](lexicos10x5f8c4.md#l12516) |
|   | [emblemas recentes](lexicos10x5f8c4.md#l12517) |
|   | [emblemas conquistados.](lexicos10x5f8c4.md#l12518) |



# emblemas conquistados.
### L12518

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    emblemas conquistados.   |
|  **Noção**      |    Atividade cumprida.   |
|**Classificação**|    estado   |
|  **Impacto**    |    Os [emblemas](lexicos10x5f8c4.md#l12495) conquistados ficam salvos em [emblemas](lexicos10x5f8c4.md#l12495) obtidos.</br>Os [emblemas](lexicos10x5f8c4.md#l12495) servem evidenciar o progresso do [usuário](lexicos10x5f8c4.md#l12660) no brainly.   |
|  **Sinônimos**  |    emblemas adquiridos .   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# emblemas mais próximos
### L12516

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    emblemas mais próximos   |
|  **Noção**      |    Atividades perto de serem cumpridas.   |
|**Classificação**|    estado   |
|  **Impacto**    |    [emblemas](lexicos10x5f8c4.md#l12495) que estão mais perto de serem cumpridos são mostrados em [emblemas](lexicos10x5f8c4.md#l12495) mais próximos.</br>Os [emblemas](lexicos10x5f8c4.md#l12495) mais próximos podem impulsionar um [usuário](lexicos10x5f8c4.md#l12660) a se empenhar em uma atividade.   |
|  **Sinônimos**  |    próxima conquista.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# emblemas recentes
### L12517

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    emblemas recentes   |
|  **Noção**      |    Últimas atividades cumpridas;</br>Últimos [emblemas](lexicos10x5f8c4.md#l12495) adquiridos.   |
|**Classificação**|    estado   |
|  **Impacto**    |    Os últimos [emblemas](lexicos10x5f8c4.md#l12495) ficam salvos em [emblemas](lexicos10x5f8c4.md#l12495) mais recentes.   |
|  **Sinônimos**  |    conquista recente.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# entrar com facebook
### L12650

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    entrar com facebook   |
|  **Noção**      |    [tarefa](lexicos10x5f8c4.md#l12494) realizada por um [usuário](lexicos10x5f8c4.md#l12660).</br></br>Acontece quando o [usuário](lexicos10x5f8c4.md#l12660) não está [logado](lexicos10x5f8c4.md#l12651) e deseja [logar](lexicos10x5f8c4.md#l12648).</br></br>[usuário](lexicos10x5f8c4.md#l12660) clica em [entrar](lexicos10x5f8c4.md#l12648) ou [cadastrar](lexicos10x5f8c4.md#l12647) depois clica em [entrar](lexicos10x5f8c4.md#l12648) com facebook e no final coloca seu [usuário](lexicos10x5f8c4.md#l12660) e senha do facebook.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    [usuário](lexicos10x5f8c4.md#l12660) está [logado](lexicos10x5f8c4.md#l12651) no Brainly e no facebook.</br></br>Se o [usuário](lexicos10x5f8c4.md#l12660) está [logado](lexicos10x5f8c4.md#l12651), não pode [logar](lexicos10x5f8c4.md#l12648) novamente.</br></br>[usuário](lexicos10x5f8c4.md#l12660) ganha as vantagens de estar [logado](lexicos10x5f8c4.md#l12651).   |
|  **Sinônimos**  |    logar com facebook.   |
| **Requisitos** | [INT3.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [entre agora!](lexicos10x5f8c4.md#l12649) |



# entre agora!
### L12649

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    entre agora!   |
|  **Noção**      |    O [usuário](lexicos10x5f8c4.md#l12660) clica no texto "ENTRE AGORA!"</br>O [usuário](lexicos10x5f8c4.md#l12660) clica quando deseja se [cadastrar](lexicos10x5f8c4.md#l12647) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) escolhe se deseja se [cadastrar](lexicos10x5f8c4.md#l12647) usando seu email ou Facebook ([entrar com facebook](lexicos10x5f8c4.md#l12650))   |
|**Classificação**|    verbo   |
|  **Impacto**    |    O [usuário](lexicos10x5f8c4.md#l12660) transita da tela de [log in](lexicos10x5f8c4.md#l12648) para a tela de cadastro de [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Sinônimos**  |    cadastre-se, registre-se.   |
| **Requisitos** | [AP3.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.13](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# entre!
### L12652

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    entre!   |
|  **Noção**      |    O [usuário](lexicos10x5f8c4.md#l12660) clica no texto "ENTRE!"</br>O [usuário](lexicos10x5f8c4.md#l12660) clica quando deseja [entrar](lexicos10x5f8c4.md#l12648) em uma [conta](lexicos10x5f8c4.md#l12532) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) escolhe se deseja [entrar](lexicos10x5f8c4.md#l12648) usando email/nome de [usuário](lexicos10x5f8c4.md#l12660) e senha ou o Facebook.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    O [usuário](lexicos10x5f8c4.md#l12660) transita da tela de [cadastre-se](lexicos10x5f8c4.md#l12649) para a tela de login.   |
|  **Sinônimos**  |    login.   |
| **Requisitos** | [INT3.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# esqueceu sua senha
### L12654

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    esqueceu sua senha   |
|  **Noção**      |    O [usuário](lexicos10x5f8c4.md#l12660) clica no texto “Esqueceu sua senha?”</br>O [usuário](lexicos10x5f8c4.md#l12660) clica quando deseja recuperar sua [conta](lexicos10x5f8c4.md#l12532) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) insere o email ao qual a [conta](lexicos10x5f8c4.md#l12532) foi vinculada.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    O [usuário](lexicos10x5f8c4.md#l12660) receberá um email que o levará para uma página de redefinição de senha.   |
|  **Sinônimos**  |    recuperar senha, recuperar conta, redefinir senha.   |
| **Requisitos** | [BR1.14](https://welisonr.github.io/2019.1-Requisitos-Brainly/brainstorm/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# infrator
### L12531

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    infrator   |
|  **Noção**      |    [pessoa](lexicos10x5f8c4.md#l12660) que não cumpre com as políticas do regulamento do Brainly.</br>Responsável pela perda de tempo de [moderadores](lexicos10x5f8c4.md#l12528) e estudantes devido ao cometimento de irregularidades.   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    O infrator prática irregularidades na plataforma;</br>O infrator prejudica aos [moderadores](lexicos10x5f8c4.md#l12528), aos estudantes e à plataforma devido ao tempo e recurso gasto.</br>O infrator participa em [perguntas](lexicos10x5f8c4.md#l12494), [respostas](lexicos10x5f8c4.md#l12521), [comentários](lexicos10x5f8c4.md#l12506) e no chat de maneira inadequada.</br>O infrator prática spam, brincadeiras e pedidos de informações pessoais.   |
|  **Sinônimos**  |    infratores.   |
| **Requisitos** | [INT2.10](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) |   |



# log in
### L12648

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    log in   |
|  **Noção**      |    O [usuário](lexicos10x5f8c4.md#l12660) [loga](lexicos10x5f8c4.md#l12651).</br>O [usuário](lexicos10x5f8c4.md#l12660) [loga](lexicos10x5f8c4.md#l12651) quando deseja entrar em sua [conta](lexicos10x5f8c4.md#l12532) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) digita seu nome de [usuário](lexicos10x5f8c4.md#l12660) ou email e senha.   |
|**Classificação**|    verbo   |
|  **Impacto**    |    O [usuário](lexicos10x5f8c4.md#l12660) está em sua [conta](lexicos10x5f8c4.md#l12532) no Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) ganha [pontos](lexicos10x5f8c4.md#l12492) por entrar em sua [conta](lexicos10x5f8c4.md#l12532) periodicamente.</br>O [usuário](lexicos10x5f8c4.md#l12660) pode fazer [perguntas](lexicos10x5f8c4.md#l12494).</br>O [usuário](lexicos10x5f8c4.md#l12660) pode [responder](lexicos10x5f8c4.md#l12489) [perguntas](lexicos10x5f8c4.md#l12494) e ganha [pontos](lexicos10x5f8c4.md#l12492) por essas [respostas](lexicos10x5f8c4.md#l12521).   |
|  **Sinônimos**  |    entrar, logar.   |
| **Requisitos** | [INT3.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [cadastrar](lexicos10x5f8c4.md#l12647) |
|   | [entre agora!](lexicos10x5f8c4.md#l12649) |



# logado
### L12651

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    logado   |
|  **Noção**      |    [usuário](lexicos10x5f8c4.md#l12660) ainda não está logado ao sistema</br></br>Isso ocorre quando o [usuário](lexicos10x5f8c4.md#l12660) não logou no sistema ou quando acabou de se desconectar   |
|**Classificação**|    estado   |
|  **Impacto**    |    Quando o [usuário](lexicos10x5f8c4.md#l12660) está logado ele possui:</br></br>-[ranking](lexicos10x5f8c4.md#l12498) </br>-[pontos](lexicos10x5f8c4.md#l12492) </br>-[níveis](lexicos10x5f8c4.md#l12491) </br>[usuário](lexicos10x5f8c4.md#l12660) pode [responder](lexicos10x5f8c4.md#l12489) e fazer [perguntas](lexicos10x5f8c4.md#l12494).</br>Estado:</br>-[usuário](lexicos10x5f8c4.md#l12660) logado</br></br>[usuário](lexicos10x5f8c4.md#l12660) se desconecta : Estado – [usuário](lexicos10x5f8c4.md#l12660) [deslogado](lexicos10x5f8c4.md#l12653).   |
|  **Sinônimos**  |    loga, logou, conectado, entrou.   |
| **Requisitos** | [INT3.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [responder tarefa](cenarios10x5f8c4.md#c2997) | [entrar com facebook](lexicos10x5f8c4.md#l12650) |
| [iniciar desafios](cenarios10x5f8c4.md#c2998) | [deslogado](lexicos10x5f8c4.md#l12653) |
| [fazer uma pergunta](cenarios10x5f8c4.md#c3036) | [confirmar email](lexicos10x5f8c4.md#l12657) |
| [alterar perfil](cenarios10x5f8c4.md#c3032) |   |
| [adicionar anexo para pergunta](cenarios10x5f8c4.md#c3033) |   |
| [adicionar símbolo para pergunta](cenarios10x5f8c4.md#c3034) |   |
| [adicionar equação para pergunta](cenarios10x5f8c4.md#c3035) |   |
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) |   |
| [deletar conta](cenarios10x5f8c4.md#id=3039) |   |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) |   |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) |   |
| [adicionar comentário](cenarios10x5f8c4.md#c3042) |   |



# matéria
### L12499

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    matéria   |
|  **Noção**      |    Área de conhecimento.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    As [perguntas](lexicos10x5f8c4.md#l12494) são divididas por matéria;</br>Um [usuário](lexicos10x5f8c4.md#l12660) pode filtrar os resultados por matéria.   |
|  **Sinônimos**  |    materias, tema, matérias.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [fazer uma pergunta](cenarios10x5f8c4.md#c3036) |   |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) |   |



# melhor resposta
### L12490

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    melhor resposta   |
|  **Noção**      |    Solução mais adequada, ou que melhor tirou a [dúvida](lexicos10x5f8c4.md#l12494).   |
|**Classificação**|    estado   |
|  **Impacto**    |    Um [usuário](lexicos10x5f8c4.md#l12660) ao ter sua [dúvida](lexicos10x5f8c4.md#l12494) respondida pode escolher a melhor [resposta](lexicos10x5f8c4.md#l12521).</br>Ao [responder](lexicos10x5f8c4.md#l12489) um [usuário](lexicos10x5f8c4.md#l12660) pode ganhar melhor [resposta](lexicos10x5f8c4.md#l12521).</br>Uma certa quantidade de melhores [respostas](lexicos10x5f8c4.md#l12521) é necessária para subir de [nível](lexicos10x5f8c4.md#l12491).   |
|  **Sinônimos**  |    melhores respostas.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [nível](lexicos10x5f8c4.md#l12491) |
|   | [pergunta](lexicos10x5f8c4.md#l12494) |
|   | [notificações](lexicos10x5f8c4.md#l12509) |
|   | [pergunta respondida](lexicos10x5f8c4.md#l12644) |



# mensagens
### L12508

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    mensagens   |
|  **Noção**      |    Informações trocadas em forma de texto.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Um [moderador](lexicos10x5f8c4.md#l12528) poder chamar atenção de alguém ou fazer um esclarecimento.</br>Um [usuário](lexicos10x5f8c4.md#l12660) pode mandar mensagem para o [moderador](lexicos10x5f8c4.md#l12528).</br>A [comunidade](lexicos10x5f8c4.md#l12525) não pode trocar mensagem privada.   |
|  **Sinônimos**  |    mensagem, mensagem privada.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [usuário](lexicos10x5f8c4.md#l12660) |



# moderador
### L12528

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    moderador   |
|  **Noção**      |    [pessoa](lexicos10x5f8c4.md#l12660) que modera os conteúdos do Brainly.</br>Responsável por esclarecer as políticas da plataforma à [comunidade](lexicos10x5f8c4.md#l12525);</br>Responsável por manter o [nível](lexicos10x5f8c4.md#l12491) de qualidade da plataforma em [pergunta](lexicos10x5f8c4.md#l12494), [resposta](lexicos10x5f8c4.md#l12521) e [comentário](lexicos10x5f8c4.md#l12506).   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    O moderador exclui [pergunta](lexicos10x5f8c4.md#l12494), [resposta](lexicos10x5f8c4.md#l12521) ou [comentário](lexicos10x5f8c4.md#l12506) indevido;</br>O moderador comunica [infratores](lexicos10x5f8c4.md#l12531) as políticas do regulamento;</br>O moderador retira [dúvida](lexicos10x5f8c4.md#l12494) de estudantes sobre o regulamento da plataforma;</br>O moderador pode [bloquear usuários](lexicos10x5f8c4.md#l12574) irregulares.</br>O moderador define [respostas verificadas](lexicos10x5f8c4.md#l12522), corretas.   |
|  **Sinônimos**  |    moderadores.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [mensagens](lexicos10x5f8c4.md#l12508) |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) | [administrador](lexicos10x5f8c4.md#l12529) |
|   | [denunciar](lexicos10x5f8c4.md#l12533) |
|   | [bloquear usuário](lexicos10x5f8c4.md#l12574) |
|   | [editar](lexicos10x5f8c4.md#l12659) |
|   | [usuário](lexicos10x5f8c4.md#l12660) |



# nível
### L12491

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    nível   |
|  **Noção**      |    Classificação do desempenho do [usuário](lexicos10x5f8c4.md#l12660).   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Para subir de nível é necessário alcançar uma meta de [pontos](lexicos10x5f8c4.md#l12492) e de [melhor resposta](lexicos10x5f8c4.md#l12490).</br>Níveis podem servir como meta para [usuários](lexicos10x5f8c4.md#l12525).   |
|  **Sinônimos**  |    níveis.   |
| **Requisitos** | [EN2.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/),  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) | [melhor resposta](lexicos10x5f8c4.md#l12490) |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) | [pontos](lexicos10x5f8c4.md#l12492) |
|   | [notificações](lexicos10x5f8c4.md#l12509) |
|   | [moderador](lexicos10x5f8c4.md#l12528) |



# nível das perguntas
### L12656

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    nível das perguntas   |
|  **Noção**      |    Divisão de dificuldade por escolaridade.</br>Responsável por uma melhor divisão das [perguntas](lexicos10x5f8c4.md#l12494).   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Divide as [perguntas](lexicos10x5f8c4.md#l12494) nas dificuldades:</br>-Ensino Fundamental(Básico)</br>-Ensino Médio(Secundário)</br>-Ensino Superior   |
|  **Sinônimos**  |    dificuldade das perguntas, level das perguntas.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) |   |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) |   |



# notificações
### L12509

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    notificações   |
|  **Noção**      |    Feedback do sistema.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Uma [pessoa](lexicos10x5f8c4.md#l12660) recebe uma notificação ao receber um [obrigado](lexicos10x5f8c4.md#l12497), ter uma [pergunta expirada](lexicos10x5f8c4.md#l12510) ou respondida, cumprir um [desafio](lexicos10x5f8c4.md#l12496), ganhar um [emblema](lexicos10x5f8c4.md#l12495), ganhar [melhor resposta](lexicos10x5f8c4.md#l12490), subir de [nível](lexicos10x5f8c4.md#l12491) ou quando outra [pessoa](lexicos10x5f8c4.md#l12660) adiciona [comentário](lexicos10x5f8c4.md#l12506) em sua [pergunta](lexicos10x5f8c4.md#l12494) ou [resposta](lexicos10x5f8c4.md#l12521).   |
|  **Sinônimos**  |    notificação, aviso.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [administrador](lexicos10x5f8c4.md#l12529) |



# obrigados
### L12497

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    obrigados   |
|  **Noção**      |    Agradecimento.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Obrigados são representados por corações.</br>Pode-se agradecer a uma [resposta](lexicos10x5f8c4.md#l12521) com um obrigado.   |
|  **Sinônimos**  |    botão de agradecimento, obrigado.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [dar obrigado](cenarios10x5f8c4.md#c2999) |   |



# perfil
### L12532

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    perfil   |
|  **Noção**      |    Ambiente que possui as informações do [usuário](lexicos10x5f8c4.md#l12660).   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Apresenta as informações do [usuário](lexicos10x5f8c4.md#l12660).</br>Permite o [usuário](lexicos10x5f8c4.md#l12660) alterar algumas de sua informações.   |
|  **Sinônimos**  |    perfis, conta, contas.   |
| **Requisitos** | [INT1.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [iniciar desafios](cenarios10x5f8c4.md#c2998) |   |
| [fazer uma pergunta](cenarios10x5f8c4.md#c3036) |   |
| [alterar perfil](cenarios10x5f8c4.md#c3032) |   |
| [adicionar anexo para pergunta](cenarios10x5f8c4.md#c3033) |   |
| [adicionar símbolo para pergunta](cenarios10x5f8c4.md#c3034) |   |
| [adicionar equação para pergunta](cenarios10x5f8c4.md#c3035) |   |
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) |   |
| [deletar conta](cenarios10x5f8c4.md#id=3039) |   |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) |   |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) |   |



# pergunta
### L12494

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    pergunta   |
|  **Noção**      |    Questão proposta para que alguém tire uma dúvida.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Para fazer um pergunta o [usuário](lexicos10x5f8c4.md#l12660) deve oferecer [pontos](lexicos10x5f8c4.md#l12492).</br>Quando alguém tem sua [pergunta respondida](lexicos10x5f8c4.md#l12644), pode escolher a [melhor resposta](lexicos10x5f8c4.md#l12490).   |
|  **Sinônimos**  |    tarefa, dúvida, tarefas, perguntas.   |
| **Requisitos** | [EN2.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [AP1.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.9](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [responder tarefa](cenarios10x5f8c4.md#c2997) | [pontos](lexicos10x5f8c4.md#l12492) |
| [iniciar desafios](cenarios10x5f8c4.md#c2998) | [comentário](lexicos10x5f8c4.md#l12506) |
| [dar obrigado](cenarios10x5f8c4.md#c2999) | [notificações](lexicos10x5f8c4.md#l12509) |
| [pesquisar](cenarios10x5f8c4.md#c3000) | [pergunta expirada](lexicos10x5f8c4.md#l12510) |
| [fazer uma pergunta](cenarios10x5f8c4.md#c3036) | [tarefas resolvidas](lexicos10x5f8c4.md#l12512) |
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [tarefas adicionadas](lexicos10x5f8c4.md#l12514) |
| [adicionar anexo para pergunta](cenarios10x5f8c4.md#c3033) | [recebendo resposta](lexicos10x5f8c4.md#l12520) |
| [adicionar símbolo para pergunta](cenarios10x5f8c4.md#c3034) | [moderador](lexicos10x5f8c4.md#l12528) |
| [adicionar equação para pergunta](cenarios10x5f8c4.md#c3035) | [denunciar](lexicos10x5f8c4.md#l12533) |
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) | [pergunta popular](lexicos10x5f8c4.md#l12575) |
| [pesquisar pelo google](cenarios10x5f8c4.md#c3038) | [editar](lexicos10x5f8c4.md#l12659) |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) |   |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) |   |
| [adicionar comentário](cenarios10x5f8c4.md#c3042) |   |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) |   |



# pergunta expirada
### L12510

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    pergunta expirada   |
|  **Noção**      |    [pergunta](lexicos10x5f8c4.md#l12494) com prazo de [resposta](lexicos10x5f8c4.md#l12521) vencido.   |
|**Classificação**|    estado   |
|  **Impacto**    |    Ao ter o prazo de [resposta](lexicos10x5f8c4.md#l12521) vencido os [pontos](lexicos10x5f8c4.md#l12492) oferecidos são devolvidos.</br>Uma [pergunta](lexicos10x5f8c4.md#l12494) expirada é eliminada do brainly.   |
|  **Sinônimos**  |    pergunta deletada, tarefa expirada.   |
| **Requisitos** | [AP1.9](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [BR2.15](https://welisonr.github.io/2019.1-Requisitos-Brainly/brainstorm/)|


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [notificações](lexicos10x5f8c4.md#l12509) |



# pergunta popular
### L12575

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    pergunta popular   |
|  **Noção**      |    [pergunta](lexicos10x5f8c4.md#l12494) muito acessada por estudantes.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    A [pergunta](lexicos10x5f8c4.md#l12494) popular recebe maior destaque no Brainly.</br>A [pergunta](lexicos10x5f8c4.md#l12494) popular é responsável por atrair maior acesso à plataforma.</br>O [time de respostas](lexicos10x5f8c4.md#l12576), os [moderadores](lexicos10x5f8c4.md#l12528), os [universitários](lexicos10x5f8c4.md#l12577), a [administração](lexicos10x5f8c4.md#l12529) e os [usuários](lexicos10x5f8c4.md#l12525) empenham-se mais em [responder](lexicos10x5f8c4.md#l12489) essas [perguntas](lexicos10x5f8c4.md#l12494).   |
|  **Sinônimos**  |    perguntas populares, populares, questões populares, questão popular.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# pergunta respondida
### L12644

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    pergunta respondida   |
|  **Noção**      |    Questões [respondidas](lexicos10x5f8c4.md#l12521) pela [comunidade](lexicos10x5f8c4.md#l12525).   |
|**Classificação**|    estado   |
|  **Impacto**    |    Os [usuários](lexicos10x5f8c4.md#l12525) podem agradecer pela [resposta](lexicos10x5f8c4.md#l12521);</br>Os [usuários](lexicos10x5f8c4.md#l12525) que teve sua [dúvida](lexicos10x5f8c4.md#l12494) tirada pode escolher a [melhor resposta](lexicos10x5f8c4.md#l12490).   |
|  **Sinônimos**  |    tarefa respondida, dúvida tirada.   |
| **Requisitos** | [AP1.13](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [pergunta](lexicos10x5f8c4.md#l12494) |



# política de privacidade
### L12645

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    política de privacidade   |
|  **Noção**      |    Documento que explica como os dados pessoais do [usuário](lexicos10x5f8c4.md#l12660) são conectados e processados pelo Brainly para fins de acesso, registro ou uso.</br>Documento que descreve os termos e as finalidades de processamento dos dados pessoais do [usuário](lexicos10x5f8c4.md#l12660).   |
|**Classificação**|    objeto   |
|  **Impacto**    |    O [usuário](lexicos10x5f8c4.md#l12660) lê a política de privacidade do Brainly.</br>O [usuário](lexicos10x5f8c4.md#l12660) concorda com a política de privacidade para utilizar o Brainly.</br>Se o [usuário](lexicos10x5f8c4.md#l12660) não concordar com a política de privacidade, não deve utilizar o Brainly e preencher, compartilhar ou armazenar dados pessoais nele.   |
|  **Sinônimos**  |    termos de privacidade.   |
| **Requisitos** |  |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [cadastrar](lexicos10x5f8c4.md#l12647) |



# pontos
### L12492

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    pontos   |
|  **Noção**      |    Método de premiação.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    Um [usuário](lexicos10x5f8c4.md#l12660) ganha pontos ao [responder](lexicos10x5f8c4.md#l12489) uma [pergunta](lexicos10x5f8c4.md#l12494).</br>Para fazer uma [pergunta](lexicos10x5f8c4.md#l12494) é necessário oferecer pontos.</br>É necessário alcançar uma meta de pontos para subir de [nível](lexicos10x5f8c4.md#l12491).</br>Ao cumprir [desafios](lexicos10x5f8c4.md#l12496) o [usuário](lexicos10x5f8c4.md#l12660) ganha pontos.   |
|  **Sinônimos**  |    pontuação, ponto.   |
| **Requisitos** | [EN2.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN1.1](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [iniciar desafios](cenarios10x5f8c4.md#c2998) | [responder](lexicos10x5f8c4.md#l12489) |
| [fazer uma pergunta](cenarios10x5f8c4.md#c3036) | [nível](lexicos10x5f8c4.md#l12491) |
| [adicionar anexo para pergunta](cenarios10x5f8c4.md#c3033) | [pergunta](lexicos10x5f8c4.md#l12494) |
| [adicionar símbolo para pergunta](cenarios10x5f8c4.md#c3034) | [desafios](lexicos10x5f8c4.md#l12496) |
| [adicionar equação para pergunta](cenarios10x5f8c4.md#c3035) | [rankings](lexicos10x5f8c4.md#l12498) |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) | [pergunta expirada](lexicos10x5f8c4.md#l12510) |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) | [cadastrar](lexicos10x5f8c4.md#l12647) |
|   | [log in](lexicos10x5f8c4.md#l12648) |
|   | [logado](lexicos10x5f8c4.md#l12651) |
|   | [confirmar email](lexicos10x5f8c4.md#l12657) |



# rankings
### L12498

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    rankings   |
|  **Noção**      |    Listagem dos melhores.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    As [pessoas](lexicos10x5f8c4.md#l12660) com mais [pontos](lexicos10x5f8c4.md#l12492) aparecem no ranking.</br>o ranking é dividido em diário, semanal e mensal.   |
|  **Sinônimos**  |    ranking.   |
| **Requisitos** | [EN1.1](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN2.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN2.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# recebendo resposta
### L12520

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    recebendo resposta   |
|  **Noção**      |    [perguntas](lexicos10x5f8c4.md#l12494) que estão sendo [respondidas](lexicos10x5f8c4.md#l12521).   |
|**Classificação**|    estado   |
|  **Impacto**    |    Quando uma [pergunta](lexicos10x5f8c4.md#l12494) já está sendo respondida por duas [pessoas](lexicos10x5f8c4.md#l12660), outras [pessoas](lexicos10x5f8c4.md#l12660) podem apenas fazer [comentários](lexicos10x5f8c4.md#l12506);</br>O [usuário](lexicos10x5f8c4.md#l12660) que fez a [pergunta](lexicos10x5f8c4.md#l12494) recebe uma [notificação](lexicos10x5f8c4.md#l12509) que sua [pergunta](lexicos10x5f8c4.md#l12494) está sendo respondida.   |
|  **Sinônimos**  |    tarefa sendo respondida.   |
| **Requisitos** | [EN2.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [INT1.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# repetir desafio
### L12655

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    repetir desafio   |
|  **Noção**      |    Realizado por um [usuário](lexicos10x5f8c4.md#l12660).</br>Acontece quando o [usuário](lexicos10x5f8c4.md#l12660) falha um [desafio](lexicos10x5f8c4.md#l12496) e quer tentar novamente.</br>[usuário](lexicos10x5f8c4.md#l12660) ao falhar um [desafio](lexicos10x5f8c4.md#l12496) pode clicar em repita para tentar novamente aquele [desafio](lexicos10x5f8c4.md#l12496).   |
|**Classificação**|    verbo   |
|  **Impacto**    |    [desafio](lexicos10x5f8c4.md#l12496) está aberto e pode ser tentado novamente.</br></br>Se o [desafio](lexicos10x5f8c4.md#l12496) está aberto não se pode clicar em repita.   |
|  **Sinônimos**  |    tentar desafio novamente, outra tentativa do desafio.   |
| **Requisitos** | [AP1.8](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# responder
### L12489

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    responder   |
|  **Noção**      |    Tirar [dúvida](lexicos10x5f8c4.md#l12494) de outro [usuário](lexicos10x5f8c4.md#l12660).   |
|**Classificação**|    verbo   |
|  **Impacto**    |    Responder gera [pontos](lexicos10x5f8c4.md#l12492).</br>A [resposta](lexicos10x5f8c4.md#l12521) deve ser detalhada para que o [usuário](lexicos10x5f8c4.md#l12660) com [dúvida](lexicos10x5f8c4.md#l12494) entenda.   |
|  **Sinônimos**  |    responde.   |
| **Requisitos** | [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [INT1.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [iniciar desafios](cenarios10x5f8c4.md#c2998) | [melhor resposta](lexicos10x5f8c4.md#l12490) |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) | [pontos](lexicos10x5f8c4.md#l12492) |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) | [tarefas resolvidas](lexicos10x5f8c4.md#l12512) |
|   | [comunidade](lexicos10x5f8c4.md#l12525) |
|   | [pergunta popular](lexicos10x5f8c4.md#l12575) |
|   | [cadastrar](lexicos10x5f8c4.md#l12647) |
|   | [log in](lexicos10x5f8c4.md#l12648) |
|   | [logado](lexicos10x5f8c4.md#l12651) |



# respondidas
### L12521

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    respondidas   |
|  **Noção**      |    Dúvidas Tiradas ou respondidas.   |
|**Classificação**|    estado   |
|  **Impacto**    |    [perguntas](lexicos10x5f8c4.md#l12494) com duas respostas,  apenas podem receber [comentários](lexicos10x5f8c4.md#l12506).</br>Pode-se agradecer ou qualificar respostas.   |
|  **Sinônimos**  |    resposta, respostas.   |
| **Requisitos** | [EN2.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/=), [INT1.5](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [dar obrigado](cenarios10x5f8c4.md#c2999) | [tarefas resolvidas](lexicos10x5f8c4.md#l12512) |
| [pesquisar](cenarios10x5f8c4.md#c3000) | [sem resposta](lexicos10x5f8c4.md#l12519) |
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [recebendo resposta](lexicos10x5f8c4.md#l12520) |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) | [time de respostas](lexicos10x5f8c4.md#l12576) |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) | [universitário](lexicos10x5f8c4.md#l12577) |
| [adicionar comentário](cenarios10x5f8c4.md#c3042) | [pergunta respondida](lexicos10x5f8c4.md#l12644) |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) |   |



# respostas verificadas
### L12522

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    respostas verificadas   |
|  **Noção**      |    [respostas](lexicos10x5f8c4.md#l12521) revisadas, que foram destacadas devido seu detalhamento e precisão.   |
|**Classificação**|    estado   |
|  **Impacto**    |    As [melhores respostas](lexicos10x5f8c4.md#l12490) analisadas pelo time tornam-se verificadas.</br>Ao fazer uma pesquisa são mostradas as [respostas](lexicos10x5f8c4.md#l12521) verificadas.   |
|  **Sinônimos**  |    tarefas verificadas, respostas revisadas, resposta revisada.   |
| **Requisitos** | [AP3.2](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [pesquisar](cenarios10x5f8c4.md#c3000) | [moderador](lexicos10x5f8c4.md#l12528) |



# sem resposta
### L12519

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    sem resposta   |
|  **Noção**      |    não respondida.   |
|**Classificação**|    estado   |
|  **Impacto**    |    [perguntas](lexicos10x5f8c4.md#l12494) que podem ser [respondidas](lexicos10x5f8c4.md#l12521).</br>[tarefas](lexicos10x5f8c4.md#l12494) que ficam muito tempo sem [resposta](lexicos10x5f8c4.md#l12521) são deletadas.   |
|  **Sinônimos**  |    tarefa sem resposta.   |
| **Requisitos** | [BR2.15](https://welisonr.github.io/2019.1-Requisitos-Brainly/brainstorm/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [responder tarefa](cenarios10x5f8c4.md#c2997) |   |



# tarefas adicionadas
### L12514

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    tarefas adicionadas   |
|  **Noção**      |    [pergunta](lexicos10x5f8c4.md#l12494) feita.   |
|**Classificação**|    estado   |
|  **Impacto**    |    As dúvidas tiradas são salvas em [tarefas](lexicos10x5f8c4.md#l12494) adicionadas.</br>As [tarefas](lexicos10x5f8c4.md#l12494) adicionadas servem para [usuário](lexicos10x5f8c4.md#l12660) rever uma [pergunta](lexicos10x5f8c4.md#l12494).   |
|  **Sinônimos**  |    pergunta adicionada.   |
| **Requisitos** | [AP1.3,](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) [AP1.9](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# tarefas resolvidas
### L12512

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    tarefas resolvidas   |
|  **Noção**      |    [perguntas](lexicos10x5f8c4.md#l12494) [respondidas](lexicos10x5f8c4.md#l12521).   |
|**Classificação**|    estado   |
|  **Impacto**    |    Ao [responder](lexicos10x5f8c4.md#l12489) uma [pergunta](lexicos10x5f8c4.md#l12494) a [tarefa](lexicos10x5f8c4.md#l12494) fica salva em [tarefas](lexicos10x5f8c4.md#l12494) [respondidas](lexicos10x5f8c4.md#l12521).</br>As [perguntas](lexicos10x5f8c4.md#l12494) resolvidas servem para o [comunidade](lexicos10x5f8c4.md#l12525) ver as [respostas](lexicos10x5f8c4.md#l12521) de um [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Sinônimos**  |    perguntas resolvidas.   |
| **Requisitos** | [EN2.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [AP1.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.9](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# termos de uso
### L12646

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    termos de uso   |
|  **Noção**      |    Documento que descreve as regras e condições que um [usuário](lexicos10x5f8c4.md#l12660) deve seguir para utilizar o Brainly.   |
|**Classificação**|    objeto   |
|  **Impacto**    |    [usuário](lexicos10x5f8c4.md#l12660) lê os termos de uso do Brainly</br>O [usuário](lexicos10x5f8c4.md#l12660) concorda com os termos de uso para utilizar o Brainly</br>Se o [usuário](lexicos10x5f8c4.md#l12660) não concordar com os Termos de Uso, não deve utilizar o Brainly.   |
|  **Sinônimos**  |    condições de uso.   |
| **Requisitos** | [BR2.12](https://welisonr.github.io/2019.1-Requisitos-Brainly/brainstorm/), [AP1.13](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [cadastrar](lexicos10x5f8c4.md#l12647) |



# time de respostas
### L12576

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    time de respostas   |
|  **Noção**      |    [usuários](lexicos10x5f8c4.md#l12525) mais experientes em dar [respostas](lexicos10x5f8c4.md#l12521) na plataforma.</br>Time coordenado e selecionado pela [administração](lexicos10x5f8c4.md#l12529) do Brainly devido ao bom desempenho.   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    O time de [respostas](lexicos10x5f8c4.md#l12521) aumenta a qualidade das [perguntas](lexicos10x5f8c4.md#l12494) [respondidas](lexicos10x5f8c4.md#l12521).</br>As [perguntas populares](lexicos10x5f8c4.md#l12575) são focalizadas pelo time de [respostas](lexicos10x5f8c4.md#l12521).</br>O time de [respostas](lexicos10x5f8c4.md#l12521) recebe orientações de participação na plataforma por parte dos [administradores](lexicos10x5f8c4.md#l12529).   |
|  **Sinônimos**  |    equipe de resposta, equipes de respostas, time de resposta.   |
| **Requisitos** | [INT1.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao), [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [EN2.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [AP3.2](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [INT3.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
|   | [administrador](lexicos10x5f8c4.md#l12529) |
|   | [pergunta popular](lexicos10x5f8c4.md#l12575) |



# universitário
### L12577

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    universitário   |
|  **Noção**      |    É o [usuário](lexicos10x5f8c4.md#l12660) da plataforma que cursa ensino superior.</br>Estudante selecionado pela [administração](lexicos10x5f8c4.md#l12529) a partir de processo seletivo em universidade.</br>Possui amparo e resguardo de ações por parte da [administração](lexicos10x5f8c4.md#l12529).   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    O universitário [responde](lexicos10x5f8c4.md#l12489) questões específicas, especialmente as [perguntas populares](lexicos10x5f8c4.md#l12575).</br>O universitário recebe orientação por parte da [administração](lexicos10x5f8c4.md#l12529) sobre as [perguntas](lexicos10x5f8c4.md#l12494) a serem [respondidas](lexicos10x5f8c4.md#l12521).</br>O universitário gera [respostas](lexicos10x5f8c4.md#l12521) com alta qualidade no Brainly.   |
|  **Sinônimos**  |    acadêmico, universitários, acadêmicos.   |
| **Requisitos** | [AP1.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [INT3.6](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| - | - |



# usuário
### L12660

|  Informações    | Símbolo |
|:---------------:|:-------:|
|  **Nome**       |    usuário   |
|  **Noção**      |    Pessoa singular identificável que utiliza o Brainly.   |
|**Classificação**|    sujeito   |
|  **Impacto**    |    Um usuário tem acesso às funcionalidade comuns da plataforma (fazer [perguntas](lexicos10x5f8c4.md#l12494), escrever [respostas](lexicos10x5f8c4.md#l12521) e [comentários](lexicos10x5f8c4.md#l12506), adicionar [amigos](lexicos10x5f8c4.md#l12502), entre outras) e pode evoluir para se tornar um usuário avançado ([moderador](lexicos10x5f8c4.md#l12528) ou [administrador](lexicos10x5f8c4.md#l12529)) e acessar outras funcionalidades ([mensagens](lexicos10x5f8c4.md#l12508)).   |
|  **Sinônimos**  |    pessoas, pessoa.   |
| **Requisitos** | [EN2.4](https://welisonr.github.io/2019.1-Requisitos-Brainly/entrevista/), [AP1.1](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.3](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP1.9](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [AP3.2](https://welisonr.github.io/2019.1-Requisitos-Brainly/analise_protocolo/), [INT2.7](https://welisonr.github.io/2019.1-Requisitos-Brainly/introspeccao) |


|  **Cenários** |**Léxicos**|
|:-------------:|:---------:|
| [responder tarefa](cenarios10x5f8c4.md#c2997) | [responder](lexicos10x5f8c4.md#l12489) |
| [iniciar desafios](cenarios10x5f8c4.md#c2998) | [melhor resposta](lexicos10x5f8c4.md#l12490) |
| [dar obrigado](cenarios10x5f8c4.md#c2999) | [nível](lexicos10x5f8c4.md#l12491) |
| [pesquisar](cenarios10x5f8c4.md#c3000) | [pontos](lexicos10x5f8c4.md#l12492) |
| [fazer uma pergunta](cenarios10x5f8c4.md#c3036) | [pergunta](lexicos10x5f8c4.md#l12494) |
| [moderar denúncia](cenarios10x5f8c4.md#c3030) | [emblemas](lexicos10x5f8c4.md#l12495) |
| [alterar perfil](cenarios10x5f8c4.md#c3032) | [desafios](lexicos10x5f8c4.md#l12496) |
| [adicionar anexo para pergunta](cenarios10x5f8c4.md#c3033) | [matéria](lexicos10x5f8c4.md#l12499) |
| [adicionar símbolo para pergunta](cenarios10x5f8c4.md#c3034) | [mensagens](lexicos10x5f8c4.md#l12508) |
| [adicionar equação para pergunta](cenarios10x5f8c4.md#c3035) | [tarefas resolvidas](lexicos10x5f8c4.md#l12512) |
| [alterar nível das perguntas](cenarios10x5f8c4.md#c3037) | [tarefas adicionadas](lexicos10x5f8c4.md#l12514) |
| [pesquisar pelo google](cenarios10x5f8c4.md#c3038) | [emblemas mais próximos](lexicos10x5f8c4.md#l12516) |
| [deletar conta](cenarios10x5f8c4.md#id=3039) | [emblemas conquistados.](lexicos10x5f8c4.md#l12518) |
| [filtrar perguntas por matéria](cenarios10x5f8c4.md#c3040) | [recebendo resposta](lexicos10x5f8c4.md#l12520) |
| [filtrar perguntas por nível escolar ](cenarios10x5f8c4.md#c3041) | [administrador](lexicos10x5f8c4.md#l12529) |
| [adicionar comentário](cenarios10x5f8c4.md#c3042) | [perfil](lexicos10x5f8c4.md#l12532) |
| [pedir correção de contéudo](cenarios10x5f8c4.md#c3045) | [denunciar](lexicos10x5f8c4.md#l12533) |
|   | [banido](lexicos10x5f8c4.md#l12534) |
|   | [bloquear usuário](lexicos10x5f8c4.md#l12574) |
|   | [universitário](lexicos10x5f8c4.md#l12577) |
|   | [política de privacidade](lexicos10x5f8c4.md#l12645) |
|   | [termos de uso](lexicos10x5f8c4.md#l12646) |
|   | [cadastrar](lexicos10x5f8c4.md#l12647) |
|   | [log in](lexicos10x5f8c4.md#l12648) |
|   | [entre agora!](lexicos10x5f8c4.md#l12649) |
|   | [entrar com facebook](lexicos10x5f8c4.md#l12650) |
|   | [logado](lexicos10x5f8c4.md#l12651) |
|   | [entre!](lexicos10x5f8c4.md#l12652) |
|   | [deslogado](lexicos10x5f8c4.md#l12653) |
|   | [esqueceu sua senha](lexicos10x5f8c4.md#l12654) |
|   | [repetir desafio](lexicos10x5f8c4.md#l12655) |
|   | [confirmar email](lexicos10x5f8c4.md#l12657) |
|   | [conta deletada](lexicos10x5f8c4.md#l12658) |
