# karatsuba-complexity-analysis

## Sobre o Projeto
Este é um projeto educativo desenvolvido para analisar a complexidade ciclomática do algoritmo de Karatsuba em Python e explorar a relação entre a complexidade ciclomática, a notação Big-O e complexidade assintótica.

## O que é Complexidade Ciclomática?
A complexidade ciclomática é uma métrica usada para medir a complexidade do fluxo de controle de um programa. Ela calcula o número de caminhos independentes no código, considerando estruturas como loops (for, while) e condicionais (if, try/except). Quanto maior o valor, mais complexo é o código.

Fórmula:
( M = E - N + 2P )

Onde:
(M): Complexidade Ciclomática
(E): Número de arestas (transições) no grafo do controle de fluxo
(N): Número de nós (blocos de código)
(P): Componentes conectados (geralmente 1 para programas simples)

## 📌 Descrição do Projeto
Este projeto implementa o **algoritmo de Karatsuba** para multiplicação de inteiros grandes.  
O algoritmo segue uma abordagem **recursiva**, reduzindo o número de multiplicações necessárias em comparação à multiplicação tradicional.

### 🔎 Explicação da Lógica
Caso base: se x ou y tiverem apenas um dígito realiza a multiplicação
Determina o tamanho do maior número
Divide os números em partes altas e baixas
Três multiplicações recursivas
Combina os resultados para formar o produto final

### 🔎 Fluxo de Controle
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

### 🔎 Grafo



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

