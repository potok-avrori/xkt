import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH = 1500
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сталкер")

player_img = pygame.image.load('pers (Малый) (Пользовательское).png')
obstacle_img = pygame.image.load('ZLo (Малый) (Пользовательское).png')
background_img = pygame.image.load('Fon.png')
game_over_img = pygame.image.load('конец.png')

player_width, player_height = 82, 120
obstacle_width, obstacle_height = 120, 72

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 50

obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height

obstacle_speed = 5
acceleration = 1
player_speed = 10
score = 0
font = pygame.font.SysFont(None, 30)


def display_score():
    score_text = font.render("Очки: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))


def display_game_over():
    screen.blit(game_over_img,
                (WIDTH // 2 - game_over_img.get_width() // 2, HEIGHT // 2 - game_over_img.get_height() // 2))


running = True
clock = pygame.time.Clock()
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        obstacle_y += obstacle_speed

        if obstacle_y > HEIGHT:
            obstacle_y = -obstacle_height
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            score += 1
            obstacle_speed += acceleration

            if score % 5 == 0:
                player_speed += 10

        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            game_over = True

    screen.blit(background_img, (0, 0))

    if not game_over:
        screen.blit(player_img, (player_x, player_y))
        screen.blit(obstacle_img, (obstacle_x, obstacle_y))
        display_score()
    else:
        display_game_over()

    pygame.display.update()
    clock.tick(60)
