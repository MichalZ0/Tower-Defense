import pygame
import math
class Cannon(pygame.sprite.Sprite):
    def __init__(self, position, image_path,range,damage):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.range=range
        self.damage=damage
        self.frames=[pygame.image.load(r"C:\Users\ignac\OneDrive\Pulpit\folder gry\PLiki do gry tower defense\wierze\moździeź\moździeź2.png").convert_alpha(),pygame.image.load(r"C:\Users\ignac\OneDrive\Pulpit\folder gry\PLiki do gry tower defense\wierze\moździeź\moździeź3.png").convert_alpha(),pygame.image.load(r"C:\Users\ignac\OneDrive\Pulpit\folder gry\PLiki do gry tower defense\wierze\moździeź\możdzieź4.png").convert_alpha()]

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
