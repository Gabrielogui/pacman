import constants
import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)

        self.imagens_pacman_up    = []
        self.imagens_pacman_down  = []
        self.imagens_pacman_left  = []
        self.imagens_pacman_right = []

        # SPRITES À DIREITA
        img = sprite_sheet.subsurface((456, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_right.append(img)
        img = sprite_sheet.subsurface((472, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_right.append(img)

        # SPRITES À ESQUERDA
        img = sprite_sheet.subsurface((456, 16), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_left.append(img)
        img = sprite_sheet.subsurface((472, 16), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_left.append(img)

        # SPRITES PARA CIMA
        img = sprite_sheet.subsurface((456, 33), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_up.append(img)
        img = sprite_sheet.subsurface((472, 33), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_up.append(img)

        # SPRITES PARA BAIXO
        img = sprite_sheet.subsurface((456, 48), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_down.append(img)
        img = sprite_sheet.subsurface((472, 48), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_down.append(img)

        # BOCA DO PACMAN FECHADA QUE TEM EM TODOS
        img = sprite_sheet.subsurface((488, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        self.imagens_pacman_right.append(img)
        self.imagens_pacman_left.append(img)
        self.imagens_pacman_up.append(img)
        self.imagens_pacman_down.append(img)

        self.index_lista = 0

        self.image = self.imagens_pacman_right[self.index_lista]

        self.direcao:constants.DirecaoPacman = constants.DirecaoPacman.RIGHT

        self.rect   = self.image.get_rect()
        self.rect.x = constants.LARGURA // 2 - constants.PACMAN_TAMANHO_PIXEL // 2
        self.rect.y = 420

    def change_direction(self, new_direction:constants.DirecaoPacman):
        self.direcao = new_direction

    def update(self):
        if self.direcao == constants.DirecaoPacman.RIGHT:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_right)):
                self.index_lista = 0

            self.image = self.imagens_pacman_right[int(self.index_lista)]

        elif self.direcao == constants.DirecaoPacman.LEFT:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_left)):
                self.index_lista = 0

            self.image = self.imagens_pacman_left[int(self.index_lista)]
        
        elif self.direcao == constants.DirecaoPacman.UP:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_up)):
                self.index_lista = 0

            self.image = self.imagens_pacman_up[int(self.index_lista)]
        
        elif self.direcao == constants.DirecaoPacman.DOWN:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_down)):
                self.index_lista = 0

            self.image = self.imagens_pacman_down[int(self.index_lista)]


class Mapa(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = sprite_sheet.subsurface((227, 0), (225, 248))
        self.image = pygame.transform.scale(self.image, (225 * 2, 248 * 2))
        
        self.rect = self.image.get_rect()
        self.rect.y = constants.ALTURA // 2 - 248 * 2 // 2
        self.rect.x = constants.LARGURA // 2 - 225 * 2 // 2


