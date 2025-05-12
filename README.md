# Python Avançado: Manipulação, Tipagem e POO

Este repositório contém exemplos avançados de Python, abordando tipagem, manipulação de dados e técnicas de programação orientada a objetos (POO).

---

## 📚 Conteúdo

1. [Tipagem Avançada com Typing](#tipagem-avançada-com-typing)
2. [POO Avançada: Metaclasses e Classes Abstratas](#poo-avançada-metaclasses-e-classes-abstratas)
3. [Manipulação e Processamento de Dados](#manipulação-e-processamento-de-dados)

---

### 🔠 1. Tipagem Avançada com Typing

O uso de tipagem estática em Python aumenta a legibilidade e ajuda a evitar erros. A partir do Python 3.5, a biblioteca `typing` fornece recursos robustos para definir tipos de maneira clara.

#### ✅ Principais Recursos:
- `List`, `Dict`, `Tuple`, `Set`: Para tipos de coleção.
- `Optional`, `Union`: Para valores opcionais.
- `Callable`, `Any`: Para funções e tipos genéricos.

#### 💡 Exemplos:

**Função com Tipagem:**
```python
from typing import List, Dict, Optional

def process_data(data: List[int], factor: int) -> Dict[str, Optional[float]]:
    result = sum(data) * factor
    return {"total": result if result > 0 else None}

print(process_data([1, 2, 3], 10))  # {'total': 60}
````

**Uso de Tipos Genéricos:**

```python
from typing import TypeVar, List

T = TypeVar('T')

def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]

print(reverse_list([1, 2, 3]))  # [3, 2, 1]
```

#### 💡 Vantagens:

* Facilita a compreensão do código.
* Melhora a verificação estática com ferramentas como `mypy`.

---

### 🏛️ 2. POO Avançada: Metaclasses e Classes Abstratas

Em Python, podemos utilizar metaclasses e classes abstratas para criar estruturas flexíveis e reutilizáveis, especialmente em arquiteturas mais complexas.

#### 🛠️ Metaclasses:

As metaclasses controlam a criação de classes, permitindo modificar o comportamento das classes no momento de sua definição.

**Exemplo de Metaclasse Singleton:**

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def log(self, message: str):
        print(f"[LOG] {message}")

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # True
```

#### 📝 Classes Abstratas:

Classes abstratas servem como modelos para outras classes, garantindo que métodos essenciais sejam implementados.

**Exemplo de Classe Abstrata:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

dog = Dog()
print(dog.make_sound())  # Woof!
```

#### 💡 Vantagens:

* Organização de código com responsabilidades bem definidas.
* Garantia de implementação de métodos essenciais.

---

### 📂 3. Manipulação e Processamento de Dados

Este módulo foca na manipulação eficiente de dados, utilizando bibliotecas para processamento assíncrono e leitura de arquivos.

#### 🚀 Processamento Assíncrono

Utilizamos o módulo `asyncio` para lidar com tarefas não bloqueantes, melhorando o desempenho em operações de I/O.

**Exemplo:**

```python
import asyncio

async def say_hello():
    print("Olá!")
    await asyncio.sleep(2)
    print("Adeus!")

asyncio.run(say_hello())
```

#### 📄 Manipulação de Arquivos

Manipulação de dados utilizando Pandas e leitura de arquivos CSV.

**Exemplo:**

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
```

#### 📊 Data Science com Pandas

Processamento e visualização de dados com Pandas e Matplotlib.

**Exemplo:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, marker='o')
plt.title("Gráfico de Exemplo")
plt.show()
```

---

### 📝 Desafio Prático:

1. Utilize **typing** para criar uma função que retorne a média de uma lista de números.
2. Crie uma **classe abstrata** para representar uma Conta Bancária e implemente as subclasses para **Conta Corrente** e **Conta Poupança**.
3. Faça um programa assíncrono que faça requisições simultâneas para diferentes APIs.

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
