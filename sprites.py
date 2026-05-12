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

        self.image = self.imagens_pacman_right[0]

        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]

