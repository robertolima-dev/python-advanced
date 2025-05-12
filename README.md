## Manipulação e Processamento de Dados em Python

Este repositório contém exemplos e práticas sobre manipulação e processamento de dados em Python, abordando conceitos avançados e boas práticas para tornar o código eficiente e escalável.

---

### 📚 Conteúdo

1. [Processamento Assíncrono](#processamento-assíncrono)
2. [Manipulação de Arquivos e Streams](#manipulação-de-arquivos-e-streams)
3. [Data Science com Python](#data-science-com-python)

---

### 🚀 1. Processamento Assíncrono

O processamento assíncrono permite que tarefas que envolvem operações de I/O sejam realizadas de forma não bloqueante. Isso significa que o programa pode executar várias operações ao mesmo tempo, melhorando o desempenho e a eficiência.

#### ✅ Tecnologias Utilizadas
- `asyncio` - Para execução assíncrona de funções.
- `aiohttp` - Para requisições HTTP assíncronas.

#### 🔧 Exemplo Básico:

```python
import asyncio

async def say_hello():
    print("Olá!")
    await asyncio.sleep(2)
    print("Adeus!")

async def main():
    await say_hello()

asyncio.run(main())
````

#### 📥 Instalação do aiohttp:

Para utilizar o `aiohttp`, execute:

```bash
pip install aiohttp
```

#### 💡 Benefícios:

* Redução de tempo de espera em operações I/O.
* Execução paralela sem utilizar threads.

---

### 📂 2. Manipulação de Arquivos e Streams

A manipulação de arquivos em Python é essencial para lidar com dados de entrada e saída de maneira eficiente. Utilizamos diferentes métodos para ler, escrever e compactar arquivos.

#### ✅ Principais Tecnologias:

* Arquivos de Texto e Binários
* Arquivos CSV (Pandas)
* Arquivos ZIP (zipfile)

#### 🔧 Exemplos:

**Leitura de Arquivos de Texto:**

```python
with open("dados.txt", "r") as f:
    content = f.read()
    print(content)
```

**Leitura de CSV com Pandas:**

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
```

**Compactação com ZIP:**

```python
import zipfile

with zipfile.ZipFile("arquivo.zip", "w") as zipf:
    zipf.write("dados.txt")
```

#### 💡 Benefícios:

* Armazenamento e organização eficientes.
* Manipulação rápida de grandes volumes de dados.

---

### 📊 3. Data Science com Python

O Python é amplamente utilizado em ciência de dados devido às suas poderosas bibliotecas para análise e visualização.

#### ✅ Tecnologias Utilizadas:

* `Pandas` - Manipulação e análise de dados.
* `NumPy` - Computação numérica eficiente.
* `Matplotlib` - Visualização de dados.

#### 🔧 Exemplos:

**Análise de Dados com Pandas:**

```python
import pandas as pd

df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
print(df.describe())  # Estatísticas básicas
```

**Gráfico Simples com Matplotlib:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, marker='o')
plt.title("Gráfico de Exemplo")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
```

#### 💡 Benefícios:

* Análise e visualização rápida de grandes volumes de dados.
* Geração de insights e relatórios visuais.

---

### 📝 Desafio Prático:

1. Utilizando **asyncio** e **aiohttp**, faça o download simultâneo de três arquivos CSV.
2. Leia os arquivos com **Pandas** e calcule a média dos valores.
3. Plote um gráfico de barras com as médias calculadas usando **Matplotlib**.

---

### 💻 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/robertolima-dev/python-advanced.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute os exemplos:

```bash
python structure_data.py
python typing_data.py
python oop_data.py
```

---

### 🤝 Contribuição

Sinta-se à vontade para abrir Issues ou Pull Requests para melhorar o conteúdo. Toda contribuição é bem-vinda!

---

## 🧠 Autor
**Roberto Lima**  
- 📧 **Email**: robertolima.izphera@gmail.com
- 🔗 [GitHub Roberto Lima](https://github.com/robertolima-dev)  
- 💼 [Linkedin Roberto Lima](https://www.linkedin.com/in/roberto-lima-01/)
- 🌐 [Website Roberto Lima](https://robertolima-developer.vercel.app/)
- 👤 [Gravatar Roberto Lima](https://gravatar.com/deliciouslyautomaticf57dc92af0)
