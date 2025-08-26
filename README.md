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

