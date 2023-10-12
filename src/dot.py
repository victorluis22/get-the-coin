import pygame
from pygame.sprite import Sprite

class Dot (Sprite):
    """Representa os projeteis do jogo."""
    def __init__(self, tela, config):
        super().__init__()
        self.config = config
        self.tela = tela
        self.rect = pygame.Rect(0, 0, self.config.dotWidth, self.config.dotWidth)
        self.cor = self.config.dotColor

        self.rect.centerx = self.config.width // 2
        self.rect.centery = self.config.height // 2

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.directionx = 1
        self.directiony = 1


    def update(self):

        if self.rect.centerx >= self.config.width or self.rect.centerx <= 0:
            self.directionx *= -1

        if self.rect.centery >= self.config.height or self.rect.centery <= 0:
            self.directiony *= -1
        
        self.centerx += self.config.dotVelocityx * self.directionx
        self.centery += self.config.dotVelocityy * self.directiony

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def draw(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)