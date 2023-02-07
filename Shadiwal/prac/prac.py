import pygame
import random
from math import sin, cos, radians

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
PADDLE_COLOR = (59, 34, 9)
STAND_COLOR = (102, 51, 0)
BULLET_COLOR = (36, 36, 36)
PVOBULLET_COLOR = (54, 9, 9)
score = 0

field = pygame.Rect(0, SCREEN_HEIGHT - 50,  SCREEN_WIDTH, 50)
stand = pygame.Rect((SCREEN_WIDTH / 2 - 80),SCREEN_HEIGHT - 110, 30, 60)
stand1 = pygame.Rect((SCREEN_WIDTH / 2 + 50),SCREEN_HEIGHT - 110 , 30, 60)
stand2 = pygame.Rect((SCREEN_WIDTH / 2 - 80),SCREEN_HEIGHT - 120 , 160, 10)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 120]
angle = 0
speed = -400

background_image = pygame.image.load('762feaedfbad9cd8c0899d8396c3d953.jpeg')
player_img = pygame.image.load("gun3.png")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AirDefense")


def rotate(surface, angle, pivot, offset): 
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  
    rotated_offset = offset.rotate(angle) 
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect 


class BULLET():
    def __init__(self, x, y, speedx, sppedy) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
         
         
    def spawn(self):
        pygame.draw.circle(screen, BULLET_COLOR, (self.x, self.y), 25)
        
        
    def move(self):
        self.x += self.speedx; self.y += self.speedy

class PVOBULLET():
        def __init__(self, x, y, speedx, sppedy, angle) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
         self.angle = angle
         
         
        def spawn(self):
            pygame.draw.circle(screen, PVOBULLET_COLOR, (self.x, self.y), 10)
            
            
        def update(self):
            self.speedy += 3
            self.x += ((self.speedx) * cos(radians(self.angle))) / 60; self.y += ((self.speedy) * sin(radians(self.angle)) + 30) / 60


bulet1 = BULLET(700, 0, -3, 3)
run = True
BULLET.x = random.randint(100, 1500); BULLET.y = 0
bullet2 = PVOBULLET(-1000, -2000, 0, 0, 0)

while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and angle <= 75:
            angle += 5
    elif keys[pygame.K_a] and angle >= -75:
            angle -= 5
    if keys[pygame.K_SPACE]:
        bullet2.x = (SCREEN_WIDTH / 2 + (sin(radians(angle)) * 120))
        bullet2.y = (SCREEN_HEIGHT - (120 + cos(radians(angle)) * 120))
        bullet2.speedx = speed
        bullet2.speedy=speed
        bullet2.angle =  angle + 90     
    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    screen.blit(background_image, (0, 0))
    bulet1.move()
    bulet1.spawn()
    bullet2.spawn()
    bullet2.update()
    screen.blit(rotated_image, rect)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)
    pygame.draw.rect(screen, STAND_COLOR, stand1)
    pygame.draw.rect(screen, STAND_COLOR, stand2)

    
    if ((abs(bullet2.x - bulet1.x) <= 25) and(abs(abs(bullet2.y - bulet1.y) <= 25)) ):
        bullet2 = PVOBULLET((0 / 2 + (sin(radians(angle)) * 120)), (0 - (120 + cos(radians(angle)) * 120)),speed, speed, angle + 90)
        bulet1.x = random.randint(100, 1400)
        bulet1.y = 0
        bulet1.speedx = random.randint(-3, 3) + 1
        bulet1.speedy = random.randint(3, 3) + 1
        score += 1
        
        
    f1 = pygame.font.Font(None, 72)
    text1 = f1.render(str(score), 0, (10, 10, 10))  
    screen.blit(text1, (0, 0))
    if bulet1.y >= 800 or bulet1.x <= 0 or bulet1.x >= 1400 :
            bulet1.x = random.randint(100, 1300);bulet1.y = 0;bulet1.speedx = random.randint(-3, 3)+1; bulet1.speedy = random.randint(0, 3)+1
            continue

    clock.tick(75)
    pygame.display.flip()
