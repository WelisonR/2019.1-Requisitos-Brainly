# [DELETAR CONTA](cenarios10x5f8c4.md#C3029)

## Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------:
| [1.0](modelagem_v1/casos_uso/casos_uso_deletar_conta.md) | 29/04/2019 | Adição da especificação de casos de uso e diagrama| Lieverton, Leonardo Medeiros, Paulo Vítor, João Matheus, Ivan Diniz, João Rossi |
| 2.0 | 22/06/2019 | Adição do diagrama de caso de uso versão 2, baseado na análise | Leonardo Medeiros |
| 2.1 | 22/06/2019 | Adição das especificações de casos de uso | Leonardo Medeiros |

## Diagrama de Casos de Uso

![Diagrama de casos de uso: Deletar Conta](images/diagramas_casos_uso/Deletar_Conta_v2.png)

## Especificação de Casos de Uso

### UC01

| UC01 | Acessar o Brainly |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado acessa à plataforma Brainly. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet. |
| **Fluxo básico** | 1. Usuário acessa plataforma via web ou aplicativo para dispositivo móvel.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Servidores da plataforma estão indisponíveis, logo usuário não terá como acessa-los |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC02

| UC02 | Editar perfil |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado acessa a pagina de edição de perfil. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter uma conta na plataforma. |
| **Fluxo básico** | 1. Usuário acessa a pagina de edição de perfil através do menu principal.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário não encontra a página de edição de perfil, no menu principal |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC03

| UC03 | Editar configurações |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado acessa o menu de alteração de perfil, dentro do menu de edição de perfil. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter uma conta na plataforma. |
| **Fluxo básico** | 1. Dentro do menu de edição de perfil, o usuário acessa o menu Configurações. |
| **Fluxos alternativos** | 1.a Usuário navega pelos menus, procurando a opção de deletar conta. |
| **Fluxos de exceções** | [1] Usuário não sabe que deve acessar o menu de Configurações para encontrar a opção de Deletar conta |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC04

| UC04 | Eliminar conta |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado opta por eliminar sua conta no menu de alteração de perfil, dentro do menu de edição de perfil. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter uma conta na plataforma. |
| **Fluxo básico** | 1. Dentro do menu de edição de configurações, o usuário acessa o botão "Quero eliminar minha conta". |
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário não encontra o botão de eliminar conta |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC05

| UC05 | Inserir senha e confirmar |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado que optou por eliminar sua conta, deve inserir sua senha, para confirmar a eliminação da conta. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter uma conta na plataforma. |
| **Fluxo básico** | 1. Após optar por eliminar a conta, o usuário deve inserir sua senha;<br/>2. O usuário confirma que deseja deletar sua conta. |
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário não lembra da senha cadastrada. |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC06

| UC06 | Usar formulário de contato |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado deve preencher o formulário de contato para solicitar a confirmação de eliminação de sua conta. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Ter uma conta na plataforma. |
| **Fluxo básico** | 1. Usuário preenche um formulário de contato, confirmando a exclusão da conta;<br/>2. Usuário envia o formulário por email para a equipe de suporte da plataforma. |
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário não encontra o formulário a ser preenchido |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |

### UC07

| UC07 | Deletar a conta |
| -------------: | :---|
| **Descrição** | Um administrador da plataforma recebe o formulário preenchido pelo usuário e confirma a eliminação da conta. |
| [Administrador](lexicos10x5f8c4.md#l12529) | Ator que trabalha no Brainly, Responsável pela gerência de contas e necessidades da plataforma. |
| **Pré-condições** | - Ter acesso à internet;<br/> - Receber o email de formulário do usuário. |
| **Fluxo básico** | 1. Administrador recebe email com formulário preenchido pelo usuário;<br/>2. Administrador confirma a exclusão da conta. |
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Usuário não preenche o formulário adequadamente |
|  **Requisitos Especiais** | - Deve ser possível ao moderador a exclusão de contas e o banimento do usuário [INT 2.15](introspeccao.md). |


