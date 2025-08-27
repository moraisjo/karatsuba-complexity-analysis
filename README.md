# Algoritmo de Karatsuba

## 📌 Descrição do Projeto
Este projeto implementa o **algoritmo de Karatsuba** para multiplicação de inteiros grandes. O algoritmo segue uma abordagem **recursiva**, reduzindo o número de multiplicações necessárias em comparação à multiplicação tradicional. O propósito deste projeto é o de analisar a complexidade ciclomática e assintótica do algoritmo do algoritmo em questão e explorar os conceitos de complexidade ciclomática, notação Big-O e complexidade assintótica.

### 🔎 Explicação da Lógica
O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números inteiros grandes usando divisão e conquista, que reduz o número de multiplicações necessárias em comparação ao método tradicional.

O funcionamento do algoritmo pode ser descrito em etapas. 

Caso base:<br>
Se um dos números for menor que 10 (ou seja, tiver apenas um dígito), o algoritmo realiza a multiplicação direta. Esse é o caso mais simples e termina a recursão.

Divisão dos números:<br>
Para números maiores, o algoritmo divide cada número em duas partes: a parte alta (high_x, high_y) e a parte baixa (low_x, low_y). Por exemplo, se o número tiver 6 dígitos, ele será dividido ao meio em dois números de 3 dígitos cada. Essa divisão é feita usando a função divmod e potências de 10, de forma que:<br>
```code
high_x, low_x = divmod(x, 10**m)
high_y, low_y = divmod(y, 10**m)
```

Chamadas recursivas:
O Karatsuba faz três multiplicações recursivas, cada uma envolvendo números menores:<br>
`z0 = karatsuba(low_x, low_y)` → multiplica as partes baixas.<br>
`z1 = karatsuba(low_x + high_x, low_y + high_y)` → multiplica a soma das partes alta e baixa.<br>
`z2 = karatsuba(high_x, high_y)` → multiplica as partes altas.<br>

A recursão continua até que todos os subproblemas cheguem ao caso base (números de um dígito).

Combinação dos resultados:<br>
Após as chamadas recursivas, os resultados são combinados para formar o produto final.  

Essa técnica reduz o número de multiplicações diretas de quatro (como na abordagem tradicional) para **três multiplicações recursivas**, tornando o algoritmo mais rápido para números grandes.

A parte **recursiva** é a chave: a cada nível, o algoritmo divide os números ao meio e multiplica apenas três pares, até chegar a números pequenos o suficiente para multiplicar diretamente.

Em resumo, o Karatsuba **divide o problema em subproblemas menores**, resolve cada um recursivamente e depois combina os resultados de forma inteligente, aproveitando somas e subtrações para reduzir o trabalho total.  

### Fluxo de Controle
| Nó      | Ação                                                                                                                  |
| ------- | --------------------------------------------------------------------------------------------------------------------- |
| **N1**  | Início da função `karatsuba(x, y)`                                                                                    |
| **N2**  | Verificação do caso base: `if x < 10 or y < 10`                                                                       |
| **N3**  | Retorno direto caso base: `return x * y`                                                                              |
| **N4**  | Cálculo do tamanho dos números: `n = max(len(str(x)), len(str(y)))`                                                   |
| **N5**  | Cálculo do ponto médio `m = n // 2`                                                                                   |
| **N6**  | Divisão dos números em partes altas e baixas: `high_x, low_x = divmod(x, 10**m)` e `high_y, low_y = divmod(y, 10**m)` |
| **N7**  | Chamada recursiva `z0 = karatsuba(low_x, low_y)`                                                                      |
| **N8**  | Chamada recursiva `z1 = karatsuba(low_x + high_x, low_y + high_y)`                                                    |
| **N9**  | Chamada recursiva `z2 = karatsuba(high_x, high_y)`                                                                    |
| **N10** | Combinação dos resultados parciais `(z1 - z2 - z0) * 10**m`                                                           |
| **N11** | Retorno final da função: `(z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0`                                           |

### Grafo
![Grafo](https://raw.githubusercontent.com/moraisjo/karatsuba-complexity-analysis/524b8e9cd84f489c8e5bd77db41966ff40b18f62/docs/graph-karatsuba.drawio.svg)

## O que é Complexidade Ciclomática?
A complexidade ciclomática é uma métrica usada para medir a complexidade do fluxo de controle de um programa. Ela calcula o número de caminhos independentes no código, considerando estruturas como loops (for, while) e condicionais (if, try/except). Quanto maior o valor, mais complexo é o código.

### Calculo da complexidade ciclomática
Fórmula:
$( M = E - N + 2P )$

Onde:
(M): Complexidade Ciclomática
(E): Número de arestas (transições) no grafo do controle de fluxo
(N): Número de nós (blocos de código)
(P): Componentes conectados (em 1 único programa)

Substituindo os valores na fórmula, temos:
<br>
$M = 10 - 11 + 2*1$<br>
$M = -1 + 2 = 1$

### Complexidade Temporal
O algoritmo de Karatsuba é um algoritmo de multiplicação de inteiros baseado em **divisão e conquista**.

1. Se $x < 10$ ou $y < 10$, multiplicação direta $O(1)$ (caso base).
2. Dividir os números ao meio (com `divmod`) → custo $O(n)$, pois envolve manipulação de strings ou logaritmo do número.
3. Três chamadas recursivas de Karatsuba:

   * $z0 = karatsuba(low_x, low_y)$
   * $z1 = karatsuba(low_x + high_x, low_y + high_y)$
   * $z2 = karatsuba(high_x, high_y)$
4. Combinar os resultados → custo $O(n)$, multiplicações por potências de 10.

✅ Logo, o valor da complexidade temporal é:

$$
\boxed{O(n^{1.585})}
$$

## Complexidade Espacial
* Cada chamada recursiva cria variáveis locais (`high_x`, `low_x`, `z0`, `z1`, `z2`), mas elas são de tamanho proporcional a $n$.
* A profundidade da recursão é $O(\log n)$ (porque o tamanho do número é dividido por 2 a cada chamada).

Então o **uso de memória da pilha** é:

$$
O(\log n)
$$

Se considerarmos **armazenamento adicional para as somas e produtos**, o custo pode ser considerado **O(n)** por nível, mas geralmente o **espaço adicional é O(n)** no total.

✅ Complexidade espacial: $O(n)$ adicional + $O(\log n)$ para a pilha de chamadas.

### Casos de execução
No Karatsuba, **o número de operações não depende dos valores específicos dos números**, apenas do tamanho $n$ (número de dígitos). Portanto:

* **Melhor caso:** $O(1)$ (quando não entra na parte recursiva e faz a multiplicação direto)
* **Caso médio:** $O(n^{1.585})$
* **Pior caso:** $O(n^{1.585})$

## Como rodar este programa?
### Ambiente virtual
Passo 1: Criar e ativar o ambiente virtual
É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

Crie um ambiente virtual usando o seguinte comando:
```code
python3 -m venv .venv
```

Ative o ambiente virtual:

No macOS e Linux:
```code
source .venv/bin/activate
```

No Windows:
```code 
.venv\Scripts\activate
```

Passo 2: Executar o script
Após ativar o ambiente virtual, execute o script principal:
```code
python main.py
```

## Versão do Python
Este projeto foi desenvolvido na versão `3.12.3` do Python e não exige a instalação de nenhuma dependência adicional.

