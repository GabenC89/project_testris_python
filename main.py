import pygame
import sys

sys.path.append('engine')
from engine import Engine

pygame.init()

engine = Engine()

engine.run_game_loop()

pygame.quit()
quit()