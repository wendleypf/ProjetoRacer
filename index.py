# coding: utf-8
import pygame
from config import *
from pygame.locals import *
from interface import *

pygame.init()

windows = pygame.display.set_mode(RESOLUCAO, 0, 32)
screen = pygame.display.get_surface()
pygame.display.set_caption("Game Racer - UFCG 2013.2")

interface = interface(screen)
interface.iniciar_jogo(screen)
interface.menu(screen)