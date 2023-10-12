import pygame
from dot import Dot
from square import Square
from target import Target
from colisions import checkLineDotColision, checkSquareDotColision, checkDotTargetColision
from levels import level1 as level

def atualizaDots(tela, config, dots, line, square, targets, som):
    """Atualiza a posição e a quantidade de elementos dot no jogo"""
    if len(dots) == 0:
        dot = Dot(tela, config)
        dots.add(dot)

    checkLineDotColision(dots, line, config)
    checkSquareDotColision(dots, square)
    checkDotTargetColision(dots, targets)

    dots.update()

def createLevel (tela, config, squares, targets):
    """Cria o desenho do mapa na tela"""

    positionx, positiony = 0, 0

    for line in level:
        for column in line:
            if column == 1:
                square = Square(tela, config)
                square.rect.left = positionx
                square.rect.top = positiony
                squares.add(square)
            elif column == 2:
                target = Target(tela, config)
                target.rect.left = positionx
                target.rect.top = positiony
                targets.add(target)
            positionx += config.squareWidth
        positiony += config.squareHeight
        positionx = 0

def atualizaTela(tela, config, dots, line, squares, targets, som):
    """Redesenha a tela a cada passagem pelo laço"""

    line.update()

    if len(squares) == 0:
        createLevel(tela, config, squares, targets)

    # Desenhar na tela
    tela.fill(config.background)

    for dot in dots:
        dot.draw()

    for square in squares:
        square.blitme()

    for target in targets:
        target.blitme()

    line.draw()

    # Atualizar a tela
    pygame.display.flip()
