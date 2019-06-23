# [GAMIFICAÇÃO](rich_picture.md#richpicture-gamificacao)

## Versionamento

|  Versão | Data | Modificação | Autor |
|  :------: | :------: | :------: | :------: |
| 0.1 | 28/04/2019 | Adição do diagrama de casos de uso de gamificação | Leonardo Medeiros, Ivan Diniz Dobbin, João Rodrigues, João Rossi|
| 1.0 | 28/04/2019 | Especificação de casos de uso | Leonardo Medeiros, Ivan Diniz Dobbin, João Rodrigues, João Rossi|
| 1.1 | 28/04/2019 | Adição do segundo diagrama de casos de uso de gamificação | Gustavo Marques e André Lucas |
| 1.2 | 28/04/2019 | Adição do terceiro diagrama de casos de uso de gamificação | Gustavo Marques e André Lucas |
| [2.0](modelagem_v1/casos_uso/casos_uso_gamificacao.md) | 28/04/2019 | Mudança nas especificações de caso de uso de acordo com o novo diagrama de casos de uso | Gustavo Marques e André Lucas |
| 3.0 | 23/06/2019 | Adição da quarta versão do diagrama de casos de uso de gamificação | Leonardo Medeiros |

## Diagrama de Casos de Uso

![Diagrama de casos de uso: Gamificação v4](images/diagramas_casos_uso/gamificacao_v4.png)

## Especificação de Casos de Uso

### UC01

| UC01 |  |
| -------------: | :---|
| **Descrição** | Um usuário cadastrado acessa à plataforma Brainly. |
| [Usuário](lexicos10x5f8c4.md#l12660) | Ator que possui acesso às funcionalidade comuns da plataforma, como, fazer perguntas, escrever respostas e comentários, adicionar amigos, entre outras. |
| **Pré-condições** | - Ter acesso à internet. |
| **Fluxo básico** | 1. Usuário acessa plataforma via web ou aplicativo para dispositivo móvel.|
| **Fluxos alternativos** | - |
| **Fluxos de exceções** | [1] Servidores da plataforma estão indisponíveis, logo usuário não terá como acessa-los |
|  **Requisitos Especiais** | - O sistema deve possuir uma versão mobile de fácil acesso e com baixo consumo de bateria/dados [INT3.11](introspeccao.md#int03). |