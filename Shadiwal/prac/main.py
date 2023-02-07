import pygame
import random


class Game():
    def __innit__(self):
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 576

        self.BG_COLOR = (250, 100, 50)
        self.PADDLE_COLOR = (20, 20, 20)
        self.GUN_COLOR = (250, 250, 250)
        self.STAND_COLOR = (46, 102, 159)

        self.field = pygame.Rect(0, 540,  1024, 100)
        self.stand = pygame.Rect((self.SCREEN_WIDTH / 2-65), 500, 70, 40)
        self.player_img = pygame.image.load("gun.png")
        self.pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pygame.display.set_caption("AirDefense")
            # player = pygame.Rect(SCREEN_WIDTH / 2-8, 435, 1, 1)

        self.offset = pygame.math.Vector2(0, -25)
        self.pivot = [(self.SCREEN_WIDTH / 2)-30, 500]
        self.angle = 0
        pygame.display.flip()
    def rotate(self, surface, angle, pivot, offset):

        self.rotated_image = pygame.transform.rotozoom( self.surface, - self.angle, 1)  # Rotate the image.
        self.rotated_offset =  self.offset.rotate( self.angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect =  self.rotated_image.get_rect(center=pivot+ self.rotated_offset)
        return  self.rotated_image, rect  # Return the rotated image and shifted rect.



    # enemy_bullet_max_speed = 11
    def main(self):
        run = True
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

            rotated_image, rect = self.rotate(self.player_img, angle, self.pivot, self.offset)
            self.screen.fill(self.BG_COLOR)
            self.screen.blit(rotated_image, rect)
            # pygame.draw.rect(screen, (30, 250, 70), rect, 1)
            # pygame.draw.rect(screen, GUN_COLOR, player)
            pygame.draw.rect(self.screen, self.PADDLE_COLOR, self.field)
            pygame.draw.rect(self.screen, self.STAND_COLOR, self.stand)


            self.clock.tick(60)
if __name__ == "__main__":
        Game.main()