import pygame
import math

import os

# Ustawiamy katalog roboczy na folder z grafikami
os.chdir("C:/Users/ignac/OneDrive/Pulpit/folder gry/graphicstd/creatures")
class Monster(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, damage, reward, image_paths, position, waypoints, image_size, animation_speed, screen_size):
        super().__init__()  # Inicjalizacja bazowego sprite

        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage
        self.reward = reward
        self.screen_size = screen_size

        self.frames = [pygame.image.load(path).convert_alpha() for path in image_paths]
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
                self.cause_damage(self.damage)
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
        """Zmniejsza zdrowie o wartość obrażeń."""
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Usuwa sprite z grupy, gdy zdrowie wynosi 0

    def cause_damage(self, damage):
        print("damaged")
        self.kill()
    def update(self):
        """Aktualizacja ruchu potwora w kierunku trasy."""
        self.move_towards_next_waypoint()
        self.animate()



class Dragon(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Smok", health=500, speed=speed, damage=50, reward=100, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["dragon.png", "dragon1.png", "dragon2.png"], position=position, waypoints=waypoints)
        self.frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
    def update(self):
        super().update()  # Wywołuje poruszanie się po trasie i animację z klasy Monster


class Troll(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Troll", health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["troll.png", "troll1.png", "troll2.png"], position=position, waypoints=waypoints)
        self.health_regen = 5

    def update(self):
        super().update()


class Ghost(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Ghost", health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["ghost.png"], position=position, waypoints=waypoints)

    def update(self):
        super().update()


class Goblin(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Goblin", health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["goblin.png","goblin2.png","goblin1.png"], position=position, waypoints=waypoints)
    def update(self):
        super().update()


class Hydra(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Hydra", health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["hydra.png","hydra1.png"], position=position, waypoints=waypoints)

    def update(self):
        super().update()


class Skeleton(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Skeleton", health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["skeleton.png","skeleton1.png","skeleton2.png"], position=position, waypoints=waypoints)

    def update(self):
        super().update()


class Thief(Monster):
    def __init__(self, position, waypoints, image_size, animation_speed, speed, screen_size):
        super().__init__(name="Nicpoń", health=600, speed=speed, damage=30, reward=75, image_size=image_size, animation_speed=animation_speed, screen_size=screen_size,
                         image_paths=["thief2.png","thief1.png","thief.png"], position=position, waypoints=waypoints)

    def update(self):
        super().update()


