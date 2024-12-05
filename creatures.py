import pygame
import math
import os

# Ustawiamy katalog roboczy na folder z grafikami 
# os.chdir(os.getcwd() + "/assets/New Folder/graphicstd/creatures")
class Monster(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, damage, reward, image_paths, position, waypoints, image_size, animation_speed, sf, max_health):
        super().__init__()  # Inicjalizacja bazowego sprite
        self.sf = sf
        self.name = name
        self.health = health
        self.max_health = max_health
        self.speed = speed
        self.damage = damage
        self.reward = reward
        self.basePath = os.path.join(os.getcwd(), "assets", 'creatures', self.name)
        self.image_size = image_size

        self.frames = [pygame.image.load(os.path.join(self.basePath, path)).convert_alpha() for path in image_paths]
        self.frames = [pygame.transform.scale(frame, image_size) for frame in self.frames]
        self.flip_to_left = False

        self.current_frame = 0
        self.animation_speed = animation_speed
        self.animation_counter = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.Vector2(position)

        # Waypoints (trasa ruchu)
        self.waypoints = [pygame.Vector2(wp) for wp in waypoints]
        self.waypoint_index = 0  # Aktualny indeks punktu trasy
        self.reached_end = False

    def animate(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            if self.flip_to_left:
                self.image = pygame.transform.flip(self.frames[self.current_frame], True, False)
            self.animation_counter = 0

    def move_towards_next_waypoint(self):
        """Przesuwa potwora w kierunku kolejnego punktu trasy."""
        if self.waypoint_index >= len(self.waypoints):
            return  # Potwór dotarł do końca trasy

        # Pobranie aktualnego punktu trasy
        target = self.waypoints[self.waypoint_index]

        # Sprawdzenie dystansu do punktu docelowego
        distance = self.position.distance_to(target)

        if distance < self.speed:  # Jeśli jest bardzo blisko punktu, uznajemy, że dotarł
            self.position = target  # Ustawiamy dokładnie na punkcie
            if (self.waypoints[-1] == self.waypoints[self.waypoint_index]):
                self.reached_end = True
                if not self.reached_end:
                    print("damaged")
                    self.kill()
            if not (self.waypoints[-1] == self.waypoints[self.waypoint_index]): #to musi byc bo inaczej blad 2 linijki nizej - sprawdzenie czy to juz nie ostatni waypoint
                self.waypoint_index += 1  # Przejście do kolejnego punktu
                self.flip_to_left = False

            if (self.waypoints[self.waypoint_index-1])[0] > (self.waypoints[self.waypoint_index])[0]:
                #print(self.waypoints[self.waypoint_index - 1][0],  self.waypoints[self.waypoint_index][0])
                self.flip_to_left = True
        else:
            direction = (target - self.position).normalize()  # Kierunek ruchu
            self.position += direction * self.speed
            self.rect.bottomleft = self.position  # Aktualizacja pozycji `rect` dla kolizji

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def draw_health_bar(self, surface, img_size):
        health_bar_width = 40*self.sf
        health_bar_height = 4*self.sf
        # Umiejscowienie paska
        health_bar_x = self.position[0] + img_size[0]*0.1
        health_bar_y = self.position[1] - (img_size[1]*1.2)
        # Rysowanie tła paska
        pygame.draw.rect(surface, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        # Obliczanie wypełnienia paska
        health_fill_width = (self.health / self.max_health) * health_bar_width
        # Rysowanie wypełnienia
        pygame.draw.rect(surface, (0, 255, 0), (health_bar_x, health_bar_y, health_fill_width, health_bar_height))

    def update(self):
        """Aktualizacja ruchu potwora w kierunku trasy."""
        self.move_towards_next_waypoint()
        self.animate()





class Dragon(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=11):
        super().__init__(name="Dragon", health=500, max_health=500, speed=speed, damage=50, reward=100, image_size=image_size, animation_speed=animation_speed,
                         image_paths=["dragon.png", "dragon1.png", "dragon2.png"], position=position, waypoints=waypoints, sf=sf)
        self.frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
    def update(self):
        super().update()  # Wywołuje poruszanie się po trasie i animację z klasy Monster
        pass


class Troll(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=3):
        super().__init__(name="Troll", health=600, max_health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed,
                         image_paths=["troll.png", "troll1.png", "troll2.png"], position=position, waypoints=waypoints, sf=sf)
        self.health_regen = 5

    def update(self):
        super().update()


class Ghost(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=3):
        super().__init__(name="Ghost", health=600, max_health=600, speed=speed, damage=20, reward=75, image_size=image_size, animation_speed=animation_speed,
                          image_paths=["ghost.png"], position=position, waypoints=waypoints, sf=sf)

    def update(self):
        super().update()

class Goblin(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=3):
        super().__init__(name="Goblin", health=600, max_health=600, speed=speed, damage=5, reward=75, image_size=image_size, animation_speed=animation_speed,
                          image_paths=["goblin.png","goblin2.png","goblin1.png"], position=position, waypoints=waypoints, sf=sf)

    def update(self):
        super().update()

class Hydra(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=3):
        super().__init__(name="Hydra", health=600, max_health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed,
                          image_paths=["hydra.png","hydra1.png"], position=position, waypoints=waypoints, sf=sf)

    def update(self):
        super().update()


class Skeleton(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=3):
        super().__init__(name="Skeleton", health=600, max_health=600, speed=speed, damage=10, reward=75, image_size=image_size, animation_speed=animation_speed,
                          image_paths=["skeleton.png","skeleton1.png","skeleton2.png"], position=position, waypoints=waypoints, sf=sf)

    def update(self):
        super().update()


class Thief(Monster):
    def __init__(self, position, waypoints, image_size, sf, animation_speed=3, speed=3):
        super().__init__(name="Thief", health=600, max_health=600, speed=speed, damage=20, reward=75, image_size=image_size, animation_speed=animation_speed,
                          image_paths=["thief2.png","thief1.png","thief.png"], position=position, waypoints=waypoints, sf=sf)

    def update(self):
        super().update()


