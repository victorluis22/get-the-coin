import pygame
import sys
from pygame.sprite import Group

from config import Config
from gameFunctions import atualizaTela, atualizaDots
from events import checa_evento

from line import Line
from som import Som

def runGame ():
    # Inicialização do Pygame
    pygame.init()
    config = Config()
    tela = pygame.display.set_mode((config.width, config.height))
    icon = pygame.image.load('src/images/coin.png')
    pygame.display.set_caption(config.name)
    pygame.display.set_icon(icon)

    

    # Objetos de interesse no jogo
    dots = Group()
    squares = Group()
    targets = Group()
    line = Line(tela, config)
    som = Som()

    # Loop do jogo
    execution = True
    while execution:
        checa_evento(line)

        atualizaDots(tela, config, dots, line, squares, targets, som)
        atualizaTela(tela, config, dots, line, squares, targets, som)
        

    # Encerrando o Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    runGame()