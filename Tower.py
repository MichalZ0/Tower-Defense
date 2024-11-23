from os import walk
import creature_classes
import pygame
import math

class Tower(creature_classes.Monster):
    def __init__(self, screen, name, pos, size):
        self.screen = screen
        self.name = name
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.pos = pos

        self.sprite = pygame.image.load("assets/towers/ghost.png")
        self.sprite = pygame.transform.scale(self.sprite, (self.rect.width, self.rect.height))

        self.attackRangeRadius = 50 


        self.currentSprite = self.sprite
        self.currentPos = self.pos


        self.attackSpriteCenter = (self.rect.x + (self.rect.width/2), self.rect.y + (self.rect.height/2))

        self.speed = 1
        self.bulletPos = self.attack((100, 180))
        self.newBulletPos = self.attack((100, 380))






    def draw(self): 
        self.screen.blit(self.currentSprite, self.currentPos)
        self.updateBullet()

    def drawAttackRadius(self):
        self.towerRadiusPos = [self.rect.x + (self.rect.width/2), self.rect.y + (self.rect.height/2)]
        self.towerRadiusSprite = pygame.Surface((self.attackRangeRadius*2, self.attackRangeRadius*2), pygame.SRCALPHA)
        self.towerCenter = ((self.attackRangeRadius - (self.rect.width/2),
                                    self.attackRangeRadius - (self.rect.height/2)))

        self.towerRadiusSprite.blit(self.sprite, self.towerCenter)

        self.towerRadius = pygame.draw.circle(self.towerRadiusSprite, "white", 
                                              (self.attackRangeRadius,self.attackRangeRadius), 
                                              radius=self.attackRangeRadius,
                                              width=3)
        
        self.currentSprite = self.towerRadiusSprite
        self.currentPos = [self.rect.x - self.towerCenter[0],
                    self.rect.y - self.towerCenter[1]]



    def attack(self, pos):
        self.attackDir = (pos[0] - self.attackSpriteCenter[0],
                          pos[1] - self.attackSpriteCenter[1])        

        self.length = math.hypot(*self.attackDir)
        if (self.length==0.0):
            self.attackDir = (0, -1)
        else:
            self.attackDir = (self.attackDir[0]/self.length, self.attackDir[1]/self.length)

        self.angle = math.degrees(math.atan2(-self.attackDir[1], self.attackDir[0]))
                                                                   
        self.bullet = pygame.Surface((7, 2)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, self.angle)

        return pos

    def updateBullet(self):
        self.bulletPos = (self.bulletPos[0]+self.attackDir[0]*self.speed, self.bulletPos[1]+self.attackDir[1]*self.speed)
        self.newBulletPos = (self.newBulletPos[0]+self.attackDir[0]*self.speed, self.newBulletPos[1]+self.attackDir[1]*self.speed)
        self.screen.blit(self.bullet, self.bulletPos)
        self.screen.blit(self.bullet, self.newBulletPos)


    def clicked(self, event):
        # if (self.rect.collidepoint(event.pos)):
        #    self.drawAttackRadius()
        # else:
        #    self.currentSprite, self.currentPos = self.sprite, self.pos
        self.clickPos = event.pos

            
        
