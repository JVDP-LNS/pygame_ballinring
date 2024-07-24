import math
import os
import pygame
from sys import exit

pygame.init()

# ---

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.main_image = pygame.image.load(os.path.dirname(__file__) + "\\ball.png").convert_alpha()
        self.main_image = pygame.transform.scale(self.main_image,[100,100.])
        self.image = pygame.transform.rotozoom(self.main_image,0,1)
        self.rect = self.image.get_rect(center = [1280/2,720/2])
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.x = 1280/2
        self.y = 720/2

        self.xspeed = 5
        self.yspeed = 0


    def bounds(self):
        pass

    def correct_angle(self):
        self.angle = math.degrees(math.atan2(self.yspeed,self.xspeed))

    def correct_rotation(self):
        self.image = pygame.transform.rotozoom(self.main_image, self.angle, 1)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def check_collision(self):
        if pygame.sprite.collide_mask(ball,ring):
            offset = [self.rect.centerx - ring.rect.centerx, self.rect.centery - ring.rect.centery]
            offset = [offset[0]/360, offset[1]/360]
            offset = [offset[0]*self.xspeed, offset[1]*self.yspeed]

            #self.xspeed -= 3*offset[0]
            #self.yspeed -= 3*offset[1]
            self.xspeed = -1.1*self.xspeed
            self.yspeed = -1.1*self.yspeed

    def change_scale(self,scale):
        self.image = pygame.transform.rotozoom(self.image,0,scale)
        self.image.set_palette()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect =self.image.get_rect(center = self.rect.center)
        print(scale)

    def gravity(self):
        self.yspeed += 0.1

    def update(self):
        self.gravity()
        self.move()
        self.check_collision()
        #self.correct_angle()
        #self.correct_rotation()


class Ring(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.main_image = pygame.image.load(os.path.dirname(__file__) + "\\ring.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.main_image,0,1)
        self.rect = self.image.get_rect(center = [1280/2,720/2])
        self.mask = pygame.mask.from_surface(self.image)

    def isCollision(self):
        return pygame.sprite.spritecollide()
        pass

    def change_scale(self, scale):
        #self.image = pygame.transform.scale(self.main_image
       pass

    def update(self):
        pass


main_screen_dim = [1280,720]
main_screen = pygame.display.set_mode(main_screen_dim)
background = pygame.image.load(os.path.dirname(__file__) + "\\yeah.jpg").convert()

ring = Ring()
ring_group = pygame.sprite.Group()
ring_group.add(ring)
ball = Ball()
ball_group = pygame.sprite.Group()
ball_group.add(ball)

clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #main_screen.blit(background,[0,0])
    ring_group.update()
    ring_group.draw(main_screen)

    ball_group.update()
    ball_group.draw(main_screen)

    pygame.display.update()
    clock.tick(fps)

    print(math.degrees(math.atan2(3,2)))

