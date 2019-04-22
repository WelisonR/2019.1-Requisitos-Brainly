# Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| [1.0](./modelagem_v1/cenarios10x58ed251.md) | 21/04/2019 | Gera primeira versão dos artefatos | Welison Regis |
| 2.0 | 22/04/2019 | Gera segunda versão dos artefatos, crawler otimizado | Welison Regis |
| 2.1 | 22/04/2019 | Adiciona introdução e descrição sobre o crawler utilizado | Welison Regis |

# Introdução

A modelagem por cenários consiste na confecção de estruturas narrativas de forma a desenvolver o contexto e descobrir informações pertinentes a ser desempenhadas pelo software. Para atingir esse objetivo, dividiu-se o cenário em: título, objetivo, contexto, atores, recursos, exceção e episódio.

O arquivo _markdown_ aqui disposto é gerado automaticamente por uma ferramenta desenvolvida em python disponível em nosso _github_ que, baseado nas _urls_, puxa todas as informações dos cenários do site [C&L](http://pes.inf.puc-rio.br/cel/aplicacao/) referente ao projeto Brainly e gera esse _markdown_ com âncoras nas palavras chaves (inclusive sinônimos). O _notebook_ com o código e as orientações está disponível em [C&L Crawler](https://github.com/WelisonR/2019.1-Requisitos-Brainly/blob/master/CeL_crawler_pucrio.ipynb).

# adicionar anexo para pergunta
### C3033

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    adicionar anexo para pergunta   |
|  **Objetivo** |    Adicionar fotos,pdfs, arquivos com terminação .txt na hora de fazer a [pergunta](lexicos10x5f8c4.md#l12494).   |
|  **Contexto** |    Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).</br>- Possuir no mínimo 10 [pontos](lexicos10x5f8c4.md#l12492) para fazer a [pergunta](lexicos10x5f8c4.md#l12494)   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    imagem ou arquivo pdf ou arquivo txt , internet,computador ou celular   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) estar sem conexão de internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) liga o computador ou celular.</br>[usuário](lexicos10x5f8c4.md#l12660) entra no Brainly pela internet ou aplicativo.</br>[usuário](lexicos10x5f8c4.md#l12660) acessa sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) decide fazer uma [pergunta](lexicos10x5f8c4.md#l12494)</br>[usuário](lexicos10x5f8c4.md#l12660) adiciona um anexo para a [pergunta](lexicos10x5f8c4.md#l12494).</br>[usuário](lexicos10x5f8c4.md#l12660) faz a [pergunta](lexicos10x5f8c4.md#l12494).   |


# adicionar comentário
### C3042

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    adicionar comentário   |
|  **Objetivo** |    adicionar conteudo a uma [resposta](lexicos10x5f8c4.md#l12521);</br>discutir uma [resposta](lexicos10x5f8c4.md#l12521).   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) disposto a contribuir;</br>brainly.   |
|  **Atores**   |    usuario;</br>[comunidade](lexicos10x5f8c4.md#l12525);   |
|  **Recursos** |    [pergunta](lexicos10x5f8c4.md#l12494);</br>[resposta](lexicos10x5f8c4.md#l12521);</br>campo para [comentário](lexicos10x5f8c4.md#l12506).   |
|  **Excecão**  |    cair a internet;</br>[usuário](lexicos10x5f8c4.md#l12660) não estar [logado](lexicos10x5f8c4.md#l12651).   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) entra no brainly;</br>[usuário](lexicos10x5f8c4.md#l12660) vê as peguntas feitas pela [comunidade](lexicos10x5f8c4.md#l12525);</br>[usuário](lexicos10x5f8c4.md#l12660) escolhe uma [pergunta](lexicos10x5f8c4.md#l12494);</br>[usuário](lexicos10x5f8c4.md#l12660) comenta na [pergunta](lexicos10x5f8c4.md#l12494) ou em alguma [resposta](lexicos10x5f8c4.md#l12521).   |


# adicionar equação para pergunta
### C3035

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    adicionar equação para pergunta   |
|  **Objetivo** |    Escrever uma sentença na [pergunta](lexicos10x5f8c4.md#l12494) e o brainly tentar transformar em uma equação(exemplo:a^2 = a²).   |
|  **Contexto** |    Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).</br>- Possuir no mínimo 10 [pontos](lexicos10x5f8c4.md#l12492) para fazer a [pergunta](lexicos10x5f8c4.md#l12494)   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    programa do brainly que transforma sua sentença em equação,internet,computador ou celular   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) estar sem conexão de internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) liga o computador ou celular.</br>[usuário](lexicos10x5f8c4.md#l12660) entra no Brainly pela internet ou aplicativo.</br>[usuário](lexicos10x5f8c4.md#l12660) acessa sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) decide fazer uma [pergunta](lexicos10x5f8c4.md#l12494)</br>[usuário](lexicos10x5f8c4.md#l12660) escreve uma sentença para a [pergunta](lexicos10x5f8c4.md#l12494).</br>Programa do brainly transforma a sentença em equação.</br>[usuário](lexicos10x5f8c4.md#l12660) faz a [pergunta](lexicos10x5f8c4.md#l12494).   |


# adicionar símbolo para pergunta
### C3034

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    adicionar símbolo para pergunta   |
|  **Objetivo** |    Adicionar símbolos matemáticos como &#960;,&#8804;</br>e outros na hora de fazer uma [pergunta](lexicos10x5f8c4.md#l12494).   |
|  **Contexto** |    Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).</br>- Possuir no mínimo 10 [pontos](lexicos10x5f8c4.md#l12492) para fazer a [pergunta](lexicos10x5f8c4.md#l12494)   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    símbolos disponíveis pelo brainly , internet,computador ou celular   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) estar sem conexão de internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) liga o computador ou celular.</br>[usuário](lexicos10x5f8c4.md#l12660) entra no Brainly pela internet ou aplicativo.</br>[usuário](lexicos10x5f8c4.md#l12660) acessa sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) decide fazer uma [pergunta](lexicos10x5f8c4.md#l12494)</br>[usuário](lexicos10x5f8c4.md#l12660) adiciona um símbolo para a [pergunta](lexicos10x5f8c4.md#l12494).</br>[usuário](lexicos10x5f8c4.md#l12660) faz a [pergunta](lexicos10x5f8c4.md#l12494).   |


# alterar nível das perguntas
### C3037

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    alterar nível das perguntas   |
|  **Objetivo** |    Trocar a [dificuldade das perguntas](lexicos10x5f8c4.md#l12656) que o [usuário](lexicos10x5f8c4.md#l12660) faz.   |
|  **Contexto** |    Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    [perfil](lexicos10x5f8c4.md#l12532),internet,computador ou celular   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) estar sem conexão de internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) liga o computador ou celular.</br>[usuário](lexicos10x5f8c4.md#l12660) entra no Brainly pela internet ou aplicativo.</br>[usuário](lexicos10x5f8c4.md#l12660) acessa sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) decide [mudar](lexicos10x5f8c4.md#l12659) o [nível](lexicos10x5f8c4.md#l12491) de [perguntas](lexicos10x5f8c4.md#l12494) da sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) acessa  [editar](lexicos10x5f8c4.md#l12659) [perfil](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) acessa [editar](lexicos10x5f8c4.md#l12659) configurações.</br>[usuário](lexicos10x5f8c4.md#l12660) altera [perfil](lexicos10x5f8c4.md#l12532) mudando o [nível](lexicos10x5f8c4.md#l12491) de escolaridade.</br>[usuário](lexicos10x5f8c4.md#l12660) ao [mudar](lexicos10x5f8c4.md#l12659) [nível](lexicos10x5f8c4.md#l12491) de escolaridade também muda o [nível das perguntas](lexicos10x5f8c4.md#l12656).   |


# alterar perfil
### C3032

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    alterar perfil   |
|  **Objetivo** |    Alterar informações da [conta](lexicos10x5f8c4.md#l12532) do [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Contexto** |    Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    [conta](lexicos10x5f8c4.md#l12532) de [usuário](lexicos10x5f8c4.md#l12660),internet,computador ou celular   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) estar sem conexão de internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) liga o computador ou celular.</br>[usuário](lexicos10x5f8c4.md#l12660) entra no Brainly pela internet ou aplicativo.</br>[usuário](lexicos10x5f8c4.md#l12660) acessa sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) decide trocar alguma ou algumas informações de sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) entra em [editar](lexicos10x5f8c4.md#l12659) [perfil](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) altera a informação ou as informações da sua [conta](lexicos10x5f8c4.md#l12532).   |


# dar obrigado
### C2999

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    dar obrigado   |
|  **Objetivo** |    Agradecer por uma [resposta](lexicos10x5f8c4.md#l12521).   |
|  **Contexto** |    Local:</br>- Plataforma Brainly</br></br>Pré-condições:</br>- Ter acesso à internet.   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    [pergunta](lexicos10x5f8c4.md#l12494), [respostas](lexicos10x5f8c4.md#l12521), [botão de agradecimento](lexicos10x5f8c4.md#l12497);   |
|  **Excecão**  |    O servidor do site caiu.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) ler uma [resposta](lexicos10x5f8c4.md#l12521);</br>[usuário](lexicos10x5f8c4.md#l12660) entende a [tarefa](lexicos10x5f8c4.md#l12494);</br>[usuário](lexicos10x5f8c4.md#l12660) clica no coração pra dar [obrigado](lexicos10x5f8c4.md#l12497).   |


# deletar conta
### C3029

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    deletar conta   |
|  **Objetivo** |    Retirar sua [conta](lexicos10x5f8c4.md#l12532) da plataforma Brainly   |
|  **Contexto** |    Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    [conta](lexicos10x5f8c4.md#l12532),internet,computador ou celular   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) estar sem conexão de internet.</br>Servidores da plataforma estarem offline.</br>Ninguém confirmar o apagamento da sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) liga o computador ou celular.</br>[usuário](lexicos10x5f8c4.md#l12660) entra no Brainly pela internet ou aplicativo.</br>[usuário](lexicos10x5f8c4.md#l12660) acessa sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) decide apagar sua [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) acessa  [editar](lexicos10x5f8c4.md#l12659) [perfil](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) acessa [editar](lexicos10x5f8c4.md#l12659) configurações.</br>[usuário](lexicos10x5f8c4.md#l12660) clica na opção quero eliminar minha [conta](lexicos10x5f8c4.md#l12532).</br>[usuário](lexicos10x5f8c4.md#l12660) usa o formulário de contato confirmar sua decisão.</br>[usuário](lexicos10x5f8c4.md#l12660) espera sua [conta](lexicos10x5f8c4.md#l12532) ser apagada, ou seja [conta deletada](lexicos10x5f8c4.md#l12658).   |


# fazer uma pergunta
### C3036

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    fazer uma pergunta   |
|  **Objetivo** |    Tirar uma duvida;   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) com [dúvida](lexicos10x5f8c4.md#l12494)</br></br>Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).</br>- Possuir no mínimo 10 [pontos](lexicos10x5f8c4.md#l12492) para fazer a [pergunta](lexicos10x5f8c4.md#l12494)   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    campos de texto, anexo, equações e símbolos.   |
|  **Excecão**  |    cair a internet;</br>servidor cair.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) clica no botão faça sua [pergunta](lexicos10x5f8c4.md#l12494)</br>[usuário](lexicos10x5f8c4.md#l12660) digita sua [dúvida](lexicos10x5f8c4.md#l12494)</br>[usuário](lexicos10x5f8c4.md#l12660) pode adicionar anexo</br>[usuário](lexicos10x5f8c4.md#l12660) pode adicionar equações</br>[usuário](lexicos10x5f8c4.md#l12660) pode adicionar símbolo</br>[usuário](lexicos10x5f8c4.md#l12660) escolhe a [matéria](lexicos10x5f8c4.md#l12499) relacionada</br>[usuário](lexicos10x5f8c4.md#l12660) oferece os [pontos](lexicos10x5f8c4.md#l12492) para [pergunta](lexicos10x5f8c4.md#l12494)</br>Para concluir, o [usuário](lexicos10x5f8c4.md#l12660) clica em um novo botão também com o nome faça sua [pergunta](lexicos10x5f8c4.md#l12494)   |


# filtrar perguntas por matéria
### C3040

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    filtrar perguntas por matéria   |
|  **Objetivo** |    encontrar [perguntas](lexicos10x5f8c4.md#l12494) com que se possa contribuir ([responder](lexicos10x5f8c4.md#l12489))   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) disposto à contribuir e ganhar [pontos](lexicos10x5f8c4.md#l12492).</br></br>Local: Plataforma Brainly</br></br>Pré-condições:</br>- Possuir uma [conta](lexicos10x5f8c4.md#l12532) no Brainly;</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Recursos** |    [perfil](lexicos10x5f8c4.md#l12532) no Brainly;</br>Lista de [matérias](lexicos10x5f8c4.md#l12499).   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) sem conexão com a internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) acessa o Brainly.</br>[usuário](lexicos10x5f8c4.md#l12660) entra em sua [conta](lexicos10x5f8c4.md#l12532).</br></br>Plataforma mobile:</br>Na aba [resposta](lexicos10x5f8c4.md#l12521), o [usuário](lexicos10x5f8c4.md#l12660) clica em [matéria](lexicos10x5f8c4.md#l12499) e escolhe uma [matéria](lexicos10x5f8c4.md#l12499) na lista apresentada.</br></br>Plataforma Web:</br>Na lista apresentada no lado esquerdo da página principal, o [usuário](lexicos10x5f8c4.md#l12660) escolhe uma [matéria](lexicos10x5f8c4.md#l12499).</br></br>[usuário](lexicos10x5f8c4.md#l12660) escolhe uma [pergunta](lexicos10x5f8c4.md#l12494) que possa contribuir.</br>[usuário](lexicos10x5f8c4.md#l12660) [responde](lexicos10x5f8c4.md#l12489) a [pergunta](lexicos10x5f8c4.md#l12494).</br>[usuário](lexicos10x5f8c4.md#l12660) recebe [pontos](lexicos10x5f8c4.md#l12492) pela [resposta](lexicos10x5f8c4.md#l12521).   |


# filtrar perguntas por nível escolar
### C3041

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    filtrar perguntas por nível escolar   |
|  **Objetivo** |    encontrar [perguntas](lexicos10x5f8c4.md#l12494) com que se possa contribuir ([responder](lexicos10x5f8c4.md#l12489))   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) disposto à contribuir e ganhar [pontos](lexicos10x5f8c4.md#l12492).</br></br>Local: Plataforma Brainly.</br></br>Pré-condições:</br>- Possuir uma [conta](lexicos10x5f8c4.md#l12532) no Brainly;</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Recursos** |    [perfil](lexicos10x5f8c4.md#l12532) no Brainly.</br>Lista de [níveis](lexicos10x5f8c4.md#l12491) escolares.   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) sem conexão com a internet.</br>Servidores da plataforma estarem offline.   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) acessa o Brainly.</br>[usuário](lexicos10x5f8c4.md#l12660) entra em sua [conta](lexicos10x5f8c4.md#l12532).</br></br>Plataforma mobile:</br>Na aba [resposta](lexicos10x5f8c4.md#l12521), o [usuário](lexicos10x5f8c4.md#l12660) clica em [nível](lexicos10x5f8c4.md#l12491) escolar ([nível das perguntas](lexicos10x5f8c4.md#l12656)) e escolhe o [nível](lexicos10x5f8c4.md#l12491) adequado para si na lista apresentada.</br></br>Plataforma web:</br>Na página principal, clicar no menu dropdown "Todos os [níveis](lexicos10x5f8c4.md#l12491)" e escolher o [nível](lexicos10x5f8c4.md#l12491) adequado para si na lista apresentada.</br></br>[usuário](lexicos10x5f8c4.md#l12660) escolhe uma [pergunta](lexicos10x5f8c4.md#l12494) que possa contribuir.</br>[usuário](lexicos10x5f8c4.md#l12660) [responde](lexicos10x5f8c4.md#l12489) a [pergunta](lexicos10x5f8c4.md#l12494).</br>[usuário](lexicos10x5f8c4.md#l12660) recebe [pontos](lexicos10x5f8c4.md#l12492) pela [resposta](lexicos10x5f8c4.md#l12521).   |


# iniciar desafios
### C2998

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    iniciar desafios   |
|  **Objetivo** |    incentivar [usuários](lexicos10x5f8c4.md#l12525) a [responder](lexicos10x5f8c4.md#l12489).   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) quer ganhar mais [pontos](lexicos10x5f8c4.md#l12492)</br></br>Local:</br>-Plataforma Brainly</br></br>Pré-condições:</br>- Ter uma [conta](lexicos10x5f8c4.md#l12532) no brainly.</br>- Estar [logado](lexicos10x5f8c4.md#l12651) na sua [conta](lexicos10x5f8c4.md#l12532).   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Recursos** |    [desafios](lexicos10x5f8c4.md#l12496).   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) já estar em um [desafio](lexicos10x5f8c4.md#l12496).   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) vê os [desafios](lexicos10x5f8c4.md#l12496) propostos;</br>[usuário](lexicos10x5f8c4.md#l12660) aceita [desafio](lexicos10x5f8c4.md#l12496) clicando no botão comece;</br>[usuário](lexicos10x5f8c4.md#l12660) cumpre as [tarefas](lexicos10x5f8c4.md#l12494) previstas em um período de tempo;</br>[usuário](lexicos10x5f8c4.md#l12660) ganha [pontos](lexicos10x5f8c4.md#l12492).</br>[usuário](lexicos10x5f8c4.md#l12660) pode repetir um [desafio](lexicos10x5f8c4.md#l12496).   |


# moderar denúncia
### C3030

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    moderar denúncia   |
|  **Objetivo** |    Verificar se houve infração ou não em uma denúncia.   |
|  **Contexto** |    Suspeita de irregularidade em alguma [pergunta](lexicos10x5f8c4.md#l12494), [resposta](lexicos10x5f8c4.md#l12521) ou [comentário](lexicos10x5f8c4.md#l12506).   |
|  **Atores**   |    [moderador](lexicos10x5f8c4.md#l12528), [administração](lexicos10x5f8c4.md#l12529), [infrator](lexicos10x5f8c4.md#l12531), denunciante   |
|  **Recursos** |    ferramenta de moderação, denúncia   |
|  **Excecão**  |    Instabilidade nos servidores Brainly.</br>Falta de [moderadores](lexicos10x5f8c4.md#l12528) ou denunciantes.</br></br>Restrição:</br>Denúncia ter procedência.   |
|  **Episódio** |    O [moderador](lexicos10x5f8c4.md#l12528) ou [administrador](lexicos10x5f8c4.md#l12529) verifica a denúncia no painel de moderação.</br>Se a [pergunta](lexicos10x5f8c4.md#l12494), [resposta](lexicos10x5f8c4.md#l12521) ou [comentário](lexicos10x5f8c4.md#l12506) é apropriado, os [moderadores](lexicos10x5f8c4.md#l12528) ou [administradores](lexicos10x5f8c4.md#l12529) aprovam o conteúdo.</br>Se há possibilidade de correção, os [moderadores](lexicos10x5f8c4.md#l12528) ou [administradores](lexicos10x5f8c4.md#l12529) solicitam a [edição](lexicos10x5f8c4.md#l12659) da atividade.</br>Se a denuncia é verídica, os [moderadores](lexicos10x5f8c4.md#l12528) ou [administradores](lexicos10x5f8c4.md#l12529) advertem o [infrator](lexicos10x5f8c4.md#l12531) e exclui sua [pergunta](lexicos10x5f8c4.md#l12494), [resposta](lexicos10x5f8c4.md#l12521) ou [comentário](lexicos10x5f8c4.md#l12506).</br>Se a ação do [usuário](lexicos10x5f8c4.md#l12660) tiver conteúdo extremamente inapropriado, os [moderadores](lexicos10x5f8c4.md#l12528) ou [administradores](lexicos10x5f8c4.md#l12529) tornam o [usuário](lexicos10x5f8c4.md#l12660) [banido](lexicos10x5f8c4.md#l12534) ou [bloqueiam usuário](lexicos10x5f8c4.md#l12574).   |


# pedir correção de contéudo
### C3045

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    pedir correção de contéudo   |
|  **Objetivo** |    Corrigir irregularidades em conteúdos prestados na plataforma.   |
|  **Contexto** |    O [usuário](lexicos10x5f8c4.md#l12660) escreve na plataforma informações incorretas.</br>[moderadores](lexicos10x5f8c4.md#l12528), [administradores](lexicos10x5f8c4.md#l12529) ou o [usuário](lexicos10x5f8c4.md#l12660) nota o erro.   |
|  **Atores**   |    [moderador](lexicos10x5f8c4.md#l12528), [administrador](lexicos10x5f8c4.md#l12529), [usuário](lexicos10x5f8c4.md#l12660).   |
|  **Recursos** |    Editor de [perguntas](lexicos10x5f8c4.md#l12494) e [respostas](lexicos10x5f8c4.md#l12521).   |
|  **Excecão**  |    [usuário](lexicos10x5f8c4.md#l12660) sem conexão com a internet.</br>Servidores da plataforma estarem instáveis.   |
|  **Episódio** |    [moderador](lexicos10x5f8c4.md#l12528) ou [administrador](lexicos10x5f8c4.md#l12529) verifica um erro na [pergunta](lexicos10x5f8c4.md#l12494), [resposta](lexicos10x5f8c4.md#l12521) ou [comentário](lexicos10x5f8c4.md#l12506) do [usuário](lexicos10x5f8c4.md#l12660) e solicita a correção, [edição](lexicos10x5f8c4.md#l12659).</br>[usuário](lexicos10x5f8c4.md#l12660) é notificado sobre o erro no conteúdo.</br>[usuário](lexicos10x5f8c4.md#l12660) edita a [tarefa](lexicos10x5f8c4.md#l12494) e envia para [avaliação](lexicos10x5f8c4.md#l12506) de quem solicitou a correção.</br>O [moderador](lexicos10x5f8c4.md#l12528) ou [administrador](lexicos10x5f8c4.md#l12529) responsável pelo pedido de correção avalia a questão e torna a [resposta](lexicos10x5f8c4.md#l12521) verificada.   |


# pesquisar
### C3000

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    pesquisar   |
|  **Objetivo** |    tirar dúvidas.   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) com [dúvida](lexicos10x5f8c4.md#l12494)</br></br>Local:</br>-Plataforma Brainly   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660);</br>[comunidade](lexicos10x5f8c4.md#l12525);</br>time brainly.   |
|  **Recursos** |    [respostas verificadas](lexicos10x5f8c4.md#l12522);</br>campo de pesquisa.   |
|  **Excecão**  |    não ter [respostas verificadas](lexicos10x5f8c4.md#l12522).   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) tem uma [dúvida](lexicos10x5f8c4.md#l12494);</br>[usuário](lexicos10x5f8c4.md#l12660) digita no capo de pesquisa;</br>[perguntas](lexicos10x5f8c4.md#l12494) verificadas são retornadas;</br>[usuário](lexicos10x5f8c4.md#l12660) lê [perguntas](lexicos10x5f8c4.md#l12494) e [respostas](lexicos10x5f8c4.md#l12521) para tirar sua [dúvida](lexicos10x5f8c4.md#l12494).   |


# pesquisar pelo google
### C3038

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    pesquisar pelo google   |
|  **Objetivo** |    Tirar uma [dúvida](lexicos10x5f8c4.md#l12494).   |
|  **Contexto** |    Contexto:[usuário](lexicos10x5f8c4.md#l12660) com [dúvida](lexicos10x5f8c4.md#l12494)</br></br>Local:</br>-Plataforma Brainly</br>-Google   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660)   |
|  **Recursos** |    google   |
|  **Excecão**  |    Não ter dados na plataforma brainly relacionados com a pesquisa   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) faz uma pesquisa no google.</br>[usuário](lexicos10x5f8c4.md#l12660) vê um resultado relacionado à plataforma brainly.</br>[usuário](lexicos10x5f8c4.md#l12660) clica no resultado.</br>[usuário](lexicos10x5f8c4.md#l12660) é redirecionado para plataforma brainly.</br>[usuário](lexicos10x5f8c4.md#l12660) visualiza uma [tarefa](lexicos10x5f8c4.md#l12494) verificada.   |


# responder tarefa
### C2997

|  Informações  | Cenário |
|:-------------:|:-------:|
|  **Título**   |    responder tarefa   |
|  **Objetivo** |    ajudar alguém;</br>testar conhecimento.   |
|  **Contexto** |    [usuário](lexicos10x5f8c4.md#l12660) disposto a ajudar;</br>brainly.   |
|  **Atores**   |    [usuário](lexicos10x5f8c4.md#l12660);</br>[comunidade](lexicos10x5f8c4.md#l12525).   |
|  **Recursos** |    [perguntas](lexicos10x5f8c4.md#l12494) [sem resposta](lexicos10x5f8c4.md#l12519);</br>campo pra [resposta](lexicos10x5f8c4.md#l12521).   |
|  **Excecão**  |    cair a internet;</br>[usuário](lexicos10x5f8c4.md#l12660) não estar [logado](lexicos10x5f8c4.md#l12651).   |
|  **Episódio** |    [usuário](lexicos10x5f8c4.md#l12660) entra no brainly;</br>[usuário](lexicos10x5f8c4.md#l12660) vê as peguntas feitas pela [comunidade](lexicos10x5f8c4.md#l12525);</br>[usuário](lexicos10x5f8c4.md#l12660) escolhe uma [pergunta](lexicos10x5f8c4.md#l12494);</br>[usuário](lexicos10x5f8c4.md#l12660) [responde](lexicos10x5f8c4.md#l12489).   |


