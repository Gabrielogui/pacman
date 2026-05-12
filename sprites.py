import constants
import pygame
import os

class Pacman(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)

        self.imagens_pacman_up    = []
        self.imagens_pacman_down  = []
        self.imagens_pacman_left  = []
        self.imagens_pacman_right = []

        img = sprite_sheet.subsurface((456, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        self.imagens_pacman_right.append(img)
        img = sprite_sheet.subsurface((472, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        self.imagens_pacman_right.append(img)
        img = sprite_sheet.subsurface((488, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        self.imagens_pacman_right.append(img)


        self.index_lista = 0

        self.image = self.imagens_pacman_right[self.index_lista]

        self.direcao:constants.DirecaoPacman = constants.DirecaoPacman.RIGHT

        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]

    def update(self):
        if self.direcao == constants.DirecaoPacman.RIGHT:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_right)):
                self.index_lista = 0

            self.image = self.imagens_pacman_right[int(self.index_lista)]

