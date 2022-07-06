# Jogo da Velha
## Abordagem com algoritmo Minimax

### Formulação do Problema:
**Estado Inicial:** dois jogadores podem inserir os valores "X" ou "O" são inseridos na tabela;

**Ações possíveis e disponíveis:** existem nove posições que podem ser inseridas os simbolos, exceto na célula onde já contem um simbolo inserindo;

**Modelo de transição:**  é necessáro que se completem três jogadas para cada jogador;

**Teste de Objetivo:** para cada jogada é observado a jogada do adversário em bausca de minimizar a viória do outro maximizando a possibilidade de vitória do jogador;

**Estado Ótimo:** o jogador atinge o estádo ótimo quando insere três simbolos em linha, seja na diagnonal, horizontal ou vertical;

### Desenvolvimento
Um algoritmo foi desenvolvivo em Python, inicialmente com objetivo de compreender como seria o funcionamento e os resultados obtidos. Também foi craido o algoritmo Minmax para compreender os resultados e sua estrutura.

Após a criação dos dois algoritmos foi imcorporado ao algoritmo de "Jogo da Velha" o algoritmo de Minimax adaptando suas funcionalidades.

### Estrutura do algoritmo
**1. Foram criadas as funções:**
- **_def mostrarGrade(grade):_** exibe a grade do jogo a cada nova jogada;
- **_def espacoLivre(posicao):_** verifica se a posição está vazia para inserir o simbolo;
- **_def inserirSimbolo(simbolo,posicao):_** insere o simbolo conforme a posisão;
- **_def verificarVitoria():_** verifica a vitória do do jogador conforme os critérios do jogos retornando valor '1'.
- **_def verificarVencedor(escolha):_** verficar o vencedor conforme o simbolo escolhido retornando valor '-1';
- **_def verificarEmpate():_** verifica empate retornado valor '0';
- **_def jogadorMovimento():_** solicita ao jogador a posição a ser inserida entre 1 e 9;
- **_def Movimento():_** insere a posição computada para maquina dentro da melhor posição maximizada;
- **_def minimax(grade, profundidade, maximizado):_** responsável por percorrer os nós da "grade" conforme a profundidade até atingir o nó folha efetuando as podas conforme os valores minimizados e maximizando a melhor pontuação, entragando a melhor pontuação e melhor posição. Quando todas as posições forem precorridas será obtido um valor TRUE para valiável "maximizado".

### Conclusão
Durante a cada nova interação do jogador o algoritmo Minimax é acionado para verificar qual o melhor movimento trazendo a melhor pontuação e a melhor posição, dessa forma é possível percorrer cada nó efetuando as podas dos nós folhas quando atingido o valor maximizado, que seria o estado ótimo de vitória do jogo.
