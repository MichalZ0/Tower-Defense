import pygame
import os
import math

class Cannon(pygame.sprite.Sprite):
    def __init__(self, position, image_path,range,damage):
        super().__init__()

        self.framesPath = os.path.join(image_path, 'moździeź')
        self.image = pygame.image.load(os.path.join(self.framesPath, 'moździeź1.png')).convert_alpha()
    
        self.rect = self.image.get_rect(center=position)
        print('rectior', self.rect)
        self.range=range
        self.damage=damage

        self.frames=[pygame.image.load(os.path.join(self.framesPath,'moździeź1.png')).convert_alpha(),
                    pygame.image.load(os.path.join(self.framesPath, 'moździeź2.png')).convert_alpha(),
                    pygame.image.load(os.path.join(self.framesPath, 'moździeź3.png')).convert_alpha(),
                    pygame.image.load(os.path.join(self.framesPath, 'możdzieź4.png')).convert_alpha()]

    def is_in_range(self, monster):
        #"""Sprawdza, czy dany potwór znajduje się w zasięgu wieży."""
        distance = math.hypot(
            self.rect.centerx - monster.rect.centerx,
            self.rect.centery - monster.rect.centery
        )
        return distance <= self.range

    def attack(self, monster):
        #"""Zadaje obrażenia potworowi."""
        self.image = self.frames[2]
        monster.take_damage(self.damage)


    def update(self, monsters):
        #"""Sprawdza zasięg i atakuje najbliższego potwora."""
        self.target = None  # Resetowanie celu

        # Szukamy najbliższego potwora w zasięgu
        for monster in monsters:
            if self.is_in_range(monster):
                self.target = monster
                break

        # Atak, jeśli znaleziono cel
        if self.target:
            self.attack(self.target)
            names=["Ghost","Smok","Troll","Skeleton"]
            if self.target.name not in names:
                print(self.target.name)

    def getRect(self):
        return self.rect

    def showRadius(self):
        self.towerRadiusSprite = pygame.Surface((self.rect.width, self.rect.height))
        pygame.draw.circle(self.towerRadiusSprite, 
                           "white", 
                           (self.rect.x, self.rect.y), 
                           self.range/2, 
                           3)

        return self.towerRadiusSprite
