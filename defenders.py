import pygame
import os
import math
import time

class Cannon(pygame.sprite.Sprite):
    def __init__(self, position, image_path, range, damage,animation_speed):
        super().__init__()
        self.framesPath = os.path.join(image_path, 'katapulta')
        self.frames = [pygame.image.load(os.path.join(self.framesPath, 'katapulta 0.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'katapulta 1.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'katapulta 2.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'katapulta 3.png')).convert_alpha(),
                       pygame.image.load(os.path.join(self.framesPath, 'katapulta4.png')).convert_alpha()
                       ]

        self.current_frame = 0
        self.animation_speed = animation_speed
        self.animation_counter = 0

        self.image = self.frames[self.current_frame]

        self.imageCopy = self.image

        self.rect = self.image.get_rect(center=position)
        self.range = range
        self.damage = damage



        self.shouldShowRadius = False
        self.last_attack_time = 0  # Czas ostatniego ataku (w milisekundach)
        self.attack_interval = 2000
        self.animate_interwal = 200
        self.last_animate_time=0

    def is_in_range(self, monster):
        # """Sprawdza, czy dany potwór znajduje się w zasięgu wieży."""
        distance = math.hypot(
            self.rect.centerx - monster.rect.centerx,
            self.rect.centery - monster.rect.centery
        )
        return distance <= self.range

    def attack(self, monster):
        self.image = self.frames[2]
        if self.shouldShowRadius:
            self.showRadius()

        monster.take_damage(self.damage)
        self.last_attack_time = pygame.time.get_ticks()

    def update(self, monsters):
        self.target = None
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time < self.attack_interval:
            self.animate()

            return

        # Resetowanie celu


        # Znajdowanie najbliższego potwora w zasięgu
        for monster in monsters:
            if self.is_in_range(monster):

                self.target = monster
                break

        # Atak, jeśli znaleziono cel
        if self.target:

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
        self.towerRadiusSprite = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.circle(self.towerRadiusSprite,
                           "white",
                           (self.rect.width / 2, self.rect.height / 2),
                           self.range,
                           3)

        self.towerRadiusSprite.blit(self.image, (0, 0))

        self.image = self.towerRadiusSprite
        self.shouldShowRadius = True

    def getMask(self):
        return pygame.mask.from_surface(self.imageCopy)

    def hideRadius(self):
        self.image = self.imageCopy
        self.shouldShowRadius = False

    def getFirstFrame(self):
        return self.frames[0]

    def animate(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_animate_time < self.animate_interwal:
            return


        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.image = self.frames[self.current_frame]
        self.last_animate_time = current_time
