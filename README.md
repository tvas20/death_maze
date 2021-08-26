
# Death Maze
  É um jogo baseado em uma experiência 2D que mistura um jogo de _shooting_ com sobrevivência. Dentro do _game_, o jogador deve coletar recursos como munição, para que a horda seja combatida, e tempo extra, para atrasar em alguns segundos a chegada dos zumbis. A sua pontuação é baseada na quantidade de vezes em que você consegue combater a horda e sair vitorioso. Os itens (munição e tempo extra) surgem aleatóriamente no labirinto enquanto o jogador coleta os próprios itens. O jogo tem fim quando seu jogador é derrotado durante uma horda.

## Equipe:
- Abhner Adriel (aacs2)
- Lucas Acioly (jlca)
- Lucas Pontes (lpp3)
- Lucas Van (lvll)
- Pedro Fonseca (paalf)
- Tiago Victor (tvas)

## Link para o codigo fonte:
- https://github.com/tvas20/death_maze

## Código:


## Bibliotecas/Módulos usada(o)s:
- **Pygame**:
> Esta biblioteca é um conjunto de módulos que foi desenvolvida para a escrita de jogos, ela permite que você crie jogos e programas multimidia a partir da linguagem python.
- **Os**:
> Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes do sistema operacional. Em nosso código foi usado para o acesso aos _Assets_ (imagens e sons, usados no jogo)
- **Random**:
> Este módulo implementa geradores de números pseudoaleatórios. Foi usado no jogo para o _spawn_ aleatorio de itens e zumbis.
- **Sys**:
> Este módulo te da acesso a algumas variaveis usadas pelo interpretador e que interagem diretamente com o código. Dentro do _game_ foi usado a função _sys.exit()_ para a parada total do script.

## Divisão de tarefas:

|      Equipe      |     Tarefas (principal)     |
| ------------------- | ------------------- |
|  **aacs2** |  Movimentação: Zumbis & Criação: sistema de _shooting_|
|  **jlca** |  Criação: Labirinto |
|  **lpp3** |  Criação: Menu |
|  **lvll** |  Gerenciamento: Itens |
|  **paalf** |  Criação/Colisão: Labirinto |
|  **tvas** |  Spawn: Itens |


## Conceitos:
- **Laços**:
> Podem ser usados no código a partir dos comandos _For_ e _While_, estas estruturas permitem a execução de instruções repetidas vezes, até que uma condição seja atingida. Dentro do jogo essa função cumpre talvez o papel mais essencial, que se trata do _loop_ principal onde ocorre as mudanças como a movimentação do jogador e a atualização do _frame_ do jogo.
- **Estruturas condicionais**:
> Podem ser usados no código a partir dos comandos _If_, _Elif_ e _Else_, esta estrutura permite a checagem de preposições, quando uma condição é verdade ela executará o trecho de código atrelado a ela. Dentro do jogo essa função é usada essencialmente na movimentação do player principal. 
- **Funções**:
> Podem ser usados no código apenas se definidas previamente com a sintaxe _def()_, a partir de sua definição podemos invoca-la quantas vezes for necessario dentro do código utilizando apenas o nome que foi dado a ela no momento de sua definição, esta estrutura define um conjunto de comandos, dentro de qualquer programa com um conjunto de comandos que se repita muitas vezes se torna imprescindivel seu uso.


## Desafios/Experiência:

- **Github**:
> Inicialmente, o github foi um grande desafio para todos no grupo pois poucos ou nenhum tinham conhecimento dessa ferramenta. Muitos conceitos foram aprendidos a partir de seu estudo, tanto a criação de um novo repositório quanto fazer um git pull,pull request, criar branchs, e até mesmo aprender a formatação de texto de arquivo legivel.   
- **Programação em equipe**:
> A programação em equipe, já é um grande desafio, se torna ainda maior quando se usa uma ferramenta (Github) que não conhece, ou que não se tem muita experiencia, contudo a programção em equipe se torna vantajosa apartir do momento que se encontram algumas barreiras e dificuldades, pois algumas dificuldades para alguns podem não ser para outros e vice-versa.
- **Pygame**:
> O pygame foi um dos grandes desafios para toda equipe pois, foi um instrumento de uso obrigatório em que todos deveriam saber sobre e entender o minimo para já começarmos a trabalhar. Muitas coisas foram aprendidas com o uso dessa vasta biblioteca desde a criação de um simples quadrado movél na tela até um jogo mais complexo conforme foi apresentado em nosso projeto. 

#
###### *Projeto referente a matéria de Introdução a programação/CIN-UFPE no periodo de 2020.2. Começamos em 12/08/2021*
