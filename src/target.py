import pygame
from pygame.sprite import Sprite

class Target (Sprite):
    """Classe que representa as moedas alvo do jogo"""
    def __init__(self, tela, config) :
        super().__init__()
        self.config = config
        self.tela = tela
        self.image = pygame.image.load('src/images/coin.bmp')
        self.rect = self.image.get_rect()
        self.tela_rect = self.tela.get_rect()


    def blitme(self):
        self.tela.blit(self.image, self.rect)


