# Especificações

- [Especificações](#especificações)
  - [Entidades](#entidades)
    - [usuarios](#usuarios)
    - [atletas](#atletas)
    - [equipe](#equipe)
    - [organizador](#organizador)
    - [prova](#prova)
    - [equipamentos](#equipamentos)
    - [alimentos](#alimentos)
    - [SMART](#smart)
    - [SWOT](#swot)

## Entidades

### usuarios

regras de negócio

- um usuário pode criar um ou mais times
- um usuário pode cadastrar uma ou mais provas
- um usuário pode convidar um ou mais atletas

### atletas

regras de négócio

- um atleta pode estar em um ou mais times
- um alteta pode participar de uma ou mais provas
- um atleta pode ter um ou mais equipamentos
- um atleta pode cadastrar um ou mais alimentos

atributos

- nome
- sexo
- telefone
- email
- data de nascimento

### equipe

regras de négócio

- uma equipe pode ter várias formações (quarteto/dupla/solo)
- uma equipe pode ter vários atletas
- uma equipe participa de uma ou mais provas com formações diferentes

atributos

- nome
- formação
- logo

### organizador

regras de négócio

- um organizador pode criar uma ou mais provas

atributos

- nome
- telefone
- email

### prova

regras de négócio

- uma prova tem apenas um time
- uma prova tem um ou mais equipamentos obrigatórios
- uma prova tem um ou mais organizadores

atributos

- nome
- loca
- data
- distância
- site prova
- características local
- caracteristicas prova
- outra informações

### equipamentos

regras de négócio

- um equipamento pertece apenas a um atleta
- um equipamento pode ser utilizado em uma ou mais provas

atributos

- nome
- quantidade
- obrigatório
- características
- situação

### alimentos

regras de négócio

- um tipo de alimento pode ser compartilhado com o time
- um tipo de alimento pode ser utilizado em uma ou mais provas

atributos

- nome
- tipo
- qtde
- calorias
- observação

### SMART

regras de négócio

- uma avaliação está ligada a apenas uma prova
- uma avaliação está ligada a apenas um atleta

atributos

- item
- resposta

### SWOT

regras de négócio

- uma avaliação está ligada a apenas uma prova
- uma avaliação está ligada a apenas um atleta

atributos

- item
- resposta
