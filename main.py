import pygame
import constants
import sprites
import os

class Game:
    def __init__(self):
        # CRIANDO TELA
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constants.LARGURA, constants.ALTURA))
        pygame.display.set_caption(constants.TITULO_JOGO)
        self.relogio = pygame.time.Clock()

        self.esta_rodando = True

        self.fonte = pygame.font.match_font(constants.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        """ INSTANCIA TODAS AS SPRITES DO JOGO """
        self.todas_as_sprites = pygame.sprite.Group()

        self.mapa   = sprites.Mapa(self.sprite_sheet)
        self.pacman = sprites.Pacman(self.sprite_sheet)

        self.todas_as_sprites.add(self.mapa)
        self.todas_as_sprites.add(self.pacman)

        self.rodar()

    def rodar(self):
        """ LOOP PRINCIPAL DO JOGO """
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constants.FPS)

            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        """ DEFINE OS EVENTOS DO JOGO """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.esta_rodando = False
                if self.jogando:
                    self.jogando  = False

            if event.type == pygame.KEYDOWN:

                # MOVIMENTAÇÃO DO PACMAN
                if event.key == pygame.K_UP:
                    self.pacman.change_direction(constants.DirecaoPacman.UP)
                if event.key == pygame.K_DOWN:
                    self.pacman.change_direction(constants.DirecaoPacman.DOWN)
                if event.key == pygame.K_RIGHT:
                    self.pacman.change_direction(constants.DirecaoPacman.RIGHT)
                if event.key == pygame.K_LEFT:
                    self.pacman.change_direction(constants.DirecaoPacman.LEFT)


    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(constants.PRETO)       # LIMPANDO A TELA
        self.todas_as_sprites.draw(self.tela) # DESENHANDO AS SPRITES
        pygame.display.flip()

    def carregar_arquivos(self):
        """ CARREGAR TODOS OS ARQUIVOS DE IMAGEM E ÁUDIO DO JOGO """
        diretorio_imagens     = os.path.join(os.getcwd(), "imagens")
        self.diretorio_audios = os.path.join(os.getcwd(), "audios")

        self.sprite_sheet       = os.path.join(diretorio_imagens, constants.SPRITESHEET)
        self.packman_start_logo = os.path.join(diretorio_imagens, constants.PACKMAN_START_LOGO)

        
        self.sprite_sheet       = pygame.image.load(self.sprite_sheet).convert_alpha()
        self.packman_start_logo = pygame.image.load(self.packman_start_logo).convert() # TRANSFORMANDO EM IMAGEM

    def mostrar_texto(self, texto: str, tamanho: int, cor: tuple, x: int, y: int):
        """ EXIBE TEXTO NA TELA DO JOGO """
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)

        texto_rect        = texto.get_rect()
        texto_rect.midtop = (x, y)

        self.tela.blit(texto, texto_rect)

    def mosrar_start_logo(self, x: int, y: int):
        start_logo_rect = self.packman_start_logo.get_rect()
        start_logo_rect.midtop = (x, y)

        self.tela.blit(self.packman_start_logo, start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constants.MUSICA_START))
        pygame.mixer.music.play()

        self.mosrar_start_logo(constants.LARGURA // 2, 20)

        self.mostrar_texto(
            "Pressione uma tecla para jogar",
            32,
            constants.AMARELO,
            constants.LARGURA // 2,
            320
        )

        self.mostrar_texto(
            "Desenvolvido por Gabriel Rodrigues",
            20,
            constants.BRANCO,
            constants.LARGURA // 2,
            550
        )

        pygame.display.flip()
        self.esperar_jogador()


    def esperar_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constants.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False

                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_audios, constants.TECLA_START))

    def mostrar_tela_gameover(self):
        pass

if __name__ == "__main__":
    game = Game()

    game.mostrar_tela_start()

    while game.esta_rodando:
        game.novo_jogo()
        game.mostrar_tela_gameover()