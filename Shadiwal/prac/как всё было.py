import pygame
import random
import time
import math
def rotate(surface, angle, pivot, offset):

    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

class BULLET():
    def __init__(self, x, y, speedx, sppedy) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
    def spawn(self):
        pygame.draw.circle(screen, "WHITE", (self.x, self.y), 25)
    def move(self):
        self.x += self.speedx; self.y += self.speedy

class PVOBULLET():
        def __init__(self, x, y, speedx, sppedy) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
        def spawn(self):
            pygame.draw.circle(screen, "WHITE", (self.x, self.y), 25)
        def move(self):
            self.x += self.speedx; self.y += self.speedy
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BG_COLOR = (250, 100, 50)
PADDLE_COLOR = (20, 20, 20)
GUN_COLOR = (250, 250, 250)
STAND_COLOR = (46, 102, 159)

field = pygame.Rect(0, SCREEN_HEIGHT - 100,  SCREEN_WIDTH, 100)
stand = pygame.Rect((SCREEN_WIDTH / 2-65),SCREEN_HEIGHT - 140 , 70, 40)
# player = pygame.Rect(SCREEN_WIDTH / 2-8, 435, 1, 1)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2)-30, SCREEN_HEIGHT - 100]
angle = 0


# enemy_bullet_max_speed = 11

player_img = pygame.image.load("gun1.png")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AirDefense")
bulet1 = BULLET(700, 300, -3, 3)
run = True
BULLET.x = random.randint(100, 1500); BULLET.y = random.randint(50, 500)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
            angle += 5
    elif keys[pygame.K_a]:
            angle -= 5
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_w:
        #         player_img = pygame.transform.rotate(player_img, -15)
        #     elif event.key == pygame.K_s:e
        #         player_img = pygame.transform.rotate(player_img, 15)

    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    screen.fill(BG_COLOR)
    bulet1.move()
    bulet1.spawn()
    
    screen.blit(rotated_image, rect)
    # pygame.draw.rect(screen, (30, 250, 70), rect, 1)
    # pygame.draw.rect(screen, GUN_COLOR, player)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)
  
    if bulet1.y >= 800:
        bulet1.x = random.randint(100, 1500)
        bulet1.y = random.randint(50, 500)
        bulet1.speedx = random.randint(-3, 3)
        bulet1.speedy = random.randint(0, 3)
        continue
    print(bulet1.x, bulet1.y)
    clock.tick(60)
    pygame.display.flip()