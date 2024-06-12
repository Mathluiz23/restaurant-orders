# Projeto `Restaurant Orders`!


<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
A lanchonete :baguette_bread: :cook: Pão na Chapa :baguette_bread: :cook: possui um sistema de faturamento de pedidos de clientes que salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento. A gerência da lanchonete quer aumentar suas vendas e melhorar sua gestão interna e, para isso, foi implementaado um projeto de melhorias, o Projeto `Restaurant Orders`. </br>
    Em um primeiro momento o sistema ira gerar relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete. Estes dados irão auxiliar o trabalho de uma agência de marketing com o objetivo de alavancar as vendas e o número de pessoas clientes. </br>
    Em um segundo momento deverá ser o controle do estoque de ingredientes para garantir que o cardápio digital da :baguette_bread: :cook: Pão na Chapa :baguette_bread: :cook: mostrando sempre produtos que estão disponíveis no estoque, evitando frustrações por parte das pessoas clientes. </br>
    </br>
</br>
🚵 Habilidades exercitadas: </br>
  - Trabalhar com `Hashmap` e `Dict` e; </br>
  - Trabalhar com `Set`. </br>

</details>

# Orientações
<details>
  <summary><strong>⚠️ Antes de começar a desenvolver</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-014-b-restaurant-orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-0x-project-restaurant-orders`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `master`

  - Verifique que você está na branch `master`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `master`
    - Exemplo: `git checkout master`
  - Crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-de-usuario-nome-do-projeto`
    - Exemplo: `git checkout -b nome_da_sua_branch`

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />

  No diretório `src/` você vai encontrar os arquivos em que devem ser implementadas todas as classes e métodos que você considerar importantes para resolver cada etapa do projeto.

  No diretório `data/` você vai encontrar os arquivos de log que deverão ser utilizados em cada etapa.

  Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  .
  ├── data
  │   ├──🔸 orders_1.csv
  │   └──🔸 orders_2.csv
  ├── src
  │   ├──🔹 analyze_log.py
  │   ├──🔹 inventory_control.py
  │   ├──🔹 main.py
  │   └──🔹 track_orders.py
  ├──tests
  │   ├──🔸 test_analyze_log.py
  │   ├──🔸 test_inventory_control.py
  │   └──🔸 test_track_orders.py
  ├──🔸 dev-requirements.txt
  ├──🔸 pyproject.toml
  ├──🔸 README.md
  ├──🔸 requirements.txt
  ├──🔸 setup.cfg
  ├──🔸 setup.py
  └──🔸 trybe.yml

Legenda:
  🔸 Arquivos que não podem ser alterados.
  🔹 Arquivos alterados.
```
</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

  ```bash
  pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>


# O projeto 

## 1 - Campanha de publicidade

> Implementado  método `analyze_log` no módulo `src/analyze_log.py` que gera informações de uma lanchonete.

A lanchonete quer promover ações de marketing e, para isso, a agência de publicidade precisa das informações abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi à lanchonete?

#### Dados

O atual sistema da lanchonete 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳  guarda os `logs` de todos os pedidos feitos em um arquivo _csv_, contendo o formato `cliente, pedido, dia`, um por linha e sem nome das colunas (a primeira linha já é um pedido).

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. Todas as informações são _strings_ com letras minúsculas. O histórico contém pedidos feitos em todos os dias da semana que a lanchonete abre, e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio e agenda completos. Os dias da semana estão no formato `"...-feira", "sabado" ou "domingo"`, e **não nos interessa informações sobre os dias que a lanchonete não abre**.

#### Implementação

No arquivo `analyze_log.py`, implementado função que responde às seguintes perguntas abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi à lanchonete?

A função não retorna nada e apenas salva as respostas no arquivo `data/mkt_campaign.txt`, na mesma ordem das peguntas acima.

<details>

</details>

<details>
<summary><b>saída da função.</b></summary>

```
hamburguer
1
{'pizza', 'coxinha', 'misto-quente'}
{'sabado', 'segunda-feira'}
```
</details>


## 2 - Análises contínuas

> Implementado a classe `TrackOrders` que gera informações contínuas da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 .

Agora um sistema que mantenha um registro contínuo dessas informações. Mais especificamente, deseja que o sistema permita, a qualquer momento, a extração das seguintes informações:

- Prato favorito por cliente;

- Pratos nunca pedidos por cada cliente;

- Dias nunca visitados por cada cliente;

- Dia mais movimentado;

- Dia menos movimentado.

Para isso, você deverá implementar uma classe que entregue as informações acima.

#### Implementação

**TestANDO o comportamento do arquivo `main.py`**.

Abra o arquivo `main.py` e complete a variável _path_ com `data/orders_1.csv`. Rode o arquivo `main.py`. Quatro linhas de `None` devem ser impressas. Isso acontece, porque as funções não estão devidamente implementadas ainda.


## 3 - Controle de estoque

A 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 - Automatizar o controle: no final da semana, a gerência irá imprimir uma lista de compras com as respectivas quantidades.

#### Dados

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. É garantido que os pedidos da semana não irão zerar nenhum dos estoques.

#### Implementação

No arquivo `inventory_control.py` você deve implementar a classe `InventoryControl` que retorna a lista de compras da semana, a partir da informação de cada pedido. É importante que a lista seja atualizada a cada pedido.
<details>
<summary><b>Estrutura básica da classe. Lá já contém as informações dos ingredientes, bem como o estoque mínimo de cada um. O método <code>get_quantities_to_buy</code> deve retornar um <code>Dict</code> que mapeia o ingrediente para a quantidade a ser comprada.</b></summary>

```python
class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho', 'tomate'],
        'queijo-quente': ['pao', 'queijo', 'queijo'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_quantities_to_buy(self):
        pass
```

</details>

- Classe `InventoryControl` implementada;

- A classe está devidamente modularizada;

- Garanta que todos os ingredientes e pratos foram testados;

- Os métodos devem fazer uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima, geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`.


## 4 - Estoque pode acabar

<b>Gerenciamento de estoques:</b>

```md
- Pao: 1;
- Queijo: 5;
- Presunto: 3.
```
Implementar um código que, caso algum ingrediente acabe, todos os pratos que usam aquele ingrediente devem ser imediatamente removidos do cardápio eletrônico, evitando gerar frustração em clientes.



