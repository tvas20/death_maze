'''
    ===================================================
    ====    Projeto de Introdução à Programação    ====
    ===================================================

    Tema: Sistema Interativo - Jogo 
    Alunos: Abhner Adriel, Lucas Acioly, Lucas Pimentel, Lucas Van-Lume, Pedro Fonseca, Tiago Victor

'''

import random
import pygame
from pygame.locals import *
from sys import exit

clock = pygame.time.Clock()  # Set up the clock

# Window
pygame.init()
pygame.display.set_caption('Death Maze')
icon = pygame.image.load('death_maze/Assets/images/icon.png')
pygame.display.set_icon(icon)
width, height = 640, 760

window = pygame.display.set_mode((width, height))
canvas = pygame.Surface((640, 640))

# fonte das letras na tela
fonte = pygame.font.Font("death_maze/Font/PKMN.ttf", 20)

# Player
player_img = pygame.image.load('death_maze/Assets/images/sprites/player-right.png')
x_player = (width / 2) - player_img.get_width() 
y_player = (height / 2) - player_img.get_width()
player_rect = pygame.Rect(x_player, y_player, player_img.get_width(), player_img.get_height())  # Set up the hitbox
player_speed = 8.65 # ------> ALTEREI AQUI <------
player_health = 100 # ------> ALTEREI AQUI <------

# colisão do player com as bordas do labirinto:
player_img_rect = player_img.get_rect()
player_img_rect.center = [x_player, y_player]
dead = False

def player(x, y):
    canvas.blit(player_img, (x, y))
    player_img_rect.center = [x, y]

moving_u = False
moving_d = False
moving_r = False
moving_l = False

# ------> ALTEREI AQUI <------

# criação da bala do player:
bullet_img = pygame.image.load('death_maze/Assets/images/sprites/bullet.png')
x_bullet = width + 64
y_bullet = height + 64
bullet_rect = pygame.Rect(x_bullet, y_bullet, bullet_img.get_width(), bullet_img.get_height())
bullet_spped = 30
bullet_state = 'ready' # pronta para ser disparada
bullet_collided_zombie = False

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    canvas.blit(bullet_img, (x + 10.5, y + 10.4))

# gravar o sentido apontado pelo player:
ultima_tecla_pressionada = 'd'

def colisao_bala_zombie(rect_bullet, lista_zombie):
    global player_img, bullet_collided_zombie, killstreak
    lista_zombie_copia = [x for x in lista_zombie]
    for zombie in lista_zombie_copia:
        if rect_bullet.colliderect(zombie[2]):
            lista_zombie.remove(zombie)
            bullet_collided_zombie = True
            killstreak += int(1)

def colisao_bala_parede(bullet_rect):
    global tile_rects
    for tile in tile_rects:
        if bullet_rect.colliderect(tile):
            return True
    return False

# criação do zombie (inimigo):
inimigos = []
inimigo_img = pygame.image.load('death_maze/Assets/images/sprites/zombie-right.png')
killstreak = int(0)

def criar_inimigos(lista_zombie):
    qnt_zombie = random.randint(5, 10)
    for i in range(qnt_zombie):
        x_inimigo = random.choice([-inimigo_img.get_width(), width + inimigo_img.get_width()])
        y_inimigo = random.choice([-inimigo_img.get_height(), height + inimigo_img.get_height()])
        inimigo_speed = random.choice([1.88, 2.95, 3.8, 4.95])
        inimigo_rect = pygame.Rect(x_inimigo, y_inimigo, inimigo_img.get_width(), inimigo_img.get_height())
        # cria um zombie com suas propriedades:
        lista_zombie.append([i, inimigo_img, inimigo_rect, inimigo_speed])

def desenhar_inimigos(lista_zombie): 
    for zombie in lista_zombie:
        canvas.blit(zombie[1], (zombie[2].x, zombie[2].y))

def colisao_player_inimigo(rect_player, lista_zombies):
    global player_health
    for zombie in lista_zombies:
        if rect_player.colliderect(zombie[2]):
            player_health -= 0.1

# munição-------------------------------------------------------------------------------------------------------------
ammo_count = 0

ammo1_img = pygame.image.load('death_maze/Assets/images/ammo.png')
x_ammo1 = random.randint(40, 600)
y_ammo1 = random.randint(40, 600)
ammo1_rect = pygame.Rect(x_ammo1, y_ammo1, ammo1_img.get_width(), ammo1_img.get_height())  # Set up the hitbox

ammo2_img = pygame.image.load('death_maze/Assets/images/ammo.png')
x_ammo2 = random.randint(40, 600)
y_ammo2 = random.randint(40, 600)
ammo2_rect = pygame.Rect(x_ammo2, y_ammo2, ammo2_img.get_width(), ammo2_img.get_height())  # Set up the hitbox

ammo3_img = pygame.image.load('death_maze/Assets/images/ammo.png')
x_ammo3 = random.randint(40, 600 - 32)
y_ammo3 = random.randint(40, 600 - 32)
ammo3_rect = pygame.Rect(x_ammo3, y_ammo3, ammo3_img.get_width(), ammo3_img.get_height())  # Set up the hitbox
# -------------------------------------------------------------------------------------------------------------------

# timer -------------------------------------------------------------------------------------------
current_time = 0
time_objective = 60

clock_img = pygame.image.load('death_maze/Assets/images/clock.png')
x_clock = random.randint(40, 600)
y_clock = random.randint(40, 600)
clock_rect = pygame.Rect(x_clock, y_clock, clock_img.get_width(), clock_img.get_height())  # set up hitbox

# -------------------------------------------------------------------------------------------------

# Map
ground_img, wall_img = pygame.image.load('death_maze/Assets/images/grass.png'), pygame.image.load('death_maze/Assets/images/wall.png')

game_map = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# configurações de audio:
pygame.mixer.music.set_volume(0.25) #------> ALTEREI AQUI <------
bg_music = pygame.mixer.music.load('death_maze/Assets/audio/bg_music.mp3')
pygame.mixer.music.play(-1)
shot_sound = pygame.mixer.Sound('death_maze/Assets/audio/shot_bullet.wav')
shot_sound.set_volume(0.11)

# Collision Detection Function
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


# Movement Function
def movement(rect, move, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

    # x axis colisions
    rect.x += move[0]
    hit_list = collision_test(rect, tiles)

    for tile in hit_list:
        if move[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif move[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    # y axis colisions
    rect.y += move[1]
    hit_list = collision_test(rect, tiles)

    for tile in hit_list:
        if move[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif move[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True

    return rect, collision_types

def colision_test_for_spawnables(sprite_rect, sprite_img, x, y):
    global tile_rects

    coliding_wall = True
    while coliding_wall:
        for tile in tile_rects:
            if sprite_rect.colliderect(tile):
                x = random.randint(40, 600)
                y = random.randint(40, 600)
                sprite_rect = pygame.Rect(x, y, sprite_img.get_width(), sprite_img.get_height())  # Set up the hitbox
            else:
                coliding_wall = False
    return sprite_rect
    
def restart():
    global ammo_count, player_health, killstreak, inimigos, dead

    ammo_count = 0
    player_health = 100
    killstreak = 0
    inimigos.clear()
    dead = False

tempo_rel = 0 #spawn de itens (tempo)
tempo_mun = 0 #spawn de itens (tempo)

# Game Loop
while True:
    tempo_rel += 1
    tempo_mun += 1
    # deleta a tela de fundo
    # necessario para blits não se sobreporem
    window.fill((0, 0, 0))
    canvas.fill((0, 0, 0))
    # map construction
    tile_rects = []
    r = 0  # r for row
    for row in game_map:
        c = 0  # c for column
        for tile in row:
            if tile == 0:
                canvas.blit(ground_img, (c * 32, r * 32))

            if tile == 1:
                canvas.blit(wall_img, (c * 32, r * 32))
                tile_rects.append(pygame.Rect(c * 32, r * 32, 32, 32))
            c += 1
        r += 1

    # player movement atributes
    player_movement = [0, 0]
    if moving_u and player_img_rect.top > -(player_img.get_width() / 2):
        player_movement[1] -= player_speed
    if moving_d and player_img_rect.bottom < (width - (player_img.get_width() / 2)):
        player_movement[1] += player_speed
    if moving_r and player_img_rect.right < (width - (player_img.get_width() / 2)):
        player_movement[0] += player_speed
    if moving_l and player_img_rect.left > -(player_img.get_width() / 2):
        player_movement[0] -= player_speed

    player_rect, collisions_direction = movement(player_rect, player_movement, tile_rects)

    player(player_rect.x, player_rect.y)
    
    if len(inimigos) == 0:
        criar_inimigos(inimigos)
    else:
        for zombie in inimigos:
            inimigo_movement = [0, 0]
            if player_rect.x > zombie[2].x:
                inimigo_movement[0] += zombie[3]
                if player_rect.colliderect(zombie[2]):
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-attack-right.png')
                else:
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-right.png')
            if player_rect.x < zombie[2].x:
                inimigo_movement[0] -= zombie[3]
                if player_rect.colliderect(zombie[2]):
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-attack-left.png')
                else:
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-left.png')
            if player_rect.y > zombie[2].y:
                inimigo_movement[1] += zombie[3]
                if player_rect.colliderect(zombie[2]):
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-attack-down.png')
                else:
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-down.png')
            if player_rect.y < zombie[2].y:
                inimigo_movement[1] -= zombie[3]
                if player_rect.colliderect(zombie[2]):
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-attack-up.png')
                else:
                    zombie[1] = pygame.image.load('death_maze/Assets/images/sprites/zombie-up.png')

            zombie[2], collisions_direction_zombie = movement(zombie[2], inimigo_movement, tile_rects)

        desenhar_inimigos(inimigos)

        colisao_player_inimigo(player_rect, inimigos)

        life_string = str(f'Life: {player_health:.1f}')
        texto_vida = fonte.render(life_string, True, (255, 255, 255))
        window.blit(texto_vida, (20, 720))

    # ammo spawn-------------------------------------------------------------------------------------------------
    # spawn inicial
    ammo1_rect = colision_test_for_spawnables(ammo1_rect, ammo1_img, x_ammo1, y_ammo1)  # posiciona o spawn sem colidir com as paredes
    canvas.blit(ammo1_img, (ammo1_rect.x, ammo1_rect.y))  # printa munição na tela

    # colisão com player
    if player_rect.colliderect(ammo1_rect):
        ammo_count += 3  # incrementa o total de munição

        # novo spawn
        x_ammo1 = random.randint(700, 700)
        y_ammo1 = random.randint(700, 700)
        ammo1_rect = pygame.Rect(x_ammo1, y_ammo1, player_img.get_width(), player_img.get_height())  # Set up the hitbox
        # teste de colisão pre spawn
        ammo1_rect = colision_test_for_spawnables(ammo1_rect, ammo1_img, x_ammo1, y_ammo1)
        canvas.blit(ammo1_img, (ammo1_rect.x, ammo1_rect.y))  # print na tela

    if tempo_mun == 150:
        tempo_mun = 0
        # novo spawn
        x_ammo1 = random.randint(40, 600)
        y_ammo1 = random.randint(40, 600)
        ammo1_rect = pygame.Rect(x_ammo1, y_ammo1, player_img.get_width(), player_img.get_height())  # Set up the hitbox
        # teste de colisão pre spawn
        ammo1_rect = colision_test_for_spawnables(ammo1_rect, ammo1_img, x_ammo1, y_ammo1)
        canvas.blit(ammo1_img, (ammo1_rect.x, ammo1_rect.y))  # print na tela

    ammo_string = str(f'Ammo: {str(ammo_count)}')
    texto_municao = fonte.render(ammo_string, True, (255, 255, 255))
    window.blit(texto_municao, (500, 20))

    # ----------------------------------------------------------------------------------------------------------------

    # timer implementation -------------------------------------------------------------------------------------------
    current_time = pygame.time.get_ticks() // 1000  # pega o tempo a partir da execução do programa em milissegundos e
    # converte para segundos
    timer = time_objective - current_time  # cronometro propriamente dito

    # spawn dos relógios
    # primeiro spawn
    clock_rect = colision_test_for_spawnables(clock_rect, clock_img, x_clock, y_clock)
    canvas.blit(clock_img, (clock_rect.x, clock_rect.y))  # prpinta relogio na tela

    # colisão com player
    if player_rect.colliderect(clock_rect):
        time_objective += 5  # incremento no objetivo de tempo

        # novo spawn
        x_clock = random.randint(700, 700)
        y_clock = random.randint(700, 700)
        clock_rect = pygame.Rect(x_clock, y_clock, clock_img.get_width(), clock_img.get_height())  # set up hitbox
        # teste de colisão pre spawn
        clock_rect = colision_test_for_spawnables(clock_rect, clock_img, x_clock, y_clock)
        canvas.blit(clock_img, (clock_rect.x, clock_rect.y))  # printa relogio na tela

    if tempo_rel == 350:
        tempo_rel = 0
        # novo spawn
        x_clock = random.randint(40, 600)
        y_clock = random.randint(40, 600)
        clock_rect = pygame.Rect(x_clock, y_clock, clock_img.get_width(), clock_img.get_height())  # set up hitbox
        # teste de colisão pre spawn
        clock_rect = colision_test_for_spawnables(clock_rect, clock_img, x_clock, y_clock)
        canvas.blit(clock_img, (clock_rect.x, clock_rect.y))  # printa relogio na tela

    cronometro = f"Zombies coming in: {timer}s"
    texto_cronometro = fonte.render(cronometro, True, (255, 255, 255))
    window.blit(texto_cronometro, (20, 20))

    # -----------------------------------------------------------------------------------------------------------

    for event in pygame.event.get():
        if event.type == QUIT:  # Check for window quit
            pygame.quit()  # Stop pygame
            exit()  # Stop script
        # game over
        if player_health <= 0:
            game_over = str('YOU DIED')
            press_r = str("Press 'R' to retry")
            message_go = fonte.render(game_over, True, (255, 0, 0))
            message_r = fonte.render(press_r, True, (255, 255, 255))
            rect_go = message_go.get_rect()
            rect_r = message_r.get_rect()
            dead = True
            while dead:
                window.fill((0,0,0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            restart()
                
                rect_go.center = (width//2, height//2 - 15)
                rect_r.center = (width//2, height//2 + 15)
                window.blit(message_go, rect_go)
                window.blit(message_r, rect_r)
                pygame.display.update()
        
        # movement events
        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                moving_u = True
                if bullet_state == 'ready':
                    ultima_tecla_pressionada = 'w'
                    player_img = pygame.image.load('death_maze/Assets/images/sprites/player-up.png')
            if event.key == K_a or event.key == K_LEFT:
                moving_l = True
                if bullet_state == 'ready':
                    ultima_tecla_pressionada = 'a'
                    player_img = pygame.image.load('death_maze/Assets/images/sprites/player-left.png')
            if event.key == K_s or event.key == K_DOWN:
                moving_d = True
                if bullet_state == 'ready':
                    ultima_tecla_pressionada = 's'
                    player_img = pygame.image.load('death_maze/Assets/images/sprites/player-down.png')
            if event.key == K_d or event.key == K_RIGHT:
                moving_r = True
                if bullet_state == 'ready':
                    ultima_tecla_pressionada = 'd'
                    player_img = pygame.image.load('death_maze/Assets/images/sprites/player-right.png')
            if event.key == K_SPACE and bullet_state == 'ready' and ammo_count > 0:
                bullet_rect.x = player_rect.x
                bullet_rect.y = player_rect.y
                fire_bullet(bullet_rect.x, bullet_rect.y)
                ammo_count -= 1 # ALTEREI AQUI <------
                shot_sound.play()
                

        if event.type == KEYUP:
            if event.key == K_w or event.key == K_UP:
                moving_u = False
            if event.key == K_a or event.key == K_LEFT:
                moving_l = False
            if event.key == K_s or event.key == K_DOWN:
                moving_d = False
            if event.key == K_d or event.key == K_RIGHT:
                moving_r = False
    
    # ------> ALTEREI AQUI <------
    # movimento da bala:
    if (bullet_rect.x < -(player_img.get_width() / 2) or bullet_rect.x >= width or bullet_rect.y <= 0 or bullet_rect.y >= height
        or bullet_collided_zombie or colisao_bala_parede(bullet_rect)):
        bullet_rect.x = width + 64
        bullet_rect.y = height + 64
        bullet_state = 'ready' 
        bullet_collided_zombie = False
    
    if bullet_state == 'fire':
        if ultima_tecla_pressionada == 'w':
            bullet_rect.y -= bullet_spped
        if ultima_tecla_pressionada == 'a':
            bullet_rect.x -= bullet_spped
        if ultima_tecla_pressionada == 's':
            bullet_rect.y += bullet_spped
        if ultima_tecla_pressionada == 'd':
            bullet_rect.x += bullet_spped
        fire_bullet(bullet_rect.x, bullet_rect.y)

    if len(inimigos) > 0:
        colisao_bala_zombie(bullet_rect, inimigos)

    killstreak_string = str(f'Killstreak: {killstreak}')
    texto_killstreak = fonte.render(killstreak_string, True, (255, 255, 255))
    window.blit(texto_killstreak, (400, 720))

    surf = pygame.transform.scale(canvas, (640, 640))
    window.blit(surf, (0, 60))
    pygame.display.update()
    clock.tick(30)  # Framerate