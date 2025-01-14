import pygame
import math

class Attack():
    def __init__(self, targetRect, towerRect, bulletSpeed):
            self.targetRect = targetRect

            self.pos = [towerRect.x + (towerRect.width/2),
                        towerRect.y + (towerRect.height/2)]


            self.posRect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

            self.dir = pygame.Vector2(
                    targetRect.x - (towerRect.x + (towerRect.width/2)), 
                    targetRect.y - (towerRect.y + (towerRect.height/2))).normalize()


            
            self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
            self.speed = bulletSpeed  

            self.bulletSprite = pygame.Surface(( 10, 3 )).convert_alpha()
            self.bulletSprite.fill('white')
            self.bulletSprite = pygame.transform.rotate(self.bulletSprite, self.angle)





    def update(self):
        self.pos = [self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed]


        self.posRect.x = self.pos[0]
        self.posRect.y = self.pos[1]

    def getPosition(self):
        return self.pos

    def getSprite(self):
        return self.bulletSprite

    def checkCollision(self):
        if (self.posRect.colliderect(self.targetRect)):
            return True
        return False

    def getBulletRect(self):
        return self.bulletSprite.get_rect(center = self.pos)
            

