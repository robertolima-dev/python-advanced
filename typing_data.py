from typing import Dict, List, Optional, Protocol, TypeVar

T = TypeVar('T')

"""
💡 1. Tipos Imutáveis vs. Mutáveis
Em Python, é crucial entender a diferença entre tipos mutáveis e imutáveis, especialmente para evitar problemas com referência e cópia de objetos.

Tipos Imutáveis:
Exemplos: int, float, str, tuple, frozenset

Não podem ser alterados após a criação.

Modificações criam um novo objeto na memória.

Tipos Mutáveis:
Exemplos: list, dict, set

Podem ser alterados após a criação.

Modificações afetam o objeto original.

Exemplo Prático:
""" # noqa501

x = 5
y = x
x = 10
print(y)


a = [1, 2, 3]
b = a
a.append(4)
print(b)


"""
✏️ 2. Anotações de Tipo com typing
Desde o Python 3.5, temos suporte para anotações de tipo. Elas ajudam na documentação e na verificação estática.

Principais Tipos:
List, Dict, Tuple, Set

Optional, Union

Callable, Any

Exemplo de Função com Anotações:
""" # noqa501


def process_data(data: List[int], factor: int) -> Dict[str, Optional[float]]:
    result = sum(data) * factor
    return {"total": result if result > 0 else None}


print(process_data([1, 2, 3], 10))


"""
🔄 3. Tipos Genéricos e Protocolos
Tipos Genéricos:
Permitem criar funções que aceitam diferentes tipos, mantendo a tipagem.

Exemplo:
""" # noqa501


def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]


print(reverse_list([1, 2, 3]))
print(reverse_list(['a', 'b', 'c']))


"""
Protocolos:
Definem um conjunto de métodos que uma classe deve ter para ser considerada compatível.

Exemplo:
""" # noqa501


class Flyer(Protocol):
    def fly(self) -> str:
        ...


class Bird:
    def fly(self) -> str:
        return "Flapping wings!"


def take_off(flyer: Flyer) -> None:
    print(flyer.fly())


bird = Bird()
take_off(bird)
