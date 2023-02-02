import pygame
import random


class PVO():
    def rotate(surface, angle, pivot, offset):

        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.
    def bullet(X, Y):
       pygame.draw.circle(screen, "WHITE", (Y, X), 25)
    def bullet_angry():

       pygame.draw.circle(screen, "GREEN", (200, 200), 25)

    def bullet_move(X, Y):
        while X != 200 and Y != 150:
            X -= 1
            Y -= 1
            print(X, Y)
        return X, Y

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

BG_COLOR = (250, 100, 50)
PADDLE_COLOR = (20, 20, 20)
GUN_COLOR = (250, 250, 250)
STAND_COLOR = (46, 102, 159)


field = pygame.Rect(0, 540,  1024, 100)
stand = pygame.Rect((SCREEN_WIDTH / 2-65), 500, 70, 40)
# player = pygame.Rect(SCREEN_WIDTH / 2-8, 435, 1, 1)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2)-30, 500]
angle = 0


# enemy_bullet_max_speed = 11

player_img = pygame.image.load("gun.png")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AirDefense")
X = 300
Y = 300
run = True
F = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
            angle += 5
    elif keys[pygame.K_a]:
            angle -= 5
    elif keys[pygame.K_SPACE]:
            X, Y = PVO.bullet_move(X, Y)
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_w:
        #         player_img = pygame.transform.rotate(player_img, -15)
        #     elif event.key == pygame.K_s:e
        #         player_img = pygame.transform.rotate(player_img, 15)
    rotated_image, rect = PVO.rotate(player_img, angle, pivot, offset)
    screen.fill(BG_COLOR)
    screen.blit(rotated_image, rect)
    # pygame.draw.rect(screen, (30, 250, 70), rect, 1)
    # pygame.draw.rect(screen, GUN_COLOR, player)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)

    PVO.bullet(X, Y)
    PVO.bullet_angry()
    if X ==200 and  Y == 200:
            #### del func i want fuck and i lazy
            pass
            
    clock.tick(60)
    pygame.display.flip()
    ################################ Осталось функцимю направления пули переложить на управление наклоном
    
    ################################