'''
    ===================================================
    ====    Projeto de Introdução à Programação    ====
    ===================================================

    Tema: Sistema Interativo - Jogo 
    Alunos: Abhner Adriel, 

'''

import random
import pygame
from pygame.locals import *
from sys import exit
#from Objects import * (está dando erro no carregamento do jogo)

clock = pygame.time.Clock()  # Set up the clock

# Window
pygame.init()
pygame.display.set_caption('Death Maze')
width, height = 640, 700

window = pygame.display.set_mode((width, height))
canvas = pygame.Surface((640, 640))

# fonte das letras na tela
fonte = pygame.font.SysFont("arial", 20, True, False)

# Player
player_img = pygame.image.load('game_theme/Assets/images/sprites/player-right.png')
x_player = 288
y_player = 320
player_rect = pygame.Rect(x_player, y_player, player_img.get_width(), player_img.get_height())  # Set up the hitbox
player_speed = 3.5

moving_u = False
moving_d = False
moving_r = False
moving_l = False

# munição-------------------------------------------------------------------------------------------------------------
ammo_count = 0

ammo1_img = pygame.image.load('game_theme/Assets/images/bullets.png')
x_ammo1 = random.randint(40, 600)
y_ammo1 = random.randint(40, 600)
ammo1_rect = pygame.Rect(x_ammo1, y_ammo1, ammo1_img.get_width(), ammo1_img.get_height())  # Set up the hitbox

ammo2_img = pygame.image.load('game_theme/Assets/images/bullets.png')
x_ammo2 = random.randint(40, 600)
y_ammo2 = random.randint(40, 600)
ammo2_rect = pygame.Rect(x_ammo2, y_ammo2, ammo2_img.get_width(), ammo2_img.get_height())  # Set up the hitbox

ammo3_img = pygame.image.load('game_theme/Assets/images/bullets.png')
x_ammo3 = random.randint(40, 600 - ammo3_img.get_width())
y_ammo3 = random.randint(40, 600 - ammo3_img.get_height())
ammo3_rect = pygame.Rect(x_ammo3, y_ammo3, ammo3_img.get_width(), ammo3_img.get_height())  # Set up the hitbox
# -------------------------------------------------------------------------------------------------------------------

# timer -------------------------------------------------------------------------------------------
current_time = 0
time_objective = 60

clock_img = pygame.image.load('game_theme/Assets/images/hourglass.png')
x_clock = random.randint(40, 600)
y_clock = random.randint(40, 600)
clock_rect = pygame.Rect(x_clock, y_clock, clock_img.get_width(), clock_img.get_height())  # set up hitbox

# -------------------------------------------------------------------------------------------------

# Map
ground_img, wall_img = pygame.image.load('game_theme/Assets/images/grassdirt-small.png'), pygame.image.load('game_theme/Assets/images/wall.jpeg')

game_map = [[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

# background music (test):
pygame.mixer.music.set_volume(0.07)
bg_music = pygame.mixer.music.load('game_theme/Assets/audio/bg_music.mp3')
pygame.mixer.music.play(-1)

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
                sprite_rect = pygame.Rect(x, y, sprite_img.get_width(),
                                     sprite_img.get_height())  # Set up the hitbox
            else:
                coliding_wall = False
    return sprite_rect


# Game Loop
while True:
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
    if moving_u:
        player_movement[1] -= player_speed
    if moving_d:
        player_movement[1] += player_speed
    if moving_r:
        player_movement[0] += player_speed
    if moving_l:
        player_movement[0] -= player_speed

    player_rect, collisions_direction = movement(player_rect, player_movement, tile_rects)

    canvas.blit(player_img, (player_rect.x, player_rect.y))

    # ammo spawn-------------------------------------------------------------------------------------------------
    # spawn inicial
    ammo1_rect = colision_test_for_spawnables(ammo1_rect, ammo1_img, x_ammo1,
                                              y_ammo1)  # posiciona o spawn sem colidir com as paredes
    canvas.blit(ammo1_img, (ammo1_rect.x, ammo1_rect.y))  # printa munição na tela

    # colisão com player
    if player_rect.colliderect(ammo1_rect):
        ammo_count += 1  # incrementa o total de munição

        # novo spawn
        x_ammo1 = random.randint(40, 600)
        y_ammo1 = random.randint(40, 600)
        ammo1_rect = pygame.Rect(x_ammo1, y_ammo1, player_img.get_width(), player_img.get_height())  # Set up the hitbox
        # teste de colisão pre spawn
        ammo1_rect = colision_test_for_spawnables(ammo1_rect, ammo1_img, x_ammo1, y_ammo1)
        canvas.blit(ammo1_img, (ammo1_rect.x, ammo1_rect.y))  # print na tela

    ammo_string = str(f'munição: {str(ammo_count)}')
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
        x_clock = random.randint(40, 600)
        y_clock = random.randint(40, 600)
        clock_rect = pygame.Rect(x_clock, y_clock, clock_img.get_width(), clock_img.get_height())  # set up hitbox
        # teste de colisão pre spawn
        clock_rect = colision_test_for_spawnables(clock_rect, clock_img, x_clock, y_clock)
        canvas.blit(clock_img, (clock_rect.x, clock_rect.y))  # prpinta relogio na tela

    cronometro = f"Zombie coming: {timer}s"
    texto_cronometro = fonte.render(cronometro, True, (255, 255, 255))
    window.blit(texto_cronometro, (20, 20))

    # -----------------------------------------------------------------------------------------------------------

    for event in pygame.event.get():
        if event.type == QUIT:  # Check for window quit
            pygame.quit()  # Stop pygame
            exit()  # Stop script
        # movement events
        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                moving_u = True
                player_img = pygame.image.load('game_theme/Assets/images/sprites/player-up.png')
            if event.key == K_a or event.key == K_LEFT:
                moving_l = True
                player_img = pygame.image.load('game_theme/Assets/images/sprites/player-left.png')
            if event.key == K_s or event.key == K_DOWN:
                moving_d = True
                player_img = pygame.image.load('game_theme/Assets/images/sprites/player-down.png')
            if event.key == K_d or event.key == K_RIGHT:
                moving_r = True
                player_img = pygame.image.load('game_theme/Assets/images/sprites/player-right.png')

        if event.type == KEYUP:
            if event.key == K_w or event.key == K_UP:
                moving_u = False
            if event.key == K_a or event.key == K_LEFT:
                moving_l = False
            if event.key == K_s or event.key == K_DOWN:
                moving_d = False
            if event.key == K_d or event.key == K_RIGHT:
                moving_r = False

    surf = pygame.transform.scale(canvas, (640, 640))
    window.blit(surf, (0, 60))
    pygame.display.update()
    clock.tick(30)  # Framerate

# criar uma função que retorna a matriz do mapa e a lista das hitboxes de cada tile
