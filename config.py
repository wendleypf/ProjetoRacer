import os
import pygame

pygame.init()

RESOLUCAO = (550,600)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
FPS = 35
QUANTIDADE_INIMIGO = 2
os.environ['SDL_VIDEO_CENTERED'] = '1' # CENTRALIZA A TELA DO JOGO  

IMAGEM_BACKGROUND = os.path.join("img","background","background.png")
IMAGEM_INICIAL = os.path.join("img","interface","tela_inicial.png")
IMAGEM_MENU = os.path.join("img","interface","menu.png")
IMAGEM_CARRO = os.path.join("img","objetos","carro.png")
IMAGEM_CARRO_INIMIGO = os.path.join("img","objetos","carro_inimigo.png")
IMAGEM_BURACO = os.path.join("img", "objetos","buraco.png")
SELECIONADO_JOGAR = os.path.join("img", "interface", "selecionado1.png")
SELECIONADO_CONTROLES = os.path.join("img", "interface", "selecionado2.png")
SELECIONADO_CREDITOS = os.path.join("img", "interface", "selecionado3.png")
CREDIT = os.path.join("img", "interface", "creditos.png")
CONTROLS = os.path.join("img", "interface", "controles.png")
FIM = os.path.join("img", "interface", "game_over.png")
TROFEU = os.path.join("img","objetos","trophy.png")
CAMINHO_DA_FONTE_PIXEL = os.path.join("font","Computer.ttf")
CAMINHO_DA_FONTE_DG = os.path.join("font","DS-DIGI.TTF")
CAMINHO_DA_MUSICA = os.path.join("music","musica.mp3")
CAMINHO_DA_MUSICA_GAMEOVER = os.path.join("music","game_over.wav")
CAMINHO_DA_MUSICA_SELECIONAR = os.path.join("music","retorno.wav")
CAMINHO_DA_MUSICA_RETORNO = os.path.join("music","selecionar.wav")
ARQUIVO_SALVA_SCORE = os.path.join("data","score.dat")
FONTE_PIXEL = pygame.font.Font(CAMINHO_DA_FONTE_PIXEL, 20)
FONTE_DG = pygame.font.Font(CAMINHO_DA_FONTE_DG, 30)
