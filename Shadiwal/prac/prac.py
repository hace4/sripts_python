import pygame
import random
from math import sin, cos, radians, atan
import itertools
import time
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
PADDLE_COLOR = (59, 34, 9)
STAND_COLOR = (102, 51, 0)
BULLET_COLOR = (36, 36, 36)
PVOBULLET_COLOR = (54, 9, 9)
RLS_COLOR = (30, 250, 17)

score = 0

field = pygame.Rect(0, SCREEN_HEIGHT - 50,  SCREEN_WIDTH, 50)
stand = pygame.Rect((SCREEN_WIDTH / 2 - 80),SCREEN_HEIGHT - 110, 30, 60)
stand1 = pygame.Rect((SCREEN_WIDTH / 2 + 50),SCREEN_HEIGHT - 110 , 30, 60)
stand2 = pygame.Rect((SCREEN_WIDTH / 2 - 80),SCREEN_HEIGHT - 120 , 160, 10)
rls =  pygame.Rect((SCREEN_WIDTH / 2 + 400),SCREEN_HEIGHT - 120 , 100, 70)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 120]
angle = 0
speed = -400
Health_ = 100

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
    def __init__(self, x, y, speed) -> None:
         self.x = x
         self.y = y
         self.speedx = speed *sin(atan((SCREEN_WIDTH / 2 + random.randint(400, 500) - x) / (SCREEN_HEIGHT - 170 - y)))
         self.speedy = speed * cos((atan((SCREEN_WIDTH / 2 + random.randint(400, 500) - x) / (SCREEN_HEIGHT - 170 - y))))
    def spawn(self):
        pygame.draw.circle(screen, BULLET_COLOR, (self.x, self.y), 25)
    def move(self):
        self.x += self.speedx; self.y += self.speedy
    def dispawn(self):
            self.x = -100
            self.y = -100
            self.spawn()
            self.spawn()

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
        
        def dispawn(self):
            self.x = -100
            self.y = -100
            self.spawn()
            
class RLS():

    def len_bullet( x, x_BULLET, y_BULLET, y):
        return ((x_BULLET - x)**2 + (y_BULLET- y)**2)**0.5
a = 0

massive1 = [BULLET(random.randint(200 , 1400), -100, random.randint(1, 2)) for i in range(3)]
massive2 = [None, None, None]
run = True
score = 0

while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and angle <= 75:
            angle += 1
    elif keys[pygame.K_a] and angle >= -75:
            angle -= 1
    if keys [pygame.K_SPACE]:    
        for i in range(3):
            if massive2[i] == None and a >= 10:
                massive2[i] = PVOBULLET((SCREEN_WIDTH / 2 + (sin(radians(angle)) * 120)), (SCREEN_HEIGHT - (120 + cos(radians(angle)) * 120)),speed, speed, angle + 90)
                a = 0
                
                break
    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    screen.blit(background_image, (0, 0))

    screen.blit(rotated_image, rect)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)
    pygame.draw.rect(screen, STAND_COLOR, stand1)
    pygame.draw.rect(screen, STAND_COLOR, stand2)
    pygame.draw.rect(screen, RLS_COLOR, rls)
    

    
    for bulet1, bulllet2 in itertools.product (massive1, massive2):

        if bulllet2 != None and bulet1 != None: 
            if ((abs(bulllet2.x - bulet1.x) <= 25) and(abs(abs(bulllet2.y - bulet1.y) <= 25))):
                score += 1
                bulllet2.dispawn()
                bulllet2 = None
                bulet1.dispawn()
                bulet1 = None

                
        

    for bulet1 in range(len(massive1)):
            if massive1[bulet1] != None:
                len_rls = RLS.len_bullet(massive1[bulet1].x, (SCREEN_WIDTH / 2 + 400),SCREEN_HEIGHT - 120, massive1[bulet1].y)
                count = bulet1
                print(RLS.len_bullet(massive1[bulet1].x, (SCREEN_WIDTH / 2 + 400),SCREEN_HEIGHT - 120, massive1[bulet1].y), bulet1)
            if massive1[bulet1] == None:
                massive1[bulet1] = BULLET(random.randint(200 , 1400), 100, random.randint(1 ,3))
            if massive1[bulet1] != None and (massive1[bulet1].y >= 700 or massive1[bulet1].x <= 0 or massive1[bulet1].x >= 1400):
                Health_ -= 2
                massive1[bulet1].dispawn()
                massive1[bulet1] = None
            if massive1[bulet1] != None:
                massive1[bulet1].spawn()
                massive1[bulet1].move()
                
    for bulllet2 in range(len(massive2)):
            if massive2[bulllet2] != None:

                massive2[bulllet2].spawn()
                massive2[bulllet2].update()  
            if massive2[bulllet2] != None and (massive2[bulllet2].y >= 700 or massive2[bulllet2].x <= 0 or massive2[bulllet2].x >= 1400):
                massive2[bulllet2].dispawn()
                massive2[bulllet2] = None
                
    f1 = pygame.font.Font(None, 72)
    text1 = f1.render(str(score), 0, (10, 10, 10))  
    screen.blit(text1, (0, 0))
    f2 = pygame.font.Font(None, 40)
    text2 = f1.render(str(Health_), 0, (10, 10, 10))  
    screen.blit(text2, (0, 70))
    a += 1
    text3 = f1.render(str(angle), 0, (10, 10, 10))  
    screen.blit(text3, (0, 120))
    text4 = f2.render('Расстояние до ракеты {len_rls}, {count}'.format(len_rls=round(len_rls), count = count), 0, (10, 10, 10))  
    screen.blit(text4, (0, 170))
    clock.tick(75)
    pygame.display.flip()