import pygame
import sys

def checa_evento_KEYDOWN(event, line):
    """Checa eventos de keydown"""
    if event.key == pygame.K_RIGHT:
        line.goingRight = True
    elif event.key == pygame.K_LEFT:
        line.goingLeft = True
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
        
            
def checa_evento_KEYUP(event, line):
    """Checa eventos de keyup"""
    if event.key == pygame.K_RIGHT:
        line.goingRight = False
    elif event.key == pygame.K_LEFT:
        line.goingLeft = False
            
def checa_evento(line):
    """Laço que checa eventos durante o jogo"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
        elif event.type == pygame.KEYDOWN:
            checa_evento_KEYDOWN(event, line)
            
        elif event.type == pygame.KEYUP:
            checa_evento_KEYUP(event, line)
            