import pygame
import os
import math
import time


from Attack import *
from Components.BottomPanel import *

class Cannon(pygame.sprite.Sprite):
    def __init__(self, position, image_path, range, damage,animation_speed, name='', updateSidePanel=None):
        super().__init__()
        self.name = "Cannon"
        self.damage = 100
        self.image_path=image_path
        self.position=position
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






        self.current_frame = 0
        self.animation_speed = animation_speed
        self.animation_counter = 0

        self.towerInRadiusBlitPos =  [self.range - (self.frames[0].get_width()/2), 
                                      self.range - (self.frames[0].get_height()/2)] 


        self.image = self.frames[self.current_frame]

        self.imageCopy = self.image.copy()

        self.rect = self.image.get_rect(center=self.position)
        self.rectWithoutRadius = self.image.get_rect(center=self.position)
        self.animationRect = self.rect.copy()

        self.anim_x = self.rect.x
        self.anim_y = self.rect.y



        self.typ_obrażeń="Podstawowy"


        self.damage = damage
        self.income=0
        self.generated_income = False

        self.shouldShowRadius = False
        self.last_attack_time = 0  # Czas ostatniego ataku (w milisekundach)
        self.attack_interval = 2000
        self.animate_interwal = 200
        self.last_animate_time=0

        self.updateBottomPanel = updateSidePanel

        self.radiusColor = 'white'
        self.bullets = []
        self.level=0

    def is_in_range(self, monster):
        # """Sprawdza, czy dany potwór znajduje się w zasięgu wieży."""
        distance = math.hypot(
            self.rect.centerx - monster.rect.centerx,
            self.rect.centery - monster.rect.centery
        )
        return distance <= self.range

    def attack(self, monster,money):
        monster.take_damage(self.damage,self.typ_obrażeń)
        self.last_attack_time = pygame.time.get_ticks()

    def update(self, monsters,money):

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

            self.bullets.append(Attack(self.target.rect, self.rect, 30))
            self.attack(self.target,money)  # Wywołuje atak, ustawia czas ostatniego ataku
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
        # print(self.position)
        self.rect = self.image.get_rect(center=self.position)
        
        self.shouldShowRadius = True





    def getMask(self):
        return pygame.mask.from_surface(self.image)

    def hideRadius(self):
        self.image = self.frames[self.current_frame]
        self.rect.x = self.anim_x + self.framesOffset[self.current_frame][0]
        self.rect.y = self.anim_y + self.framesOffset[self.current_frame][1]
                                                
        self.shouldShowRadius = False

    def getFirstFrame(self):
        return self.frames[0]

    def setPosition(self, newPosition):
        self.position = newPosition
        self.rect = self.image.get_rect(center=newPosition)
        self.rectWithoutRadius = self.rect.copy()
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

    def upgrade(self):
        if self.level == 1:
            self.damage += 100
            self.range += 100
            self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Cannon0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon3.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon4.png')).convert_alpha()
                       ]

            print("upgrade2")
            self.level = 2

            self.towerInRadiusBlitPos =  [self.range - (self.frames[0].get_width()/2), 
                                          self.range - (self.frames[0].get_height()/2)] 


        if self.level == 0:
            self.damage+=100
            self.range+=100
            self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Cannon0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon3.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Cannon4.png')).convert_alpha()
                           ]

            print("upgrade")
            self.towerInRadiusBlitPos =  [self.range - (self.frames[0].get_width()/2), 
                                          self.range - (self.frames[0].get_height()/2)] 
            self.level=1
            print(
            self.current_frame,
            self.animation_speed,
            self.animation_counter
            )



class MageTower(Cannon):
    def __init__(self, position, image_path, range, damage, animation_speed,updateSidePanel=None):
            # Dziedziczenie konstruktora z klasy Cannon
        super().__init__(position, image_path, range, damage, animation_speed,updateSidePanel=None)

            # Zmiana ścieżki do animacji (na animację wieży maga)
        #self.rect.center = (16, 16)
        self.name="MageTower"
        self.level=0
        self.level2=0
        self.framesPath = os.path.join(image_path, 'MageTower')  # Folder z grafikami wieży maga
        self.frames = [pygame.image.load(os.path.join(self.framesPath, 'MageTower0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'MageTower1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'MageTower2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'MageTower3.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'MageTower4.png')).convert_alpha()
                           ]

            # Ustawienie szybszej animacji i krótszego czasu pomiędzy atakami
        self.animate_interwal = 100  # Czas pomiędzy klatkami animacji (w ms)
        self.attack_interval = 1000  # Czas pomiędzy atakami (w ms)
        self.typ_obrażeń="Magiczny"
            # Resetuj animację na pierwszą klatkę
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.imageCopy = self.image

    def upgrade2(self):
        self.level2=1

    def upgrade(self):
        if self.level2==0:
            if self.level == 1:
                self.damage += 100
                self.range += 20
                self.framesPath = os.path.join(self.image_path, 'MageTower3.0')
                self.frames = [pygame.image.load(os.path.join(self.framesPath, 'MageTower0.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower1.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower2.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower3.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower4.png')).convert_alpha()

                               ]

                print("upgrade2")
                self.level = 1



            if self.level == 0:
                self.damage += 100
                self.range += 20
                self.framesPath = os.path.join(self.image_path, 'MageTower2.0')
                self.frames = [pygame.image.load(os.path.join(self.framesPath, 'MageTower0.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower1.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower2.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower3.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower4.png')).convert_alpha()

                               ]

                print("upgrade")
                self.level = 1

        if self.level2==1:
            if self.level == 2:
                self.damage += 175
                self.range += 200
                self.framesPath = os.path.join(self.image_path, 'MageTower3.1')
                self.frames = [pygame.image.load(os.path.join(self.framesPath, 'MageTower0.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower1.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower2.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower3.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower4.png')).convert_alpha()

                               ]

                print("upgrade3.1")
                self.level = 3



            if self.level == 1:
                self.damage += 150
                self.range += 20
                self.framesPath = os.path.join(self.image_path, 'MageTower2.1')
                self.frames = [pygame.image.load(os.path.join(self.framesPath, 'MageTower0.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower1.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower2.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower3.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower4.png')).convert_alpha()

                               ]

                print("upgrade2.1")
                self.level = 2

            if self.level == 0:
                self.damage += 100
                self.range += 200
                self.framesPath = os.path.join(self.image_path, 'MageTower1.1')
                self.frames = [pygame.image.load(os.path.join(self.framesPath, 'MageTower0.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower1.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower2.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower3.png')).convert_alpha(),
                               pygame.image.load(os.path.join(self.framesPath, 'MageTower4.png')).convert_alpha()

                               ]

                print("upgrade1.1")
                self.level = 1





class Archer(Cannon):
    def __init__(self, position, image_path, range, damage, animation_speed,updateSidePanel=None):
        # Dziedziczenie konstruktora z klasy Cannon
        super().__init__(position, image_path, range, damage, animation_speed,updateSidePanel=None)

        # Zmiana ścieżki do animacji (na animację wieży strzelca)
        self.name="Archer"
        self.framesPath = os.path.join(image_path, 'Archer')  # Folder z grafikami wieży strzelca
        self.frames = [
            pygame.image.load(os.path.join(self.framesPath, 'Archer0.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Archer1.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Archer2.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Archer3.png')).convert_alpha()

        ]

        # Ustawienie szybszej animacji i krótszego czasu pomiędzy atakami
        self.animate_interwal = 100  # Czas pomiędzy klatkami animacji (w ms)
        self.attack_interval = 800  # Czas pomiędzy atakami (w ms) - dla strzelca będzie krótszy
        self.typ_obrażeń="Podstawowy"
        # Resetowanie animacji na pierwszą klatkę
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=position)
        #print(self.rect)
        #self.imageCopy = self.image

    def upgrade(self):
        if self.level == 1:
            self.damage += 100
            self.range += 100
            self.framesPath = os.path.join(self.image_path, 'Archer2')
            self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Archer0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Archer1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Archer2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Archer3.png')).convert_alpha()


                           ]

            print("upgrade2")
            self.level = 2





        if self.level == 0:
            self.damage+=100
            self.range+=100
            self.framesPath = os.path.join(self.image_path, 'Archer3')
            self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Archer0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Archer1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Archer2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Archer3.png')).convert_alpha()

                           ]

            print("upgrade")
            self.level=1

class Temple(Cannon):
    def __init__(self, position, image_path, range, damage, animation_speed,updateSidePanel=None):
        # Dziedziczenie konstruktora z klasy Cannon
        super().__init__(position, image_path, range, damage, animation_speed,updateSidePanel=None)

        # Zmiana ścieżki do animacji (na animację wieży Temple)
        self.name="Temple"
        self.framesPath = os.path.join(image_path, 'Temple')  # Folder z grafikami wieży Temple
        self.frames = [
            pygame.image.load(os.path.join(self.framesPath, 'Temple0.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Temple1.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Temple2.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Temple3.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Temple4.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Temple5.png')).convert_alpha()
        ]

        # Ustawienie szybszej animacji i dłuższego czasu pomiędzy atakami
        self.animate_interwal = 150  # Czas pomiędzy klatkami animacji (w ms)
        self.attack_interval = 1200  # Czas pomiędzy atakami (w ms) - dla Temple jest nieco dłuższy
        self.typ_obrażeń="ognisty"
        # Resetowanie animacji na pierwszą klatkę
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.imageCopy = self.image

    def upgrade(self):
        if self.level == 1:
            self.damage += 100
            self.range += 100
            self.framesPath = os.path.join(self.image_path, 'Temple3')
            self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Temple0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Temple1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Temple2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Temple3.png')).convert_alpha()


                           ]

            print("upgrade2")
            self.level = 2





        if self.level == 0:
            self.damage+=100
            self.range+=100
            self.framesPath = os.path.join(self.image_path, 'Temple2')
            self.frames = [pygame.image.load(os.path.join(self.framesPath, 'Temple0.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Temple1.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Temple2.png')).convert_alpha(),
                           pygame.image.load(os.path.join(self.framesPath, 'Temple3.png')).convert_alpha()

                           ]

            print("upgrade")
            self.level=1


class WithHut(Cannon):
    def __init__(self, position, image_path, range, damage, animation_speed,updateSidePanel=None):
        # Dziedziczenie konstruktora z klasy Cannon
        super().__init__(position, image_path, range, damage, animation_speed,updateSidePanel=None)
        self.name='Witchhouse'
        self.framesPath = os.path.join(image_path, 'Witchhouse')  # Folder z grafikami wieży Temple
        self.frames = [
            pygame.image.load(os.path.join(self.framesPath, 'Witchhouse0.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Witchhouse1.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Witchhouse2.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Witchhouse3.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Witchhouse4.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Witchhouse5.png')).convert_alpha()
        ]

        # Ustawienie szybszej animacji i dłuższego czasu pomiędzy atakami
        self.animate_interwal = 150  # Czas pomiędzy klatkami animacji (w ms)
        self.attack_interval = 1200  # Czas pomiędzy atakami (w ms) - dla Temple jest nieco dłuższy
        self.typ_obrażeń="brak"
        self.slow_down=35
        # Resetowanie animacji na pierwszą klatkę
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.imageCopy = self.image


    def upgrade(self):
        if self.level == 1:
            self.slow_down += 10
            self.range += 100
            self.framesPath = os.path.join(self.image_path, 'Witchhouse3')
            self.frames = [
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse0.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse1.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse2.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse3.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse4.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse5.png')).convert_alpha()
            ]

            print("upgrade2")
            self.level = 2





        if self.level == 0:
            self.slow_down+=15
            self.range+=100
            self.framesPath = os.path.join(self.image_path, 'Witchhouse2')
            self.frames = [
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse0.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse1.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse2.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse3.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse4.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Witchhouse5.png')).convert_alpha()
            ]

            print("upgrade")
            self.level=1

    def update(self, monsters, money):
        self.target = []
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time < self.attack_interval:
            self.animate()

            return

        # Resetowanie celu

        # Znajdowanie najbliższego potwora w zasięgu
        for monster in monsters:
            if self.is_in_range(monster):
                self.target.append(monster)

        # Atak, jeśli znaleziono cel
        if self.target:
            for monster in self.target:
                #self.bullets.append(Attack(monster.rect, self.rect, 30))  # Przykład ataku
                self.attack(monster,money)  # Wywołanie ataku na każdym z potworów
                print(monster.name)





    def attack(self, monster,money):
        self.image = self.frames[2]
        if self.shouldShowRadius:
            self.showRadius()

        monster.slow_down(self.slow_down, 2000)
        self.last_attack_time = pygame.time.get_ticks()

class Factory(Cannon):
    def __init__(self, position, image_path, range, damage, animation_speed, updateSidePanel=None,name='fabryka'):
            # Dziedziczenie konstruktora z klasy Cannon
        super().__init__(position, image_path, range, damage, animation_speed, updateSidePanel=None)
        self.name="Factory"
        self.framesPath = os.path.join(image_path, 'Factory')  # Folder z grafikami wieży Temple
        self.frames = [
            pygame.image.load(os.path.join(self.framesPath, 'Factory0.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Factory0.png')).convert_alpha(),
            pygame.image.load(os.path.join(self.framesPath, 'Factory0.png')).convert_alpha()

            ]

            # Ustawienie szybszej animacji i dłuższego czasu pomiędzy atakami
        self.animate_interwal = 150  # Czas pomiędzy klatkami animacji (w ms)
        self.attack_interval = 1200  # Czas pomiędzy atakami (w ms) - dla Temple jest nieco dłuższy
        self.typ_obrażeń="brak"
            # Resetowanie animacji na pierwszą klatkę
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.imageCopy = self.image
        self.target=None
        self.generated_income=False
        self.income=50
        self.range = 1000


    def attack(self, monster,money):
        self.image = self.frames[2]
        if self.shouldShowRadius:
            self.showRadius()

        self.generated_income=True
        self.last_attack_time = pygame.time.get_ticks()

    def update(self, monsters,money):
        self.generated_income=False
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time < self.attack_interval:
            self.animate()

            return

        # Resetowanie celu


        # Znajdowanie najbliższego potwora w zasięgu


        # Atak, jeśli znaleziono cel
        for monster in monsters:
            if self.is_in_range(monster):
                self.attack(monster,money)



            #self.bullets.append(Attack(self.target.rect, self.rect, 30))
             # Wywołuje atak, ustawia czas ostatniego ataku
            #print(self.target.name)

    def upgrade(self):
        if self.level == 1:
            self.income += 30
            self.range += 100
            self.framesPath = os.path.join(self.image_path, 'Factory')  # Folder z grafikami wieży Temple
            self.frames = [
                pygame.image.load(os.path.join(self.framesPath, 'Factory2.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Factory2.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Factory2.png')).convert_alpha()

            ]

            print("upgrade2")
            self.level = 2

        if self.level == 0:
            self.income+=35
            self.range += 100
            self.framesPath = os.path.join(self.image_path, 'Factory')  # Folder z grafikami wieży Temple
            self.frames = [
                pygame.image.load(os.path.join(self.framesPath, 'Factory1.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Factory1.png')).convert_alpha(),
                pygame.image.load(os.path.join(self.framesPath, 'Factory1.png')).convert_alpha()

            ]

            print("upgrade")
            self.level = 1
