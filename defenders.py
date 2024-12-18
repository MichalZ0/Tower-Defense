import pygame
import os
import math
import time


from Attack import *
from Components.BottomPanel import *

class Cannon(pygame.sprite.Sprite):
    def __init__(self, position, image_path, range, damage,animation_speed, name='', updateSidePanel=None, cost=100):
        super().__init__()
        self.name = name
        self.damage = damage
        self.position = position
        self.cost = cost
        self.range = range

        self.framesPath = os.path.join(image_path, 'Cannon')
        self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Cannon0.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'Cannon1.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'Cannon2.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'Cannon3.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'Cannon4.png')).convert_alpha()
                       ]


        self.framesOffset = [[0,0], 
                             [0,-(self.frames[1].get_rect().height - self.frames[0].get_rect().height)],
                             [0,-(self.frames[2].get_rect().height - self.frames[0].get_rect().height)],
                             [0,-(self.frames[3].get_rect().height - self.frames[0].get_rect().height)],
                             [0,-(self.frames[4].get_rect().height - self.frames[0].get_rect().height)]]



        self.towerInRadiusBlitPos =  [self.range - (self.frames[0].get_width()/2), 
                                      self.range - (self.frames[0].get_height()/2)] 



        self.current_frame = 0
        self.animation_speed = animation_speed
        self.animation_counter = 0

        self.image = self.frames[self.current_frame]

        self.imageCopy = self.image.copy()

        self.rect = self.image.get_rect(center=position)
        self.animationRect = self.rect.copy()

        self.anim_x = self.rect.x
        self.anim_y = self.rect.y


        self.selectedTowerRect = self.rect.copy()
        self.damage = damage





        self.shouldShowRadius = False
        self.last_attack_time = 0  # Czas ostatniego ataku (w milisekundach)
        self.attack_interval = 2000
        self.animate_interwal = 1000
        self.last_animate_time=0

        self.updateBottomPanel = updateSidePanel

        self.bullets = []
         
        self.radiusColor = 'white' 

    def is_in_range(self, monster):
        # """Sprawdza, czy dany potwór znajduje się w zasięgu wieży."""
        distance = math.hypot(
            self.rect.centerx - monster.rect.centerx,
            self.rect.centery - monster.rect.centery
        )
        return distance <= self.range

    def attack(self, monster):
        monster.take_damage(self.damage)
        self.last_attack_time = pygame.time.get_ticks()

    def update(self, monsters):
        self.target = None
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time < self.attack_interval:
            self.animate()
            return

        # Znajdowanie najbliższego potwora w zasięgu
        for monster in monsters:
            if self.is_in_range(monster):

                self.target = monster
                break

        # Atak, jeśli znaleziono cel
        if self.target:
            self.bullets.append(Attack(self.target.rect, self.rect, 30))
            self.attack(self.target)  # Wywołuje atak, ustawia czas ostatniego ataku
            print(self.target.name)





    def getRect(self):
        return self.rect

    def setSprite(self, newSprite=None):
        if (newSprite == None):
            self.image = self.imageCopy
            return
        self.image = newSprite

    def showRadius(self):
        self.towerRadiusSprite = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
        pygame.draw.circle(self.towerRadiusSprite,
                            self.radiusColor,
                           (self.range, self.range),
                           self.range,
                           3)

        self.towerRadiusSprite.blit(self.frames[self.current_frame], (self.towerInRadiusBlitPos[0] + self.framesOffset[self.current_frame][0], 
                                                self.towerInRadiusBlitPos[1] + self.framesOffset[self.current_frame][1]))
        
        self.image = self.towerRadiusSprite

        self.rect = self.image.get_rect(center=self.position)
        
        self.shouldShowRadius = True

    def getMask(self):
        return pygame.mask.from_surface(self.image)

    def hideRadius(self):
        self.image = self.frames[self.current_frame]
        self.rect.x = self.anim_x + self.framesOffset[self.current_frame][0]
        self.rect.y = self.anim_y + self.framesOffset[self.current_frame][1]
                                                

        self.shouldShowRadius = False

    def setPosition(self, newPosition):
        self.position = newPosition
        self.rect = self.image.get_rect(center=newPosition)
        self.animationRect = self.image.get_rect(center=newPosition).copy()

        self.anim_x = self.rect.x
        self.anim_y = self.rect.y
        
    def animate(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_animate_time < self.animate_interwal:
            return


        self.current_frame = (self.current_frame + 1) % len(self.frames)

        self.image = self.frames[self.current_frame]

        self.rect.x = self.anim_x + self.framesOffset[self.current_frame][0]
        self.rect.y = self.anim_y + self.framesOffset[self.current_frame][1]

        self.last_animate_time = current_time
            
        if (self.shouldShowRadius == True):
            self.showRadius()
        
    def getBullets(self):
        return self.bullets
