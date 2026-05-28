from typing import TypeVar

# 1. Declara a variável de tipo
T = TypeVar("T")


# 2. Usa na função (sem os colchetes no nome da função)
def primeiro_elemento_antigo(lista: list[T]) -> T:
    return lista[0]


result = primeiro_elemento_antigo(["2"])
print(type(result))