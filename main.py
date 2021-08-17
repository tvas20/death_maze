import pygame
from pygame.locals import *
from sys import exit

clock = pygame.time.Clock()  # Set up the clock

# Window
pygame.init()
pygame.display.set_caption('Labyrinth')
width, height = 640, 700

window = pygame.display.set_mode((width, height))
canvas = pygame.Surface((640, 640))

# Player
player_img = pygame.image.load('char.jpeg')

moving_u = False
moving_d = False
moving_r = False
moving_l = False

player_rect = pygame.Rect(288, 320, player_img.get_width(), player_img.get_height())  # Set up the hitbox

# Map
ground_img, wall_img = pygame.image.load('ground.jpeg'), pygame.image.load('wall.jpeg')

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

    rect.x += move[0]
    hit_list = collision_test(rect, tiles)

    for tile in hit_list:
        if move[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif move[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

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


# Game Loop
while True:

    canvas.fill((0, 0, 0))

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
        player_movement[1] -= 10
    if moving_d:
        player_movement[1] += 10
    if moving_r:
        player_movement[0] += 10
    if moving_l:
        player_movement[0] -= 10

    player_rect, collisions_direction = movement(player_rect, player_movement, tile_rects)

    canvas.blit(player_img, (player_rect.x, player_rect.y))

    for event in pygame.event.get():
        if event.type == QUIT:  # Check for window quit
            pygame.quit()  # Stop pygame
            exit()  # Stop script
        if event.type == KEYDOWN:
            if event.key == K_w:
                moving_u = True
            if event.key == K_a:
                moving_l = True
            if event.key == K_s:
                moving_d = True
            if event.key == K_d:
                moving_r = True

        if event.type == KEYUP:
            if event.key == K_w:
                moving_u = False
            if event.key == K_a:
                moving_l = False
            if event.key == K_s:
                moving_d = False
            if event.key == K_d:
                moving_r = False

    surf = pygame.transform.scale(canvas, (640, 640))
    window.blit(surf, (0, 60))
    pygame.display.update()
    clock.tick(30)  # Framerate

# criar uma função que retorna a matriz do mapa e a lista das hitboxes de cada tile

