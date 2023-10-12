import pygame

def checkLineDotColision(dots, line, config):
    """Checa colisões entre line e dots"""

    collisions = pygame.sprite.spritecollide(line, dots, False)
    
    if collisions:
        for dot in collisions:
            dot.directiony *= -1

            if dot.rect.centerx - line.rect.centerx < 0:
                config.dotVelocityx = config.dotVelocityy
                dot.directionx = -1
            elif dot.rect.centerx - line.rect.centerx > 0:
                config.dotVelocityx = config.dotVelocityy
                dot.directionx = 1
            else:
                config.dotVelocityx = 0

def checkSquareDotColision(dots, squares):
    """Checa colisões entre dot e squares"""

    collisions = pygame.sprite.groupcollide(dots, squares, False, False)
    
    if collisions:
        dot, square = list(collisions.items())[0][0], list(collisions.items())[0][1][0]

        # print(dot.rect.top, square.rect.bottom)
        if dot.rect.top+1 == square.rect.bottom or dot.rect.bottom == square.rect.top+1:
            dot.directiony *= -1

        if dot.rect.right == square.rect.left+1 or dot.rect.left+1 == square.rect.right:
            dot.directionx *= -1

def checkDotTargetColision(dots, targets):
    """Checa colisões entre dot e targets"""

    collisions = pygame.sprite.groupcollide(dots, targets, False, True)
    
    if collisions:
        pass
        # print(collisions)

    