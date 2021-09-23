import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1109, 605))
pygame.display.set_caption('MyGame')
icon = pygame.image.load('icon.png')
bg = pygame.image.load("bg.jpg")
player = pygame.image.load('bipedal-unit1.png')
spikes_image = pygame.image.load('spikes.png')
spikes_image = pygame.transform.scale(spikes_image,(96,96))
enemy_image = pygame.image.load('enemy.png')
enemy_image = pygame.transform.scale(enemy_image,(200,200))

pygame.display.set_icon(icon)
running = True


vel_x = 10
vel_y = 10
x = 50
y = 350
jump = False
bg_x = 9
spike_x = 9
enemy_x = 9
###CLASS###
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #adding all the images to sprite array
        anim1 = pygame.image.load('bipedal-unit1.png').convert()
        anim1 = pygame.transform.scale(anim1, (300,200))
        anim2 = pygame.image.load('bipedal-unit2.png').convert()
        anim2 = pygame.transform.scale(anim2, (300,200))
        anim3 = pygame.image.load('bipedal-unit3.png').convert()
        anim3 = pygame.transform.scale(anim3, (300,200))
        anim5 = pygame.image.load('bipedal-unit4.png').convert()
        anim5 = pygame.transform.scale(anim5, (300,200))
        anim4 = pygame.image.load('bipedal-unit5.png').convert()
        anim4 = pygame.transform.scale(anim4, (300,200))
        anim6 = pygame.image.load('bipedal-unit6.png').convert()
        anim6 = pygame.transform.scale(anim6, (300,200))
        anim7 = pygame.image.load('bipedal-unit7.png').convert()
        anim7 = pygame.transform.scale(anim7, (300,200))
        self.images = []
        self.images.append(anim1)
        self.images.append(anim2)
        self.images.append(anim3)
        self.images.append(anim5)
        self.images.append(anim4)
        self.images.append(anim6)
        self.images.append(anim7)

        #index value to get the image from the array
        #initially it is 0
        self.index = 0

        #now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(x, y, 300, 200)
    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0

        #finally we will update the image that will be displayed
        self.image = self.images[self.index]
######
class claspike(pygame.sprite.Sprite):
    def __init__(self):
        super(claspike, self).__init__()
        #adding all the images to sprite array
        spike_anim1 = pygame.image.load('spikes1.png').convert()
        spike_anim1 = pygame.transform.scale(spike_anim1, (96,96))
        spike_anim2 = pygame.image.load('spikes2.png').convert()
        spike_anim2 = pygame.transform.scale(spike_anim2, (96,96))
        spike_anim3 = pygame.image.load('spikes3.png').convert()
        spike_anim3 = pygame.transform.scale(spike_anim3, (96,96))
        spike_anim4 = pygame.image.load('spikes4.png').convert()
        spike_anim4 = pygame.transform.scale(spike_anim4, (96,96))
        self.images = []
        self.images.append(spike_anim1)
        self.images.append(spike_anim2)
        self.images.append(spike_anim3)
        self.images.append(spike_anim4)

        #index value to get the image from the array
        #initially it is 0
        self.index = 0

        #now the image that we will display will be the index from the image array
        self.image = self.images[self.index]
        
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(300, 490, 300, 200)
    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0

        #finally we will update the image that will be displayed
        self.image = self.images[self.index]
###FUNCS###

my_sprite = MySprite()
my_group = pygame.sprite.Group(my_sprite)
my_spike = claspike()
my_group2 = pygame.sprite.Group(my_spike)

while running:

    rel_bg_x = bg_x % bg.get_rect().width
    screen.blit(bg, (rel_bg_x - bg.get_rect().width, 0))
    if rel_bg_x < 1980:
        screen.blit(bg,(rel_bg_x,0))
    bg_x -= 8
    rel_spike_x = spike_x % 3000

    screen.blit(spikes_image, (rel_spike_x - spikes_image.get_rect().width, 490))
    if rel_spike_x < 10000:

        screen.blit(spikes_image,(rel_spike_x+10000000000,490))
    spike_x -= 15
    rel_enemy_x = enemy_x % 3500

    screen.blit(enemy_image, (rel_enemy_x - enemy_image.get_rect().width, 430))
    if rel_enemy_x < 10000:

        screen.blit(enemy_image,(rel_enemy_x+10000000000,430))
    enemy_x -= 10
    keys = pygame.key.get_pressed()
    my_group.update()
    my_group.draw(screen)
    my_group2.update()
    my_group2.draw(screen)


    pygame.display.update()

    if not jump and keys[pygame.K_SPACE]:
        jump = True

    if not jump and keys[pygame.K_UP]:
        jump = True
    if jump:
        my_sprite.__init__()
        y -= vel_y*4.2
        vel_y -= 1
        if vel_y < -10:
            jump = False
            my_sprite.__init__()
            vel_y = 10

    pygame.time.delay(30)
    pygame.display.update()
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
