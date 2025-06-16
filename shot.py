from constants import *
from circleshape import *
from player import *
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        pygame.sprite.Sprite.__init__(self,*self.containers)
        self.velocity = pygame.Vector2(0,0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius,width=0)

    def update(self, dt):
        self.position += self.velocity*dt