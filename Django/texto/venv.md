# O que é venv?

`venv` é uma abreviação para "Virtual Environment" em Python. É uma ferramenta que permite criar ambientes virtuais isolados para projetos Python. Cada ambiente virtual tem sua própria instalação de pacotes Python, permitindo que você trabalhe em diferentes projetos com diferentes conjuntos de dependências sem interferências entre eles.

Quando você cria um ambiente virtual usando `venv`, uma nova estrutura de diretórios é criada dentro do seu projeto. Isso inclui uma cópia do interpretador Python, bem como uma cópia do utilitário `pip` (o gerenciador de pacotes do Python) específico para o ambiente virtual. Quando você ativa o ambiente virtual, ele substitui temporariamente o interpretador Python e o `pip` do sistema, de modo que todas as instalações de pacotes feitas enquanto o ambiente virtual está ativado são específicas para esse ambiente.

Para criar um ambiente virtual usando `venv`, você pode usar o seguinte comando no terminal, dentro do diretório do seu projeto:

```
python -m venv nome_do_ambiente
```

Depois de criar o ambiente virtual, você pode ativá-lo executando um script específico no diretório `bin` (ou `Scripts` no Windows) do ambiente virtual. Por exemplo, no Linux ou macOS, você pode fazer:

```
source nome_do_ambiente/bin/activate
```

No Windows, você pode fazer:

```
nome_do_ambiente\Scripts\activate
```

Quando o ambiente virtual estiver ativado, você verá o nome do ambiente aparecer no prompt do terminal, indicando que você está trabalhando dentro do ambiente virtual. Você pode então instalar pacotes Python usando o `pip`, e eles serão instalados apenas no ambiente virtual atual, não no sistema global. Isso ajuda a evitar conflitos entre diferentes projetos que podem depender de versões diferentes de pacotes Python.


# Boas Praticas

## Atualizar o pip

Logo apos de ativar o venv atualiza o pip antes de instalar 
~~~
pip install --upgrade pip
~~~


## Nome 

É comum colocamos o nome de `venv` ou `.venv`


## Venv para cada projeto

Sempre que começa um projeto novo crie um novo venv

# Desativa

Digite no terminal 

~~~ bash 
desactivate
~~~
