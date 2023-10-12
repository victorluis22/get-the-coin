class Config ():
    """Classe para configurações gerais do jogo."""

    def __init__(self):
        # Configurações gerais do jogo
        self.name = "Get The Coin"
        self.width = 600
        self.height = 600
        self.background = (19, 19, 18)

        # Configurações do ponto
        self.dotWidth = 5
        self.dotColor = (255, 255, 255)
        self.dotVelocityx = 0
        self.dotVelocityy = 0.5

        # Configurações da plataforma
        self.lineWidth = 50
        self.lineHeight = 2
        self.lineColor = (255, 255, 255)
        self.lineVelocity = 0.5

        # Configurações das paredes
        self.squareWidth = 30
        self.squareHeight = 30
        self.squareColor = (255, 255, 255)