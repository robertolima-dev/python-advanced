import asyncio
import zipfile

import aiohttp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
💡 1. Processamento Assíncrono
O processamento assíncrono permite que um programa execute operações de I/O sem bloquear o fluxo principal. Isso é especialmente útil para:

Operações de rede (APIs, WebSockets)

Entrada/Saída (I/O) de arquivos grandes

Tarefas que envolvem espera
""" # noqa501


async def say_hello():
    print("Olá!")
    await asyncio.sleep(2)
    print("Adeus!")


async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_hello())
    await task1
    await task2

asyncio.run(main())


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main2():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result[:100])

asyncio.run(main2())



"""
📂 2. Manipulação de Arquivos e Streams
2.1 Arquivos de Texto e Binários
Leitura e Escrita Simples

2.2 Manipulação de Arquivos ZIP
""" # noqa501


with open("data.txt", "w") as f:
    f.write("Aprendendo Python!\n")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)


df = pd.read_csv("data.csv")
print(df.head())
df.to_csv("output.csv", index=False)


with zipfile.ZipFile("my_file.zip", "w") as zipf:
    zipf.write("data.txt")

with zipfile.ZipFile("my_file.zip", "r") as zipf:
    zipf.extractall("extracted")


df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
print(df.head())

print(df.describe())
if 'JAN' in df.columns:
    print(df['JAN'].mean())
else:
    print("Coluna 'JAN' não encontrada!")

arr = np.array([1, 2, 3, 4])
print(arr * 2)

print(np.mean(arr))
print(np.std(arr))


x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, marker='o')
plt.title("Gráfico Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
