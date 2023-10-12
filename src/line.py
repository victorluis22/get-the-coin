import pygame
from pygame.sprite import Sprite

class Line(Sprite):
    """Representa a plataforma interativa do jogo"""
    def __init__(self, tela, config):
        super().__init__()
        self.config = config
        self.tela = tela
        self.rect = pygame.Rect(0, 0, self.config.lineWidth, self.config.lineHeight)
        self.cor = self.config.lineColor

        self.rect.centerx = self.config.width // 2
        self.rect.centery = self.config.height - 100

        self.center = float(self.rect.centerx)
        self.goingRight = False
        self.goingLeft = False

    def update(self):
        if self.goingRight and self.rect.right < self.config.width:
            self.center += self.config.lineVelocity
        elif self.goingLeft and self.rect.left > 0:
            self.center -= self.config.lineVelocity

        self.rect.centerx = self.center

    def draw(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)