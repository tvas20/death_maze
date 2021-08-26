# Death Maze
  Death Maze é baseado em uma experiência 2D que mistura um jogo de _shooting_ com sobrevivência. Dentro do _game_, o jogador inicialmente deverá se preparar para as muitas hordas de zumbis que terá de enfrentar. Para isso, ele contará com 60s para coletar munição, podende também coletar tempo extra para atrasar em alguns segundos a chegada dos zumbis e ter a oprtunidade recolher ainda mais munição. Ao termino desse tempo de preparação, chega o momento de combater as sucessivas hordas de zumbis e o único item coletável disponível ao jogador será a munição. A sua pontuação é baseada na quantidade de zumbis combatidos a cada horda que se passa. Os itens (munição e tempo extra) surgem aleatóriamente no labirinto enquanto eles são coletados. O jogo tem fim quando seu jogador é derrotado durante uma horda.

## Equipe:
- Abhner Adriel (aacs2)
- Lucas Acioly (jlca)
- Lucas Pontes (lpp3)
- Lucas Van-Lume (lvll)
- Pedro Fonseca (paalf)
- Tiago Victor (tvas)

## Link para o codigo fonte:
- https://github.com/tvas20/death_maze

## Divisão de tarefas:

|      Equipe      |     Tarefas (principal)     |
| ------------------- | ------------------- |
|  **aacs2** |  Movimentação dos zumbis e do player & Criação sistema de _shooting_|
|  **jlca** |  Gerenciamento dos itens e sistema de colisão |
|  **lpp3** |  Relatório e planejamento da apresentação |
|  **lvll** |  Gerenciamento dos itens |
|  **paalf** |  Criação do Labirinto e sistema de colisão|
|  **tvas** |  Spawn dos itens |

## Organização do código:
  Trata-se de um código monolítico que contém um loop principal onde toda a lógica do _game_ acontece. Tendo algumas funções de grande valia para que tudo funcione:
- **def player(x, y)**:
> A função é responsável por desenhar a sprite do player principal na tela a partir de um par ordenado recebido como parâmetro.
- **def fire_bullet(x, y)**:
> Função que recebe como parâmetro um par ordenado vinculado ao player principal, e desenha a sprite da bala de fogo na tela com um pequeno incremento em cada coordenada para posiciona-la com a arma da sprite do player principal.
- **def colisao_bala_zombie(rect_bullet, lista_zombie)**:
> Função que tem como parâmetro a bala de fogo e uma matriz que contém os zumbis presentes na tela do jogo, verificando se houve colisão entre a bala de fogo e algum dos zumbis. Em caso de colisão, o zumbi é removido da tela.
- **def colisao_bala_parede(bullet_rect)**:
> Função definida para verificar a ocorrência de colisão entre a bala de fogo e as paredes presentes no mapa do jogo.
- **def criar_inimigos(lista_zombie)**:
> Função responsável pela implementação dos zumbis em um sistema de matriz que conterá as coordenadas do zumbi e sua velocidade com auxílio da biblioteca random.
- **def desenhar_inimigo(lista_zombie)**:
> Função responsável por receber a matriz dos inimigos (zumbis) e desenhá-los na tela do jogo.
- **def colisao_player_inimigo(rect_player, lista_zombies)**:
> Função que determina a ocorrência de colisão entre o player principal e os zumbis. Se confirmada a colisão, a vida do player é decrescida.
- **def collision_test(rect, tiles)**:
> Função implementada com o objetivo de analisar possíveis colisões entre um objeto e as paredes do mapa.
- **def movement(rect, move, titles)**:
> Função que detecta a direção e o sentido de colisão entre o player e as paredes do mapa a partir da função collision_test.
- **def colision_test_for_spawnables(sprite_tect, sprite_img, x, y)**:
> Função que detecta a colisão entre os objetos gerenciáveis e as paredes no momento do spaw. Caso ocorra a colisão, novas coordenadas são escolhidas por meio da biblioteca random.
- **def restart()**:
> Nessa função, as principais variáveis do jogo são atualizadas para os seus valores de inicio e o jogo é recomeçado.

## Bibliotecas/Módulos usada(o)s:
- **Pygame**:
> Esta biblioteca é um conjunto de módulos que foi desenvolvida para a escrita de jogos, ela permite que você crie jogos e programas multimidia a partir da linguagem python.
- **Os**:
> Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes do sistema operacional. Em nosso código foi usado para o acesso aos _Assets_ (imagens e sons, usados no jogo)
- **Random**:
> Este módulo implementa geradores de números pseudoaleatórios. Foi usado no jogo para o _spawn_ aleatorio de itens e zumbis.
- **Sys**:
> Este módulo te da acesso a algumas variaveis usadas pelo interpretador e que interagem diretamente com o código. Dentro do _game_ foi usado a função _sys.exit()_ para a parada total do script.

## Conceitos:
- **Laços**:
> Podem ser usados no código a partir dos comandos _For_ e _While_, estas estruturas permitem a execução de instruções repetidas vezes, até que uma condição seja atingida. Dentro do jogo essa função cumpre talvez o papel mais essencial, que se trata do _loop_ principal onde ocorre as mudanças como a movimentação do jogador e a atualização do _frame_ do jogo.
- **Estruturas condicionais**:
> Podem ser usados no código a partir dos comandos _If_, _Elif_ e _Else_, esta estrutura permite a checagem de preposições, quando uma condição é verdade ela executará o trecho de código atrelado a ela. Dentro do jogo essa função é usada essencialmente na movimentação do player principal. 
- **Funções**:
> Podem ser usados no código apenas se definidas previamente com a sintaxe _def()_, a partir de sua definição podemos invoca-la quantas vezes for necessario dentro do código utilizando apenas o nome que foi dado a ela no momento de sua definição, esta estrutura define um conjunto de comandos, dentro de qualquer programa com um conjunto de comandos que se repita muitas vezes se torna imprescindivel seu uso.

## Desafios/Experiência:

- **Github**:
> Inicialmente, o _Github_ foi um grande desafio para todos no grupo, pois poucos tinham conhecimento dessa ferramenta. Muitos conceitos foram aprendidos a partir de seu estudo, tanto a criação de um novo repositório quanto fazer um _git pull_, _pull request_, criar _branch_, e até mesmo aprender a formatação texto de um arquivo legivel (_README_).   
- **Programação em equipe**:
> A programação em equipe já é um grande desafio, e se torna ainda maior quando se usa uma ferramenta (Github) que pouco se conhece, ou que não se tem muita experiencia, contudo a programação em equipe se torna vantajosa apartir do momento que se encontram algumas barreiras e dificuldades, pois algumas dificuldades para alguns podem não ser para outros e vice-versa.
- **Pygame**:
> O _pygame_ foi um dos grandes desafios para toda equipe, pois foi um instrumento de uso obrigatório, em que todos deveriam saber sobre e entender o mínimo, para de imediato começarmos a trabalhar. Muitas coisas foram aprendidas com o uso dessa vasta biblioteca, que vai desde a criação de um simples quadrado movél na tela, até um jogo mais complexo conforme foi apresentado em nosso projeto. 

#
###### *Projeto referente a matéria de Introdução a programação/CIN-UFPE no periodo de 2020.2. Começamos em 12/08/2021*
