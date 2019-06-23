# [CADASTRO](rich_picture.md#richpicture-primeiros-passos-de-novo-usuario-nao-cadastrado)

## Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------:
| 1.0 | 29/04/2019 | Adição da especificação de casos de uso | Lieverton, Leonardo Medeiros, Paulo Vítor, João Matheus, João Rossi |
| [1.1](modelagem_v1/casos_uso/casos_uso_cadastro.md) | 29/04/2019 | Adição do Diagrama de casos de uso | Ivan Diniz Dobbin,João Matheus, João Rossi, Leonardo Medeiros |
| 2.0 | 22/06/2019 | Refatoração do diagrama de casos de uso de Cadastro | Leonardo Medeiros |
| 2.1 | 22/06/2019 | Adicionas especificações de casos de uso de Cadastro | Leonardo Medeiros |

## Diagrama de Casos de Uso

![Diagrama de casos de uso: Cadastro v2](images/diagramas_casos_uso/Cadastro_v2.png)

## Especificação de Casos de Uso

### UC01

| UC01 | Acessar o Brainly |
| -------------: | :---|
| **Descrição** | Um usuário não cadastrado acessa a plataforma Brainly. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet. |
| **Fluxo básico** | 1. Usuário acessa à plataforma via web ou aplicativo para dispositivo móvel;|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | - |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC02

| UC02 | Cadastrar conta |
| -------------: | :---|
| **Descrição** | Um usuário não cadastrado deseja cadastrar-se na plataforma Brainly. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet. |
| **Fluxo básico** | 1. Usuário deseja cadastrar-se na plataforma para utilizar de tods os recursos disponiveis;<br/>2. Usuário clica no botão "cadastrar". |
| **Fluxos alternativos** | 1.a Usuário deseja realizar uma pergunta, durante este processo será solicitado que faça cadastro. |
| **Fluxos de exceções** | - |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Manter o sistema gratuito para atrair mais usuários, utilizando apenas de ads para a monetização [EN1.3](entrevista.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md) |

### UC03

| UC03 | Entrar com Facebook |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma desejesa usar sua conta do Facebook para cadastrar-se. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter uma conta no Facebook. |
| **Fluxo básico** | 1. No momento inicial do cadastro, usuário opta por usar sua conta do Facebook;<br/>2. Usuário faz login no Facebook;<br/>3. Usuário concede as devidas permissões para que o Brainly acesse seus dados do Facebook. |
| **Fluxos alternativos** |  |
| **Fluxos de exceções** | [2] Usuário não consegue acessar sua conta do Facebook;<br/> [3] Usuário não concorda em conceder as permissões solicitadas |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md) |

### UC04

| UC04 | Usar email |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma opta por usar um endereço email para concluir seu cadastro. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet. |
| **Fluxo básico** | 1. No momento inicial do cadastro, usuário opta por usar email. |
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | - |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md) |

### UC05

| UC05 | Digitar email |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma deverá inserir um endereço email para concluir seu cadastro. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter um endereço de email. |
| **Fluxo básico** | 1. Usuário insere endereço de email |
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário insere um email invélido, recebendo uma mensagem de erro, solicitando-o a correção. |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md) |

### UC06

| UC06 | Inserir dados |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma deverá inserir seus dados pessoair para concluir cadastro. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter um endereço de email. |
| **Fluxo básico** | 1. Usuário insere seu Nome de usuário;<br/>2. Usuário insere sua Senha;<br/>3. Usuário seleciona seu País;<br/>4. Usuário seleciona sua Data de nascimento.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Nome de usuário já está em uso, recebendo uma mensagem de aviso, solicitando alteração;<br/> [2] Senha possui menos de 6 caracteres ou mais de 32, recebendo uma mensagem de aviso, solicitando alteração.
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md);<br/> - Não utilizar informações de pessoas menores de 16 anos sem autorização [BR2.7](brainstorm.md) |

### UC07

| UC07 | Verificar idade |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma insere sua data de nascimento. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter um endereço de email. |
| **Fluxo básico** | 1. Sistema verifica se a Data de nascimento selecionada pelo usuário correndo a uma idade menor que 13 anos.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário tem mais que 13 anos de idade, sendo levado para o fluxo de cadastro comum.
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md);<br/> - Não utilizar informações de pessoas menores de 16 anos sem autorização [BR2.7](brainstorm.md) |

### UC08

| UC08 | Inserir email de um Responsável |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma insere uma data de nascimento que corresponde a uma idade atual menor que 13 anos. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter um endereço de email;<br/> Ter menos de 13 anos de idade. |
| **Fluxo básico** | 1. Usuário insere endereço de email de um de seus responsáveis, para que o mesmo conceda a autorização de uso.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário não recebe permissão de um responsável para utilizar a plataforma.
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md);<br/> - Não utilizar informações de pessoas menores de 16 anos sem autorização [BR2.7](brainstorm.md) |

### UC09

| UC09 | Confirmar email |
| -------------: | :---|
| **Descrição** | Um usuário que está se cadastrando na plataforma usando seu email, completa seu cadastro, então precisa confirmar a posse do email. |
| Usuário não cadastrado | Ator que pretende criar uma conta, tornando-se um [usuário](lexicos10x5f8c4.md#l12660), para possuir acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter um endereço de email;<br/> Ter mais de 13 anos de idade. |
| **Fluxo básico** | 1. Usuário conclui cadastro na plataforma;<br/>2. Usuário confirma seu cadastro em sua conta de email.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [2] Usuário não possui acesso à conta de email cadastrada, impossibilitando-o de confirmar seu cadastro. 
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03);<br/> - Receber permissão total, no registro de usuário, sobre seus dados pessoais para criar trabalhos derivados, usar para publicidade ou marketing [BR2.13](brainstorm.md);<br/> - Poder monitorar e registrar atividades nos serviços da brainly sem autorização prévia [BR2.11](brainstorm.md);<br/> -  O cadastro na plataforma deve ocorrer de uma maneira rápida e prática [AP3.3](analise_protocolo.md); - Ao se cadastrar o usuário terá acesso aos termos de uso e para concluir o registro deverá aceitá-lo [AP1.13](analise_protocolo.md).
