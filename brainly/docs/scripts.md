# SCRIPTS

Durante a elaboração do projeto, desenvolveu-se scripts importantes para dinamizar o processo de confecçãao de artefatos da disciplina de Requisitos de Software. Os scripts auxiliaram a elaboração, principalmente, das tabelas em markdown e também dos artefatos de cenários e léxicos.

## CeL - Crawler - PUCRIO

A ferramenta [C&L Crawler](https://github.com/WelisonR/2019.1-Requisitos-Brainly/blob/master/scripts/CeL_crawler_pucrio.ipynb) é voltada para a obtenção de [cenários](cenarios10x5f8c4.md) e [léxicos](lexicos10x5f8c4.md) presentes no site [C&L](http://pes.inf.puc-rio.br/cel/aplicacao/). A ferramenta, desenvolvido em python e disponível em nosso [github](https://github.com/WelisonR/2019.1-Requisitos-Brainly/blob/master/scripts/CeL_crawler_pucrio.ipynb), baseia-se nas _urls_ dos artefatos puxando todas as informações dos cenários e léxicos do site  referente ao projeto em questão e, por fim, gera-se um _markdown_ com âncoras nas palavras chaves (inclusive sinônimos).


Notebook: O _notebook_ com o código e as orientações está disponível em [C&L Crawler](https://github.com/WelisonR/2019.1-Requisitos-Brainly/blob/master/scripts/CeL_crawler_pucrio.ipynb).

## Tabela .ods para .md

O script em python de conversão de tabelas em formato ODS para markdown foi fundamental para a passagem dos artefatos do nosso _google drive_ para essa wiki. O script, baseia-se em um `arquivo.ods` para converter um equivalente em markdown.

Script com as instruções de uso: [Tabela ODS para MD](https://github.com/WelisonR/2019.1-Requisitos-Brainly/blob/master/scripts/ods_para_md.py).