# coding: utf-8
import pygame
import sys
from config import *
from game import *
from pygame.locals import * 

class interface:
    def __init__(self,screen):
        self.jogar = pygame.image.load("img/interface/jogar.png")
        self.op_controles = pygame.image.load("img/interface/op_controle.png")
        self.op_creditos =  pygame.image.load("img/interface/op_creditos.png")
        self.rect_jogar = self.jogar.get_rect()
        self.rect_jogar.x, self.rect_jogar.y = 128, 195 
        self.rect_controles = self.op_controles.get_rect()
        self.rect_controles.x, self.rect_controles.y = 128, 287
        self.rect_creditos = self.op_creditos.get_rect()
        self.rect_creditos.x, self.rect_creditos.y = 128, 378
    
    def atualiza_imagem(self, screen, imagem):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
            
            self.posicao_mouse = pygame.mouse.get_pos()
            screen.blit(imagem, (0, 0))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RETURN]: 
                efeitos_sonoros("Retorno")
                break
            pygame.display.flip()
    
    def atualiza_imagem_mouse(self, screen, imagem, rect, funcao):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                   pygame.quit()
                   sys.exit()
                
                self.posicao_mouse = pygame.mouse.get_pos()
                if not rect.collidepoint((self.posicao_mouse)): return
                screen.blit(imagem, (0, 0))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    efeitos_sonoros("Click")
                    funcao(screen)
            
    def iniciar_jogo(self, screen):
        imagem_inicial = pygame.image.load(IMAGEM_INICIAL)
        self.atualiza_imagem(screen, imagem_inicial)
        
    def controles(self, screen):
        menu_controles = pygame.image.load(CONTROLS)
        self.atualiza_imagem(screen, menu_controles)
        
    def creditos(self, screen):
        menu_creditos = pygame.image.load(CREDIT)
        self.atualiza_imagem(screen, menu_creditos)             
    
    def menu(self, screen):
        imagem_menu_inicial = pygame.image.load(IMAGEM_MENU)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                
            screen.blit(imagem_menu_inicial, (0, 0))
            pygame.display.flip()
            self.posicao_mouse = pygame.mouse.get_pos()
            
            if self.rect_jogar.collidepoint((self.posicao_mouse)):
                imagem_jogar = pygame.image.load(SELECIONADO_JOGAR)
                self.atualiza_imagem_mouse(screen, imagem_jogar, self.rect_jogar, main)
                                
            elif self.rect_controles.collidepoint((self.posicao_mouse)):
                imagem_controles =  pygame.image.load(SELECIONADO_CONTROLES)
                self.atualiza_imagem_mouse(screen, imagem_controles, self.rect_controles, self.controles)
                        
            elif self.rect_creditos.collidepoint((self.posicao_mouse)):
                imagem_creditos =  pygame.image.load(SELECIONADO_CREDITOS)
                self.atualiza_imagem_mouse(screen, imagem_creditos, self.rect_creditos, self.creditos)  
