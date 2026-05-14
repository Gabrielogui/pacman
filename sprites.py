import constants
import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)

        self.imagens_pacman_up    = []
        self.imagens_pacman_down  = []
        self.imagens_pacman_left  = []
        self.imagens_pacman_right = []

        # SPRITES À DIREITA
        img = sprite_sheet.subsurface((456, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_right.append(img)
        img = sprite_sheet.subsurface((472, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_right.append(img)

        # SPRITES À ESQUERDA
        img = sprite_sheet.subsurface((456, 16), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_left.append(img)
        img = sprite_sheet.subsurface((472, 16), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_left.append(img)

        # SPRITES PARA CIMA
        img = sprite_sheet.subsurface((456, 33), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_up.append(img)
        img = sprite_sheet.subsurface((472, 33), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_up.append(img)

        # SPRITES PARA BAIXO
        img = sprite_sheet.subsurface((456, 48), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_down.append(img)
        img = sprite_sheet.subsurface((472, 48), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_down.append(img)

        # BOCA DO PACMAN FECHADA QUE TEM EM TODOS
        img = sprite_sheet.subsurface((488, 0), (constants.PACMAN_TAMANHO_PIXEL, constants.PACMAN_TAMANHO_PIXEL))
        img = pygame.transform.scale(img, (constants.PACMAN_TAMANHO_PIXEL * 1.5, constants.PACMAN_TAMANHO_PIXEL * 1.5))
        img.set_colorkey(constants.PRETO)
        self.imagens_pacman_right.append(img)
        self.imagens_pacman_left.append(img)
        self.imagens_pacman_up.append(img)
        self.imagens_pacman_down.append(img)

        self.index_lista = 0

        self.image = self.imagens_pacman_right[self.index_lista]

        self.direcao:constants.DirecaoPacman = constants.DirecaoPacman.RIGHT

        self.rect   = self.image.get_rect()
        self.rect.x = constants.LARGURA // 2 - constants.PACMAN_TAMANHO_PIXEL // 2
        self.rect.y = constants.POS_Y_INICIAL

        self.colidiu_parede = False

        self.mask = pygame.mask.from_surface(self.image)

    def change_colidiu_parede(self, colidiu_parede: bool):
        self.colidiu_parede = colidiu_parede

    def change_direction(self, new_direction:constants.DirecaoPacman):
        self.direcao = new_direction

    def update(self):
        if self.direcao == constants.DirecaoPacman.RIGHT:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_right)):
                self.index_lista = 0

            self.image = self.imagens_pacman_right[int(self.index_lista)]

           
            self.rect.x += constants.VELOCIDADE_PACMAN

        elif self.direcao == constants.DirecaoPacman.LEFT:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_left)):
                self.index_lista = 0

            self.image = self.imagens_pacman_left[int(self.index_lista)]

           
            self.rect.x -= constants.VELOCIDADE_PACMAN
        
        elif self.direcao == constants.DirecaoPacman.UP:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_up)):
                self.index_lista = 0

            self.image = self.imagens_pacman_up[int(self.index_lista)]

           
            self.rect.y -= constants.VELOCIDADE_PACMAN
        
        elif self.direcao == constants.DirecaoPacman.DOWN:
            self.index_lista += constants.VELOCIDADE_SPRITE

            if(self.index_lista == len(self.imagens_pacman_down)):
                self.index_lista = 0

            self.image = self.imagens_pacman_down[int(self.index_lista)]

           
            self.rect.y += constants.VELOCIDADE_PACMAN


class Mapa(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = sprite_sheet.subsurface((227, 0), (225, 248))
        self.image = pygame.transform.scale(self.image, (225 * 2, 248 * 2))

        self.image.set_colorkey(constants.PRETO)

        self.rect = self.image.get_rect()
        
        self.rect.y = constants.ALTURA // 2 - 248 * 2 // 2
        self.rect.x = constants.LARGURA // 2 - 225 * 2 // 2

        self.mask = pygame.mask.from_surface(self.image)


class Bolinha(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: pygame.surface.Surface, pos_x: int, pos_y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = sprite_sheet.subsurface((10, 10), (4, 4))
        self.image = pygame.transform.scale(self.image, (4 * 2, 4 * 2))

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y



